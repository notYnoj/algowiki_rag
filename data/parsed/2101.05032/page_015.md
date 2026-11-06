We can now express this lower bound in terms of _k_ or _m_ as follows: As _m=M<sup>M</sup>_, we have llg_m=M_lg_M_ and hence _M=W_<sup>-1</sup>(lg_m_). As _k=M_<sup>_M_+1</sup>, we have lg_k_=(_M_+1)lg_M_ and hence \(M=\Omega(W^{-1}(lgk))\). Thus, the theorem follows.

\(\blacktriangleright\) **Theorem 4.12.** _No deterministic algorithm ALG attains_ \(\mathrm{ALG}_k\le\mathrm{opt}_k+\mathrm{o}(lgmin\{k,m\})\).

**Proof.** Let _k=m_ be an arbitrarily large integer. The intervals of the _m_ sets are chosen as in the proof of Theorem 4.11, for a sufficiently large value of _M_. Let _a_ be the number of active sets at the start of a round; initially _a=m_. After each round, the adversary considers the set _S<sub>j</sub>_ in which the algorithm has made the largest number of queries, which must be at least _k/a_. The adversary picks the minimum element in _S<sub>j</sub>_ in such a way that a single query in the current round would have been enough to solve it, and keeps all other sets active. This continues for _m_ rounds. The number of wasted queries is at least \(k/m+k/(m-1)+\cdots+k/2+k-m=k\cdot(H(m)-1)=k\cdot\Omega(lgk)\). As the algorithm must also make all queries in OPT<sub>1</sub>, the theorem follows from Proposition 2.1.

We conclude thus that the balanced algorithm attains matching upper bounds for disjoint sets. For non-disjoint sets, a small gap remains between our lower and upper bounds.

## 5 Selection

An instance of the Selection problem is given by a set I of _n_ intervals and an integer _i_, \(1\le i\le n\). Throughout this section we denote the _i_-th smallest value in the set of _n_ precise values by _v_<sup>∗</sup>.

### 5.1 Finding the Value _v_<sup>∗</sup>

If we only want to find the value _v_<sup>∗</sup>, then we can adapt the analysis in [20] to obtain an algorithm that performs at most opt<sub>1</sub>+_i_-1 queries, simply by querying the intervals in the order of their left endpoints. This is the best possible and can easily be parallelized in \(\mathrm{opt}_k+\left\lceil\frac{i-1}{k}\right\rceil\) rounds. Note that we can assume \(i\le\lceil n/2\rceil\), since otherwise we can consider the _i_-th largest value problem, noting that the _i_-th smallest value is the (_n-i_+1)-th largest value. We also assume that every input interval is either trivial or open, since otherwise (if arbitrary closed intervals are allowed) the problem has a lower bound of _n_ on the competitive ratio, using the same instance as presented in [20] for the problem of identifying the minimum element.

Let _I_<sub>_j_<sub>1</sub></sub> be the interval with the _i_-th smallest left endpoint, and let _I_<sub>_j_<sub>2</sub></sub> be the interval with the _i_-th smallest right endpoint. Note that any interval _I<sub>j</sub>_ with \(u_j<\ell_{j_1}\) or \(\ell_j>u_{j_2}\) can be discarded (and the value of _i_ adjusted accordingly).

We analyze the algorithm that simply queries the _k_ leftmost non-trivial intervals until the problem is solved.

\(\blacktriangleright\) **Theorem 5.1.** _For instances of the i-th smallest value problem where all input intervals are open or trivial, there is an algorithm that returns the i-th smallest value v_<sup>∗</sup> _and uses at most_

_rounds._

\(\left|\frac{\mathrm{opt}_1+i-1}{k}\right|\le\mathrm{opt}_k+\left|\frac{i-1}{k}\right|\)

