// ==========================================
// Program: Control Flow in Scala
// ==========================================

object Main {
  def main(args: Array[String]): Unit = {
    // 1. Conditionals
    println("Conditionals:")
    val num = 15
    if (num > 0) {
      if (num % 2 == 0) println(s"$num is Positive and Even")
      else println(s"$num is Positive and Odd")
    } else if (num < 0) {
      println(s"$num is Negative")
    } else {
      println("Number is Zero")
    }

    println("\nPattern Matching / Switch:")
    // 2. Pattern Matching
    val grade = "B"
    val msg = grade match {
      case "A" => "Grade A: Excellent!"
      case "B" => "Grade B: Good Job!"
      case "C" => "Grade C: Fair"
      case _   => "Keep Trying!"
    }
    println(msg)

    // 3. For Loop (1 to 5 inclusive)
    println("\nFor Loop (1 to 5):")
    for (i <- 1 to 5) {
      print(if (i == 5) s"$i\n" else s"$i ")
    }

    // 4. While Loop
    println("\nWhile Loop (Countdown):")
    var count = 3
    while (count > 0) {
      print(s"$count ")
      count -= 1
    }
    println("Blastoff!")
  }
}
