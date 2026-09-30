# Lua Reference Guide

> **Category**: Shell & Scripting  
> **Paradigm**: Multi-paradigm (Scripting, procedural, prototype-based)  
> **Initial Release**: 1993  
> **Created By**: Roberto Ierusalimschy et al.  

---

## 1. Program 1: Hello World (`hello_world.lua`)

```lua
-- ==========================================
-- Program: Hello World in Lua
-- ==========================================
print("Hello, World!")
```

### Explanation
`print()` writes values to stdout.

### Run Hello World
```bash
lua hello_world.lua
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.lua`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```lua
-- ==========================================
-- Program: Basic Operations in Lua (+, -, *, /, //, %)
-- ==========================================
local a = 20
local b = 6

print(string.format("a = %d, b = %d", a, b))
print(string.format("Addition (a + b)        : %d", a + b))
print(string.format("Subtraction (a - b)     : %d", a - b))
print(string.format("Multiplication (a * b)  : %d", a * b))
print(string.format("Division (a / b)        : %f", a / b))
print(string.format("Integer Division (a // b): %d", a // b)) -- Lua 5.3+ integer division
print(string.format("Modulo (a %%%% b)          : %d", a % b))
```

### Explanation
Lua 5.3+ supports `//` for integer division and `%` for remainder.

### Run Basic Operations
```bash
lua basic_operations.lua
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.3333333333333
Integer Division (a // b): 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: lua.org

---

## 3. Program 3: Control Flow & Logic (`control_flow.lua`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```lua
-- ==========================================
-- Program: Control Flow in Lua
-- ==========================================

function main()
    -- 1. Conditionals
    print("Conditionals:")
    local num = 15
    if num > 0 then
        if num % 2 == 0 then
            print(num .. " is Positive and Even")
        else
            print(num .. " is Positive and Odd")
        end
    elseif num < 0 then
        print(num .. " is Negative")
    else
        print("Number is Zero")
    end

    print("\nPattern Matching / Switch:")
    -- 2. Table lookup (idiomatic Lua switch)
    local grade = "B"
    local switchTable = {
        A = "Grade A: Excellent!",
        B = "Grade B: Good Job!",
        C = "Grade C: Fair"
    }
    print(switchTable[grade] or "Keep Trying!")

    -- 3. Numeric For Loop (inclusive 1, 5)
    print("\nFor Loop (1 to 5):")
    local forItems = {}
    for i = 1, 5 do
        table.insert(forItems, i)
    end
    print(table.concat(forItems, " "))

    -- 4. While Loop
    print("\nWhile Loop (Countdown):")
    local count = 3
    local whileItems = {}
    while count > 0 do
        table.insert(whileItems, count)
        count = count - 1
    end
    table.insert(whileItems, "Blastoff!")
    print(table.concat(whileItems, " "))
end

main()
```

### Explanation
Demonstrates Lua `if/elseif/else`, table-lookup pattern matching (Lua idiom for switch), numeric `for` loop, and `while` loop.

### Run Control Flow
```bash
lua control_flow.lua
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
