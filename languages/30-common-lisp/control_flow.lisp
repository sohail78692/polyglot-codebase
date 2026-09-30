;; ==========================================
;; Program: Control Flow in Common Lisp
;; ==========================================

(defun main ()
  ;; 1. Conditionals (cond)
  (format t "Conditionals:~%")
  (let ((num 15))
    (cond
      ((> num 0)
       (if (= (mod num 2) 0)
           (format t "~A is Positive and Even~%" num)
           (format t "~A is Positive and Odd~%" num)))
      ((< num 0) (format t "~A is Negative~%" num))
      (t (format t "Number is Zero~%"))))

  (format t "~%Pattern Matching / Switch:~%")
  ;; 2. Case macro
  (let ((grade 'B))
    (case grade
      (A (format t "Grade A: Excellent!~%"))
      (B (format t "Grade B: Good Job!~%"))
      (C (format t "Grade C: Fair~%"))
      (otherwise (format t "Keep Trying!~%"))))

  ;; 3. For loop (loop for i from 1 to 5)
  (format t "~%For Loop (1 to 5):~%")
  (loop for i from 1 to 5 do
    (format t "~A~A" i (if (= i 5) "~%" " ")))

  ;; 4. While loop (countdown)
  (format t "~%While Loop (Countdown):~%")
  (let ((count 3))
    (loop while (> count 0) do
      (format t "~A " count)
      (decf count)))
  (format t "Blastoff!~%"))

(main)
