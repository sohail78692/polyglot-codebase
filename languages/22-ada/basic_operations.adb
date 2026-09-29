-- ==========================================
-- Program: Basic Operations in Ada (+, -, *, /, mod)
-- ==========================================
with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

procedure Basic_Operations is
    A : Integer := 20;
    B : Integer := 6;
begin
    Put_Line ("a = 20, b = 6");
    Put ("Addition (a + b)        : "); Put (A + B); New_Line;
    Put ("Subtraction (a - b)     : "); Put (A - B); New_Line;
    Put ("Multiplication (a * b)  : "); Put (A * B); New_Line;
    Put ("Integer Division (a / b): "); Put (A / B); New_Line;
    Put ("Modulo (a mod b)        : "); Put (A mod B); New_Line;
end Basic_Operations;
