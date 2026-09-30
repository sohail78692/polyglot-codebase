REM ==========================================
REM Program: Control Flow in BASIC (FreeBASIC)
REM ==========================================

Sub Main()
    ' 1. Conditionals
    Print "Conditionals:"
    Dim num As Integer = 15
    If num > 0 Then
        If num Mod 2 = 0 Then
            Print num; " is Positive and Even"
        Else
            Print num; " is Positive and Odd"
        End If
    ElseIf num < 0 Then
        Print num; " is Negative"
    Else
        Print "Number is Zero"
    End If

    Print ""
    Print "Pattern Matching / Switch:"
    ' 2. Select Case
    Dim grade As String = "B"
    Select Case grade
        Case "A"
            Print "Grade A: Excellent!"
        Case "B"
            Print "Grade B: Good Job!"
        Case "C"
            Print "Grade C: Fair"
        Case Else
            Print "Keep Trying!"
    End Select

    Print ""
    Print "For Loop (1 to 5):"
    ' 3. For Loop
    For i As Integer = 1 To 5
        If i = 5 Then
            Print Str(i)
        Else
            Print Str(i) + " ";
        End If
    Next i

    Print ""
    Print "While Loop (Countdown):"
    ' 4. While Loop
    Dim count As Integer = 3
    While count > 0
        Print Str(count) + " ";
        count = count - 1
    Wend
    Print "Blastoff!"
End Sub

Main()
