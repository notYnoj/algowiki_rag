Corollary 4.12, the probability of this is at most \(\mathbf{Pr}\left[\mathcal{E}\right]\le\frac{32}{\mathrm{log}^{99}N}\). Since |_X<sub>s</sub>_|=log_N_, from Corollary 2.10, \(\mathsf{WB}_\sigma(X_s)\le|X_s|\mathrm{log}(|X_s|)\le\mathrm{log}N\mathrm{loglog}N\). Therefore, altogether, we get that \(\mu(\sigma)\le O(\mathrm{log}N\mathrm{logloglog}N)\), and \(\mathsf{cost}_1(\sigma)=N\cdot\mu(\sigma)=O(N\mathrm{log}N\mathrm{logloglog}N)=O(N^*\mathrm{logloglog}N^*)\), as _N_<sup>∗</sup>=_N_log_N_.

## 4.5.2 Bounding Type-2 Crossings

In this section we show that for every ordering \(\sigma\) of the auxiliary columns in L, \(\mathsf{cost}_2(\sigma)\le O(N^*\mathrm{logloglog}N^*)\). For the remainder of the section, we fix an ordering \(\sigma\) of L, and we denote the corresponding partitioning tree \(T(\sigma)\) by _T_. Recall that we have defined a set C of _N_ columns, so that \(|\mathcal{C}|,|\mathcal{L}|\le N\), and |_V(T_)|=_O(N_). It is then sufficient to prove the following theorem:

**Theorem 4.15** _For every vertex_ \(v\in V(T)\), \(\mathsf{cost}_2(v)\le O(\mathrm{log}N)+O(\mathsf{cost}_1(v))\).

Assuming that the theorem is correct, we get that \(\mathsf{cost}_2(\sigma)\le O(\mathsf{cost}_1(\sigma))+O(|V(T)|\cdot\mathrm{log}N)=O(N^*\mathrm{logloglog}N^*)+O(N\mathrm{log}N)=O(N^*\mathrm{logloglog}N^*)\).

The remainder of this subsection is dedicated to the proof of Theorem 4.15. We fix a vertex \(v\in V(T)\), and we denote _S=S(v_). We also let _L=L(v_) be the vertical line that _v_ owns. Our goal is to show that the number of type-2 crossings of _L_ is bounded by _O_(cost<sub>1</sub>(_v_))+_O_(log_N_).

Recall that instances _X_<sub>1</sub>_,...,X<sub>N</sub>_ are stacked on top of each other, so that the first log_N_ rows with integral coordinates belong to _X_<sub>1</sub>, the next log_N_ rows belong to _X_<sub>2</sub>, and so on. If we have a crossing \((p,p')\), where \(p\in X_s\) and \(p'\in X_{s^\prime}\), then we say that the instances _X<sub>s</sub>_ and \(X_{s^\prime}\) are _responsible_ for this crossings. Recall that \(p,p'\) may only define a crossing if they lie on opposite sides of the line _L_, and if no point of \(\hat{X}\) lies in the strip _S_ between the row of _p_ and the row of \(p'\). It is then clear that every instance _X<sub>s</sub>_ may be responsible for at most two type-2 crossings of _L_: one in which the second instance \(X_{s^\prime}\) responsible for the crossing has \(s'<s\), and one in which \(s'>s\).

We further partition the type-2 crossings into two sub-types. Consider a crossing \((p,p')\), and let \(X_s,X_{s^\prime}\) be the two instances that are responsible for it. If either of \(X_s,X_{s^\prime}\) contributes a type-1 crossing to the cost of _L_, then we say that \((p,p')\) is a type-(2a) crossing; otherwise it is a type-(2b) crossing. Clearly, the total number of type-(2a) crossings is bounded by _O_(cost<sub>1</sub>(_v_)). It is now sufficient to show that the total number of all type-(2b) crossings is bounded by _O_(log_N_).

Consider now some type-(2b) crossing \((p,p')\), and let _X<sub>s</sub>_ and \(X_{s^\prime}\) be the two instances that are responsible for it, with \(p\in X_s\). We assume that \(s<s'\). Since neither instance contributes a crossing to cost<sub>1</sub>(_v_), it must be the case that all points of \(X_s\cap S\) lie to the left of _L_ and all points of \(X_{s^\prime}\cap S\) lie to the right of _L_ or vice versa. Moreover, if \(s'>s+1\), then for all \(s<s''<s'\), \(X_{s^{\prime\prime}}\cap S=\emptyset\).

It would be convenient for us to collapse each of the instances _X_<sub>1</sub>_,...,X<sub>N</sub>_ into a single row. In order to do so, for each \(1\le s\le N\), we replace all rows on which the points of _X<sub>s</sub>_ lie with a single row _R<sub>s</sub>_. If some point of _X<sub>s</sub>_ lies on some column _C_, then we add a point at the intersection of _R<sub>s</sub>_ and _C_.

We say that a row _R<sub>s</sub>_ is _empty_ if there are no input points in \(R_s\cap S\). We say that it is a _neutral_ row, if there are points in \(R_s\cap S\) both to the left of _L_ and to the right of _L_. We say that it is a _left row_ if \(R_s\cap S\) only contains points lying to the left of _L_, and we say that it is a _right row_ if \(R_s\cap S\) only contains points lying to the right of _L_.

