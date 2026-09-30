# ==========================================
# Program: Control Flow in AWK
# ==========================================

BEGIN {
    # 1. Conditionals
    print "Conditionals:"
    num = 15
    if (num > 0) {
        if (num % 2 == 0) {
            print num " is Positive and Even"
        } else {
            print num " is Positive and Odd"
        }
    } else if (num < 0) {
        print num " is Negative"
    } else {
        print "Number is Zero"
    }

    print "\nPattern Matching / Switch:"
    # 2. Multi-way Branching
    grade = "B"
    if (grade == "A") {
        print "Grade A: Excellent!"
    } else if (grade == "B") {
        print "Grade B: Good Job!"
    } else if (grade == "C") {
        print "Grade C: Fair"
    } else {
        print "Keep Trying!"
    }

    # 3. For Loop
    print "\nFor Loop (1 to 5):"
    out_for = ""
    for (i = 1; i <= 5; i++) {
        out_for = (i == 1) ? i : out_for " " i
    }
    print out_for

    # 4. While Loop
    print "\nWhile Loop (Countdown):"
    count = 3
    out_while = ""
    while (count > 0) {
        out_while = (out_while == "") ? count : out_while " " count
        count--
    }
    print out_while " Blastoff!"
}
