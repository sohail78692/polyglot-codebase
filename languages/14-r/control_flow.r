# ==========================================
# Program: Control Flow in R
# ==========================================

main <- function() {
  # 1. Conditionals
  cat("Conditionals:\n")
  num <- 15
  if (num > 0) {
    if (num %% 2 == 0) {
      cat(num, "is Positive and Even\n")
    } else {
      cat(num, "is Positive and Odd\n")
    }
  } else if (num < 0) {
    cat(num, "is Negative\n")
  } else {
    cat("Number is Zero\n")
  }

  cat("\nPattern Matching / Switch:\n")
  # 2. Switch function
  grade <- "B"
  msg <- switch(grade,
    "A" = "Grade A: Excellent!",
    "B" = "Grade B: Good Job!",
    "C" = "Grade C: Fair",
    "Keep Trying!"
  )
  cat(msg, "\n")

  # 3. For Loop
  cat("\nFor Loop (1 to 5):\n")
  cat(paste(1:5, collapse = " "), "\n")

  # 4. While Loop
  cat("\nWhile Loop (Countdown):\n")
  count <- 3
  while (count > 0) {
    cat(count, "")
    count <- count - 1
  }
  cat("Blastoff!\n")
}

main()
