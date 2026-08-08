$ErrorActionPreference = 'Stop'

$Repo = 'chriskulbaba2025/governed-coding-upgrade-skill'
$Owner = 'chriskulbaba2025'
$Branch = 'main'
$RequiredCheck = 'validate'

Write-Host 'Verifying GitHub authentication...'
gh auth status
if ($LASTEXITCODE -ne 0) { throw 'GitHub authentication failed.' }

Write-Host 'Verifying repository identity and sole-maintainer access...'
$RepoInfo = gh repo view $Repo --json nameWithOwner,visibility,defaultBranchRef | ConvertFrom-Json
if ($RepoInfo.nameWithOwner -ne $Repo) { throw "Unexpected repository: $($RepoInfo.nameWithOwner)" }
if ($RepoInfo.defaultBranchRef.name -ne $Branch) { throw "Expected default branch '$Branch'." }

$Collaborators = gh api "repos/$Repo/collaborators" | ConvertFrom-Json
$Unexpected = @($Collaborators | Where-Object { $_.login -ne $Owner })
if ($Unexpected.Count -gt 0) {
    $Names = ($Unexpected.login -join ', ')
    throw "Unexpected collaborator(s) with repository access: $Names"
}

if ($RepoInfo.visibility -ne 'PUBLIC') {
    Write-Host 'Making repository public...'
    gh repo edit $Repo `
      --visibility public `
      --accept-visibility-change-consequences
    if ($LASTEXITCODE -ne 0) { throw 'Repository visibility update failed.' }
} else {
    Write-Host 'Repository is already public; skipping visibility mutation.'
}

Write-Host 'Applying maintainer-controlled merge settings...'
gh repo edit $Repo `
  --enable-issues=true `
  --enable-wiki=false `
  --enable-projects=false `
  --enable-merge-commit=false `
  --enable-rebase-merge=false `
  --enable-squash-merge=true `
  --delete-branch-on-merge=true
if ($LASTEXITCODE -ne 0) { throw 'Repository settings update failed.' }

$Protection = @{
    required_status_checks = @{
        strict = $true
        contexts = @($RequiredCheck)
    }
    enforce_admins = $true
    required_pull_request_reviews = @{
        dismiss_stale_reviews = $true
        require_code_owner_reviews = $false
        required_approving_review_count = 0
        require_last_push_approval = $false
    }
    restrictions = $null
    required_linear_history = $true
    allow_force_pushes = $false
    allow_deletions = $false
    block_creations = $false
    required_conversation_resolution = $true
    lock_branch = $false
    allow_fork_syncing = $false
} | ConvertTo-Json -Depth 10

Write-Host 'Protecting main...'
$ProtectionApplied = $false
$LastProtectionError = ''

for ($Attempt = 1; $Attempt -le 8; $Attempt++) {
    $PreviousPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    $ProtectionOutput = $Protection | gh api `
      --method PUT `
      -H 'Accept: application/vnd.github+json' `
      -H 'X-GitHub-Api-Version: 2022-11-28' `
      "repos/$Repo/branches/$Branch/protection" `
      --input - 2>&1
    $ProtectionExit = $LASTEXITCODE
    $ErrorActionPreference = $PreviousPreference

    if ($ProtectionExit -eq 0) {
        $ProtectionApplied = $true
        break
    }

    $LastProtectionError = ($ProtectionOutput | Out-String).Trim()
    if ($LastProtectionError -match 'Repository has been locked') {
        Write-Host "GitHub still has the repository transition-locked; retrying protection ($Attempt/8)..."
        Start-Sleep -Seconds 5
        continue
    }

    throw "Branch protection update failed: $LastProtectionError"
}

if (-not $ProtectionApplied) {
    throw "Branch protection update failed after transition retries: $LastProtectionError"
}

Write-Host 'Verifying final repository state...'
$FinalRepo = gh repo view $Repo --json nameWithOwner,visibility,defaultBranchRef | ConvertFrom-Json
$FinalCollaborators = gh api "repos/$Repo/collaborators" | ConvertFrom-Json
$FinalProtection = gh api "repos/$Repo/branches/$Branch/protection" | ConvertFrom-Json

$Checks = @(
    [pscustomobject]@{ Name = 'Repository is PUBLIC'; Pass = ($FinalRepo.visibility -eq 'PUBLIC') },
    [pscustomobject]@{ Name = 'Default branch is main'; Pass = ($FinalRepo.defaultBranchRef.name -eq $Branch) },
    [pscustomobject]@{ Name = 'Only canonical maintainer has collaborator access'; Pass = (@($FinalCollaborators | Where-Object { $_.login -ne $Owner }).Count -eq 0) },
    [pscustomobject]@{ Name = 'Branch protection applies to admin'; Pass = [bool]$FinalProtection.enforce_admins.enabled },
    [pscustomobject]@{ Name = 'Required CI check is validate'; Pass = (@($FinalProtection.required_status_checks.contexts) -contains $RequiredCheck) },
    [pscustomobject]@{ Name = 'Pull request workflow is required'; Pass = ($null -ne $FinalProtection.required_pull_request_reviews) },
    [pscustomobject]@{ Name = 'No external approval required for sole maintainer'; Pass = ($FinalProtection.required_pull_request_reviews.required_approving_review_count -eq 0) },
    [pscustomobject]@{ Name = 'Linear history required'; Pass = [bool]$FinalProtection.required_linear_history.enabled },
    [pscustomobject]@{ Name = 'Force pushes blocked'; Pass = (-not [bool]$FinalProtection.allow_force_pushes.enabled) },
    [pscustomobject]@{ Name = 'Branch deletion blocked'; Pass = (-not [bool]$FinalProtection.allow_deletions.enabled) },
    [pscustomobject]@{ Name = 'Conversations must be resolved'; Pass = [bool]$FinalProtection.required_conversation_resolution.enabled }
)

$Checks | Format-Table -AutoSize
$Failed = @($Checks | Where-Object { -not $_.Pass })
if ($Failed.Count -gt 0) {
    throw "Public hardening verification failed: $($Failed.Name -join '; ')"
}

Write-Host ''
Write-Host 'PASS — repository is public, sole-maintainer controlled, and main is protected.'
Write-Host "https://github.com/$Repo"
