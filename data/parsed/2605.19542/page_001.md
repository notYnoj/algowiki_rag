# LINEAR ALGEBRAIC METHOD AND THE ERD ̋S-HEILBRONN CONJECTURE

GUANZHONG YANG

Abstract. Additive combinatorics asks for lower bounds on sumsets and restricted sumsets over finite fields. Central examples are the Cauchy–Davenport theorem and the Erd ̋os–Heilbronn conjecture. In this note, we develop Das’s linear algebraic method and give a new elementary proof of the Alon–Nathanson–Ruzsa theorem for restricted sumsets, which implies the Erd ̋os–Heilbronn conjecture. Compared with the classical polynomial method via Combinatorial Nullstellensatz, our proof uses only basic linear algebra over finite fields, including Vandermonde matrices and solvability of linear systems.

### 1. Introduction

Additive combinatorics is a central branch of combinatorial number theory, focusing on the additive structure of subsets of integers and finite fields [7]. A foundational problem in this field is to give sharp lower bounds for the cardinality of sumsets, which has wide applications in number theory, combinatorics, and theoretical computer science.

Let _p_ be a prime number, and let Z_/p_Z denote the finite field of integers modulo _p_. For nonempty subsets _A,B_ of Z_/p_Z, the classical sumset is defined as

\(A+B=\{a+b:a\in A,b\in B\}.\)

The celebrated Cauchy-Davenport theorem, a cornerstone of additive combinatorics, gives a tight lower bound for the size of such sumsets:

\(|A+B|\unknown min\{p,|A|+|B|-1\}.\)

In 1964, Erd ̋os and Heilbronn proposed a famous conjecture for the so-called restricted sumset, where the summands are required to be distinct [5]. For nonempty subsets _A,B_ of Z_/p_Z, we define the restricted sumset as

\(A\dot{+}B=\{a+b:a\in A,b\in B,a\neq b\}.\)

2020 _Mathematics Subject Classification._ Primary 11B75; Secondary 11P70. _Key words and phrases._ sumset, Erd ̋os–Heilbronn conjecture, linear algebra.

arXiv:2605.19542v1 [math.CO] 19 May 2026

