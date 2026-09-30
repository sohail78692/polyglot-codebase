#!/usr/bin/env perl
use strict;
use warnings;

# ==========================================
# Program: Control Flow in Perl
# ==========================================

sub main {
    # 1. Conditionals
    print "Conditionals:\n";
    my $num = 15;
    if ($num > 0) {
        if ($num % 2 == 0) {
            print "$num is Positive and Even\n";
        } else {
            print "$num is Positive and Odd\n";
        }
    } elsif ($num < 0) {
        print "$num is Negative\n";
    } else {
        print "Number is Zero\n";
    }

    print "\nPattern Matching / Switch:\n";
    # 2. Dispatch / pattern switch
    my $grade = "B";
    my %grade_table = (
        "A" => "Grade A: Excellent!",
        "B" => "Grade B: Good Job!",
        "C" => "Grade C: Fair"
    );
    my $msg = $grade_table{$grade} // "Keep Trying!";
    print "$msg\n";

    # 3. For Loop over range
    print "\nFor Loop (1 to 5):\n";
    print join(" ", (1..5)) . "\n";

    # 4. While Loop
    print "\nWhile Loop (Countdown):\n";
    my $count = 3;
    while ($count > 0) {
        print "$count ";
        $count--;
    }
    print "Blastoff!\n";
}

main();
