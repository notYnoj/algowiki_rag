We can now state the precise statement of the IPM of \[BLL<sup>+</sup>21\], given by Algorithm 1 and Lemma 4.7.

**Lemma 4.7** (\[BLL<sup>+</sup>21, Lemma 4.12\])**.** _Consider a call to IPM (Algorithm 1). Let x_<sup>(init)</sup>_, s_<sup>(init)</sup>, \(\mu\) _be such that_ **A**_z+s_<sup>(init)</sup>=_c for some z, let_ \(\tau^{(\mathrm{init})}\) _be such that_ \(\|T(x^{(\mathrm{init})})^{-1}(\tau^{(\mathrm{init})}=\tau(x^{(\mathrm{init})}))\|_\infty\le\epsilon\)_, and let_ \(\epsilon,\gamma\) _be as defined in Algorithm 1, and_ \(\left\|\frac{s+\mu\tau(x^{(\mathrm{init})})\phi^\prime(x^{(\mathrm{init})})}{\mu\tau(x^{(\mathrm{init})})\sqrt{\phi^{\prime\prime}(x(\mathrm{init})})}\right\|_\infty\le\epsilon\) _and_ \(\|\mathbf{A}^\top x^{(\mathrm{init})}-b\|_{(\mathbf{A}^\top(\mathbf{T}(x^{(\mathrm{init})})\Phi^{\prime\prime}(x^{(\mathrm{init})}))^{-1}\mathbf{A})^{-1}}\le\epsilon\gamma(1-p)/C\)_. Then Algorithm 1 returns_ \(x,s\in\mathbb{R}^m\) _such that Ay+s=c for some_ \(y\in\mathbb{R}^n\) _and_ \(c^\top x-\mathrm{min}_{\mathbf{A}^\top x=bl_i\le x_i\le u_i\forall i\in[m]}c^\top x\lesssim n\mu\)_. The algorithm takes_ \(\widetilde{O}(\sqrt{n}\mathrm{log}(\mu/\mu^{(\mathrm{final})}))\) _iterations. Throughout all iterations,_ \(\left\|\frac{s+\mu\tau(x)\phi^\prime(x)}{\mu\tau(x)\sqrt{\phi^{\prime\prime}(x)}}\right\|_\infty\le\epsilon\).

## 4.3 Implicit Representation of \(\tau\)

Recall that the first step of each iteration is to find the Lewis weights \(\tau(x)\) of our new point _x_ where \(\tau(x)\) is defined as the solution to

\(\tau(x)=\sigma(\mathbf{T}^{1/2-1/p}\Phi''(x)\mathbf{A})+\frac{n}{m}\)

where **T** is the diagonal matrix with \(\tau\) on the diagonal.

Specifically, in the step of the algorithm, we want to maintain an approximate \(\overline{\tau}\approx_\epsilon\tau(x)\). Here, we in fact maintain an \(\overline{\tau}\approx_{\epsilon_\tau}\tau(x)\) for \(\epsilon_\tau:=\gamma/60<\epsilon\) where \(\gamma\) and \(\tau\) are globally defined above in the interior point method (Algorithm 1). We here show how to compute such \(\overline{\tau}\). Note that for our choice of accuracy \(\epsilon_\tau\), it is logarithmic in _n_, and thus can be subsumed into the \(\widetilde{O}\)s.

**Theorem 4.8.** _There is a randomized algorithm that receives as input:_ \(p\in[\frac{1}{2},2)\)_, a directed weighted graph G_=(_V,E_) _given as stream,_ \(x\in\mathbb{R}_{>0}^E\) _with query time T<sub>x</sub>, and error parameter_ \(\epsilon_\tau\).

_Then, within_ \(\widetilde{O}(mT_x+\epsilon_\tau^{-2})\) _time,_ \(\widetilde{O}(1)\) _passes through the stream, and with_ \(\widetilde{O}(n\epsilon_\tau^{-2})\) _space, the algorithm constructs w.h.p. an implicit representation of_ \(\overline{\tau}\) _with_ \(\overline{\tau}\approx_{\epsilon_\tau}\tau(x)\) _. Each edge query can be done in_ \(T_x+\widetilde{O}(1)\) _time._

To prove Theorem 4.8, we first use the following lemmas.

**Lemma 4.9** (\[BLL<sup>+</sup>21, Lemma 5.3\])**.** _Let w, z,_ \(\overline{\sigma}\in\mathbb{R}_{>0}^m\), \(\epsilon,\epsilon_\sigma>0\) _and_ \(p\in(0,2)\) _with_ \(w\approx_\epsilon\sigma(\mathbf{W}^{1/2-1/p}\mathbf{A})+z\) _and_ \(\overline{\sigma}\approx_{\epsilon_\sigma}\sigma(\mathbf{W}^{1/2-1/p}\mathbf{A})+z\)_. Define_ \(w'=(w^{2/p-1}\overline{\sigma})^{p/2}\)_, then_ \(w'\approx_{(\epsilon+\epsilon_\sigma)|1-p/2|+\epsilon_\sigma}\sigma(\mathbf{W}^{1/2-1/p}\mathbf{A})\).

**Lemma 4.10** (\[BLL<sup>+</sup>21, Lemma 5.5\])**.** _For any_ \(w,z\in\mathbb{R}_{>0}^m\), \(\epsilon>0\)_, and_ \(p\in(0,2]\) _with_ \(w\approx_\epsilon\sigma(\mathbf{W}^{\frac{1}{2}-\frac{1}{p}}\mathbf{A})+z\) _we have_ \(w\approx_\epsilon\tau(\mathbf{A})\).

_Proof of Theorem 4.8._ The algorithm starts by picking some initial candidate for \(\overline{\tau}\), and then iteratively refines it. Let us start with the refinement procedure.

### Refinement

Suppose we already have some candidate \(\overline{\tau}\approx\tau(x)\) but with an approximation factor that is worse than \(\epsilon_\tau\). The general approach is to iteratively improve the approximation factor. If for \(\epsilon_\sigma\le\epsilon_\tau/10\) we had a \(\overline{\sigma}\approx_{\epsilon_\sigma}\sigma(\overline{\mathbf{T}^{1/2-1/p}}\Phi''(x)\mathbf{A})\), then we can then perform the following update,

\(\overline{\tau}\leftarrow(\overline{\tau^{2/p-1}}(\overline{\sigma_e}+\frac{n}{m}))^{p/2},\) (14)

which by Lemma 4.9 would decrease the approximation factor by about a 1-2_/p_ factor.

It remains to find such an \(\overline{\sigma}\). To do so, we take, for each edge _e_,

\(\overline{\sigma_e}=\|\mathbf{R}\overline{\mathbf{T}^{1/2-1/p}}\Phi''(x)^{-1/2}\mathbf{A}\mathbf{M}^{-1}\mathbf{A}^\top\Phi''(x)^{-1/2}\overline{\mathbf{T}^{1/2-1/p}}\chi_e\|_2^2,\)

where **R** is a random sparse Johnson-Lindenstrauss matrix giving an \(\epsilon_\sigma/2\) approximation, and **M** is a \((1\pm\epsilon_\sigma/2)\)-spectral sparsifier for \(\mathbf{A}^\top\Phi''(x)^{-1/2}\overline{\mathbf{T}^{1-2/p}}(x)^{-1/2}\mathbf{A}\), constructed by Lemma 2.1. In each iteration, we store \(\mathbf{P}:=\mathbf{R}\overline{\mathbf{T}^{1/2-1/p}}\Phi''(x)^{-1/2}\mathbf{A}\mathbf{M}^{-1}\), which is a \(O((\epsilon_\sigma/2)^{-2}\mathrm{log}n)\times n\) matrix.

