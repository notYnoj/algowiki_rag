contradicting the fact that line 3 did not terminate. Hence \(|M|\ge c'n/3\) on this event, and \(\mathbb{E}_u|\mathtt{Matching}(u)|\ge\zeta c'n/6\).

Let us define \(c',\sigma,\delta\) as in Theorem 23, and set

\(\Delta=\sqrt{\frac{\varepsilon}{logn}}\) (15)

\(\mu\in[\mu_0,2\mu_0],\mu_0=\frac{6\alpha}{c'n\Delta}\) (16)

The cost of the element cut in line 2 of the algorithm is then at most \(2c'n\mu=\Theta\left(\alpha\sqrt{(logn)/\varepsilon}\right)\), which corresponds to an \(O\left(\sqrt{(logn)/\varepsilon}\right)\) pseudo-approximation algorithm.

## 7.1 Chaining algorithm

The remaining part is identical to the algorithm in \[24\]. Assume that case (i) in Lemma 23 holds (otherwise calling `Matching`(_u_) for _u_∼N(0_,I<sub>d</sub>_) will terminate the oracle after _O_(1) expected calls). Assume also that \(\mathtt{Matching}(\cdot)\) is _skew-symmetric_, i.e. `Matching`(-_u_) is obtained from `Matching`(_u_) by reversing edge orientations. (This can be easily enforced algorithmically). The idea is to use procedure \(\mathtt{Matching}(\cdot)\) to find many "violating paths", i.e. paths \(p=(p_0,\dots,p_{\ell(p)})\) that satisfy

\(\sum_{j=1}^{\ell(p)}\|p_j-p_{j-1}\|^2\le\|p_{\ell(p)}-p_0\|^2-\Delta\) (17)

For a set of directed paths _M_ let _M_<sup>`violating`</sup> be the set of paths \(p\in M\) that are either violating or contain a violating path _q_ as a subpath (_p_=(_...,q,..._)). For two sets of paths \(M,M'\) define

\(M\circ M'=\{p\circ q:p\in M,q\in M',\mathtt{endpoint}(p)=\mathtt{startpoint}(q)\}\)

**Theorem 24** (\[40, 24\])**.** _Let_ `Matching`(_u_) _be a procedure that for given_ \(u\in\mathbb{R}^d\) _returns a directed matching on V in which every edge_ (_x,y_) _satisfies_ \(\langle y-x,u\rangle\ge\sigma\) _and_ \(\|x-y\|^2\le\Delta\)_. Assume that it is skew-symmetric and_ \(\mathbb{E}_u[|\mathtt{Matching}(u)|]=\Omega(n)\).

_For any_ \(K\in[1,O(1/\Delta)]\) _(with an appropriate constant) there exists an efficiently samplable distribution_ D _of vectors_ **u**=(_u_<sub>1</sub>_,...,u<sub>K</sub>_) _such that set_ \(M(\mathbf{u})=\mathtt{Matching}(u_1)\circ\dots\circ\mathtt{Matching}(u_K)\) _satisfies_ \(\mathbb{E}_{\mathbf{u}\sim\mathcal{D}}|M(\mathbf{u})^\mathtt{violating}|\ge e^{-\Theta(K^2)}n\).

Set \(K=\Theta(\Delta logn)=\Theta\left(\sqrt{\varepsilon logn}\right)\) with a sufficiently small constant, then indeed \(K=O(1/\Delta)=O\left(\sqrt{(logn)/\varepsilon}\right)\) since \(\varepsilon=O(1)\). Let us run the algorithm in Theorem 24 until we get \(|M(\mathbf{u})^\mathtt{violating}|\ge e^{-\Theta(K^2)}n=n^{1-\Theta(\varepsilon)}\). Since we always have \(|M(\mathbf{u})|\le n\), this will happen after \(n/n^{1-\Theta(\varepsilon)}=n^{\Theta(\varepsilon)}\) runs in expectation (or \(Kn^{\Theta(\varepsilon)}=n^{\Theta(\varepsilon)}\) calls to \(\mathtt{Matching}(\cdot)\)). Once we have a set _P_ of violating paths with \(|P|\ge n^{1-\Theta(\varepsilon)}\), the output of the oracle is constructed as follows. Set \(\lambda_{ij}=0\) for all \(ij\in E\). Set \(f_p=\frac{2\alpha}{|P|\Delta}\) for all \(p\in P\), and _f<sub>p</sub>_=0 for all other paths. Then \(N=\sum_pf_pT_p-\mathcal{L}(G^\lambda)=\frac{2\alpha}{|P|\Delta}(\mathcal{L}(F)-\mathcal{L}(D))\) where multigraph _F_ is the union of paths in _P_ and multigraph _D_ is the union of edges \(\partial p=\{\mathtt{startpoint}(p),\mathtt{endpoint}(p)\}\) over \(p\in P\). Note that the complexity of the oracle is dominated by \(n^{\Theta(\varepsilon)}\) maximum flow computations.

**Lemma 25.** _Suppose that parameters_ \(\tau,\gamma\) _in eq._ (6) _satisfy_ \(\tau<2\) _and_ \(\gamma\le\frac{\Delta}{20(K+1)}\)_. Then variables_ \(\lambda_{ij}\) _and matrix N defined above are valid output of the reduced oracle. Matrix N has at most_ \(O(n\sqrt{logn})\) _non-zero entries, and its spectral norm is at most_ \(\frac{\alpha\cdot\text{polylog}(n)}{n^{1-\Theta(\varepsilon)}}\) .

