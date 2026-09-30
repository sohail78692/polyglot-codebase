# Haskell Reference Guide

> **Category**: Functional & Declarative  
> **Paradigm**: Purely functional, lazy evaluation  
> **Initial Release**: 1990  
> **Created By**: Simon Peyton Jones et al.  

---

## 1. Program 1: Hello World (`hello_world.hs`)

```hs
-- ==========================================
-- Program: Hello World in Haskell
-- ==========================================
main :: IO ()
main = putStrLn "Hello, World!"
```

### Explanation
Haskell uses `putStrLn` to output strings in the `IO` monad.

### Run Hello World
```bash
runhaskell hello_world.hs
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.hs`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```hs
-- ==========================================
-- Program: Basic Operations in Haskell (+, -, *, div, mod, /)
-- ==========================================
main :: IO ()
main = do
    let a = 20 :: Int
    let b = 6 :: Int
    putStrLn "a = 20, b = 6"
    putStrLn ("Addition (a + b)        : " ++ show (a + b))
    putStrLn ("Subtraction (a - b)     : " ++ show (a - b))
    putStrLn ("Multiplication (a * b)  : " ++ show (a * b))
    putStrLn ("Integer Division (div)  : " ++ show (a `div` b))
    putStrLn ("Float Division (/)      : " ++ show (fromIntegral a / fromIntegral b))
    putStrLn ("Modulo (mod)            : " ++ show (a `mod` b))
```

### Explanation
Haskell uses backticks for infix functions like `` `div` `` and `` `mod` ``. `fromIntegral` converts Int to Fractional.

### Run Basic Operations
```bash
runhaskell basic_operations.hs
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (div)  : 3
Float Division (/)      : 3.3333333333333335
Modulo (mod)            : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: GHC / ghcup

---

## 3. Program 3: Control Flow & Logic (`control_flow.hs`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```hs
-- ==========================================
-- Program: Control Flow in Haskell
-- ==========================================

countdown :: Int -> IO ()
countdown 0 = putStrLn "Blastoff!"
countdown n = do
    putStr (show n ++ " ")
    countdown (n - 1)

main :: IO ()
main = do
    -- 1. Conditionals (if then else expressions)
    putStrLn "Conditionals:"
    let num = 15 :: Int
    putStrLn $ if num > 0
               then if num `mod` 2 == 0
                    then show num ++ " is Positive and Even"
                    else show num ++ " is Positive and Odd"
               else if num < 0
                    then show num ++ " is Negative"
                    else "Number is Zero"

    putStrLn "\nPattern Matching / Switch:"
    -- 2. Case Expression (Pattern Matching)
    let grade = 'B'
    let msg = case grade of
                'A' -> "Grade A: Excellent!"
                'B' -> "Grade B: Good Job!"
                'C' -> "Grade C: Fair"
                _   -> "Keep Trying!"
    putStrLn msg

    -- 3. Loop via List mapping (unwords)
    putStrLn "\nFor Loop (1 to 5):"
    putStrLn $ unwords (map show [1..5])

    -- 4. While Loop via recursion
    putStrLn "\nWhile Loop (Countdown):"
    countdown 3
```

### Explanation
Demonstrates pure functional branching via `if/then/else`, `case ... of` pattern matching, and recursion / list mapping for loops.

### Run Control Flow
```bash
runghc control_flow.hs
```
**Expected Output**:
```text
Conditionals:
15 is Positive and Odd

Pattern Matching / Switch:
Grade B: Good Job!

For Loop (1 to 5):
1 2 3 4 5

While Loop (Countdown):
3 2 1 Blastoff!
```
