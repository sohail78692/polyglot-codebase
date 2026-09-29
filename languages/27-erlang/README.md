# Erlang Reference Guide

> **Category**: Functional & Declarative  
> **Paradigm**: Functional, Concurrent (Actor model)  
> **Initial Release**: 1986  
> **Created By**: Joe Armstrong et al.  

---

## 1. Program 1: Hello World (`hello_world.erl`)

```erl
% ==========================================
% Program: Hello World in Erlang
% ==========================================
-module(hello_world).
-export([start/0]).

start() ->
    io:format("Hello, World!~n").
```

### Explanation
Erlang module with exported `start/0`.

### Run Hello World
```bash
erlc hello_world.erl && erl -noshell -s hello_world start -s init stop
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.erl`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```erl
% ==========================================
% Program: Basic Operations in Erlang (+, -, *, div, rem)
% ==========================================
-module(basic_operations).
-export([start/0]).

start() ->
    A = 20,
    B = 6,
    io:format("a = ~p, b = ~p~n", [A, B]),
    io:format("Addition: ~p, Subtraction: ~p, Multiplication: ~p, Division: ~p, Remainder: ~p~n",
              [A + B, A - B, A * B, A div B, A rem B]).
```

### Explanation
Erlang variables are capitalized (`A`, `B`). `div` is integer division, and `rem` is remainder.

### Run Basic Operations
```bash
erlc basic_operations.erl && erl -noshell -s basic_operations start -s init stop
```
**Expected Output**:
```text
a = 20, b = 6
Addition: 26, Subtraction: 14, Multiplication: 120, Division: 3, Remainder: 2
```

---

## 3. Prerequisites & Installation

- **Guide**: erlang.org
