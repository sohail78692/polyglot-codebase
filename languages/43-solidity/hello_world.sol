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
