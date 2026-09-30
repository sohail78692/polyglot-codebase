// ==========================================
// Program: Control Flow in F#
// ==========================================

let main () =
    // 1. Conditionals
    printfn "Conditionals:"
    let num = 15
    if num > 0 then
        if num % 2 = 0 then
            printfn "%d is Positive and Even" num
        else
            printfn "%d is Positive and Odd" num
    elif num < 0 then
        printfn "%d is Negative" num
    else
        printfn "Number is Zero"

    printfn "\nPattern Matching / Switch:"
    // 2. Match expression
    let grade = "B"
    let msg = 
        match grade with
        | "A" -> "Grade A: Excellent!"
        | "B" -> "Grade B: Good Job!"
        | "C" -> "Grade C: Fair"
        | _   -> "Keep Trying!"
    printfn "%s" msg

    // 3. For loop
    printfn "\nFor Loop (1 to 5):"
    for i in 1..5 do
        printf "%d%s" i (if i = 5 then "\n" else " ")

    // 4. While loop
    printfn "\nWhile Loop (Countdown):"
    let mutable count = 3
    while count > 0 do
        printf "%d " count
        count <- count - 1
    printfn "Blastoff!"

main ()
