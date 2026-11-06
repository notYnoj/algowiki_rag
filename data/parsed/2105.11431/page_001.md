# A LOWER BOUND FOR THE _n_-QUEENS PROBLEM

ZUR LURIA AND MICHAEL SIMKIN

Abstract. The _n_-queens puzzle is to place _n_ mutually non-attacking queens on an \(n\times n\) chessboard. We present a simple two stage randomized algorithm to construct such configurations. In the first stage, a random greedy algorithm constructs an approximate _toroidal n_-queens configuration. In this well-known variant the diagonals wrap around the board from left to right and from top to bottom. We show that with high probability this algorithm succeeds in placing (1-_o_(1))_n_ queens on the board. In the second stage, the method of absorbers is used to obtain a complete solution to the non-toroidal problem. By counting the number of choices available at each step of the random greedy algorithm we conclude that there are more than \(\left(\left(1-o(1)\right)ne^{-3}\right)^n\) solutions to the _n_-queens problem. This proves a conjecture of Rivin, Vardi, and Zimmerman in a strong form.

### 1. Introduction

An _n_-queens configuration is a placement of _n_ mutually non-attacking queens on an \(n\times n\) chessboard. Equivalently, it is an order-_n_ permutation matrix in which the sum of each diagonal is at most 1.

Let Q(_n_) be the number of solutions to the _n_-queens puzzle. The problem of determining Q(_n_) was posed in 1848 by German chess enthusiast Max Bezzel (specifically for _n_=8). It soon attracted the attention of several eminent mathematicians, including Gauss. Pólya also considered the toroidal _n_-queens problem, in which the diagonals wrap around the board from left to right and from top to bottom. We call such diagonals **toroidal diagonals**. Although our main result concerns the classical _n_-queens problem, the toroidal problem features prominently in our proof. For more on the history of the problem, as well as a survey of results and a list of open problems, we refer the reader to Bell and Stevens [1].

To date, the best known upper bound on Q(_n_) is due to the first author [8, Theorem 1.4]: For \(\alpha=1.587\), it holds that \(\mathcal{Q}(n)\le\left(\left(1+o\left(1\right)\right)ne^{-\alpha}\right)^n\). Regarding lower bounds, it is not immediately obvious that Q(_n)\>_0 for all (large enough) _n_. Pauls [10, 11] showed that this holds for all \(n\ge 4\). Thus, \(\mathcal{Q}(n)=\Omega(1)\), and to our knowledge this is the best known general lower bound. Rivin, Vardi, and Zimmerman [12, Theorem 1] gave an exponential lower bound on Q(_n_) that holds for a dense set of integers, and the first author [8, Theorem 1.1] showed that for infinitely many _n_, the superexponential bound \(\mathcal{Q}(n)\ge n^{n/16-o(n)}\) holds.

Our main result is the following lower bound on Q(_n_).

**Theorem 1.1.** _For all natural numbers n,_

\(\mathcal{Q}(n)\ge\left(\left(1-o\left(1\right)\right)\frac{n}{e^3}\right)^n.\)

arXiv:2105.11431v2 [math.CO] 9 Jul 2021

