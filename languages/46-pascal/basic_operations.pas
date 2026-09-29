(* ==========================================
   Program: Basic Operations in Pascal (+, -, *, /, div, mod)
   ========================================== *)
program BasicOperations;
var
    a, b: integer;
begin
    a := 20;
    b := 6;

    writeln('a = 20, b = 6');
    writeln('Addition (a + b)        : ', a + b);
    writeln('Subtraction (a - b)     : ', a - b);
    writeln('Multiplication (a * b)  : ', a * b);
    writeln('Integer Division (div)  : ', a div b);
    writeln('Float Division (/)      : ', (a / b):0:2);
    writeln('Modulo (mod)            : ', a mod b);
end.
