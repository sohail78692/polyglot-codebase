% ==========================================
% Program: Basic Operations in Prolog (+, -, *, //, mod)
% ==========================================
:- initialization(main).

main :-
    A = 20,
    B = 6,
    Add is A + B,
    Sub is A - B,
    Mul is A * B,
    Div is A // B,   % // is integer division in ISO Prolog
    Mod is A mod B,  % mod is modulo remainder
    format('a = ~w, b = ~w~n', [A, B]),
    format('Addition: ~w, Subtraction: ~w, Multiplication: ~w, Division: ~w, Modulo: ~w~n',
           [Add, Sub, Mul, Div, Mod]),
    halt.
