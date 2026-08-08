$ErrorActionPreference = "Stop"

$Owner = "chriskulbaba2025"
$Repo = "governed-coding-upgrade-skill"
$FullRepo = "$Owner/$Repo"
$Description = "Deterministic governance protocol for AI-assisted software changes with frozen scope, executable proof, exact-head audit, and evidence-based release."

Write-Host "Validating local package..."
python scripts/validate-package.py
if ($LASTEXITCODE -ne 0) { throw "Package validation failed." }

Write-Host "Verifying GitHub authentication..."
gh auth status
if ($LASTEXITCODE -ne 0) { throw "GitHub CLI is not authenticated." }

cmd /c "gh repo view $FullRepo --json nameWithOwner >nul 2>nul"
if ($LASTEXITCODE -eq 0) {
    throw "Repository $FullRepo already exists. No changes were pushed."
}

if (-not (Test-Path ".git")) {
    git init -b main
    git config user.name "Chris Kulbaba"
    git config user.email "196350408+chriskulbaba2025@users.noreply.github.com"
    git add .
    git commit -m "chore: initialize governed coding upgrade skill v1.0.0"
}

Write-Host "Creating private GitHub repository..."
gh repo create $FullRepo --private --source=. --remote=origin --push --description $Description --disable-wiki

Write-Host "Applying professional repository settings..."
gh repo edit $FullRepo `
  --enable-issues `
  --enable-wiki=false `
  --enable-projects=false `
  --enable-squash-merge `
  --enable-merge-commit=false `
  --enable-rebase-merge=false `
  --delete-branch-on-merge `
  --add-topic ai-coding `
  --add-topic coding-agents `
  --add-topic software-governance `
  --add-topic code-quality `
  --add-topic claude-code `
  --add-topic deterministic-testing `
  --add-topic audit `
  --add-topic ci-cd `
  --add-topic software-engineering `
  --add-topic agentic-development

Write-Host "Creating repository labels..."
gh label create governance --repo $FullRepo --color 0F766E --description "Changes to governance rules, gates, or protocol" --force
gh label create defect --repo $FullRepo --color B91C1C --description "Reproducible defect in the skill, templates, or validation" --force

Write-Host "Verifying remote repository..."
gh repo view $FullRepo --json nameWithOwner,url,isPrivate,defaultBranchRef,description,repositoryTopics

Write-Host "DONE: https://github.com/$FullRepo"
