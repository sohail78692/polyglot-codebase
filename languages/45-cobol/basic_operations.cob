      * ==========================================
      * Program: Basic Operations in COBOL (+, -, *, /, %)
      * ==========================================
       IDENTIFICATION DIVISION.
       PROGRAM-ID. BASIC-OPS.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 A          PIC 99 VALUE 20.
       01 B          PIC 99 VALUE 6.
       01 RES-ADD    PIC 99.
       01 RES-SUB    PIC 99.
       01 RES-MUL    PIC 999.
       01 RES-DIV    PIC 99.
       01 RES-MOD    PIC 99.

       PROCEDURE DIVISION.
           COMPUTE RES-ADD = A + B.
           COMPUTE RES-SUB = A - B.
           COMPUTE RES-MUL = A * B.
           DIVIDE A BY B GIVING RES-DIV REMAINDER RES-MOD.

           DISPLAY 'A = 20, B = 6'.
           DISPLAY 'ADDITION: ' RES-ADD.
           DISPLAY 'SUBTRACTION: ' RES-SUB.
           DISPLAY 'MULTIPLICATION: ' RES-MUL.
           DISPLAY 'DIVISION: ' RES-DIV.
           DISPLAY 'REMAINDER: ' RES-MOD.
           STOP RUN.
