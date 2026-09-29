// ==========================================
// Program: Basic Operations in Rust (+, -, *, /, %)
// ==========================================
fn main() {
    let a: i32 = 20;
    let b: i32 = 6;

    println!("a = {}, b = {}", a, b);
    println!("Addition (a + b)        : {}", a + b);
    println!("Subtraction (a - b)     : {}", a - b);
    println!("Multiplication (a * b)  : {}", a * b);
    println!("Integer Division (a / b): {}", a / b);
    println!("Float Division (f64)    : {}", (a as f64) / (b as f64));
    println!("Modulo (a % b)          : {}", a % b);
}
