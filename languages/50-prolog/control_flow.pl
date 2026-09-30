% ==========================================
% Program: Control Flow in Prolog
% ==========================================

:- initialization(main).

% 1. Conditional classification clauses
classify_num(N) :-
    N > 0,
    1 is N mod 2,
    write(N), write(' is Positive and Odd'), nl.
classify_num(N) :-
    N > 0,
    0 is N mod 2,
    write(N), write(' is Positive and Even'), nl.
classify_num(N) :-
    N < 0,
    write(N), write(' is Negative'), nl.
classify_num(_) :-
    write('Number is Zero'), nl.

% 2. Unification pattern matching (Switch equivalent)
grade_feedback('A') :- write('Grade A: Excellent!'), nl.
grade_feedback('B') :- write('Grade B: Good Job!'), nl.
grade_feedback('C') :- write('Grade C: Fair'), nl.
grade_feedback(_)   :- write('Keep Trying!'), nl.

% 3. Recursive loop (For loop equivalent)
for_loop(I, Max) :-
    I =< Max,
    write(I),
    (I =:= Max -> nl ; write(' ')),
    Next is I + 1,
    for_loop(Next, Max).
for_loop(I, Max) :- I > Max.

% 4. Recursive countdown (While loop equivalent)
countdown(0) :-
    write('Blastoff!'), nl.
countdown(N) :-
    N > 0,
    write(N), write(' '),
    Next is N - 1,
    countdown(Next).

main :-
    write('Conditionals:'), nl,
    classify_num(15),
    nl,
    write('Pattern Matching / Switch:'), nl,
    grade_feedback('B'),
    nl,
    write('For Loop (1 to 5):'), nl,
    for_loop(1, 5),
    nl,
    write('While Loop (Countdown):'), nl,
    countdown(3),
    halt.
