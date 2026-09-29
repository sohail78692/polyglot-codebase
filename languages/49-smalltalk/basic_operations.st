"==========================================
 Program: Basic Operations in Smalltalk (+, -, *, //, \\)
 =========================================="
| a b |
a := 20.
b := 6.

Transcript show: 'a = 20, b = 6'; cr.
Transcript show: 'Addition (a + b)        : ', (a + b) printString; cr.
Transcript show: 'Subtraction (a - b)     : ', (a - b) printString; cr.
Transcript show: 'Multiplication (a * b)  : ', (a * b) printString; cr.
Transcript show: 'Integer Division (//)   : ', (a // b) printString; cr.
Transcript show: 'Exact Fraction (/)      : ', (a / b) printString; cr.
Transcript show: 'Modulo (\\)             : ', (a \\ b) printString; cr.
