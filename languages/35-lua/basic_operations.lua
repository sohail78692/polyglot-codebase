-- ==========================================
-- Program: Basic Operations in Lua (+, -, *, /, //, %)
-- ==========================================
local a = 20
local b = 6

print(string.format("a = %d, b = %d", a, b))
print(string.format("Addition (a + b)        : %d", a + b))
print(string.format("Subtraction (a - b)     : %d", a - b))
print(string.format("Multiplication (a * b)  : %d", a * b))
print(string.format("Division (a / b)        : %f", a / b))
print(string.format("Integer Division (a // b): %d", a // b)) -- Lua 5.3+ integer division
print(string.format("Modulo (a %%%% b)          : %d", a % b))
