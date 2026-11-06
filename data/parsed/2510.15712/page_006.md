In fact, we can replace the step functions with continuous functions. For this, we add dummy players with only one strategy consisting of occupying a single resource, so that any resource can be occupied by 4 players (effectively this corresponds to making all clauses have length exactly 4). We define a common function _f(x_) and set the delay of the resource _C<sub>j</sub>_ under load \(x\in\{0,1,2,3,4\}\) to _d<sub>C<sub>j</sub></sub>(x_)=_f(mx+j_). Note that _j\<m_, since _m_ is the number of clauses. We choose _f_ such that

\(f(x+1)\ge(1+\alpha)f(x)\) (2.3)

and \(f(x)\ge 0\) hold for any \(x\in[0,5m-1]\). The term in (2.1) is then _f(x_) for some _x\<_5_m_ and the term in Equation (2.2) is then \(\sum_{k<x}f(k)\) as flipping _x<sub>i</sub>_ may lead to all smaller clauses being false (that means 4 players using the clause resource) and in higher-priority clauses that contain _x<sub>i</sub>_, the number of unsatisfied literals may increase to some \(l\le 3\). This is a gross overestimate. From (2.3) it follows that \(f(k-i)\le(1+\alpha)^{-i}f(x)\) and thus (2.2) is at most

\(\sum_{k<x}f(k)=\sum_{i=1}^xf(x-i)\le f(x)\sum_{i=1}^x(1+\alpha)^{-i}\le f(x)\sum_{i=1}^\infty(1+\alpha)^{-i}=\frac{f(x)}{\alpha}.\)

Therefore this is an \(\alpha\)-improving move. Now setting \(f(x):=(1+\alpha)^x\) obviously fulfills (2.3); so does _f(x_):=_x<sup>d</sup>_ with \(d\ge 5mln(\alpha+1)\) since \((\frac{x+1}{x})^d\ge e^\frac{d}{x+1}\ge e^{d/5m}\ge\alpha+1\).

## 3 Permutation Orbit Local Minimum with Abelian groups - Proof of Theorem 4

We will show a PLS-reduction from LocalLexMax-4-SAT to Permutation Orbit Local Minimum where all the \(\pi_i\) commute. We use a technique by Buchheim and Jünger [2]. Let the 4-CNF \(F=C_1\wedge\cdots\wedge C_m\) be the input instance and _V_={_x_<sub>1</sub>_,...,x<sub>n</sub>_} its variables. Clause _C<sub>i</sub>_ has weight 2<sup>_m-i_</sup>. We assume for simplicity that each clause in _F_ has exactly four literals; the reduction for the general case is almost identical, but notation would become less readable. We will now describe the instance of Polm - set of positions, initial bit string, the commuting permutations, and, finally, the order on the positions.

**1. The set of positions.** For each 4-clause _C_ and each \(b\in\{0,1\}^4\) we construct a position _C<sub>b</sub>_. There is exactly one assignment \(b^*\in\{0,1\}^4\) to the four variables in _C_ that violates it; the corresponding position _C_<sub>_b_<sup>∗</sup></sub> is called a _violating position_ and denoted by _C_<sup>∗</sup>. We have a total of 16_m_ positions; among those, _m_ are violating.

**2. The initial bit string.** Our initial bit string \(\vec{s}\) puts a 1 on \(C_\vec{0}\) for each clause and a 0 on all other _C<sub>b</sub>_. This corresponds to the assignment that sets all variables to 0.

**3. The permutations.** For a variable _x_ and a clause _C_, let \(\pi_{x,C}\) be the permutation defined as follows:

**a.** If _x_ does not show up in _C_, then \(\pi_{x,C}\) is the identity.

**b.** If _x_ is the _i_-th variable of _C_ (with \(1\le i\le 4\)), then \(\pi_{x,C}\) is the involution that swaps each position _C<sub>b</sub>_ with position \(C_{b\oplus e_i}\).

So \(\pi_{x,C}\) basically switches the value of _x in clause C_. We define \(\pi_x\) to be

\(\pi_x:=\prod_{C\in F}\pi_{x,C}\)

so \(\pi_x\) switches the value of _x_ in every clause. Our set of generators is

\(G:=\{\pi_x|x\in V\}\)

