Using \(|\mu_{i,j}|\le 1/2\) and \(\|\mathbf{b}_j^*\|_2\le\gamma(n)\lambda_n(\mathcal{L})\), we get

\(\|\mathbf{b}_i\|_2^2\le\gamma(n)^2\lambda_n(\mathcal{L})^2+\frac{1}{4}(i-1)\gamma(n)^2\lambda_n(\mathcal{L})^2,\)<br>
\(\le n\gamma(n)^2\lambda_n(\mathcal{L})^2.\)

Therefore, \(\|\mathbf{b}_i\|_2\le\sqrt{n}\gamma(n)\lambda_n(\mathcal{L})\) for all \(i\in[n]\)

Next, we use the best algorithms for the approximate Shortest Vector Problem. This follows from the block reduction introduced by Schnorr \[Sch87\].

**Theorem B.2** (\[Sch87, SE94, GN08, ALNSD20\])**.** _Let_ \(\kappa\ge 1\)_. There exists a randomized algorithm that, given an n-dimensional lattice_ L_, computes a nonzero vector_ \(\mathbf{v}\in\mathcal{L}\) _in time_ \(2^{\mathcal{O}(n/\kappa)}\) _such that_

\(\|\mathbf{v}\|_2\le n^\kappa\cdot\lambda_1(\mathcal{L}).\)

To the best of our knowledge, the currently best algorithm actually runs in time \(\mathcal{O}^\star(2^{\frac{0.802n}{\kappa+1}})\) and returns \(n^\kappa\)-approximation (see \[ALNSD20,  1\] for historical overview). Nevertheless, Theorem B.2 is sufficient as the exact dependence on behind \(\mathcal{O}(\cdot)\) does not matter for us.

Combining Theorem B.1 and Theorem B.2 gives Theorem 5.1.

## B.1 Variant of Theorem B.1 for _n_-SMP

Also, we need the following slightly different variant of Theorem B.1, when the oracle solves _n_-SMP.

**Theorem B.3.** _Let_ \(\gamma:\mathbb{N}\rightarrow\mathbb{R}_{\ge 1}\) _be non-decreasing. Suppose there is an oracle that, on input any rank-m lattice_ M_, returns a nonzero vector_ \(\mathbf{x}\in\mathcal{M}\) _such that_<tbc>

\(\|\mathbf{x}\|_2\le\gamma(m)\lambda_m(\mathcal{M}).\)

<tbc>_Then there is a polynomial-time algorithm that, given an n-dimensional lattice_ L_, makes n oracle calls and outputs n linearly independent vectors_ \(\mathbf{b}_1,\dots,\mathbf{b}_n\in\mathcal{L}\) _such that_<tbc>

\(\|\mathbf{b}_i\|_2\le\sqrt{n}\gamma(n)\lambda_n(\mathcal{L})\text{\textit{for all}}i\in[n].\)

<tbc>_Proof sketch._ The proof is modified only in the step where we bound the oracle output on the projected lattice. At iteration _i_, let \(\mathcal{L}_i:=\pi_i(\mathcal{L})\), where \(\pi_i\) is the orthogonal projection onto \(W_{i-1}^\perp\) and _W_<sub>_i_-1</sub>=span(**b**<sub>1</sub>_,...,_**b**<sub>_i_-1</sub>). Then L_<sub>i</sub>_ has rank _m=n-i_+1. So the oracle now returns a nonzero vector \(\mathbf{y}_i\in\mathcal{L}_i\) satisfying<tbc>

\(\|\mathbf{y}_i\|_2\le\gamma(m)\lambda_m(\mathcal{L}_i).\)

<tbc>The rest of the construction of **b**_<sub>i</sub>_ from a lift of **y**_<sub>i</sub>_ is unchanged. The only point to reprove is the bound on \(\|\mathbf{b}_i^*\|_2=\|\mathbf{y}_i\|_2\). For this, take _n_ linearly independent vectors \(\mathbf{v}_1,\dots,\mathbf{v}_n\in\mathcal{L}\) such that

\(\|\mathbf{v}_t\|_2\le\lambda_n(\mathcal{L})\text{for all}t\in[n].\)

Since _W_<sub>_i_-1</sub> has dimension _i_-1, at most _i_-1 of these vectors can lie in _W_<sub>_i_-1</sub>. Hence at least _n_-(_i_-1)=_m_ of the projected vectors \(\pi_i(v_t)\) are nonzero. Moreover, these projected vectors are linearly independent in L_<sub>i</sub>_. Indeed, if a nontrivial linear combination of them were zero, then the same combination of the corresponding **v**_<sub>t</sub>_’s would lie in _W_<sub>_i_-1</sub>, contradicting the linear independence of the **v**_<sub>t</sub>_’s together with dim(_W_<sub>_i_-1</sub>)=_i_-1.

