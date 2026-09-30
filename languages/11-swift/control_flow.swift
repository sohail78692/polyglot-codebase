// ==========================================
// Program: Control Flow in Swift
// ==========================================

import Foundation

func main() {
    // 1. Conditionals
    print("Conditionals:")
    let num = 15
    if num > 0 {
        if num % 2 == 0 {
            print("\(num) is Positive and Even")
        } else {
            print("\(num) is Positive and Odd")
        }
    } else if num < 0 {
        print("\(num) is Negative")
    } else {
        print("Number is Zero")
    }

    print("\nPattern Matching / Switch:")
    // 2. Switch
    let grade = "B"
    switch grade {
    case "A":
        print("Grade A: Excellent!")
    case "B":
        print("Grade B: Good Job!")
    case "C":
        print("Grade C: Fair")
    default:
        print("Keep Trying!")
    }

    // 3. For Loop with closed range
    print("\nFor Loop (1 to 5):")
    for i in 1...5 {
        print(i, terminator: i == 5 ? "\n" : " ")
    }

    // 4. While Loop
    print("\nWhile Loop (Countdown):")
    var count = 3
    while count > 0 {
        print(count, terminator: " ")
        count -= 1
    }
    print("Blastoff!")
}

main()
