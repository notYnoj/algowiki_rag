The input of a large block contains _B/w_<sub>2</sub> large elements. The memory can contain at most (_M-B)/w_<sub>1</sub> small elements, and so the total number of possible permutations achievable is

\(P=\left(\frac{M-B}{w_1}+\frac{B}{w_2}\right)\left(\frac{B}{w_2}!\right)\)<br>
\(<\left(\frac{M}{w_1}\right)\left(\frac{B}{w_2}!\right)\)<br>
\(<\left(\frac{ew_2M}{Bw_1}\right)^{B/w_2}\left(\frac{B}{w_2}!\right)\)

This gives

\(logP=O\left(\frac{B}{w_2}log\left(\frac{Mw_2}{Bw_1}\right)+\frac{B}{w_2}log\left(\frac{B}{w_2}\right)\right)\)<br>
\(=O\left(\frac{B}{w_2}log\left(\frac{M}{w_1}\right)\right)\)

bits per I/O.

In both cases, the amortized number of bits achieved is:

1. _O(B/w_<sub>1</sub>) bits per I/O, equivalent to _O_(1) bit per _w_<sub>1</sub>_/B_ I/Os.<tbc>

2. \(\frac{B}{w_2}log\left(\frac{M}{w_1}\right)\) bits per I/O, equivalent to log(_M/w_<sub>1</sub>) bits per _w_<sub>2</sub>_/B_ I/Os.

## 6 Upper bounds on Sorting and the Batched Predecessor Problem

Our algorithm for Sort(_S,L_) works in three steps:1) sort the short elements using traditional multi-way external memory merge-sort [1], 2) solve the associated PLE(_S,L_) problem, and 3) sort the long stripes obtained again using multi-way mergesort. The first and third steps give the first and third terms in the sorting complexity in Theorem 2.

We give two algorithms to solve PLE(_S,L_): PLE-DFS and PLE-BFS. The final upper bound is the minimum of the two terms, as presented in Theorem 18.

