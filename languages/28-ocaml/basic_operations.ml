(* ==========================================
   Program: Basic Operations in OCaml (+, -, *, /, mod)
   ========================================== *)
let () =
  let a = 20 in
  let b = 6 in
  Printf.printf "a = %d, b = %d\n" a b;
  Printf.printf "Addition (a + b)        : %d\n" (a + b);
  Printf.printf "Subtraction (a - b)     : %d\n" (a - b);
  Printf.printf "Multiplication (a * b)  : %d\n" (a * b);
  Printf.printf "Integer Division (a / b): %d\n" (a / b);
  Printf.printf "Float Division (float)  : %f\n" (float_of_int a /. float_of_int b);
  Printf.printf "Modulo (a mod b)        : %d\n" (a mod b)
