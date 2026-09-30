@echo off
setlocal enabledelayedexpansion

:: ==========================================
:: Program: Control Flow in Windows Batch
:: ==========================================

echo Conditionals:
set num=15
set /a rem=num %% 2
if %num% GTR 0 (
    if !rem! EQU 0 (
        echo %num% is Positive and Even
    ) else (
        echo %num% is Positive and Odd
    )
) else (
    echo %num% is Not Positive
)

echo.
echo Pattern Matching / Switch:
set grade=B
if "%grade%"=="A" (
    echo Grade A: Excellent!
) else if "%grade%"=="B" (
    echo Grade B: Good Job!
) else (
    echo Keep Trying!
)

echo.
echo For Loop (1 to 5):
set for_line=
for /L %%i in (1,1,5) do (
    set for_line=!for_line!%%i 
)
echo !for_line:~0,-1!

echo.
echo While Loop (Countdown):
set count=3
set while_line=
:while_loop
if !count! GTR 0 (
    set while_line=!while_line!!count! 
    set /a count=!count!-1
    goto while_loop
)
echo !while_line!Blastoff!

endlocal
