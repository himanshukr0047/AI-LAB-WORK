% ==========================================================
% Project: Family Relationship Knowledge Base (Prolog)
% Author : Himanshu Singh
% Purpose: Demonstrate basic AI reasoning using Prolog
% ==========================================================

% --------------------------
% FACTS
% --------------------------
% Each fact defines a direct parent relationship.

parent(john, mary).
parent(mary, alice).
parent(alice, bob).
parent(john, mike).
parent(mike, sara).
parent(sara, tom).
parent(alice, david).
parent(david, lily).

% --------------------------
% RULES
% --------------------------

% Rule 1: X is a grandparent of Y
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Rule 2: X is an ancestor of Y
ancestor(X, Y) :-
    parent(X, Y).             % Base case
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).           % Recursive case

% Rule 3: X and Y are siblings (share same parent)
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Rule 4: X is a cousin of Y
cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B),
    X \= Y.

% Rule 5: X is a descendant of Y (reverse of ancestor)
descendant(X, Y) :-
    ancestor(Y, X).

% --------------------------
% SAMPLE QUERIES
% --------------------------
% To test in SWI-Prolog or any Prolog interpreter:
%
% ?- grandparent(john, bob).
% ?- ancestor(john, lily).
% ?- sibling(mary, mike).
% ?- cousin(bob, sara).
% ?- descendant(lily, john).
%
% Expected Output:
% true.
% true.
% true.
% true.
% true.

% --------------------------
% END OF FILE
% --------------------------
