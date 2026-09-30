# ==========================================
# Program: Control Flow in Nim
# ==========================================

proc main() =
    # 1. Conditionals
    echo "Conditionals:"
    let num = 15
    if num > 0:
        if num mod 2 == 0:
            echo $num & " is Positive and Even"
        else:
            echo $num & " is Positive and Odd"
    elif num < 0:
        echo $num & " is Negative"
    else:
        echo "Number is Zero"

    echo "\nPattern Matching / Switch:"
    # 2. Case Statement
    let grade = "B"
    case grade
    of "A":
        echo "Grade A: Excellent!"
    of "B":
        echo "Grade B: Good Job!"
    of "C":
        echo "Grade C: Fair"
    else:
        echo "Keep Trying!"

    # 3. For Loop with range 1..5
    echo "\nFor Loop (1 to 5):"
    for i in 1..5:
        stdout.write($i & (if i == 5: "\n" else: " "))

    # 4. While Loop
    echo "\nWhile Loop (Countdown):"
    var count = 3
    while count > 0:
        stdout.write($count & " ")
        count -= 1
    echo "Blastoff!"

main()
