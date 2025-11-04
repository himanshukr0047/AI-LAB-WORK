# Fundamentals of Prolog

---

##  Introduction

**Prolog (Programming in Logic)** is a high-level declarative programming language primarily used in **Artificial Intelligence** and **Computational Linguistics**.

Instead of writing *how* to perform a task (procedural style), Prolog defines *what* is true through **facts** and **rules**, and then uses **queries** to find logical conclusions.

Prolog is based on:
- Predicate Logic
- Backtracking
- Pattern Matching
- Unification

---

##  Key Concepts

### 1. Facts
Facts are statements that are always true.
prolog
parent(john, mary).
parent(mary, alice).

2. Rules

Rules define relationships between facts using logical implication (:-).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
3. Queries

Queries are questions asked to Prolog to test the facts and rules.

?- grandparent(john, alice).

f the statement is logically true based on the facts and rules, Prolog returns:

true.

How Prolog Works (Mechanism)

Prolog works using Backward Chaining:

Goal-driven reasoning:
Start from the goal (query) and work backward to find facts/rules that satisfy it.

Unification:
Match variables and constants to make conditions true.

Backtracking:
If one path fails, Prolog automatically tries alternative rules or facts.

Success:
When all conditions are satisfied, Prolog returns true or variable substitutions.


Example Knowledge Base

% Facts
parent(john, mary).
parent(mary, alice).
parent(alice, bob).
parent(john, mike).
parent(mike, sara).

% Rule
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).


Query

?- grandparent(john, bob).


Output

true.

## Pseudocode for a Simple Prolog Inference Process
Algorithm: Prolog Backward Chaining
Algorithm PROLOG_INFERENCE(goal):
1. Input: Goal (query) to be proved
2. If goal is a known fact:
       return TRUE
3. Else if goal matches the head of a rule:
       For each rule where head(goal) matches:
           For each sub-goal in rule body:
                if PROLOG_INFERENCE(sub-goal) = TRUE for all sub-goals:
                    return TRUE
4. If all rules fail:
       return FALSE

## Example (Human Family Tree)
% ------------------------------------------
% Example: Family Tree Knowledge Base
% ------------------------------------------

% Facts
parent(john, mary).
parent(mary, alice).
parent(alice, bob).
parent(john, mike).
parent(mike, sara).

% Rules
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).


Sample Queries

?- grandparent(john, bob).
?- ancestor(john, sara).
?- ancestor(mary, bob).


Expected Output

true.
true.
true.

## Advantages

Simple and declarative syntax

Ideal for AI, reasoning, and knowledge representation

Automatically handles pattern matching and backtracking

Natural fit for expert systems and logic-based problem solving

## Limitations

Inefficient for numeric and large-scale data computations

Can be hard to debug with large rule sets

Requires logical thinking to structure facts and rules correctly

## Applications

Expert Systems

Natural Language Processing

Theorem Proving

Knowledge-Based Systems

AI Planning and Reasoning
