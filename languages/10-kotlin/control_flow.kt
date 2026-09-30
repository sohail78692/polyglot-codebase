// ==========================================
// Program: Control Flow in Kotlin
// ==========================================

fun main() {
    // 1. Conditionals
    println("Conditionals:")
    val num = 15
    if (num > 0) {
        if (num % 2 == 0) {
            println("$num is Positive and Even")
        } else {
            println("$num is Positive and Odd")
        }
    } else if (num < 0) {
        println("$num is Negative")
    } else {
        println("Number is Zero")
    }

    println("\nPattern Matching / Switch:")
    // 2. When Expression
    val grade = "B"
    val result = when (grade) {
        "A" -> "Grade A: Excellent!"
        "B" -> "Grade B: Good Job!"
        "C" -> "Grade C: Fair"
        else -> "Keep Trying!"
    }
    println(result)

    // 3. For Loop with range 1..5
    println("\nFor Loop (1 to 5):")
    for (i in 1..5) {
        print(if (i == 5) "$i\n" else "$i ")
    }

    // 4. While Loop
    println("\nWhile Loop (Countdown):")
    var count = 3
    while (count > 0) {
        print("$count ")
        count--
    }
    println("Blastoff!")
}
