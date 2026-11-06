_L(v_), and cost<sub>2</sub>(_v_) the total number of type-2 crossings. Note that cost(_v_)=cost<sub>1</sub>(_v_)+cost<sub>2</sub>(_v_). We also define \(\mathtt{cost}_1(\sigma)=\sum_{v\in V(T)}\mathtt{cost}_1(v)\) and \(\mathtt{cost}_2(\sigma)=\sum_{v\in V(T)}\mathtt{cost}_2(v)\). Clearly, \(\mathsf{WB}_\sigma(\hat{X})=\mathtt{cost}_1(\sigma)+\mathtt{cost}_2(\sigma)\). In the next subsections, we bound \(\mathtt{cost}_1(\sigma)\) and \(\mathtt{cost}_2(\sigma)\) separately. We will show that each of these costs is bounded by _O(N_<sup>∗</sup>logloglog_N_<sup>∗</sup>).

## 4.5.1 Bounding Type-1 Crossings

The goal of this subsection is to prove the following theorem.

**Theorem 4.8** _For every ordering_ \(\sigma\) _of the auxiliary columns in_ L, \(\mathtt{cost}_1(\sigma)\le O(N^*logloglogN^*)\).

We prove this theorem by a probabilistic argument. Consider the following experiment. Fix the permutation \(\sigma\) of L. Pick an integer \(s\in\{0,\dots,N-1\}\) uniformly at random, and let _X_ be the resulting instance _X<sub>s</sub>_. This random process generates an input _X_ containing _n_=log_N_ points. Equivalently, let _p_<sub>1</sub>_,p_<sub>2</sub>_,...,p_log_N_ be the points in \(\mathsf{BRS}(\ell)\) ordered from left to right. Once we choose a random shift _s_, we move these points to columns in C_<sub>s</sub>_={2_<sup>j</sup>+s_mod_N_}, where point _p<sub>j</sub>_ would be moved to _x_-coordinate 2_<sup>j</sup>+s_mod_N_. Therefore, in the analysis, we view the location of points _p_<sub>1</sub>_,...,p_log_N_ as random variables.

We denote by \(\mu(\sigma)\) the expected value of \(\mathsf{WB}_\sigma(X)\), over the choices of the shift _s_. The following observation is immediate, and follows from the fact that the final instance \(\hat{X}\) contains every instance _X<sub>s</sub>_ for all shifts \(s\in\{0,\dots,N-1\}\).

**Observation 4.9** \(\mathtt{cost}_1(\sigma)=N\cdot\mu(\sigma)\)

Therefore, in order to prove Theorem 4.8, it is sufficient to show that, for every fixed permutation \(\sigma\) of L, \(\mu(\sigma)\le O(logNlogloglogN)\) (recall that _N_<sup>∗</sup>=_N_log_N_).

We assume from now on that the permutation \(\sigma\) (and the corresponding partitioning tree _T_) is fixed, and we analyze the expectation \(\mu(\sigma)\). Let \(v\in V(T)\). We say that _S(v_) is a _seam strip_ iff point _p_<sub>1</sub> lies in the strip _S(v_). We say that _S(v_) is a _bad_ strip (or that _v_ is a bad node) if the following two conditions hold: (i) _S(v_) is not a seam strip; and (ii) _S(v_) contains at least 100loglog_N_ points of _X_. Let E(_v_) be the bad event that _S(v_) is a bad strip.

**Claim 4.10** _For every vertex_ \(v\in V(T)\), \(\mathbf{Pr}\left[\mathcal{E}(v)\right]\le\frac{8\mathrm{width}(S(v))}{N\mathrm{log}^{100}N}\) .

**Proof:** Fix a vertex \(v\in V(T)\). For convenience, we denote _S(v_) by _S_. Let _s_ be the random integer chosen by the algorithm and let _X<sub>s</sub>=X_ be the resulting point set. Assume that _S_ is a bad strip, and let _L_ be the vertical line that serves as the left boundary of _S_. Let _p<sub>j</sub>_ be the point of _X<sub>s</sub>_ that lies to the left of _L_, and among all such points, we take the one closest to _L_. Recall that for each \(1\le j<\mathrm{log}N\), there are 2_<sup>j</sup>_-1 columns of C that lie between the column of _p<sub>j</sub>_ and the column of _p_<sub>_j_+1</sub>.

If _S_ is a bad strip, then it must contain points _p_<sub>_j_+1</sub>_,p_<sub>_j_+2</sub>_,...,p_<sub>_j+q_</sub>, where _q_=100loglog_N_. Therefore, the number of columns of C in strip _S_ is at least 2<sup>_j+q_-2</sup>, or, equivalently, \(\mathrm{width}(S)\ge 2^{j+q}/4\ge(2^j\mathrm{log}^{100}N)/4\). In particular, \(2^j\le 4\mathrm{width}(S)/\mathrm{log}^{100}N\).

Therefore, in order for _S_ to be a bad strip, the shift _s_ must be chosen in such a way that the point _p<sub>j</sub>_, that is the rightmost point of _X<sub>s</sub>_ lying to the left of _L_, has \(2^j\le 4\mathrm{width}(S)/\mathrm{log}^{100}N\). It is easy to verify that the total number of all such shifts _s_ is bounded by 8width(_S)/_log<sup>100</sup>_N_.

