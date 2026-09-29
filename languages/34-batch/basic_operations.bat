@echo off
rem ==========================================
rem Program: Basic Operations in Windows Batch (+, -, *, /, %%)
rem ==========================================
set a=20
set b=6

set /a add=a+b
set /a sub=a-b
set /a mul=a*b
set /a div=a/b
set /a mod=a%%b

echo a = %a%, b = %b%
echo Addition (a + b)        : %add%
echo Subtraction (a - b)     : %sub%
echo Multiplication (a * b)  : %mul%
echo Integer Division (a / b): %div%
echo Modulo (a %%%% b)          : %mod%
