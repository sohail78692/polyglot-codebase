# TypeScript Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (Static typed superset of JavaScript)  
> **Initial Release**: 2012  
> **Created By**: Anders Hejlsberg (Microsoft)  

---

## 1. Program 1: Hello World (`hello_world.ts`)

```ts
// ==========================================
// Program: Hello World in TypeScript
// ==========================================

function greet(message: string): void {
    console.log(message);
}

greet("Hello, World!");
```

### Explanation
TypeScript enforces parameter types (`: string`) and return types (`: void`).

### Run Hello World
```bash
npx ts-node hello_world.ts
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.ts`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```ts
// ==========================================
// Program: Basic Operations in TypeScript (+, -, *, /, %)
// ==========================================

function calculate(a: number, b: number): void {
    console.log(`a = ${a}, b = ${b}`);
    console.log(`Addition (a + b)        : ${a + b}`);
    console.log(`Subtraction (a - b)     : ${a - b}`);
    console.log(`Multiplication (a * b)  : ${a * b}`);
    console.log(`Division (a / b)        : ${a / b}`);
    console.log(`Integer Division        : ${Math.floor(a / b)}`);
    console.log(`Modulo (a % b)          : ${a % b}`);
}

calculate(20, 6);
```

### Explanation
TypeScript provides static type safety for numeric variables (`: number`) with standard math operators.

### Run Basic Operations
```bash
npx ts-node basic_operations.ts
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.3333333333333335
Integer Division        : 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: `npm install -g typescript ts-node` or `npx ts-node`
