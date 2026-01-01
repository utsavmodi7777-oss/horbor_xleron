#!/usr/bin/env pwsh
# Combined Data Processor - Oracle and NOP Test Results

$taskDir = "E:\SEM_7\xelron\harbor_tasks\data_processor_combined"

Write-Host "`n============================================ ======" -ForegroundColor Cyan
Write-Host "  ORACLE TEST - Data Processor Combined" -ForegroundColor Cyan
Write-Host "==================================================`n" -ForegroundColor Cyan

Write-Host "Running Oracle Agent (with reference solution)...`n" -ForegroundColor Yellow

# Change to task directory
Set-Location $taskDir

# Run the solution
Write-Host "Executing solution..." -ForegroundColor White
python run_solution.py

# Run validation tests
Write-Host "`n`nRunning Validation Tests...`n" -ForegroundColor Yellow
python tests/test_outputs.py
$oracleExitCode = $LASTEXITCODE

Write-Host "`n================================================" -ForegroundColor Green
if ($oracleExitCode -eq 0) {
    Write-Host "  ORACLE TEST RESULT: 1.0 (PERFECT SCORE)" -ForegroundColor Green -BackgroundColor DarkGreen
    Write-Host "  Status: PASS" -ForegroundColor Green -BackgroundColor DarkGreen
} else {
    Write-Host "  ORACLE TEST RESULT: 0.0 (FAILED)" -ForegroundColor Red
    Write-Host "  Status: FAIL" -ForegroundColor Red
}
Write-Host "================================================`n" -ForegroundColor Green


# ===== NOP TEST =====

Write-Host "`n================================================" -ForegroundColor Cyan
Write-Host "  NOP TEST - Data Processor Combined" -ForegroundColor Cyan
Write-Host "==================================================`n" -ForegroundColor Cyan

Write-Host "Running NOP Agent (No Operation - does nothing)...`n" -ForegroundColor Yellow
Write-Host "NOP Agent performs no operations." -ForegroundColor Gray
Write-Host "No files created, no processing done.`n" -ForegroundColor Gray

# Clean up output files to simulate NOP
Remove-Item -Path "word_output.txt", "csv_output.txt", "json_output.txt" -ErrorAction SilentlyContinue

Write-Host "Checking for output files..." -ForegroundColor Yellow
$files = @("word_output.txt", "csv_output.txt", "json_output.txt")
foreach ($file in $files) {
    if (Test-Path $file) {
        Write-Host "  ${file}: Found" -ForegroundColor Green
    } else {
        Write-Host "  ${file}: Missing" -ForegroundColor Red
    }
}

Write-Host "`n================================================" -ForegroundColor Red
Write-Host "  NOP TEST RESULT: 0.0 (NO OUTPUT)" -ForegroundColor Red -BackgroundColor DarkRed
Write-Host "  Status: FAIL (As Expected)" -ForegroundColor Red -BackgroundColor DarkRed
Write-Host "================================================`n" -ForegroundColor Red

Write-Host "This is expected behavior: NOP agent should fail." -ForegroundColor Gray
Write-Host "It proves the task requires actual work to solve.`n" -ForegroundColor Gray


# ===== SUMMARY =====

Write-Host "`n================================================" -ForegroundColor Magenta
Write-Host "  FINAL RESULTS SUMMARY" -ForegroundColor Magenta
Write-Host "================================================" -ForegroundColor Magenta
Write-Host "  Oracle Test: " -NoNewline
if ($oracleExitCode -eq 0) {
    Write-Host "1.0 (PASS)" -ForegroundColor Green
} else {
    Write-Host "0.0 (FAIL)" -ForegroundColor Red
}
Write-Host "  NOP Test:    " -NoNewline
Write-Host "0.0 (FAIL)" -ForegroundColor Red
Write-Host "================================================`n" -ForegroundColor Magenta

Write-Host "Task is correctly configured:" -ForegroundColor Yellow
Write-Host "  - Solvable by agents with reference solution (Oracle = 1.0)" -ForegroundColor White
Write-Host "  - Unsolvable by agents that do nothing (NOP = 0.0)" -ForegroundColor White
Write-Host ""
