#!/usr/bin/env perl
# ==========================================
# Program: Basic Operations in Perl (+, -, *, /, %)
# ==========================================
use strict;
use warnings;

my $a = 20;
my $b = 6;

print "a = $a, b = $b
";
print "Addition (a + b)        : " . ($a + $b) . "
";
print "Subtraction (a - b)     : " . ($a - $b) . "
";
print "Multiplication (a * b)  : " . ($a * $b) . "
";
print "Division (a / b)        : " . ($a / $b) . "
";
print "Integer Division (int)  : " . int($a / $b) . "
";
print "Modulo (a % b)          : " . ($a % $b) . "
";
