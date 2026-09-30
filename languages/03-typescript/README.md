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

---

## 3. Program 3: Control Flow & Logic (`control_flow.ts`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```ts
// ==========================================
// Program: Control Flow in TypeScript
// ==========================================

function main(): void {
    // 1. Conditionals
    console.log("Conditionals:");
    const num: number = 15;
    if (num > 0) {
        if (num % 2 === 0) {
            console.log(`${num} is Positive and Even`);
        } else {
            console.log(`${num} is Positive and Odd`);
        }
    } else if (num < 0) {
        console.log(`${num} is Negative`);
    } else {
        console.log("Number is Zero");
    }

    console.log("\nPattern Matching / Switch:");
    type Grade = "A" | "B" | "C" | "F";
    const grade: Grade = "B";
    switch (grade) {
        case "A":
            console.log("Grade A: Excellent!");
            break;
        case "B":
            console.log("Grade B: Good Job!");
            break;
        case "C":
            console.log("Grade C: Fair");
            break;
        default:
            console.log("Keep Trying!");
    }

    // 3. For Loop
    console.log("\nFor Loop (1 to 5):");
    const forItems: number[] = [];
    for (let i: number = 1; i <= 5; i++) {
        forItems.push(i);
    }
    console.log(forItems.join(" "));

    // 4. While Loop
    console.log("\nWhile Loop (Countdown):");
    let count: number = 3;
    const countdown: string[] = [];
    while (count > 0) {
        countdown.push(count.toString());
        count--;
    }
    countdown.push("Blastoff!");
    console.log(countdown.join(" "));
}

main();
```

### Explanation
Demonstrates typed conditional branching, exhaustive `switch` statements, `for` iteration, and `while` loop.

### Run Control Flow
```bash
ts-node control_flow.ts
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
