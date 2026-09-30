# ==========================================
# Program: Control Flow in Crystal
# ==========================================

def main
  # 1. Conditionals
  puts "Conditionals:"
  num = 15
  if num > 0
    if num % 2 == 0
      puts "#{num} is Positive and Even"
    else
      puts "#{num} is Positive and Odd"
    end
  elsif num < 0
    puts "#{num} is Negative"
  else
    puts "Number is Zero"
  end

  puts "\nPattern Matching / Switch:"
  # 2. Case Expression
  grade = "B"
  msg = case grade
  when "A" then "Grade A: Excellent!"
  when "B" then "Grade B: Good Job!"
  when "C" then "Grade C: Fair"
  else "Keep Trying!"
  end
  puts msg

  # 3. For Loop over range
  puts "\nFor Loop (1 to 5):"
  puts (1..5).to_a.join(" ")

  # 4. While Loop
  puts "\nWhile Loop (Countdown):"
  count = 3
  while count > 0
    print "#{count} "
    count -= 1
  end
  puts "Blastoff!"
end

main
