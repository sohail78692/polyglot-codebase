#lang racket
;; ==========================================
;; Program: Control Flow in Scheme / Racket
;; ==========================================

(define (main)
  ;; 1. Conditionals (cond)
  (displayln "Conditionals:")
  (define num 15)
  (cond
    [(> num 0)
     (if (= (remainder num 2) 0)
         (printf "~a is Positive and Even\n" num)
         (printf "~a is Positive and Odd\n" num))]
    [(< num 0) (printf "~a is Negative\n" num)]
    [else (displayln "Number is Zero")])

  (displayln "\nPattern Matching / Switch:")
  ;; 2. Case statement
  (define grade 'B)
  (case grade
    [(A) (displayln "Grade A: Excellent!")]
    [(B) (displayln "Grade B: Good Job!")]
    [(C) (displayln "Grade C: Fair")]
    [else (displayln "Keep Trying!")])

  ;; 3. For loop
  (displayln "\nFor Loop (1 to 5):")
  (for ([i (in-range 1 6)])
    (display i)
    (if (= i 5) (newline) (display " ")))

  ;; 4. While loop via named let recursion
  (displayln "\nWhile Loop (Countdown):")
  (let loop ([count 3])
    (when (> count 0)
      (printf "~a " count)
      (loop (- count 1))))
  (displayln "Blastoff!"))

(main)
