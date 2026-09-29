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
