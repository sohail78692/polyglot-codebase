# ==========================================
# Program: Basic Operations in PowerShell (+, -, *, /, %)
# ==========================================
$a = 20
$b = 6

Write-Output "a = $a, b = $b"
Write-Output "Addition (a + b)        : $($a + $b)"
Write-Output "Subtraction (a - b)     : $($a - $b)"
Write-Output "Multiplication (a * b)  : $($a * $b)"
Write-Output "Division (a / b)        : $($a / $b)"
Write-Output "Integer Division ([int]): $([Math]::Floor($a / $b))"
Write-Output "Modulo (a % b)          : $($a % $b)"
