#!/usr/bin/env bash
# ==========================================
# Program: Control Flow in Bash
# ==========================================

main() {
    # 1. Conditionals
    echo "Conditionals:"
    num=15
    if (( num > 0 )); then
        if (( num % 2 == 0 )); then
            echo "${num} is Positive and Even"
        else
            echo "${num} is Positive and Odd"
        fi
    elif (( num < 0 )); then
        echo "${num} is Negative"
    else
        echo "Number is Zero"
    fi

    echo ""
    echo "Pattern Matching / Switch:"
    # 2. Case statement
    grade="B"
    case "$grade" in
        "A") echo "Grade A: Excellent!" ;;
        "B") echo "Grade B: Good Job!" ;;
        "C") echo "Grade C: Fair" ;;
        *)   echo "Keep Trying!" ;;
    esac

    echo ""
    echo "For Loop (1 to 5):"
    # 3. For loop
    for (( i = 1; i <= 5; i++ )); do
        if (( i == 5 )); then
            echo "$i"
        else
            printf "%d " "$i"
        fi
    done

    echo ""
    echo "While Loop (Countdown):"
    # 4. While loop
    count=3
    while (( count > 0 )); do
        printf "%d " "$count"
        (( count-- ))
    done
    echo "Blastoff!"
}

main
