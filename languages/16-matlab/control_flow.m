% ==========================================
% Program: Control Flow in MATLAB / Octave
% ==========================================

function main()
    % 1. Conditionals
    disp("Conditionals:");
    num = 15;
    if num > 0
        if rem(num, 2) == 0
            fprintf("%d is Positive and Even\n", num);
        else
            fprintf("%d is Positive and Odd\n", num);
        end
    elseif num < 0
        fprintf("%d is Negative\n", num);
    else
        fprintf("Number is Zero\n");
    end

    fprintf("\nPattern Matching / Switch:\n");
    % 2. Switch Statement
    grade = 'B';
    switch grade
        case 'A'
            disp("Grade A: Excellent!");
        case 'B'
            disp("Grade B: Good Job!");
        case 'C'
            disp("Grade C: Fair");
        otherwise
            disp("Keep Trying!");
    end

    % 3. For Loop
    fprintf("\nFor Loop (1 to 5):\n");
    for i = 1:5
        if i == 5
            fprintf("%d\n", i);
        else
            fprintf("%d ", i);
        end
    end

    % 4. While Loop
    fprintf("\nWhile Loop (Countdown):\n");
    count = 3;
    while count > 0
        fprintf("%d ", count);
        count = count - 1;
    end
    fprintf("Blastoff!\n");
end

main();
