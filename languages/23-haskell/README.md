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
