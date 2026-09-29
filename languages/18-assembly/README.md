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
