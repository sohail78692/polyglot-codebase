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
