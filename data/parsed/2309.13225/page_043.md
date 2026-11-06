<tbc>**Theorem 5.12.** _Let_ \(\beta\ge 4\) _be an even integer and C\>_0 _be a constant. Let G be an undirected, unweighted graph with n vertices. Algorithm 7 computes_ \(\hat{\delta}\) _in time,_<tbc>

\(\tilde{O}\left(n^{2+\frac{2x}{\beta+2}}\right)\)

<tbc>_x is the solution to,_

\(\omega\left(1-\frac{\beta-2}{\beta+2}x,1-x,1-\frac{\beta-4}{\beta+2}x\right)=2+\frac{2x}{\beta+2}\)

_such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\) _for all u,v and whenever_ \(\delta(u,v)\le C\), \(\hat{\delta}(u,v)\le\delta(u,v)+\beta\).

The above result also implies a more efficient algorithm for approximating distances up to small polynomials.

**Corollary 5.13.** _Let_ \(\varepsilon>0\)_. Then, there is an algorithm computing_ \(\hat{\delta}\) _in time_<tbc>

\(\tilde{O}\left(n^{2+\frac{2x}{\beta+2}}\right)\)

<tbc>_x is the solution to,_

\(\omega\left(1-\frac{\beta-2}{\beta+2}x,1-x,1-\frac{\beta-4}{\beta+2}x\right)+\varepsilon=2+\frac{2x}{\beta+2}\)

_such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\) _for all u,v and whenever_ \(\delta(u,v)\le n^\varepsilon\), \(\hat{\delta}(u,v)\le\delta(u,v)+\beta\).

_Proof._ The only difference with the proof of Theorem 5.12 is the setting of _x_ and the complexity analysis. For bounded _C_, the computation of the (min,+) product requires time,

\(Cn^\omega\big(1-\frac{\beta-2}{\beta+2}x,1-x,1-\frac{\beta-4}{\beta+2}x\big)\)

Now, since the entries are bounded instead by \(n^\varepsilon\), we bound the computation of the (min,+) product by,

\(n^\omega\big(1-\frac{\beta-2}{\beta+2}x,1-x,1-\frac{\beta-4}{\beta+2}x\big)+\varepsilon\)

We now present a high level overview of Theorem 5.12.

## High Level Overview

The algorithm is essentially a simplification of the previous Algorithm 6. Indeed, we can invoke `BoundedMinPlus` in place of `MonotoneMinPlus`, which is a faster algorithm and does not require the transformation `BDtoMonotone`.

## Algorithm

Algorithm 7 is identical to Algorithm 6. The only modification is the invocation of `BoundedMinPlus` in place of `AdditiveAPASP`, as the entries to the matrices are now bounded by constant _C_.

Below, we exhibit some running times for specific choices of \(\beta\), using \[Bra\].

**Corollary 5.14.** _We obtain the following running times for an additive approximation on distances_ \(\delta(u,v)\le C\).

We now present the algorithm and proof of Theorem 5.12.

\begin{tabular}{cc}
\(\beta\) & _time_ \\
4 & _n_<sup>2.09314841</sup> \\
6 & _n_<sup>2.05794292</sup> \\
8 & _n_<sup>2.04220679</sup> \\
10 & _n_<sup>2.03322582</sup> \\
\end{tabular}

