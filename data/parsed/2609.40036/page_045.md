**Lemma 11** (Walks with prescribed edge probabilities)**.** _Let_ \(\mathbf{z}\neq 0\) _be nonnegative edge weights satisfying (208), and write_ \(Z=\sum_fz_f\)_. For every integer_ \(h\ge 1\) _there is a probability distribution on nonbacktracking walks W_=(_F_<sub>1</sub>_,...,F<sub>h</sub>_) _of h edges with_ Pr(_F<sub>i</sub>=f_)=_z<sub>f</sub>/Z for every step i. Consequently,_

\(\unknown_W\left[\sum_{i=1}^h\omega_{F_i}\right]=\frac{h}{Z}\sum_f\omega_fz_f\) (211)

_for every real edge-weight vector_ \(\unknown\)_. Repeated edges are counted with multiplicity._

_Proof._ For each vertex _v_, put \(S_v=\sum_{f\in\partial v}z_f\). The inequalities (208) say that no edge in the check support has weight greater than _S<sub>v</sub>/_2. We construct nonnegative numbers \(b_{ff^\prime}^v\), indexed by \(f,f'\in\partial v\), that are symmetric in \(f,f'\), vanish when \(f=f'\), and sum to _z<sub>f</sub>_ over \(f'\). After arrival along an edge _f_ with _z<sub>f</sub>\>_0, the ratio \(b_{ff^\prime}^v/z_f\) will be the probability of continuing along \(f'\).

If _S<sub>v</sub>\>_0, partition a circle of circumference _S<sub>v</sub>_ into consecutive half-open intervals _I<sub>f</sub>_ of lengths _z<sub>f</sub>_, and let

\(b_{ff^\prime}^v=\left|I_f\cap(I_{f^\prime}+S_v/2)\right|.\) (212)

Here addition is modulo _S<sub>v</sub>_, and the absolute-value signs denote arc length. Rotating by half the circumference preserves length and is its own inverse, so \(b_{ff^\prime}^v=b_{f^\prime f}^v\). An interval of length at most _S<sub>v</sub>/_2 is disjoint from its half-turn except possibly at endpoints, so \(b_{ff}^v=0\). The rotated intervals partition the circle, giving row sums \(\sum_{f^\prime\in\partial v}b_{ff^\prime}^v=|I_f|=z_f\). Set _b<sup>v</sup>_=0 when _S<sub>v</sub>_=0.

Choose the first directed edge from the following distribution on both directions of each edge with _z<sub>f</sub>\>_0:

\(\pi(u,v)=\frac{z_{\{u,v\}}}{2Z}.\) (213)

After traversing _f_={_u,v_} towards _v_, choose the next edge \(f'=\{v,w\}\) with probability \(b_{ff^\prime}^v/z_f\). The row sums make this a Markov chain, and the zero diagonal prohibits immediate reversal. For each directed edge (_v,w_), its incoming probability under \(\pi\) is

\(\sum_{u:\{u,v\}\in E}\frac{z_{\{u,v\}}}{2Z}\frac{b_{\{u,v\},\{v,w\}}^v}{z_{\{u,v\}}}=\frac{z_{\{v,w\}}}{2Z}=\pi(v,w),\) (214)

where terms with zero weight are omitted. Thus \(\pi\) is _stationary_: the distribution on directed edges is unchanged after a step. At every step, the probability of traversing the undirected edge _f_ is therefore _z<sub>f</sub>/Z_. Summing the expected edge weights over the _h_ steps proves (211).

**Lemma 12** (A sufficient condition for unique LP recovery)**.** _Fix_ \(h\ge 1\)_. If every nonbacktracking walk of h edges has strictly fewer than h/_2 _erroneous positions, counting multiplicity, then_ **x**<sup>**e**</sup> _is the unique optimal marginal vector of the LP. In particular the LP decoder returns_ **e**.

_Proof._ A walk’s total weight is _h_ minus twice its number of erroneous positions, so the hypothesis makes every such weight strictly positive. If a distinct feasible marginal vector **x** satisfied \(\mathcal{L}(\mathbf{x})\le|\mathbf{e}|\), then (209) and Lemma 11 would give a distribution on these walks with nonpositive expected weight, a contradiction.

This condition is sufficient, not necessary: the existence of a walk with at least half its positions corrupted does not by itself imply a decoding failure. The argument rules out both integral and fractional competitors, including equal-cost ties, and depends only on the error locations.

