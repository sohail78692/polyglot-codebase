% ==========================================
% Program: Control Flow in Erlang
% ==========================================

-module(control_flow).
-export([main/1]).

countdown(0) ->
    io:format("Blastoff!~n");
countdown(N) ->
    io:format("~p ", [N]),
    countdown(N - 1).

main(_) ->
    % 1. Conditionals
    io:format("Conditionals:~n"),
    Num = 15,
    if
        Num > 0 ->
            case Num rem 2 of
                0 -> io:format("~p is Positive and Even~n", [Num]);
                _ -> io:format("~p is Positive and Odd~n", [Num])
            end;
        Num < 0 ->
            io:format("~p is Negative~n", [Num]);
        true ->
            io:format("Number is Zero~n")
    end,

    % 2. Case Pattern Matching
    io:format("~nPattern Matching / Switch:~n"),
    Grade = "B",
    Msg = case Grade of
        "A" -> "Grade A: Excellent!";
        "B" -> "Grade B: Good Job!";
        "C" -> "Grade C: Fair";
        _   -> "Keep Trying!"
    end,
    io:format("~s~n", [Msg]),

    % 3. Loop via lists:foreach
    io:format("~nFor Loop (1 to 5):~n"),
    lists:foreach(fun(I) ->
        case I of
            5 -> io:format("~p~n", [I]);
            _ -> io:format("~p ", [I])
        end
    end, lists:seq(1, 5)),

    % 4. While Loop via recursion
    io:format("~nWhile Loop (Countdown):~n"),
    countdown(3).
