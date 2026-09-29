% ==========================================
% Program: Basic Operations in Erlang (+, -, *, div, rem)
% ==========================================
-module(basic_operations).
-export([start/0]).

start() ->
    A = 20,
    B = 6,
    io:format("a = ~p, b = ~p~n", [A, B]),
    io:format("Addition: ~p, Subtraction: ~p, Multiplication: ~p, Division: ~p, Remainder: ~p~n",
              [A + B, A - B, A * B, A div B, A rem B]).
