#lang racket
;; ==========================================
;; Program: Basic Operations in Racket / Scheme
;; ==========================================
(define a 20)
(define b 6)

(printf "a = ~a, b = ~a\n" a b)
(printf "Addition: ~a, Subtraction: ~a, Multiplication: ~a, Quotient: ~a, Exact Division: ~a, Remainder: ~a\n"
        (+ a b)
        (- a b)
        (* a b)
        (quotient a b)
        (/ a b)
        (remainder a b))
