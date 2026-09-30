% ==========================================
% Program: Basic Operations in Erlang (+, -, *, div, rem)
% ==========================================
-module(prog).
-export([main/0, main/1, start/0]).

main() -> start().
main(_) -> start().

start() ->
    A = 20,
    B = 6,
    io:format("a = ~p, b = ~p~n", [A, B]),
    io:format("Addition: ~p, Subtraction: ~p, Multiplication: ~p, Division: ~p, Remainder: ~p~n",
              [A + B, A - B, A * B, A div B, A rem B]).
