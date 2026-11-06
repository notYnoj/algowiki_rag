In order to see this, consider an equivalent experiment, in which we keep the instance _X_<sub>1</sub> fixed, and instead choose a random shift \(s\in\{0,\dots,N-1\}\) for the line _L_. For the bad event E(_v_) to happen, the line _L_ must fall in the interval between _x_-coordinate 0 and _x_-coordinate 8width(_S)/_log<sup>100</sup>_N_. Since every integral shift _s_ is chosen with the same probability 1_/N_, the probability that E(_v_) happens is at most \(\frac{8\mathrm{width}(S)}{N\mathrm{log}^{100}N}\). \(\square\)

Consider now the partitioning tree _T_. We partition the vertices of _T_ into log_N_+1 classes _Q_<sub>1</sub>_,...,Q_log_N_+1. A vertex \(v\in V(T)\) lies in class _Q<sub>i</sub>_ iff \(2^i\le\mathrm{width}(S(v))<2^{i+1}\). Therefore, every vertex of _T_ belongs to exactly one class.

Consider now some vertex \(v\in V(T)\), and assume that it lies in class _Q<sub>i</sub>_. We say that _v_ is an _important vertex_ for class _Q<sub>i</sub>_ iff no ancestor of _v_ in the tree _T_ belongs to class _Q<sub>i</sub>_. Notice that, if _u_ is an ancestor of _v_, and \(u\in Q_j\), then \(j\ge i\) must hold.

For each \(1\le i\le\mathrm{log}N+1\), let _U<sub>i</sub>_ be the set of all important vertices of class _Q<sub>i</sub>_.

**Observation 4.11** _For each_ \(1\le i\le\mathrm{log}N+1\), \(|U_i|\le N/2^i\).

**Proof:** Since no vertex of _U<sub>i</sub>_ may be an ancestor of another vertex, the strips in \(\{S(v)|v\in U_i\}\) are mutually disjoint, except for possibly sharing their boundaries. Since each strip has width at least 2_<sup>i</sup>_, and we have exactly _N_ columns, the number of such strips is bounded by _N/_2_<sup>i</sup>_. \(\square\)

Let E be the bad event that there is some index \(1\le i\le\mathrm{log}N+1\), and some important vertex \(v\in U_i\) of class _Q<sub>i</sub>_, for which the event E(_v_) happens. Applying the Union Bound to all strips in \(\{S(v)|v\in U_i\}\) and all indices \(1\le i\le\mathrm{log}N\), we obtain the following corollary of Claim 4.10.

**Corollary 4.12** \(\mathbf{Pr}\left[\mathcal{E}\right]\le\frac{32}{\mathrm{log}^{99}N}\).

**Proof:** Fix some index \(1\le i\le\mathrm{log}N\). Recall that for every important vertex \(v\in U_i\), the probability that the event E(_v_) happens is at most \(\frac{8\mathrm{width}(S(v))}{N\mathrm{log}^{100}N}\le\frac{8\cdot 2^{i+1}}{N\mathrm{log}^{100}N}=\frac{16\cdot 2^i}{N\mathrm{log}^{100}N}\). From Observation 4.11, \(|U_i|\le N/2^i\). From the union bound, the probability that event E(_v_) happens for any \(v\in U_i\) is bounded by \(\frac{16}{\mathrm{log}^{100}N}\). Using the union bound over all \(1\le i\le\mathrm{log}N+1\), we conclude that \(\mathbf{Pr}\left[\mathcal{E}\right]\le\frac{32}{\mathrm{log}^{99}N}\). \(\square\)

Lastly, we show that, if event E does not happen, then the cost of the Wilber Bound is sufficiently small.

**Lemma 4.13** _Let_ \(1\le s\le N\) _be a shift for which_ E _does not happen. Then:_

\(WB_\sigma(X_s)\le O(\mathrm{log}N\mathrm{logloglog}N).\)

**Proof:** Consider the partitioning tree \(T=T(\sigma)\). We say that a vertex \(v\in V(T)\) is a _seam vertex_ iff _S(v_) is a seam strip, that is, the point _p_<sub>1</sub> in instance _X<sub>s</sub>_ lies in _S(v_). Clearly, the root of _T_ is a seam vertex, and for every seam vertex _v_, exactly one of its children is a seam vertex. Therefore, there is a root-to-leaf path _P_ that only consists of seam vertices, and every seam vertex lies on _P_. We denote the vertices of _P_ by _v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>q</sub>_, where _v_<sub>1</sub> is the root of _T_, and _v<sub>q</sub>_ is a leaf. For \(1<i\le q\), we denote by \(v'_i\) the sibling of the vertex _v<sub>i</sub>_. Note that all strips \(S(v'_2),\dots,S(v'_q)\) are mutually disjoint, except for possibly sharing boundaries, and so \(\sum_{i=2}^qN(v'_i)\le|X_s|=\mathrm{log}N\). Moreover, from Claim 4.1, \(\sum_{i=1}^q\mathsf{cost}(v_i)\le 2|X_s|=2\mathrm{log}N\).

