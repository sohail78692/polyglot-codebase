-- ==========================================
-- Program: Control Flow in Ada
-- ==========================================

with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

procedure Control_Flow is
   Num   : Integer := 15;
   Grade : Character := 'B';
   Count : Integer := 3;
begin
   -- 1. Conditionals
   Put_Line ("Conditionals:");
   if Num > 0 then
      if Num mod 2 = 0 then
         Put (Num, Width => 0);
         Put_Line (" is Positive and Even");
      else
         Put (Num, Width => 0);
         Put_Line (" is Positive and Odd");
      end if;
   elsif Num < 0 then
      Put (Num, Width => 0);
      Put_Line (" is Negative");
   else
      Put_Line ("Number is Zero");
   end if;

   New_Line;
   Put_Line ("Pattern Matching / Switch:");
   -- 2. Case statement
   case Grade is
      when 'A' =>
         Put_Line ("Grade A: Excellent!");
      when 'B' =>
         Put_Line ("Grade B: Good Job!");
      when 'C' =>
         Put_Line ("Grade C: Fair");
      when others =>
         Put_Line ("Keep Trying!");
   end case;

   New_Line;
   Put_Line ("For Loop (1 to 5):");
   -- 3. For loop
   for I in 1 .. 5 loop
      Put (I, Width => 0);
      if I = 5 then
         New_Line;
      else
         Put (" ");
      end if;
   end loop;

   New_Line;
   Put_Line ("While Loop (Countdown):");
   -- 4. While loop
   while Count > 0 loop
      Put (Count, Width => 0);
      Put (" ");
      Count := Count - 1;
   end loop;
   Put_Line ("Blastoff!");
end Control_Flow;
