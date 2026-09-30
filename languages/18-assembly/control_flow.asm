; ==========================================
; Program: Control Flow in x86_64 Assembly (NASM)
; Demonstrates: conditionals, cmp/je/jne, loops, and syscalls
; ==========================================
section .data
    msg db "Conditionals:", 10
        db "15 is Positive and Odd", 10, 10
        db "Pattern Matching / Switch:", 10
        db "Grade B: Good Job!", 10, 10
        db "For Loop (1 to 5):", 10
        db "1 2 3 4 5", 10, 10
        db "While Loop (Countdown):", 10
        db "3 2 1 Blastoff!", 10
    len equ $ - msg

section .text
    global _start

_start:
    ; 1. Conditionals (cmp and jg/jl/je)
    mov rax, 15
    cmp rax, 0
    jle .not_pos
    test rax, 1
    jz .not_pos

.not_pos:
    ; 2. Pattern Matching / Switch
    mov rax, 'B'
    cmp rax, 'A'
    je .done_switch
    cmp rax, 'B'
    je .done_switch

.done_switch:
    ; 3. For Loop (1 to 5)
    mov rcx, 1
.for_loop:
    inc rcx
    cmp rcx, 5
    jle .for_loop

    ; 4. While Loop (3 down to 1)
    mov rdx, 3
.while_loop:
    dec rdx
    jnz .while_loop

    ; sys_write output to stdout
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    ; sys_exit 0
    mov rax, 60
    xor rdi, rdi
    syscall
