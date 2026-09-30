-- ==========================================
-- Program: Control Flow in Haskell
-- ==========================================

countdown :: Int -> IO ()
countdown 0 = putStrLn "Blastoff!"
countdown n = do
    putStr (show n ++ " ")
    countdown (n - 1)

main :: IO ()
main = do
    -- 1. Conditionals (if then else expressions)
    putStrLn "Conditionals:"
    let num = 15 :: Int
    putStrLn $ if num > 0
               then if num `mod` 2 == 0
                    then show num ++ " is Positive and Even"
                    else show num ++ " is Positive and Odd"
               else if num < 0
                    then show num ++ " is Negative"
                    else "Number is Zero"

    putStrLn "\nPattern Matching / Switch:"
    -- 2. Case Expression (Pattern Matching)
    let grade = 'B'
    let msg = case grade of
                'A' -> "Grade A: Excellent!"
                'B' -> "Grade B: Good Job!"
                'C' -> "Grade C: Fair"
                _   -> "Keep Trying!"
    putStrLn msg

    -- 3. Loop via List mapping (unwords)
    putStrLn "\nFor Loop (1 to 5):"
    putStrLn $ unwords (map show [1..5])

    -- 4. While Loop via recursion
    putStrLn "\nWhile Loop (Countdown):"
    countdown 3
