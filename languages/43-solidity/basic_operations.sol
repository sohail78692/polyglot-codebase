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
