// ==========================================
// Program: Control Flow in JavaScript
// ==========================================

function main() {
    // 1. Conditionals (if / else if / else)
    console.log("Conditionals:");
    const num = 15;
    if (num > 0) {
        if (num % 2 === 0) {
            console.log(`${num} is Positive and Even`);
        } else {
            console.log(`${num} is Positive and Odd`);
        }
    } else if (num < 0) {
        console.log(`${num} is Negative`);
    } else {
        console.log("Number is Zero");
    }

    console.log("\nPattern Matching / Switch:");
    // 2. Switch Statement
    const grade = "B";
    switch (grade) {
        case "A":
            console.log("Grade A: Excellent!");
            break;
        case "B":
            console.log("Grade B: Good Job!");
            break;
        case "C":
            console.log("Grade C: Fair");
            break;
        default:
            console.log("Keep Trying!");
    }

    // 3. For Loop
    console.log("\nFor Loop (1 to 5):");
    let forResult = [];
    for (let i = 1; i <= 5; i++) {
        forResult.push(i);
    }
    console.log(forResult.join(" "));

    // 4. While Loop
    console.log("\nWhile Loop (Countdown):");
    let count = 3;
    let whileResult = [];
    while (count > 0) {
        whileResult.push(count);
        count--;
    }
    whileResult.push("Blastoff!");
    console.log(whileResult.join(" "));
}

main();
