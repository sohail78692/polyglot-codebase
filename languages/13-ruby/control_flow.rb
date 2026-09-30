# ==========================================
# Program: Control Flow in Ruby
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
  # 2. Case statement
  grade = "B"
  case grade
  when "A"
    puts "Grade A: Excellent!"
  when "B"
    puts "Grade B: Good Job!"
  when "C"
    puts "Grade C: Fair"
  else
    puts "Keep Trying!"
  end

  # 3. For loop / Range iteration
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
