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

---

## 3. Program 3: Control Flow & Logic (`control_flow.erl`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```erl
% ==========================================
% Program: Control Flow in Erlang
% ==========================================

-module(control_flow).
-export([main/1]).

countdown(0) ->
    io:format("Blastoff!~n");
countdown(N) ->
    io:format("~p ", [N]),
    countdown(N - 1).

main(_) ->
    % 1. Conditionals
    io:format("Conditionals:~n"),
    Num = 15,
    if
        Num > 0 ->
            case Num rem 2 of
                0 -> io:format("~p is Positive and Even~n", [Num]);
                _ -> io:format("~p is Positive and Odd~n", [Num])
            end;
        Num < 0 ->
            io:format("~p is Negative~n", [Num]);
        true ->
            io:format("Number is Zero~n")
    end,

    % 2. Case Pattern Matching
    io:format("~nPattern Matching / Switch:~n"),
    Grade = "B",
    Msg = case Grade of
        "A" -> "Grade A: Excellent!";
        "B" -> "Grade B: Good Job!";
        "C" -> "Grade C: Fair";
        _   -> "Keep Trying!"
    end,
    io:format("~s~n", [Msg]),

    % 3. Loop via lists:foreach
    io:format("~nFor Loop (1 to 5):~n"),
    lists:foreach(fun(I) ->
        case I of
            5 -> io:format("~p~n", [I]);
            _ -> io:format("~p ", [I])
        end
    end, lists:seq(1, 5)),

    % 4. While Loop via recursion
    io:format("~nWhile Loop (Countdown):~n"),
    countdown(3).
```

### Explanation
Demonstrates Erlang pattern matching in function heads, `case ... of` blocks, and tail recursion for loops.

### Run Control Flow
```bash
escript control_flow.erl
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
