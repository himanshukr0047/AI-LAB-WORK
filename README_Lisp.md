Fundamentals of LISP Programming
AIM

To understand the fundamentals of LISP (LISt Processing) and its use in Artificial Intelligence for symbolic computation, recursion, and logical reasoning.

INTRODUCTION

LISP (List Processing) is one of the oldest and most popular programming languages in AI.
It was developed by John McCarthy in 1958.
LISP is mainly used for symbolic processing, natural language understanding, expert systems, and machine learning.

It is based on the concept of lists and functions, where both code and data are represented as lists.

BASIC CONCEPTS

Atoms – Basic data elements like numbers or symbols. Example: 5, 'A, 'name

Lists – Ordered collection of atoms or lists. Example: (1 2 3) or (A B C)

Expressions – Written in prefix form. Example: (+ 3 2) gives 5

Variables – Created using setq. Example: (setq x 10)

Functions – Defined using defun. Example: (defun square (x) (* x x))

PSEUDOCODE
Start
1. Define variables x, y, name using setq.
2. Perform arithmetic operations (+, -, *, /).
3. Define functions:
   - square(n)
   - factorial(n) using recursion
   - grade(marks) using cond
4. Demonstrate conditional logic using if and cond.
5. Perform list operations using car, cdr, cons, append.
6. Create a simple knowledge base (parent facts).
7. Write a function to check relationships.
Stop

LISP PROGRAM
; ==========================================================
; Project : Fundamentals of Lisp Programming
; Author  : Himanshu Singh
; Purpose : Demonstrate AI concepts using Lisp
; ==========================================================

; VARIABLE DEFINITIONS
(setq x 10)
(setq y 5)
(setq name "Himanshu")

(print "=== Variable Examples ===")
(print (list 'x x))
(print (list 'y y))
(print (list 'name name))

; BASIC ARITHMETIC OPERATIONS
(print "=== Arithmetic Examples ===")
(print (+ x y))
(print (- x y))
(print (* x y))
(print (/ x y))

; FUNCTION DEFINITIONS
(defun square (n)
  (* n n))

(defun fact (n)
  (if (<= n 1)
      1
      (* n (fact (- n 1)))))

(defun grade (marks)
  (cond ((>= marks 90) 'A)
        ((>= marks 75) 'B)
        ((>= marks 50) 'C)
        (t 'Fail)))

(print "=== Function Examples ===")
(print (list 'square-of-6 (square 6)))
(print (list 'factorial-of-5 (fact 5)))
(print (list 'grade-of-82 (grade 82)))

; CONDITIONAL EXAMPLE
(defun abs-value (x)
  (if (< x 0)
      (- x)
      x))

(print "=== Absolute Value Examples ===")
(print (list 'abs-of--5 (abs-value -5)))
(print (list 'abs-of-8 (abs-value 8)))

; LIST OPERATIONS
(setq mylist '(1 2 3 4 5))

(print "=== List Operations ===")
(print (list 'original mylist))
(print (list 'first-element (car mylist)))
(print (list 'rest-of-list (cdr mylist)))
(print (list 'new-list (cons 0 mylist)))
(print (append mylist '(6 7 8)))

; SIMPLE KNOWLEDGE BASE EXAMPLE
(print "=== Simple Knowledge Base ===")

(setq facts
  '((parent john mary)
    (parent mary alice)
    (parent alice bob)))

(defun is-parent (x y)
  (if (member (list 'parent x y) facts :test #'equal)
      (print (list x 'is 'a 'parent 'of y))
      (print (list x 'is 'not 'a 'parent 'of y))))

(is-parent 'john 'mary)
(is-parent 'john 'alice)

(print "=== End of Lisp Program ===")

SAMPLE OUTPUT
=== Variable Examples ===
(x 10)
(y 5)
(name "Himanshu")

=== Arithmetic Examples ===
15
5
50
2

=== Function Examples ===
(square-of-6 36)
(factorial-of-5 120)
(grade-of-82 B)

=== Absolute Value Examples ===
(abs-of--5 5)
(abs-of-8 8)

=== List Operations ===
(original (1 2 3 4 5))
(first-element 1)
(rest-of-list (2 3 4 5))
(new-list (0 1 2 3 4 5))
(1 2 3 4 5 6 7 8)

=== Simple Knowledge Base ===
(john is a parent of mary)
(john is not a parent of alice)

CONCLUSION

LISP is one of the core languages in Artificial Intelligence.
It supports recursion, symbolic reasoning, and dynamic data handling.
Through lists and functions, LISP can easily represent and manipulate AI knowledge structures.
This experiment shows basic arithmetic, list operations, recursion, and simple reasoning — all core AI concepts.
