// ==========================================
// Program: Control Flow in TypeScript
// ==========================================

function main(): void {
    // 1. Conditionals
    console.log("Conditionals:");
    const num: number = 15;
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
    type Grade = "A" | "B" | "C" | "F";
    const grade: Grade = "B";
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
    const forItems: number[] = [];
    for (let i: number = 1; i <= 5; i++) {
        forItems.push(i);
    }
    console.log(forItems.join(" "));

    // 4. While Loop
    console.log("\nWhile Loop (Countdown):");
    let count: number = 3;
    const countdown: string[] = [];
    while (count > 0) {
        countdown.push(count.toString());
        count--;
    }
    countdown.push("Blastoff!");
    console.log(countdown.join(" "));
}

main();
