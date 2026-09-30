# ==========================================
# Program: Control Flow in Julia
# ==========================================

function main()
    # 1. Conditionals
    println("Conditionals:")
    num = 15
    if num > 0
        if num % 2 == 0
            println("$num is Positive and Even")
        else
            println("$num is Positive and Odd")
        end
    elseif num < 0
        println("$num is Negative")
    else
        println("Number is Zero")
    end

    println("\nPattern Matching / Switch:")
    # 2. Branch matching
    grade = "B"
    msg = if grade == "A"
        "Grade A: Excellent!"
    elseif grade == "B"
        "Grade B: Good Job!"
    elseif grade == "C"
        "Grade C: Fair"
    else
        "Keep Trying!"
    end
    println(msg)

    # 3. For Loop
    println("\nFor Loop (1 to 5):")
    for i in 1:5
        print(i, i == 5 ? "\n" : " ")
    end

    # 4. While Loop
    println("\nWhile Loop (Countdown):")
    count = 3
    while count > 0
        print(count, " ")
        count -= 1
    end
    println("Blastoff!")
end

main()
