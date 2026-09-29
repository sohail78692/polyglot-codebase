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
