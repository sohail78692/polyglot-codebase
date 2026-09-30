\ ==========================================
\ Program: Control Flow in Forth
\ ==========================================

: check-num ( n -- )
    dup 0 > if
        dup 2 mod 0 = if
            . ." is Positive and Even" cr
        else
            . ." is Positive and Odd" cr
        then
    else
        drop ." Not positive" cr
    then ;

: check-grade ( c -- )
    case
        [char] A of ." Grade A: Excellent!" cr endof
        [char] B of ." Grade B: Good Job!" cr endof
        [char] C of ." Grade C: Fair" cr endof
        ." Keep Trying!" cr
    endcase ;

: for-loop ( -- )
    6 1 do
        i .
    loop cr ;

: while-countdown ( -- )
    3
    begin
        dup 0 >
    while
        dup .
        1 -
    repeat
    drop ." Blastoff!" cr ;

: main ( -- )
    ." Conditionals:" cr
    15 check-num
    cr
    ." Pattern Matching / Switch:" cr
    [char] B check-grade
    cr
    ." For Loop (1 to 5):" cr
    for-loop
    cr
    ." While Loop (Countdown):" cr
    while-countdown ;

main
