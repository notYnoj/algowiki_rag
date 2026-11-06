**Theorem 7.** _Set_ \(\eta=\frac{\delta}{2n\rho^2}\) _and_ \(T=\lceil\frac{4n^2\rho^2lnn}{\delta^2}\rceil\)_. Suppose that the algorithm does not fail during the first T iterations, and the spectral norms are bounded as_ \(\|N^{(t)}\|\le\rho\) _for all_ \(t\in[T]\)_. Then optimal values of problems 1 and 2 are at least_ \(\alpha-\delta\).

We will set \(\delta=\frac{1}{2}\alpha\), and require Algorithm 1 to produce a \(\Theta(1)\)-balanced element cut of cost at most \(\Theta(\kappa\alpha)\) whenever it outputs `Fail`.

## 3.1 Partial-variable MMWU framework

To prove Theorem 7, we will first derive an MMWU framework for more general SDPs, and then specialize it to Algorithm 1.

Let us consider an SDP with a block-diagonal symmetric-matrix _X_=blkdiag(_X_<sub>1</sub>_,...,X<sub>K</sub>_), \(X_k\in\mathbb{S}^{n_k}\) given by

\(min_{X_1,\dots,X_K}\sum_{k=1}^K\langle C_k,X_k\rangle\) (3a)

\(\text{s.t.}\sum_{k=1}^K\langle A_{ik},X_k\rangle\ge b_i\forall i\in\mathcal{I}\) (3b)

\(\sum_{k=1}^K\langle A_{ik},X_k\rangle=b_i\forall i\in\mathcal{I}'\) (3c)

\(X_k\unknown 0\forall k\in[K]\) (3d)

The corresponding dual problem is

\(max_yb^\top y\) (4a)

\(\text{s.t.}S_k(y)=^\text{def}C_k-\sum_iy_iA_{ik}\unknown 0\forall k\in[K]\) (4b)

\(y\in\mathbb{R}_{\ge 0}^\mathcal{I}\times\mathbb{R}^{\mathcal{I}^\prime}\) (4c)

where \(\sum_i\) means the sum over \(i\in\mathcal{I}\cup\mathcal{I}'\).

We will describe an algorithm that maintains variables _X<sub>k</sub>_ only for some blocks _k_. The set of such blocks will be denoted as \(\mathcal{K}\subseteq[K]\).

We assume that there exists _R\>_0 such that for each \(k\in\mathcal{K}\) the linear constraints (3b), (3c) of the primal problem imply that \(\text{\texttt{Tr}}(X_k)\le R\), i.e. a linear combination of these constraints yields constraint \(\text{\texttt{Tr}}(X_k)\le R\). We further assume that if the _i_-constraint is present in this linear combination with a non-zero coefficient then \(A_{i\ell}=0\) for all \(\ell\neq k\).

1 for t=1,2_,...,T_ do<br>
   For each \(k\in\mathcal{K}\) compute<br>
  \(W_k^{(t)}=exp\left(\eta\sum_{r=1}^{t-1}N_k^{(r)}\right),X_k^{(t)}=R\cdot\frac{W_k^{(t)}}{\text{\texttt{Tr}}(W_k^{(t)})}\)<br>
   Either output `Fail`, or find vector \(y=y^{(t)}\in\mathbb{R}_{\ge 0}^\mathcal{I}\times\mathbb{R}^{\mathcal{I}^\prime}\) such that \(b^\top y\ge\alpha\) and<br>
\(N_k^{(t)}\bullet X_k^{(t)}\le 0,N_k^{(t)}=^\text{def}-S_k(y)\forall k\in\mathcal{K}\) (5a)<br>
\(S_k(y)\unknown 0\forall k\in[K]-\mathcal{K}\) (5b)

**Algorithm 2:** Partial-variable MMWU algorithm.

