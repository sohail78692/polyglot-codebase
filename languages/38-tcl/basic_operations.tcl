# ==========================================
# Program: Basic Operations in Tcl (+, -, *, /, %)
# ==========================================
set a 20
set b 6

puts "a = $a, b = $b"
puts "Addition (a + b)        : [expr {$a + $b}]"
puts "Subtraction (a - b)     : [expr {$a - $b}]"
puts "Multiplication (a * b)  : [expr {$a * $b}]"
puts "Integer Division (a / b): [expr {$a / $b}]"
puts "Float Division          : [expr {double($a) / $b}]"
puts "Modulo (a % b)          : [expr {$a % $b}]"
