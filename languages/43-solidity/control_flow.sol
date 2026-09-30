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
