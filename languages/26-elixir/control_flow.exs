# ==========================================
# Program: Control Flow in Elixir
# ==========================================

defmodule ControlFlow do
  def countdown(0), do: IO.puts("Blastoff!")
  def countdown(n) do
    IO.write("#{n} ")
    countdown(n - 1)
  end

  def main do
    # 1. Conditionals (cond)
    IO.puts("Conditionals:")
    num = 15
    cond do
      num > 0 ->
        if rem(num, 2) == 0 do
          IO.puts("#{num} is Positive and Even")
        else
          IO.puts("#{num} is Positive and Odd")
        end
      num < 0 -> IO.puts("#{num} is Negative")
      true    -> IO.puts("Number is Zero")
    end

    IO.puts("\nPattern Matching / Switch:")
    # 2. Case Pattern Matching
    grade = "B"
    msg = case grade do
      "A" -> "Grade A: Excellent!"
      "B" -> "Grade B: Good Job!"
      "C" -> "Grade C: Fair"
      _   -> "Keep Trying!"
    end
    IO.puts(msg)

    # 3. For Comprehension
    IO.puts("\nFor Loop (1 to 5):")
    Enum.each(1..5, fn i ->
      IO.write("#{i}#{if i == 5, do: "\n", else: " "}")
    end)

    # 4. While Loop via recursion
    IO.puts("\nWhile Loop (Countdown):")
    countdown(3)
  end
end

ControlFlow.main()
