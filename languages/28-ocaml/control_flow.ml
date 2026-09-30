(* ==========================================
   Program: Control Flow in OCaml
   ========================================== *)

let () =
  (* 1. Conditionals *)
  print_endline "Conditionals:";
  let num = 15 in
  if num > 0 then
    if num mod 2 = 0 then
      Printf.printf "%d is Positive and Even\n" num
    else
      Printf.printf "%d is Positive and Odd\n" num
  else if num < 0 then
    Printf.printf "%d is Negative\n" num
  else
    print_endline "Number is Zero";

  print_endline "\nPattern Matching / Switch:";
  (* 2. Pattern Matching *)
  let grade = "B" in
  let msg = match grade with
    | "A" -> "Grade A: Excellent!"
    | "B" -> "Grade B: Good Job!"
    | "C" -> "Grade C: Fair"
    | _   -> "Keep Trying!"
  in
  print_endline msg;

  (* 3. For Loop *)
  print_endline "\nFor Loop (1 to 5):";
  for i = 1 to 5 do
    Printf.printf "%d%s" i (if i = 5 then "\n" else " ")
  done;

  (* 4. While Loop *)
  print_endline "\nWhile Loop (Countdown):";
  let count = ref 3 in
  while !count > 0 do
    Printf.printf "%d " !count;
    decr count
  done;
  print_endline "Blastoff!"
