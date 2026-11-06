**Proof.** There are _n_!2_<sup>wn</sup>_ different input arrays _A_ and A<sup>∗</sup> had error probability at most 1/2 over a uniform random choice of such an input array. By Lemma 8, we get that there must be some I/O-graph shared by at least (_n_!2_<sup>nw</sup>/_2)/(_t+n(w_+lgn)_/b+nw/b_+1)<sup>_t_+1</sup> of the inputs that A<sup>∗</sup> is correct on.

## Data Must Travel Far.

The key idea in our lower bound proof, is to argue that there is a permutation for which most data bit strings _d<sub>i</sub>_ are very far away from output entry \(C[\pi(i)]\) in the corresponding I/O-graph. This would require the data to "travel" far. By Conjecture 1, this is impossible unless the I/O-graph is large. Thus we start by arguing that there is a fixed permutation where data has to travel far on the average, and where it also holds that there are many different data values that can be sent using the same I/O-graph. To make this formal, let \(\text{dist}(\pi,i,G)\) denote the distance between the block node in _G_ representing the input block storing _A_\[_i_\] (the initial node, before any I/Os were performed) and the node in _G_ representing the output block storing \(C[\pi(i)]\) in the _undirected_ version of _G_ (undirect all edges).

We prove the following:

**Lemma 10** _If_ \((t+n(w+lgn)/b+nw/b+1)^{t+1}\le(nw/b)^{(1/30)n}\)_, then there exists a permutation_ \(\pi\)_, a collection of values_ \(\mathcal{F}\subseteq\{\{0,1\}^w\}^n\) _and an I/O-graph G such that the following holds:_

1. _For all_ \((d_1,\dots,d_n)\in\mathcal{F}\) _it holds that the algorithm_ A<sup>∗</sup> _executed on the input array A corresponding to inputs_ \(\pi\) _and d_<sub>1</sub>_,...,d<sub>n</sub> results in the I/O-graph G and_ A<sup>∗</sup> _is correct on A._<tbc>

2. \(|\mathcal{F}|\ge\frac{2^{nw}}{4(t+n(w+lgn)/b+nw/b+1)^{t+1}}\).<tbc>

_3._ _There are at least_ (4/5)_n indices_ \(i\in\{1,\dots,n\}\) _for which_ \(\text{\textit{dist}}(\pi,i,G)\ge(1/2)lg_{2m/b}(nw/b)\).

<tbc>**Proof.** We start by using Lemma 9 to obtain a set \(\Gamma\) and an I/O-graph _G_ such that<tbc>

\(|\Gamma|\ge\frac{n!2^{nw}}{2(t+n(w+lgn)/b+nw/b+1)^{t+1}}.\)

<tbc>\(\Gamma\) has the property that A<sup>∗</sup> is correct on all arrays \(A\in\Gamma\) and _G_ is the I/O-graph corresponding to the execution of A<sup>∗</sup> on _A_ for every \(A\in\Gamma\). For each permutation \(\pi\), define \(\Gamma_\pi\) to be the subset of arrays in \(\Gamma\) for which the corresponding permutation is \(\pi\). We have \(|\Gamma_\pi|\le 2^{nw}\) for all \(\pi\). We now argue that there must be many \(\Gamma_\pi\)’s that are large: Let _k_ be the number of permutations \(\pi\) such that<tbc>

\(|\Gamma_\pi|\ge\frac{2^{nw}}{4(t+n(w+lgn)/b+nw/b+1)^{t+1}}.\)

<tbc>We must have

\(k2^{nw}+(n!-k)\cdot\frac{2^{nw}}{4(t+n(w+lgn)/b+nw/b+1)^{t+1}}\ge|\Gamma|\Rightarrow\)<br>
\(k\left(2^{nw}-\frac{2^{nw}}{4(t+n(w+lgn)/b+nw/b+1)^{t+1}}\right)\ge\frac{n!2^{nw}}{4(t+n(w+lgn)/b+nw/b+1)^{t+1}}\Rightarrow\)<br>
\(k2^{nw}\ge\frac{n!2^{nw}}{4(t+n(w+lgn)/b+nw/b+1)^{t+1}}\Rightarrow\)<br>
\(k\ge\frac{n!}{4(t+n(w+lgn)/b+nw/b+1)^{t+1}}\)

