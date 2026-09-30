# ==========================================
# Program: Control Flow in PowerShell
# ==========================================

function Main {
    # 1. Conditionals
    Write-Host "Conditionals:"
    $num = 15
    if ($num -gt 0) {
        if ($num % 2 -eq 0) {
            Write-Host "$num is Positive and Even"
        } else {
            Write-Host "$num is Positive and Odd"
        }
    } elseif ($num -lt 0) {
        Write-Host "$num is Negative"
    } else {
        Write-Host "Number is Zero"
    }

    Write-Host "`nPattern Matching / Switch:"
    # 2. Switch Statement
    $grade = "B"
    switch ($grade) {
        "A" { Write-Host "Grade A: Excellent!" }
        "B" { Write-Host "Grade B: Good Job!" }
        "C" { Write-Host "Grade C: Fair" }
        default { Write-Host "Keep Trying!" }
    }

    # 3. For Loop
    Write-Host "`nFor Loop (1 to 5):"
    $forItems = for ($i = 1; $i -le 5; $i++) { $i }
    Write-Host ($forItems -join " ")

    # 4. While Loop
    Write-Host "`nWhile Loop (Countdown):"
    $count = 3
    $whileItems = while ($count -gt 0) {
        $count
        $count--
    }
    Write-Host (($whileItems -join " ") + " Blastoff!")
}

Main
