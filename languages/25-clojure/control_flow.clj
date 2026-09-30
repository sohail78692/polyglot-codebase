;; ==========================================
;; Program: Control Flow in Clojure
;; ==========================================

(ns control-flow)

(defn -main []
  ;; 1. Conditionals (cond)
  (println "Conditionals:")
  (let [num 15]
    (cond
      (> num 0) (if (zero? (mod num 2))
                  (println (str num " is Positive and Even"))
                  (println (str num " is Positive and Odd")))
      (< num 0) (println (str num " is Negative"))
      :else     (println "Number is Zero")))

  (println "\nPattern Matching / Switch:")
  ;; 2. Case macro
  (let [grade "B"]
    (println (case grade
               "A" "Grade A: Excellent!"
               "B" "Grade B: Good Job!"
               "C" "Grade C: Fair"
               "Keep Trying!")))

  ;; 3. For Loop via doseq
  (println "\nFor Loop (1 to 5):")
  (doseq [i (range 1 6)]
    (print (str i (if (= i 5) "\n" " "))))

  ;; 4. While Loop via loop/recur
  (println "\nWhile Loop (Countdown):")
  (loop [count 3]
    (if (> count 0)
      (do
        (print (str count " "))
        (recur (dec count)))
      (println "Blastoff!"))))

(-main)
