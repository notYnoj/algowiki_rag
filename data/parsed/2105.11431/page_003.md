<tbc>toroidal problem, these equations are replaced by equalities modulo _n_. The toroidal diagonals containing the square (_x,y_) are \(\{(x',y')\in[n]^2:x'+y'=x+ymodn\}\) and \(\{(x',y')\in[n]^2:x'-y'=x-ymodn\}\). Note that there are _n_ toroidal diagonals of each type, all of size _n_. A **partial** _n_**-queens configuration** is a set \(Q\subset[n]^2\) such that every row, column, and diagonal contains at most one element of _Q_. An _n_-queens configuration is a partial _n_-queens configuration of size _n_. Toroidal configurations are defined similarly using toroidal diagonals.

## 2. A randomized construction of _n_-queens configurations

In this section we formally define the algorithm we use to construct _n_-queens configurations. As mentioned in the introduction, we begin by using a random greedy algorithm to construct a partial _toroidal n_-queens configuration.

Fix (a sufficiently large) \(n\in\mathbb{N}\), and set

\(\alpha=10^{-4},T=\lfloor(1-n^{-\alpha})n\rfloor.\)

_Algorithm_ 2.1.

\(\bullet\) Set \(Q(0)=\emptyset\).<tbc>

\(\bullet\) For each \(0\le t<T\), let \(\mathcal{A}(t)\subseteq[n]^2\) be the set of **available** positions, i.e., those positions lying in a row, column, and toroidal diagonals unoccupied by _Q(t_).<tbc>

\(\bullet\) If \(\mathcal{A}(t)=\emptyset\), abort.<tbc>

\(\bullet\) Otherwise, choose \((x_t,y_t)\in\mathcal{A}(t)\) uniformly at random and independently of previous choices. Set \(Q(t+1)=Q(t)\cup\{(x_t,y_t)\}\).

For technical reasons, if the algorithm aborts at time _t_, then for every \(t<s\le T\) we set _Q(s_)=_Q(t_).

In Proposition 3.1 we show that w.h.p. Algorithm 2.1 does not abort. In the next phase of the algorithm we hope to remove a small number of queens from the board, and then complete the puzzle. The key is the idea of _absorption_, which we now illustrate: Suppose \(Q\subseteq[n]^2\) is a partial _n_-queens configuration that does not cover row _r_ and column _c_. We wish to obtain a partial _n_-queens configuration \(Q'\) that covers all rows and columns covered by _Q_, and also covers row _r_ and column _c_. We might try adding (_r,c_) to _Q_, but if either of the diagonals running through (_r,c_) is occupied this will not work. Instead, we will look for a queen \((x,y)\in Q\) that satisfies:

(a) (_r,y_) and (_x,c_) do not share a diagonal (equivalently, (_r,c_) and (_x,y_) do not share a diagonal),<tbc>

(b) none of the diagonals containing (_r,y_) or (_x,c_) are occupied.

Supposing such a queen exists, we observe that \(Q':=(Q\backslash\{(x,y)\})\cup\{(r,y),(x,c)\}\) is a partial _n_-queens configuration satisfying the conditions above. In this way, we have absorbed row _r_ and column _c_ into our configuration. We call such a queen an **absorber for** (_r,c_) **in** _Q_. We denote the set of absorbers for (_r,c_) in _Q_ by B_<sub>Q</sub>(r,c_).

The following algorithm attempts to use absorbers to complete _Q(T_) (the outcome of Algorithm 2.1).

_Algorithm_ 2.2.

\(\bullet\) Let _L<sub>R</sub>_ and _L<sub>C</sub>_ be, respectively, the sets of rows and columns not covered by _Q(T_). Note that |_L<sub>R</sub>_|=|_L<sub>C</sub>_|=:_k_.<tbc>

