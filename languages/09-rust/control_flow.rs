// ==========================================
// Program: Control Flow in Rust
// ==========================================

fn main() {
    // 1. Conditionals
    println!("Conditionals:");
    let num = 15;
    if num > 0 {
        if num % 2 == 0 {
            println!("{} is Positive and Even", num);
        } else {
            println!("{} is Positive and Odd", num);
        }
    } else if num < 0 {
        println!("{} is Negative", num);
    } else {
        println!("Number is Zero");
    }

    println!("\nPattern Matching / Switch:");
    // 2. Pattern Matching
    let grade = "B";
    let message = match grade {
        "A" => "Grade A: Excellent!",
        "B" => "Grade B: Good Job!",
        "C" => "Grade C: Fair",
        _   => "Keep Trying!",
    };
    println!("{}", message);

    // 3. For Loop (1..=5 inclusive)
    println!("\nFor Loop (1 to 5):");
    for i in 1..=5 {
        if i == 5 {
            println!("{}", i);
        } else {
            print!("{} ", i);
        }
    }

    // 4. While Loop
    println!("\nWhile Loop (Countdown):");
    let mut count = 3;
    while count > 0 {
        print!("{} ", count);
        count -= 1;
    }
    println!("Blastoff!");
}
