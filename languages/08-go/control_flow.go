// ==========================================
// Program: Control Flow in Go
// ==========================================

package main

import "fmt"

func main() {
    // 1. Conditionals
    fmt.Println("Conditionals:")
    num := 15
    if num > 0 {
        if num%2 == 0 {
            fmt.Printf("%d is Positive and Even\n", num)
        } else {
            fmt.Printf("%d is Positive and Odd\n", num)
        }
    } else if num < 0 {
        fmt.Printf("%d is Negative\n", num)
    } else {
        fmt.Println("Number is Zero")
    }

    fmt.Println("\nPattern Matching / Switch:")
    // 2. Switch statement
    grade := "B"
    switch grade {
    case "A":
        fmt.Println("Grade A: Excellent!")
    case "B":
        fmt.Println("Grade B: Good Job!")
    case "C":
        fmt.Println("Grade C: Fair")
    default:
        fmt.Println("Keep Trying!")
    }

    // 3. For Loop
    fmt.Println("\nFor Loop (1 to 5):")
    for i := 1; i <= 5; i++ {
        if i == 5 {
            fmt.Println(i)
        } else {
            fmt.Printf("%d ", i)
        }
    }

    // 4. While-style Loop
    fmt.Println("\nWhile Loop (Countdown):")
    count := 3
    for count > 0 {
        fmt.Printf("%d ", count)
        count--
    }
    fmt.Println("Blastoff!")
}
