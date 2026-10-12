param([Parameter(Mandatory=$true)][string[]]$GitArgs)
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path $PSScriptRoot -Parent
$evidencePath = Join-Path $repoRoot 'docs\evidence\git_commands.txt'
$commandText = 'git ' + ($GitArgs -join ' ')
Add-Content -LiteralPath $evidencePath -Value "`n> $commandText"
$output = & git -C $repoRoot @GitArgs 2>&1
$exitCode = $LASTEXITCODE
$output | Out-String | Add-Content -LiteralPath $evidencePath
$output
Add-Content -LiteralPath $evidencePath -Value "Exit code: $exitCode"
exit $exitCode
