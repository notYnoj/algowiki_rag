2. **Separation Step:** At step _t_+1, the algorithm selects a point \(y_{t+1}\in\mathcal{P}\) that does not belong to \(\bigcup_{i\in[\ell]}\mathcal{A}_i\) if such a point exists, else it terminates. In other words, it selects a point whose weight cannot be inferred to equal that of any representative _r<sub>i</sub>_, based on the knowledge accumulated so far. (This is the central _computational_ challenge of the algorithm, which will return to in the next section.)<tbc>

3. **Update Step:** It uses binary search to locate the position of the weight _w_<sup>∗</sup>(_y_<sub>_t_+1</sub>) with respect to the ordered sequence \(w^*(r_1)<\cdots<w^*(r_\ell)\).<tbc>

<tbc>If _w_<sup>∗</sup>(_y_<sub>_t_+1</sub>)=_w_<sup>∗</sup>(_r<sub>i</sub>_) for some \(i\in[\ell]\), then it inserts _y_<sub>_t_+1</sub> into _B<sub>i</sub>_, and updates A to include the new direction (_y_<sub>_t_+1</sub>-_r<sub>i</sub>_) in its span, thereby increasing its dimension. This also changes the definitions of all the affine subspaces A_<sub>j</sub>_. Else the weight _w_<sup>∗</sup>(_y_<sub>_t_+1</sub>) is a weight it has not seen before, so the algorithm starts a fresh singleton bucket containing _y_<sub>_t_+1</sub> as its representative.

**Lemma 4.1.** _The number of iterations of the Global Subspace Learning algorithm is at most_ 2_nB+n._

_Proof._ The potential \(\phi=\mathrm{dim}(\mathcal{A})+\ell\), starts at zero and is upper-bounded by (_n_-1)+(2_nB_+1)=2_nB+n_. It is sufficient to prove that \(\phi\) increases by exactly 1 each time a new point is encountered. We have two cases when a new point _y_<sub>_t_+1</sub> is considered:

1. If _w_<sup>∗</sup>(_y_<sub>_t_+1</sub>)=_w_<sup>∗</sup>(_r<sub>i</sub>_) for some \(i\in[\ell]\), the number of buckets \(\ell\) remains unchanged, as _y_<sub>_t_+1</sub> is inserted into _B<sub>i</sub>_.<tbc>

<tbc>This vector is guaranteed to be linearly independent of A thus increasing the dimension because \(y_{t+1}-r_i\notin\mathcal{A}\), which follows directly from the condition \(y_{t+1}\notin\mathcal{A}_i\).<tbc>

2. Else, a new weight value is discovered. A new bucket is opened, which increases \(\ell\) by one, while A remains unchanged.

In both cases, the potential function \(\phi\) increases by exactly one. This completes the proof.

**Theorem 4.2** (Boolean Linear Optimization: Bounded-Weights)**.** _For any family_ \(\mathcal{F}\subseteq 2^U\) _and unknown integer weight function satisfying_ \(|w_e^*|\le B\)_, we can sort the feasible sets according to their weight w_<sup>∗</sup>(_S_) _and hence solve_ \(\mathrm{argmin}_{S\in\mathcal{F}}w^*(S)\) _using O(nB_log_nB_) _comparison queries, where_ |_U_|=_n. In fact, the number of comparison queries required is O_((_n+C_)log_C_) _if C is the number of distinct weight values realized by the feasible set._

_Proof._ Algorithm 4.1.1 maintains a structured representation which allows us to identify the weight class of any point \(x\in\mathcal{P}\). We can decide that _w_<sup>∗</sup>(_x_) is the _i_th smallest weight by checking if \(x\in\mathcal{A}_i\) (or equivalently, \(x-r_i\in\mathcal{A}\)), simply because the algorithm’s termination condition ensures that \(\mathcal{P}\subseteq\bigcup_{i\in[\ell]}\mathcal{A}_i\). This serves as a compact representation for the sorted order of all points by their weights _w_<sup>∗</sup>(_x_). Moreover, _r_<sub>1</sub> (or any other point in _B_<sub>1</sub>) is a point of minimum weight.

The number of comparison queries per point encountered is \(O(\mathrm{log}\ell)=O(\mathrm{log}nB)\) due to binary search over at most _O(nB_) weights, summing up to _O(nB_log(_nB_)) queries over its entire execution. This bound can be improved to _O_((_n+C_)log_C_) if _C_ is the number of distinct weight values realized by sets in F, because \(O(\mathrm{log}\ell)=O(\mathrm{log}C)\) and the number of points encountered is at most _n_-1+_C_.

The GSL framework provides a powerful information-theoretic bound. More importantly, it provides a clear path toward computationally efficient algorithms, which we turn to in the next section. We make two final observations:

