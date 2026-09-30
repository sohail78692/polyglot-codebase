// ==========================================
// Program: Control Flow in C#
// ==========================================

using System;

class Program
{
    static void Main()
    {
        // 1. Conditionals
        Console.WriteLine("Conditionals:");
        int num = 15;
        if (num > 0)
        {
            if (num % 2 == 0)
                Console.WriteLine($"{num} is Positive and Even");
            else
                Console.WriteLine($"{num} is Positive and Odd");
        }
        else if (num < 0)
        {
            Console.WriteLine($"{num} is Negative");
        }
        else
        {
            Console.WriteLine("Number is Zero");
        }

        Console.WriteLine("\nPattern Matching / Switch:");
        // 2. Switch Expression
        string grade = "B";
        string feedback = grade switch
        {
            "A" => "Grade A: Excellent!",
            "B" => "Grade B: Good Job!",
            "C" => "Grade C: Fair",
            _   => "Keep Trying!"
        };
        Console.WriteLine(feedback);

        // 3. For Loop
        Console.WriteLine("\nFor Loop (1 to 5):");
        for (int i = 1; i <= 5; i++)
        {
            Console.Write(i + (i == 5 ? "\n" : " "));
        }

        // 4. While Loop
        Console.WriteLine("\nWhile Loop (Countdown):");
        int count = 3;
        while (count > 0)
        {
            Console.Write(count + " ");
            count--;
        }
        Console.WriteLine("Blastoff!");
    }
}
