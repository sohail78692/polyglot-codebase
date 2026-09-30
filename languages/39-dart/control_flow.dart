// ==========================================
// Program: Control Flow in Dart
// ==========================================

void main() {
  // 1. Conditionals
  print("Conditionals:");
  int num = 15;
  if (num > 0) {
    if (num % 2 == 0) {
      print("$num is Positive and Even");
    } else {
      print("$num is Positive and Odd");
    }
  } else if (num < 0) {
    print("$num is Negative");
  } else {
    print("Number is Zero");
  }

  print("\nPattern Matching / Switch:");
  // 2. Dart 3.0 Switch Expression
  String grade = "B";
  String message = switch (grade) {
    "A" => "Grade A: Excellent!",
    "B" => "Grade B: Good Job!",
    "C" => "Grade C: Fair",
    _   => "Keep Trying!"
  };
  print(message);

  // 3. For Loop
  print("\nFor Loop (1 to 5):");
  List<int> forItems = [];
  for (int i = 1; i <= 5; i++) {
    forItems.add(i);
  }
  print(forItems.join(" "));

  // 4. While Loop
  print("\nWhile Loop (Countdown):");
  int count = 3;
  List<String> whileItems = [];
  while (count > 0) {
    whileItems.add(count.toString());
    count--;
  }
  whileItems.add("Blastoff!");
  print(whileItems.join(" "));
}
