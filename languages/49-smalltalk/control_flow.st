"==========================================
 Program: Control Flow in Smalltalk (GNU Smalltalk)
 =========================================="

| num grade count forItems whileItems |

Transcript show: 'Conditionals:'; cr.
num := 15.
(num > 0)
    ifTrue: [
        ((num \ 2) = 0)
            ifTrue: [ Transcript show: num printString, ' is Positive and Even'; cr ]
            ifFalse: [ Transcript show: num printString, ' is Positive and Odd'; cr ] ]
    ifFalse: [ Transcript show: 'Not positive'; cr ].

Transcript cr.
Transcript show: 'Pattern Matching / Switch:'; cr.
grade := 'B'.
(grade = 'A') ifTrue: [ Transcript show: 'Grade A: Excellent!'; cr ].
(grade = 'B') ifTrue: [ Transcript show: 'Grade B: Good Job!'; cr ].
(grade = 'C') ifTrue: [ Transcript show: 'Grade C: Fair'; cr ].

Transcript cr.
Transcript show: 'For Loop (1 to 5):'; cr.
forItems := OrderedCollection new.
1 to: 5 do: [ :i | forItems add: i printString ].
Transcript show: (forItems fold: [ :a :b | a, ' ', b ]); cr.

Transcript cr.
Transcript show: 'While Loop (Countdown):'; cr.
count := 3.
whileItems := OrderedCollection new.
[ count > 0 ] whileTrue: [
    whileItems add: count printString.
    count := count - 1.
].
whileItems add: 'Blastoff!'.
Transcript show: (whileItems fold: [ :a :b | a, ' ', b ]); cr.
