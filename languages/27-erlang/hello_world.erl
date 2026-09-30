% ==========================================
% Program: Hello World in Erlang
% ==========================================
-module(prog).
-export([main/0, main/1, start/0]).

main() -> start().
main(_) -> start().

start() ->
    io:format("Hello, World!~n").
