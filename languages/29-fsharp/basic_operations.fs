// ==========================================
// Program: Basic Operations in F# (+, -, *, /, %)
// ==========================================
let a = 20
let b = 6

printfn "a = %d, b = %d" a b
printfn "Addition (a + b)        : %d" (a + b)
printfn "Subtraction (a - b)     : %d" (a - b)
printfn "Multiplication (a * b)  : %d" (a * b)
printfn "Integer Division (a / b): %d" (a / b)
printfn "Float Division (float)  : %f" (float a / float b)
printfn "Modulo (a %% b)          : %d" (a % b)
