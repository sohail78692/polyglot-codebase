-- ==========================================
-- Program: Control Flow in Lua
-- ==========================================

function main()
    -- 1. Conditionals
    print("Conditionals:")
    local num = 15
    if num > 0 then
        if num % 2 == 0 then
            print(num .. " is Positive and Even")
        else
            print(num .. " is Positive and Odd")
        end
    elseif num < 0 then
        print(num .. " is Negative")
    else
        print("Number is Zero")
    end

    print("\nPattern Matching / Switch:")
    -- 2. Table lookup (idiomatic Lua switch)
    local grade = "B"
    local switchTable = {
        A = "Grade A: Excellent!",
        B = "Grade B: Good Job!",
        C = "Grade C: Fair"
    }
    print(switchTable[grade] or "Keep Trying!")

    -- 3. Numeric For Loop (inclusive 1, 5)
    print("\nFor Loop (1 to 5):")
    local forItems = {}
    for i = 1, 5 do
        table.insert(forItems, i)
    end
    print(table.concat(forItems, " "))

    -- 4. While Loop
    print("\nWhile Loop (Countdown):")
    local count = 3
    local whileItems = {}
    while count > 0 do
        table.insert(whileItems, count)
        count = count - 1
    end
    table.insert(whileItems, "Blastoff!")
    print(table.concat(whileItems, " "))
end

main()
