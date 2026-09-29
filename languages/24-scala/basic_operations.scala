// ==========================================
// Program: Basic Operations in Scala (Scala 3)
// ==========================================
@main def runOps(): Unit =
  val a = 20
  val b = 6

  println(s"a = $a, b = $b")
  println(s"Addition (a + b)        : ${a + b}")
  println(s"Subtraction (a - b)     : ${a - b}")
  println(s"Multiplication (a * b)  : ${a * b}")
  println(s"Integer Division (a / b): ${a / b}")
  println(s"Float Division (toDouble): ${a.toDouble / b}")
  println(s"Modulo (a % b)          : ${a % b}")
