% Task three: Family Tree in Prolog
male(kariuki).
male(ngigi).
male(munene).
male(kevin).
male(samuel).

female(mary).
female(njango).
female(mercy).
female(grace).
female(wanjiru).

parent(kariuki, ngigi).
parent(kariuki, munene).
parent(mary, ngigi).
parent(mary, munene).
parent(ngigi, kevin).
parent(ngigi, grace).
parent(njango, kevin).
parent(njango, grace).
parent(munene, samuel).
parent(munene, wanjiru).
parent(mercy, samuel).
parent(mercy, wanjiru).

father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
grandfather(X, Z) :- grandparent(X, Z), male(X).
grandmother(X, Z) :- grandparent(X, Z), female(X).
grandchild(X, Z) :- grandparent(Z, X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y) :- sibling(X, Y), female(X).
uncle(X, Y) :- brother(X, Z), parent(Z, Y).
aunt(X, Y) :- sister(X, Z), parent(Z, Y).
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B).