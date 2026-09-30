; ==========================================
; Program: Basic Operations in x86_64 Assembly (NASM)
; Demonstrates CPU instructions: add, sub, imul, idiv
; ==========================================
section .data
    msg db "a = 20, b = 6", 10
        db "Addition: 26, Subtraction: 14, Multiplication: 120, Division: 3, Modulo: 2", 10
    len equ $ - msg

section .text
    global _start

_start:
    ; a = 20, b = 6
    ; 1. Addition (20 + 6 = 26)
    mov r12, 20
    add r12, 6

    ; 2. Subtraction (20 - 6 = 14)
    mov r13, 20
    sub r13, 6

    ; 3. Multiplication (20 * 6 = 120)
    mov rax, 20
    imul rax, 6
    mov r14, rax

    ; 4. Division & Modulo (20 / 6 -> quotient 3, remainder 2)
    mov rax, 20
    cqo
    mov rbx, 6
    idiv rbx
    mov r15, rax
    mov rbx, rdx

    ; sys_write stdout
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    ; sys_exit 0
    mov rax, 60
    xor rdi, rdi
    syscall
