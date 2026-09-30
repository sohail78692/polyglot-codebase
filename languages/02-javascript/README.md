# JavaScript Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (Event-driven, functional, imperative)  
> **Initial Release**: 1995  
> **Created By**: Brendan Eich  

---

## 1. Program 1: Hello World (`hello_world.js`)

```js
// ==========================================
// Program: Hello World in JavaScript (Node.js)
// ==========================================

function main() {
    console.log("Hello, World!");
}

main();
```

### Explanation
`console.log()` sends text to standard output.

### Run Hello World
```bash
node hello_world.js
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.js`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```js
// ==========================================
// Program: Basic Operations in JavaScript (+, -, *, /, %)
// ==========================================

function main() {
    const a = 20;
    const b = 6;

    console.log(`a = ${a}, b = ${b}`);
    console.log(`Addition (a + b)        : ${a + b}`);
    console.log(`Subtraction (a - b)     : ${a - b}`);
    console.log(`Multiplication (a * b)  : ${a * b}`);
    console.log(`Division (a / b)        : ${a / b}`);
    console.log(`Integer Division        : ${Math.floor(a / b)}`);
    console.log(`Modulo (a % b)          : ${a % b}`);
}

main();
```

### Explanation
JavaScript uses standard operators: `+`, `-`, `*`, `/`, and `%`. For integer division, `Math.floor()` truncates decimals.

### Run Basic Operations
```bash
node basic_operations.js
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

- **Guide**: nodejs.org or `winget install OpenJS.NodeJS` / `brew install node` / `apt install nodejs`

---

## 3. Program 3: Control Flow & Logic (`control_flow.js`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```js
// ==========================================
// Program: Control Flow in JavaScript
// ==========================================

function main() {
    // 1. Conditionals (if / else if / else)
    console.log("Conditionals:");
    const num = 15;
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
    // 2. Switch Statement
    const grade = "B";
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
    let forResult = [];
    for (let i = 1; i <= 5; i++) {
        forResult.push(i);
    }
    console.log(forResult.join(" "));

    // 4. While Loop
    console.log("\nWhile Loop (Countdown):");
    let count = 3;
    let whileResult = [];
    while (count > 0) {
        whileResult.push(count);
        count--;
    }
    whileResult.push("Blastoff!");
    console.log(whileResult.join(" "));
}

main();
```

### Explanation
Demonstrates `if/else if/else` statements, `switch/case` multi-branching, indexed `for` loop, and `while` loop countdown.

### Run Control Flow
```bash
node control_flow.js
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
