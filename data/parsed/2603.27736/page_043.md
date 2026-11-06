In particular, for any polynomially bounded universe \(u\le n^c\) (where _c_ is constant) the running time becomes truly subcubic, \(O(n^{\alpha_1+\alpha_2+\alpha_3-\gamma})\) for any constant \(0<\gamma<min\{\kappa,\epsilon/2\}/300000\). This contradicts the APSP Hypothesis.

Corollary 5.9 also immediately implies Theorem 1.10: APSP reduces to Min-Plus Product, which reduces to _n_-Uniform \(n^\kappa\)-Doubling Min-Plus Product by Theorem 1.10, which in turn can be seen as an APSP instance on a 3-layered graph with at most _n_ distinct weights and doubling \(n^\kappa\). For many lower bounds the following simpler corollary (that ignores the regular and low-doubling constraints) turns out to be sufficient.

**Corollary 5.10.** _Let_ \(\epsilon>0\) _and_ \(0<\alpha_2\le\alpha_1,\alpha_3\) _be constants. If_ \(\mathrm{MinPlus}(n^{\alpha_1},n^{\alpha_2},n^{\alpha_3}|D\le n^{\alpha_2})\le O(n^{\alpha_1+\alpha_2+\alpha_3-\epsilon})\) _then the APSP Hypothesis fails._

## 5.4 Large-Universe Reduction

In this subsection we finally provide the missing reduction from polynomially large universes {0_,...,n_<sup>_O_(1)</sup>} to {0_,...,n_}, conditioned on the additive combinatorics assumption Hypothesis 1.12; we refer to Appendix A for a discussion of this hypothesis. To effectively apply Hypothesis 1.12 we rely on the following greedy covering lemma.

**Lemma 5.11** (Greedy Covering)**.** _There is an algorithm that, given_ \(X,Y\subseteq\mathbb{Z}\)_, computes a set_ \(S\subseteq\mathbb{Z}\) _of size at most_ \(|Y-X|/|Y|\cdot\mathrm{ln}|X|\) _such that_ \(X\subseteq Y+S\)_. It runs in deterministic time_ \(|Y-X||S|\cdot(\mathrm{log}u)^{O(1)}\)_, where u is an upper bound on the largest integer in X,Y in absolute value._

**Proof.** We run a simple greedy algorithm. Initialize \(S\leftarrow\emptyset\). While \(X\neq\emptyset\) we compute a shift \(s\in\mathbb{Z}\) that maximizes _r_<sub>_Y-X_</sub>(_s_). We update \(S\leftarrow S\cup\{s\}\) and \(X\leftarrow X\backslash(Y+s)\). When the algorithm terminates, we return _S_.

It is clear that when the algorithm terminates the set _S_ is as desired. It remains to bound |_S_|, i.e., to bound the number of iterations. Let _X_<sub>0</sub> denote the initial set _X_. We show that with each iteration of the algorithm removes at least a |_Y|/|Y-X_<sub>0</sub>|-fraction of the elements from _X_; from this it follows easily that after \(|Y-X_0|/|Y|\cdot\mathrm{ln}|X_0|\) iterations the set _X_ must be empty. To see this, observe that<tbc>

\(\sum_{s\in Y-X}r_{Y-X}(s)=|X||Y|,\)

<tbc>and hence there is some \(s\in Y-X\) with

\(r_{Y-X}(s)\ge\frac{|X||Y|}{|Y-X|}\ge\frac{|X||Y|}{|Y-X_0|}.\)

This shift _s_ witnesses that the algorithm decreases the size of |_X_| by at least a |_Y|/|Y-X_<sub>0</sub>|-fraction as desired.

We finally consider the running time. By Lemma 2.18 we can compute the set _Y-X_ along with all multiplicities \(r_{Y-X}(\cdot)\) in deterministic time \(O(|Y-X|\cdot(\mathrm{log}u)^{O(1)})\). Finding _s_ and updating _S_ and _X_ then runs in time _O_(|_Y-X_|). We repeat this over |_S_| iterations, leading to the claimed total time.

**Remark 5.12.** _This lemma relates to the well-known "Ruzsa’s Covering Lemma" \[86\]; see \[94, Lemma 2.14\]. That fundamental result alternatively covers X by shifts of Y-Y (instead of Y ) but achieves_ \(|S|\le|Y-X|/|Y|\) _(without the logarithmic factor)._

Equipped with Lemma 5.11, we now show that Hypothesis 1.12 implies a reduction from low-doubling Min-Plus Product to small-universe Min-Plus Product.

**Lemma 5.13.** _Assuming Hypothesis 1.12 there is a constant c such that for all parameters n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>_,K with_ \(n_2\le n_1n_3\):<tbc>

\(\mathrm{MinPlus}(n_1,n_2,n_3|D\le n_2;K)=\tilde{O}(K^c\cdot\mathrm{MinPlus}(n_1,n_2,n_3|u\le n_2)).\)

