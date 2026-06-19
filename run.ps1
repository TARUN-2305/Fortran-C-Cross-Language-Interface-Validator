# run.ps1 - Run FCValidator demonstration suite on Windows PowerShell

Write-Host "=== FCValidator Demonstration Suite (Windows PowerShell) ===" -ForegroundColor Cyan
Write-Host ""

# 1. Check if virtual environment exists
if (-not (Test-Path ".\.venv")) {
    Write-Error "Error: Virtual environment '.venv' not found. Please set up python venv first."
    Exit 1
}

# 2. Check for Python executable
$pythonExe = ".\.venv\Scripts\python.exe"
$fcvExe = ".\.venv\Scripts\fcv.exe"
$pytestExe = ".\.venv\Scripts\pytest.exe"

if (-not (Test-Path $fcvExe)) {
    Write-Error "Error: fcv executable not found in '.venv\Scripts\'. Please install the package in editable mode."
    Exit 1
}

Write-Host "==================================================" -ForegroundColor Yellow
Write-Host "DEMO 1: Hidden strlen bug (TC-A-001 - Failure Case)" -ForegroundColor Yellow
Write-Host "==================================================" -ForegroundColor Yellow
& $fcvExe validate fcv/tests/hard_pairs/TC-A-001_Single_character_flag_no_BIND_/interface.f90 fcv/tests/hard_pairs/TC-A-001_Single_character_flag_no_BIND_/header.h --severity warning
Write-Host "Exit Code: $LastExitCode" -ForegroundColor DarkGray
Write-Host ""

Write-Host "==================================================" -ForegroundColor Yellow
Write-Host "DEMO 2: INTEGER vs long (TC-B-001 - Failure Case)" -ForegroundColor Yellow
Write-Host "==================================================" -ForegroundColor Yellow
& $fcvExe validate fcv/tests/hard_pairs/TC-B-001_INTEGER_vs_long_on_LP64_Linux_/interface.f90 fcv/tests/hard_pairs/TC-B-001_INTEGER_vs_long_on_LP64_Linux_/header.h --severity warning
Write-Host "Exit Code: $LastExitCode" -ForegroundColor DarkGray
Write-Host ""

Write-Host "==================================================" -ForegroundColor Yellow
Write-Host "DEMO 3: Correct interface (TC-A-003 - Clean Case)" -ForegroundColor Yellow
Write-Host "==================================================" -ForegroundColor Yellow
& $fcvExe validate fcv/tests/hard_pairs/TC-A-003_Correct_BIND_C_version_of_TC_A/interface.f90 fcv/tests/hard_pairs/TC-A-003_Correct_BIND_C_version_of_TC_A/header.h --severity warning
Write-Host "Exit Code: $LastExitCode" -ForegroundColor DarkGray
Write-Host ""

Write-Host "==================================================" -ForegroundColor Yellow
Write-Host "DEMO 4: Running full Pytest suite (68 tests)" -ForegroundColor Yellow
Write-Host "==================================================" -ForegroundColor Yellow
& $pytestExe fcv/tests/ -v --tb=short
Write-Host ""

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "DEMO COMPLETE!" -ForegroundColor Cyan
Write-Host "Refer to DESIGN.md, IMPLEMENTATION.md and EVALUATION.md" -ForegroundColor Cyan
Write-Host "for comprehensive project details." -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
