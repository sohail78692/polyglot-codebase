# SQL Reference Guide

> **Category**: Web3, Mobile & Modern  
> **Paradigm**: Declarative (Relational Database Query Language)  
> **Initial Release**: 1974  
> **Created By**: Donald D. Chamberlin and Raymond F. Boyce (IBM)  

---

## 1. Program 1: Hello World (`hello_world.sql`)

```sql
-- ==========================================
-- Program: Hello World in SQL (ANSI Standard)
-- ==========================================
SELECT 'Hello, World!' AS message;
```

### Explanation
`SELECT` outputs a query projection.

### Run Hello World
```bash
sqlite3 :memory: < hello_world.sql
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.sql`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```sql
-- ==========================================
-- Program: Basic Operations in SQL (+, -, *, /, %)
-- ==========================================
SELECT
    20 + 6 AS addition,
    20 - 6 AS subtraction,
    20 * 6 AS multiplication,
    20 / 6 AS integer_division,
    20 * 1.0 / 6 AS float_division,
    20 % 6 AS modulo;
```

### Explanation
SQL provides standard mathematical operators in `SELECT` statements; `20 * 1.0 / 6` casts to decimal.

### Run Basic Operations
```bash
sqlite3 :memory: < basic_operations.sql
```
**Expected Output**:
```text
26|14|120|3|3.33333333333333|2
```

---

## 3. Prerequisites & Installation

- **Guide**: SQLite / PostgreSQL / MySQL

---

## 3. Program 3: Control Flow & Logic (`control_flow.sql`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```sql
-- ==========================================
-- Program: Control Flow in SQL (SQLite)
-- ==========================================

-- 1. Declarative Conditionals (CASE WHEN)
SELECT 'Conditionals:' AS Output;
SELECT 
    CASE 
        WHEN 15 > 0 AND (15 % 2 = 1) THEN '15 is Positive and Odd'
        WHEN 15 > 0 AND (15 % 2 = 0) THEN '15 is Positive and Even'
        WHEN 15 < 0 THEN '15 is Negative'
        ELSE 'Number is Zero'
    END AS Result;

-- 2. Pattern Matching / Switch Equivalent (CASE)
SELECT '' AS Blank1;
SELECT 'Pattern Matching / Switch:' AS Output;
SELECT 
    CASE 'B'
        WHEN 'A' THEN 'Grade A: Excellent!'
        WHEN 'B' THEN 'Grade B: Good Job!'
        WHEN 'C' THEN 'Grade C: Fair'
        ELSE 'Keep Trying!'
    END AS GradeFeedback;

-- 3. For Loop Equivalent using Recursive CTE (1 to 5)
SELECT '' AS Blank2;
SELECT 'For Loop (1 to 5):' AS Output;
WITH RECURSIVE for_loop(val) AS (
    SELECT 1
    UNION ALL
    SELECT val + 1 FROM for_loop WHERE val < 5
)
SELECT group_concat(val, ' ') AS Sequence FROM for_loop;

-- 4. While Loop Equivalent using Recursive CTE (Countdown)
SELECT '' AS Blank3;
SELECT 'While Loop (Countdown):' AS Output;
WITH RECURSIVE while_loop(count) AS (
    SELECT 3
    UNION ALL
    SELECT count - 1 FROM while_loop WHERE count > 1
)
SELECT group_concat(count, ' ') || ' Blastoff!' AS Countdown FROM while_loop;
```

### Explanation
Demonstrates declarative SQL branching via `CASE WHEN ... THEN ... ELSE END` and iterative recursion using recursive CTEs (`WITH RECURSIVE`).

### Run Control Flow
```bash
sqlite3 :memory: < control_flow.sql
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
