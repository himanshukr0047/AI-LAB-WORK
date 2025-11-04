; ==========================================================
; Project : Fundamentals of Lisp Programming
; Author  : Himanshu Kumar
; Purpose : Demonstrate AI concepts using Lisp
; ==========================================================

; --------------------------
; VARIABLE DEFINITIONS
; --------------------------
(setq x 10)
(setq y 5)
(setq name "Himanshu")

(print "=== Variable Examples ===")
(print (list 'x x))
(print (list 'y y))
(print (list 'name name))

; --------------------------
; BASIC ARITHMETIC OPERATIONS
; --------------------------
(print "=== Arithmetic Examples ===")
(print (+ x y))   ; Addition: 15
(print (- x y))   ; Subtraction: 5
(print (* x y))   ; Multiplication: 50
(print (/ x y))   ; Division: 2

; --------------------------
; FUNCTION DEFINITIONS
; --------------------------

; Square of a number
(defun square (n)
  (* n n))

; Factorial (Recursive)
(defun fact (n)
  (if (<= n 1)
      1
      (* n (fact (- n 1)))))

; Grade calculation using COND
(defun grade (marks)
  (cond ((>= marks 90) 'A)
        ((>= marks 75) 'B)
        ((>= marks 50) 'C)
        (t 'Fail)))

(print "=== Function Examples ===")
(print (list 'square-of-6 (square 6)))   ; 36
(print (list 'factorial-of-5 (fact 5)))  ; 120
(print (list 'grade-of-82 (grade 82)))   ; B

; --------------------------
; CONDITIONAL EXAMPLE
; --------------------------

(defun abs-value (x)
  (if (< x 0)
      (- x)
      x))

(print "=== Absolute Value Examples ===")
(print (list 'abs-of--5 (abs-value -5)))  ; 5
(print (list 'abs-of-8 (abs-value 8)))    ; 8

; --------------------------
; LIST OPERATIONS
; --------------------------
(setq mylist '(1 2 3 4 5))

(print "=== List Operations ===")
(print (list 'original mylist))
(print (list 'first-element (car mylist)))       ; 1
(print (list 'rest-of-list (cdr mylist)))        ; (2 3 4 5)
(print (list 'new-list (cons 0 mylist)))         ; (0 1 2 3 4 5)
(print (append mylist '(6 7 8)))                 ; (1 2 3 4 5 6 7 8)

; --------------------------
; SYMBOLIC LOGIC EXAMPLE (AI Concept)
; --------------------------
(print "=== Simple Knowledge Base ===")

; Define knowledge base
(setq facts
  '((parent john mary)
    (parent mary alice)
    (parent alice bob)))

; Function to check if X is a parent of Y
(defun is-parent (x y)
  (if (member (list 'parent x y) facts :test #'equal)
      (print (list x 'is 'a 'parent 'of y))
      (print (list x 'is 'not 'a 'parent 'of y))))

; Example queries
(is-parent 'john 'mary)
(is-parent 'john 'alice)

; --------------------------
; END OF FILE
; --------------------------
(print "=== End of Lisp Program ===")
