; ==========================================
; Program: Basic Operations in x86_64 Assembly (NASM + printf)
; Demonstrates CPU instructions: add, sub, imul, idiv
; ==========================================
section .data
    fmt db "a = 20, b = 6", 10
        db "Addition: %d, Subtraction: %d, Multiplication: %d, Division: %d, Modulo: %d", 10, 0

section .text
    global main
    extern printf

main:
    push rbp
    mov rbp, rsp

    ; a = 20, b = 6
    ; 1. Addition (20 + 6 = 26)
    mov r12, 20
    add r12, 6          ; r12 = 26

    ; 2. Subtraction (20 - 6 = 14)
    mov r13, 20
    sub r13, 6          ; r13 = 14

    ; 3. Multiplication (20 * 6 = 120)
    mov rax, 20
    imul rax, 6         ; rax = 120
    mov r14, rax

    ; 4. Division & Modulo (20 / 6 -> quotient 3, remainder 2)
    mov rax, 20
    cqo                 ; Sign-extend rax into rdx:rax
    mov rbx, 6
    idiv rbx            ; rax = quotient (3), rdx = remainder (2)
    mov r15, rax        ; r15 = 3 (division)
    mov rbx, rdx        ; rbx = 2 (modulo)

    ; Print results via printf(fmt, add, sub, mul, div, mod)
    mov rdi, fmt
    mov rsi, r12
    mov rdx, r13
    mov rcx, r14
    mov r8, r15
    mov r9, rbx
    xor eax, eax
    call printf

    xor eax, eax
    leave
    ret
