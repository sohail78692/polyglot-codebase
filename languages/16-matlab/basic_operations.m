% ==========================================
% Program: Basic Operations in MATLAB / GNU Octave
% ==========================================
a = 20;
b = 6;

fprintf('a = %d, b = %d\n', a, b);
fprintf('Addition (a + b)        : %d\n', a + b);
fprintf('Subtraction (a - b)     : %d\n', a - b);
fprintf('Multiplication (a * b)  : %d\n', a * b);
fprintf('Division (a / b)        : %f\n', a / b);
fprintf('Integer Division (idiv) : %d\n', fix(a / b));
fprintf('Modulo (mod(a, b))      : %d\n', mod(a, b));
