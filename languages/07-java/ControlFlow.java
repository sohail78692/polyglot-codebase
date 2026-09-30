// ==========================================
// Program: Control Flow in Java
// ==========================================

class ControlFlow {
    public static void main(String[] args) {
        // 1. Conditionals
        System.out.println("Conditionals:");
        int num = 15;
        if (num > 0) {
            if (num % 2 == 0) {
                System.out.println(num + " is Positive and Even");
            } else {
                System.out.println(num + " is Positive and Odd");
            }
        } else if (num < 0) {
            System.out.println(num + " is Negative");
        } else {
            System.out.println("Number is Zero");
        }

        System.out.println("\nPattern Matching / Switch:");
        // 2. Enhanced Switch Rule
        String grade = "B";
        String message = switch (grade) {
            case "A" -> "Grade A: Excellent!";
            case "B" -> "Grade B: Good Job!";
            case "C" -> "Grade C: Fair";
            default  -> "Keep Trying!";
        };
        System.out.println(message);

        // 3. For Loop
        System.out.println("\nFor Loop (1 to 5):");
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + (i == 5 ? "\n" : " "));
        }

        // 4. While Loop
        System.out.println("\nWhile Loop (Countdown):");
        int count = 3;
        while (count > 0) {
            System.out.print(count + " ");
            count--;
        }
        System.out.println("Blastoff!");
    }
}
