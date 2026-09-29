! ==========================================
! Program: Basic Operations in Modern Fortran (+, -, *, /, mod)
! ==========================================
program basic_operations
    implicit none
    integer :: a, b

    a = 20
    b = 6

    print *, "a = 20, b = 6"
    print *, "Addition (a + b)        : ", a + b
    print *, "Subtraction (a - b)     : ", a - b
    print *, "Multiplication (a * b)  : ", a * b
    print *, "Integer Division (a / b): ", a / b
    print *, "Float Division (real)   : ", real(a) / real(b)
    print *, "Modulo (mod(a, b))      : ", mod(a, b)
end program basic_operations
