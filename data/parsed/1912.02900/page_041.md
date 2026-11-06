We define a guillotine partition of a point set _X_, together with the corresponding partitioning tree _T_. As before, every node \(v\in V(T)\) of the partitioning tree _T_ is associated with a rectangular region _S(v_) of the plane. At the beginning, we add the root vertex _r_ to the tree _T_, and we let _S(r_)=_B_, where _B_ is the bounding box containing all points of _X_. We then iterate, as long as some leaf vertex _v_ of _T_ has \(S(v)\cap X\) containing more than one point. In each iteration, we select any such leaf vertex _v_, and we select an arbitrary vertical or horizontal line _L(v_), that is contained in _S(v_), and partitions _S(v_) into two rectangular regions, that we denote by \(S'\) and \(S''\), such that \(X\cap S',X\cap S''\neq\emptyset\). We then add two child vertices _v_<sub>1</sub>_,v_<sub>2</sub> to _v_, and set \(S(v_1)=S'\) and \(S(v_2)=S''\). Once every leaf vertex _v_ has \(|S(v)\cap X|=1\), we terminate the process and obtain the final partitioning tree _T_.

The cost cost(_v_) of every vertex \(v\in V(T)\) is calculated exactly as before. We then let \(\mathsf{GB}_T(X)=\sum_{v\in V(T)}\mathsf{cost}(v)\), and we let GB(_X_) be the maximum, over all partitioning trees _T_, of GB_<sub>T</sub>(X_).

We note that the main difference between cGB(_X_) and GB(_X_) is that in cGB bound, the partitioning lines must be chosen consistently across all regions: that is, we choose a vertical or a horizontal line _L_ that crosses the entire bounding box _B_, and then we partition every region that intersects _L_ by this line _L_. In contrast, in the GB bound, we can partition each region _S(v_) individually, and choose different partitioning lines for different regions. It is then easy to see that GB is more general than cGB, and, in particular, for every point set _X_ that is a permutation, \(\mathsf{cGB}(X)\le\mathsf{GB}(X)\).

Lastly, we show that GB is a lower bound on the optimal solution cost, in the following lemma whose proof is deferred to Section D of Appendix.

**Lemma 5.3** _For any point set X that is a permutation,_ \(\mathsf{GB}(X)\le 2\mathsf{OPT}(X)\).

## 5.2 Negative Result for the GB Bound

In this section we prove Theorem 5.1.

We use three main parameters. Let \(\ell\ge 1\) be an integer, and let \(n=2^\ell\) and _N_=2_<sup>n</sup>_. As before, we will first construct point set \(\hat{X}\) that is not a permutation (in fact, it is not even a semi-permutation), and then we will turn it into our final instance _X_<sup>∗</sup> which is a permutation.

### 2D exponentially spaced bit reversal:

We define the instance 2D-ES-\(\mathsf{BRS}(\ell)\) to be a bit- reversal sequence \(\mathsf{BRS}(\ell,\mathcal{R},\mathcal{C})\), where the sets R and C of active rows and columns are defined as follows. Set C contains all columns with _x_-coordinates in \(\left\{2^j|1\le j\le n\right\}\), and similarly set R contains all rows with _y_-coordinates in \(\left\{2^j|1\le j\le n\right\}\). Note that set _X_ contains _n_ points, whose _x_- and _y_-coordinates are integers between 1 and _N_.

### 2D cyclic shifts:

Next, we define the shifted and exponentially spaced instance, but this time we shift both vertically and horizontally. We assume that we are given a horizontal shift \(0\le s<N\) and a vertical shift \(0\le s'<N\). In order to construct the instance \(X^{s,s^\prime}\), we start with the instance \(X=2\mathsf{D}-\mathsf{ES}-\mathsf{BRS}(\ell)\), and then perform the following two operations. First, we perform a horizontal shift by _s_ units as before, by moving the last _s_ columns with integral _x_-coordinates to the beginning of the instance. Next, we perform a vertical shift, by moving the last \(s'\) rows with integral _y_-coordinates to the bottom of the instance. We let \(X^{s,s^\prime}\) denote the resulting instance. By applying Claim 4.4 twice, once for the horizontal shift, and once for the vertical shift, we get that \(\mathsf{OPT}(X^{s,s^\prime})\ge\mathsf{OPT}(X)-2|X|\ge\Omega(\mathrm{log}N\mathrm{loglog}N)\), since |_X_|=log_N_.

