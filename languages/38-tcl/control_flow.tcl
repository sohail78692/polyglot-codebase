# ==========================================
# Program: Control Flow in Tcl
# ==========================================

proc main {} {
    # 1. Conditionals
    puts "Conditionals:"
    set num 15
    if {$num > 0} {
        if {$num % 2 == 0} {
            puts "$num is Positive and Even"
        } else {
            puts "$num is Positive and Odd"
        }
    } elseif {$num < 0} {
        puts "$num is Negative"
    } else {
        puts "Number is Zero"
    }

    puts "\nPattern Matching / Switch:"
    # 2. Switch command
    set grade "B"
    switch $grade {
        "A" { puts "Grade A: Excellent!" }
        "B" { puts "Grade B: Good Job!" }
        "C" { puts "Grade C: Fair" }
        default { puts "Keep Trying!" }
    }

    # 3. For loop
    puts "\nFor Loop (1 to 5):"
    set forList {}
    for {set i 1} {$i <= 5} {incr i} {
        lappend forList $i
    }
    puts [join $forList " "]

    # 4. While loop
    puts "\nWhile Loop (Countdown):"
    set count 3
    set whileList {}
    while {$count > 0} {
        lappend whileList $count
        incr count -1
    }
    lappend whileList "Blastoff!"
    puts [join $whileList " "]
}

main
