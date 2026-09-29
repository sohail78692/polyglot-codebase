// ==========================================
// Program: Basic Operations in Go (+, -, *, /, %)
// ==========================================
package main

import "fmt"

func main() {
    a := 20
    b := 6

    fmt.Printf("a = %d, b = %d\n", a, b)
    fmt.Printf("Addition (a + b)        : %d\n", a + b)
    fmt.Printf("Subtraction (a - b)     : %d\n", a - b)
    fmt.Printf("Multiplication (a * b)  : %d\n", a * b)
    fmt.Printf("Integer Division (a / b): %d\n", a / b)
    fmt.Printf("Float Division (float64): %f\n", float64(a) / float64(b))
    fmt.Printf("Modulo (a % b)          : %d\n", a % b)
}
