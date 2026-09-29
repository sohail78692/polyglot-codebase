;;; ==========================================
;;; Program: Basic Operations in Common Lisp (+, -, *, /, mod)
;;; ==========================================
(let ((a 20)
      (b 6))
  (format t "a = ~A, b = ~A~%" a b)
  (format t "Addition (+ a b)        : ~A~%" (+ a b))
  (format t "Subtraction (- a b)     : ~A~%" (- a b))
  (format t "Multiplication (* a b)  : ~A~%" (* a b))
  (format t "Floor Quotient          : ~A~%" (floor a b))
  (format t "Exact Division (/ a b)  : ~A~%" (/ a b))
  (format t "Modulo (mod a b)        : ~A~%" (mod a b)))
