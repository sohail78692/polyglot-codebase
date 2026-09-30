# ==========================================
# Program: Control Flow in Python
# ==========================================

def main():
    # 1. Conditionals (if / elif / else)
    print("Conditionals:")
    num = 15
    if num > 0:
        if num % 2 == 0:
            print(f"{num} is Positive and Even")
        else:
            print(f"{num} is Positive and Odd")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print("Number is Zero")

    print("\nPattern Matching:")
    # 2. Structural Pattern Matching (Python 3.10+)
    grade = "B"
    match grade:
        case "A":
            print("Grade A: Excellent!")
        case "B":
            print("Grade B: Good Job!")
        case "C":
            print("Grade C: Fair")
        case _:
            print("Keep Trying!")

    # 3. For Loop with range
    print("\nFor Loop (1 to 5):")
    for i in range(1, 6):
        print(i, end=" " if i < 5 else "\n")

    # 4. While Loop Countdown
    print("\nWhile Loop (Countdown):")
    count = 3
    while count > 0:
        print(count, end=" ")
        count -= 1
    print("Blastoff!")

if __name__ == "__main__":
    main()
