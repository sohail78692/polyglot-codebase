<?php
// ==========================================
// Program: Control Flow in PHP
// ==========================================

function main() {
    // 1. Conditionals
    echo "Conditionals:\n";
    $num = 15;
    if ($num > 0) {
        if ($num % 2 === 0) {
            echo "{$num} is Positive and Even\n";
        } else {
            echo "{$num} is Positive and Odd\n";
        }
    } elseif ($num < 0) {
        echo "{$num} is Negative\n";
    } else {
        echo "Number is Zero\n";
    }

    echo "\nPattern Matching / Switch:\n";
    // 2. PHP 8.0+ Match Expression
    $grade = "B";
    $message = match ($grade) {
        "A" => "Grade A: Excellent!",
        "B" => "Grade B: Good Job!",
        "C" => "Grade C: Fair",
        default => "Keep Trying!"
    };
    echo $message . "\n";

    // 3. For Loop
    echo "\nFor Loop (1 to 5):\n";
    for ($i = 1; $i <= 5; $i++) {
        echo $i . ($i === 5 ? "\n" : " ");
    }

    // 4. While Loop
    echo "\nWhile Loop (Countdown):\n";
    $count = 3;
    while ($count > 0) {
        echo $count . " ";
        $count--;
    }
    echo "Blastoff!\n";
}

main();
?>
