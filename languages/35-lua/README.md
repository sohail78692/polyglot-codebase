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
