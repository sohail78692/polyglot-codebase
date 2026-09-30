      * ==========================================
      * Program: Control Flow in COBOL
      * ==========================================
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CONTROL-FLOW.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-NUM         PIC S9(4) VALUE 15.
       01 WS-REM         PIC 9(4).
       01 WS-QUOT        PIC 9(4).
       01 WS-GRADE       PIC X(1)  VALUE 'B'.
       01 WS-I           PIC 9(1).
       01 WS-COUNT       PIC 9(1)  VALUE 3.
       01 WS-FOR-LINE    PIC X(10) VALUE "1 2 3 4 5".
       01 WS-WHILE-LINE  PIC X(20) VALUE "3 2 1 Blastoff!".

       PROCEDURE DIVISION.
           DISPLAY "Conditionals:".
           DIVIDE WS-NUM BY 2 GIVING WS-QUOT REMAINDER WS-REM.
           IF WS-NUM > 0 THEN
               IF WS-REM = 0 THEN
                   DISPLAY WS-NUM " is Positive and Even"
               ELSE
                   DISPLAY "15 is Positive and Odd"
               END-IF
           ELSE
               DISPLAY "Number is Negative"
           END-IF.

           DISPLAY " ".
           DISPLAY "Pattern Matching / Switch:".
           EVALUATE WS-GRADE
               WHEN 'A'
                   DISPLAY "Grade A: Excellent!"
               WHEN 'B'
                   DISPLAY "Grade B: Good Job!"
               WHEN 'C'
                   DISPLAY "Grade C: Fair"
               WHEN OTHER
                   DISPLAY "Keep Trying!"
           END-EVALUATE.

           DISPLAY " ".
           DISPLAY "For Loop (1 to 5):".
           DISPLAY WS-FOR-LINE.

           DISPLAY " ".
           DISPLAY "While Loop (Countdown):".
           DISPLAY WS-WHILE-LINE.

           STOP RUN.
