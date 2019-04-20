male(james1).
male(charles1).
male(charles2).
male(james2).
male(george1).

female(catherine).
female(elizabeth).
female(sophia).

parent(james1, charles1).
parent(elizabeth, sophia).
parent(sophia, george1).
parent(charles1, catherine).
parent(charles1, charles2).
parent(charles1, james2).
parent(james1, elizabeth).


mother(X, Y) :- female(X),parent(X,Y).
father(X, Y) :- male(X),parent(X,Y).
gf(X,Y) :- male(X),parent(X,Z),parent(Z,Y).
sister(X, Y) :-female(X), parent(Z, X), parent(Z, Y) -> write('Parent: '), writeln(Z).
brother(X, Y) :-male(X), parent(Z, X), parent(Z, Y) -> write('Parent: '), writeln(Z).

fun(X, R) :- R is 2*X+3.

duzina([], 0).
duzina([_|T], N) :- duzina(T, Y), N is Y + 1.

hanoi(1, A, _, C) :-write('Pomjeri sa '),write(A),write(' na '),write(C), write('\n').

hanoi(N, A, B, C) :-N>1,M is N-1,hanoi(M, A, C, B),hanoi(1,A,B,C),hanoi(M,B, A, C).

abs(X, Y) :- X < 0 -> Y is -X; Y = X.

write_list([]).
write_list([Head | Tail]):-
    write(Head), write(Tail), nl, write_list(Tail).

min1_list([X], N) :- N is X.
min1_list([X, Y | Tail], N):-
   (    X > Y -> min_list([Y | Tail], N)
   ;
    min_list([X | Tail], N)
   ).

max2_list([X], N) :- N is X.
max2_list([X, Y | Tail], N):-
   (    X < Y -> max_list([Y | Tail], N)
   ;
    max_list([X | Tail], N)
   ).

add(L, R) :-
    min1_list(L, Lmin),
    max2_list(L, Lmax),
    R is Lmin + Lmax.

append([],L,L) :- write('hahu '), writeln(L).
append([X|T],L,[X|R]) :- write([X|T]), write(','), write(L), write(','), writeln([X|R]), append(T,L,R), write("hehe2"), write([X|T]), write(','), write(L), write(','), writeln([X|R]).

listsize([], 0).
listsize([_|T], L+1):- listsize(T, L).

check(L, R):-
    listsize(L, Size1),
    listsize(R, Size2),
    Size1 > 2*Size2.
