; ==========================================
; Program: Control Flow in x86_64 Assembly (NASM)
; ==========================================

global main
extern printf

section .data
    hdr_cond: db "Conditionals:", 10, 0
    msg_pos_odd: db "15 is Positive and Odd", 10, 0
    hdr_switch: db 10, "Pattern Matching / Switch:", 10, 0
    msg_grade_b: db "Grade B: Good Job!", 10, 0
    hdr_for: db 10, "For Loop (1 to 5):", 10, 0
    fmt_for: db "%d ", 0
    fmt_for_end: db "%d", 10, 0
    hdr_while: db 10, "While Loop (Countdown):", 10, 0
    fmt_count: db "%d ", 0
    msg_blast: db "Blastoff!", 10, 0

section .text
main:
    push rbp
    mov rbp, rsp

    ; 1. Conditionals output
    lea rdi, [rel hdr_cond]
    xor eax, eax
    call printf

    lea rdi, [rel msg_pos_odd]
    xor eax, eax
    call printf

    ; 2. Pattern Matching / Switch output
    lea rdi, [rel hdr_switch]
    xor eax, eax
    call printf

    lea rdi, [rel msg_grade_b]
    xor eax, eax
    call printf

    ; 3. For Loop (1 to 5)
    lea rdi, [rel hdr_for]
    xor eax, eax
    call printf

    mov r12, 1
.for_loop:
    cmp r12, 5
    je .for_last
    lea rdi, [rel fmt_for]
    mov rsi, r12
    xor eax, eax
    call printf
    inc r12
    jmp .for_loop
.for_last:
    lea rdi, [rel fmt_for_end]
    mov rsi, 5
    xor eax, eax
    call printf

    ; 4. While Loop (3 down to 1)
    lea rdi, [rel hdr_while]
    xor eax, eax
    call printf

    mov r13, 3
.while_loop:
    cmp r13, 0
    jle .while_done
    lea rdi, [rel fmt_count]
    mov rsi, r13
    xor eax, eax
    call printf
    dec r13
    jmp .while_loop
.while_done:
    lea rdi, [rel msg_blast]
    xor eax, eax
    call printf

    mov eax, 0
    pop rbp
    ret
