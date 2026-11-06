continuations and no unforced port. These observations prove the prefix bound by induction, even if global self-avoidance constraints are dropped.

A suffix of length _b_ after the last unforced edge lies in _J-xy_ and has at most _C<sub>D</sub>(D_-1)_<sup>b</sup>_ choices when explored backwards from _y_. The intervening unforced edge is fixed by the two endpoints and contributes 1_/n_. Summing over its position, and using (167) for each simple path, bounds the probability of an alternate path of length \(\ell\) by

\(O_D(\ell(D-1)^\ell/n).\) (168)

The prescribed unforced edges of a simple path form a matching; paths that violate this contribute zero. Summing over \(\ell\le g-2\) and over the _s_ forced edges gives

\(Pr_\text{planted}(\text{invalid})\le O_D(sg(D-1)^g/n)=n^{c-1+o(1)}=o(1).\) (169)

Finally sum (166) over valid trajectories. Equations (163) and (169) prove the lower bound.

We also record an upper bound for the partial graph used in the converse. Let B_<sub>n</sub>_ denote the density event for the first _D_-3 matching rounds (the sure event when _D_=3), and let

\(G_n^T:=H\cup M_1\cup\cdots\cup M_{D-3}\cup M_T.\) (170)

Combining the proof of Lemma 3 for the preceding rounds with (158) for the final prefix gives, for every specified port-labelled _J_ with \(w\le K_0logn\),

\(Pr(J\subseteq G_n^T,\mathcal{B}_n)\le(1+o(1))n^{-w}.\) (171)

The error is uniform in _J_, including disconnected _J_. Only upper bounds are being multiplied here, conditional on the graph already constructed.

## A.4 A supply of logarithmic-length cycles

Choose once and for all

\(c<\kappa<1,L=2\lfloor\kappa log_{D-1}n/2\rfloor,s_0=\left[\frac{3logL}{log((D-1)/(D-2))}\right].\) (172)

Then _s_<sub>0</sub>=_O<sub>D</sub>_(loglog_n_), 2_s_<sub>0</sub>_\<g_, and \(L\ge g\) for large _n_.

Condition on the (_D_-1)-regular graph _A_ present before the final round. A _candidate cycle_ consists of _k_ oriented paths in _A_, of lengths

\(1\le b_i\le s_0,\sum_{i=1}^k(b_i+1)=L,\) (173)

whose vertex sets are pairwise at distance at least _g_, joined cyclically by _k_ proposed final-round matching edges. Two descriptions differing only by a cyclic starting path or reversal describe the same candidate.

The joining edges form a matching _F_, and _A+F_ has girth at least _g_. Indeed, an old path between distinct path groups has length at least _g_. A shorter new cycle would therefore have to travel within each group between its two endpoints and traverse the whole ring of joining edges. Each chosen path is the unique shortest connection between its endpoints, because its length is at most _s_<sub>0</sub>_\<g/_2. Such a ring has length at least \(L\ge g\).

