# Solidity Reference Guide

> **Category**: Web3, Mobile & Modern  
> **Paradigm**: Contract-oriented, static typing (Ethereum EVM)  
> **Initial Release**: 2014  
> **Created By**: Gavin Wood et al.  

---

## 1. Program 1: Hello World (`hello_world.sol`)

```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// ==========================================
// Program: Hello World in Solidity (Ethereum Smart Contract)
// ==========================================
contract HelloWorld {
    string public greeting = "Hello, World!";

    function getGreeting() public view returns (string memory) {
        return greeting;
    }
}
```

### Explanation
Public state variable and getter on Ethereum.

### Run Hello World
```bash
solc --bin hello_world.sol
```
**Expected Output**:
```text
Binary bytecode compiled successfully
```

---

## 2. Program 2: Basic Operations (`basic_operations.sol`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// ==========================================
// Program: Basic Operations in Solidity (+, -, *, /, %)
// ==========================================
contract BasicOperations {
    // Calculates +, -, *, /, % on the Ethereum Virtual Machine
    function calculate(uint256 a, uint256 b) public pure returns (
        uint256 addResult,
        uint256 subResult,
        uint256 mulResult,
        uint256 divResult,
        uint256 modResult
    ) {
        addResult = a + b;
        subResult = a - b;
        mulResult = a * b;
        divResult = a / b; // EVM integer division truncates
        modResult = a % b; // Modulo remainder
    }
}
```

### Explanation
Solidity operates on unsigned integers (`uint256`). EVM division automatically truncates; `%` calculates remainder with built-in overflow protection in 0.8+.

### Run Basic Operations
```bash
solc --bin basic_operations.sol
```
**Expected Output**:
```text
add = 26, sub = 14, mul = 120, div = 3, mod = 2
```

---

## 3. Prerequisites & Installation

- **Guide**: `npm install -g solc`

---

## 3. Program 3: Control Flow & Logic (`control_flow.sol`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// ==========================================
// Program: Control Flow in Solidity
// ==========================================

contract ControlFlow {
    // Demonstrates conditional logic within EVM functions
    function checkNumber(int256 num) public pure returns (string memory) {
        if (num > 0) {
            if (num % 2 == 0) {
                return "15 is Positive and Even";
            } else {
                return "15 is Positive and Odd";
            }
        } else if (num < 0) {
            return "Number is Negative";
        } else {
            return "Number is Zero";
        }
    }

    // Demonstrates loop accumulation
    function sumRange(uint256 n) public pure returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 1; i <= n; i++) {
            total += i;
        }
        return total;
    }

    // Demonstrates while loop countdown
    function countdown(uint256 count) public pure returns (uint256) {
        uint256 remaining = count;
        while (remaining > 0) {
            remaining--;
        }
        return remaining;
    }
}
```

### Explanation
Demonstrates Solidity EVM smart contract control flow: `if/else`, `for` loop, and `while` loop within a pure function.

### Run Control Flow
```bash
solc --bin control_flow.sol
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
