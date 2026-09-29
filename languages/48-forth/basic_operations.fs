\ ==========================================
\ Program: Basic Operations in Forth (+, -, *, /, MOD)
\ ==========================================
: OPERATIONS ( -- )
  ." a = 20, b = 6" CR
  ." Addition: " 20 6 + . CR
  ." Subtraction: " 20 6 - . CR
  ." Multiplication: " 20 6 * . CR
  ." Division: " 20 6 / . CR
  ." Modulo: " 20 6 MOD . CR ;

OPERATIONS
