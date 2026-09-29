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
