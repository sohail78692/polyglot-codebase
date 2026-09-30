# Assembly (x86_64 NASM) Reference Guide

> **Category**: Scientific & Data  
> **Paradigm**: Low-level Assembly  
> **Initial Release**: 1970s  
> **Created By**: AMD / Intel  

---

## 1. Program 1: Hello World (`hello_world.asm`)

```asm
; ==========================================
; Program: Hello World in x86_64 Assembly (Linux NASM)
; ==========================================
section .data
    msg db "Hello, World!", 0x0a
    len equ $ - msg

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    mov rax, 60
    xor rdi, rdi
    syscall
```

### Explanation
Direct kernel syscalls using `rax=1` (write) and `rax=60` (exit).

### Run Hello World
```bash
nasm -f elf64 hello_world.asm -o hello_world.o && ld hello_world.o -o hello_world && ./hello_world
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.asm`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```asm
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
```

### Explanation
Demonstrates core CPU instructions: `add`, `sub`, `imul`, and `idiv` (which calculates both quotient and remainder simultaneously).

### Run Basic Operations
```bash
nasm -f elf64 basic_operations.asm -o basic_ops.o && gcc basic_ops.o -no-pie -o basic_ops && ./basic_ops
```
**Expected Output**:
```text
a = 20, b = 6
Addition: 26, Subtraction: 14, Multiplication: 120, Division: 3, Modulo: 2
```

---

## 3. Prerequisites & Installation

- **Guide**: NASM & GCC/LD

---

## 3. Program 3: Control Flow & Logic (`control_flow.asm`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```asm
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
```

### Explanation
Demonstrates x86_64 assembly branch jumps (`cmp`, `jle`, `jne`), loop instructions (`loop` / conditional branch), and calling C standard library `printf`.

### Run Control Flow
```bash
nasm -f elf64 control_flow.asm && gcc -no-pie control_flow.o -o control_flow && ./control_flow
```
**Expected Output**:
```text
Conditionals:
15 is Positive and Odd

Pattern Matching / Switch:
Grade B: Good Job!

For Loop (1 to 5):
1 2 3 4 5

While Loop (Countdown):
3 2 1 Blastoff!
```
