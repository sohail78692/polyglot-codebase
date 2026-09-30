// ==========================================
// Program: Control Flow in V (Vlang)
// ==========================================

fn main() {
    // 1. Conditionals
    println("Conditionals:")
    num := 15
    if num > 0 {
        if num % 2 == 0 {
            println("${num} is Positive and Even")
        } else {
            println("${num} is Positive and Odd")
        }
    } else if num < 0 {
        println("${num} is Negative")
    } else {
        println("Number is Zero")
    }

    println("\nPattern Matching / Switch:")
    // 2. Match Expression
    grade := "B"
    msg := match grade {
        "A" { "Grade A: Excellent!" }
        "B" { "Grade B: Good Job!" }
        "C" { "Grade C: Fair" }
        else { "Keep Trying!" }
    }
    println(msg)

    // 3. For Loop
    println("\nFor Loop (1 to 5):")
    for i in 1 .. 6 {
        print("${i}${if i == 5 { "\n" } else { " " }}")
    }

    // 4. While Loop (using 'for condition')
    println("\nWhile Loop (Countdown):")
    mut count := 3
    for count > 0 {
        print("${count} ")
        count--
    }
    println("Blastoff!")
}
