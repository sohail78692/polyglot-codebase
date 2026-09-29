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
