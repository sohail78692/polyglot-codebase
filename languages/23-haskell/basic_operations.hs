-- ==========================================
-- Program: Basic Operations in Haskell (+, -, *, div, mod, /)
-- ==========================================
main :: IO ()
main = do
    let a = 20 :: Int
    let b = 6 :: Int
    putStrLn "a = 20, b = 6"
    putStrLn ("Addition (a + b)        : " ++ show (a + b))
    putStrLn ("Subtraction (a - b)     : " ++ show (a - b))
    putStrLn ("Multiplication (a * b)  : " ++ show (a * b))
    putStrLn ("Integer Division (div)  : " ++ show (a `div` b))
    putStrLn ("Float Division (/)      : " ++ show (fromIntegral a / fromIntegral b))
    putStrLn ("Modulo (mod)            : " ++ show (a `mod` b))
