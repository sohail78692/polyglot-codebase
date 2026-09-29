;;; ==========================================
;;; Program: Basic Operations in Clojure (+, -, *, quot, mod)
;;; ==========================================
(let [a 20
      b 6]
  (println (str "a = " a ", b = " b))
  (println (str "Addition (+ a b)        : " (+ a b)))
  (println (str "Subtraction (- a b)     : " (- a b)))
  (println (str "Multiplication (* a b)  : " (* a b)))
  (println (str "Quotient (quot a b)     : " (quot a b)))
  (println (str "Exact Division (/ a b)  : " (/ a b)))
  (println (str "Modulo (mod a b)        : " (mod a b))))
