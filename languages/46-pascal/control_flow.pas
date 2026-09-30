// ==========================================
// Program: Control Flow in Pascal
// ==========================================

program ControlFlow;

var
  Num, I, Count: Integer;
  Grade: Char;

begin
  // 1. Conditionals
  WriteLn('Conditionals:');
  Num := 15;
  if Num > 0 then
  begin
    if Num mod 2 = 0 then
      WriteLn(Num, ' is Positive and Even')
    else
      WriteLn(Num, ' is Positive and Odd');
  end
  else if Num < 0 then
    WriteLn(Num, ' is Negative')
  else
    WriteLn('Number is Zero');

  WriteLn;
  WriteLn('Pattern Matching / Switch:');
  // 2. Case Statement
  Grade := 'B';
  case Grade of
    'A': WriteLn('Grade A: Excellent!');
    'B': WriteLn('Grade B: Good Job!');
    'C': WriteLn('Grade C: Fair');
  else
    WriteLn('Keep Trying!');
  end;

  WriteLn;
  WriteLn('For Loop (1 to 5):');
  // 3. For Loop
  for I := 1 to 5 do
  begin
    Write(I);
    if I = 5 then
      WriteLn
    else
      Write(' ');
  end;

  WriteLn;
  WriteLn('While Loop (Countdown):');
  // 4. While Loop
  Count := 3;
  while Count > 0 do
  begin
    Write(Count, ' ');
    Count := Count - 1;
  end;
  WriteLn('Blastoff!');
end.
