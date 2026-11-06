**Algorithm 13** `HittingSet`(_U,_F_,s_)

**Input :** Universe _U_ of _n_ elements and a collection F of _n_ subsets of size at least _s_

**Output:** Hitting set _X_ of size _O(n_log_n/s_)

179 \(X\leftarrow\emptyset\)

180 \(c(j)\leftarrow|\{S_i\in\mathcal{F}\text{s.t.}j\in S_i\}|\) for all \(j\in U\)

181 **while** \(\mathcal{F}\neq\emptyset\) **do**

182 \(v\leftarrow\mathrm{argmax}_{j\in U}c(j)\)

183 \(X\leftarrow X\cup\{v\}\)

184 \(\mathcal{F}\leftarrow\{S_i\in\mathcal{F}\text{s.t.}v\notin S_i\}\)

185 \(c(j)\leftarrow|\{S_i\in\mathcal{F}\text{s.t.}j\in S_i\}|\) for all \(j\in U\)

_Proof._ We begin with the deterministic algorithm `HittingSet` with pseudocode provided in Algorithm 13. Without loss of generality, assume all |_S<sub>i</sub>_|=_s_. Otherwise, drop all but the first _s_ elements of each subset _S<sub>i</sub>_ and observe that any hitting set of the resulting collection must also be a hitting set for the original collection.

Now, initially we have \(\sum_{j\in U}c(j)=\sum_{S_i\in\mathcal{F}}|S_i|=ns\). When the algorithm terminates, we have an empty collection F so that \(\sum_{j\in U}c(j)=0\). In each iteration, the most expensive operation is to update F and _c(j_). By keeping \(\{S_i\in\mathcal{F}\text{s.t.}j\in S_i\}\) in addition to the count _c(j_) alone, we can update F and _c(j_) in \(\tilde{O}(1)\) time for each decrement of _c(j_). Thus, the overall running time can be bounded by \(\tilde{O}(ns)\).

We now bound the size of output set _X_. Let _T<sub>j</sub>_ denote the number of sets remaining in F after _j_ elements have been added to _X_. Then, _T_<sub>0</sub>=|F|=_n_, |_X_|=min<sub>_j\>_0</sub>s.t. _T<sub>j</sub>_=0_j_, and _T<sub>j</sub>=T_<sub>_j_-1</sub>-_c(u<sub>j</sub>_) where _u<sub>j</sub>_ is the _j_-th element added to _X_. By our choice of _c(u<sub>j</sub>_), we have \(c(u_j)\ge\frac{T_{j-1s}}{n-j+1}\) since there are _T_<sub>_j_-1</sub> sets of size _s_ and _n_-(_j_-1)=_n-j_+1 elements not in _X_. Then,

\(T_j\le\left(1-\frac{s}{n-j+1}\right)T_{j-1}\le T_0\prod_{l=0}^{j-1}\left(1-\frac{s}{n-l}\right)<n\left(1-\frac{s}{n}\right)^j\le ne^{-\frac{sj}{n}}\)

When \(j=\frac{n\mathrm{log}n}{s}\) we have _T<sub>j</sub>\<_1 so _T<sub>j</sub>_=0. In particular, \(|X|\le\frac{n\mathrm{log}n}{s}\) .

_Proof._ The randomized algorithm `rHittingSet` simply samples each element with probability _p_. Clearly this algorithm runs in time _O(n_).

First, we bound the probability that _X_ is not a hitting set. For each subset of size _s_, the probability that no element is sampled can be bounded as,

\((1-p)^s\le e^{-ps}\)

By the union bound, the probability some subset has no element sampled can be bounded as,

\(ne^{-ps}\)

so if _p=c_log_n/s_, we upper bound this as _n_<sup>1-_c_</sup> for some constant _c\>_1.

Then, to upper bound the size of _X_, we apply a standard Chernoff bound to see that |_X_|=_O(n_log_n/s_) with high probability.

**Lemma 2.5.** _Let G be a graph on n vertices. There is a deterministic algorithm `Dominate` and randomized algorithm `rDominate` that computes a dominating set D of size_ \(O\left(\frac{n\mathrm{log}n}{s}\right)\) _of V<sub>s</sub> in time O(m+ns_) _and O(n_) _respectively._

