_Proof._ Denote \(c_n=\mathtt{cost}_{\mu_n}(C_n)\) and \(t_n=\mathtt{cost}_{\mu_n}(T_n)\). Denote also by _v<sub>n</sub>_ the number of vertices |_V_(T_<sub>n</sub>_)|. By induction, _v<sub>n</sub>_=2<sup>_n_+1</sup>-1. Observe that _c<sub>n</sub>_ satisfies the recurrence<tbc>

\(c_n=v_n+2c_{n-1}=2^{n+1}-1+2c_{n-1},\)

<tbc>and that _c<sub>n</sub>_=2<sup>_n_+1</sup>_n_+1 is the solution for this formula. Repeating the analysis from Lemma 3.3, _t<sub>n</sub>_ satisfies the recurrence

\(t_n=t_{n-1}+(v_{n-1}+t_{n-1})+2=2^n+1+2t_{n-1}.\)

Observe that _t<sub>n</sub>_=2<sup>_n_</sup>_n_+2<sup>_n_+1</sup>-1 is the solution to this formula.

_Proof of Theorem 1.2(ii)._ Denote by \(\tilde{\mu}_n\) the uniform distribution over _V_(T). Using Lemma 3.4 we have<tbc>

\(\frac{\mathtt{cost}_{\tilde{\mu}_n}(C_n)}{\mathtt{OPT}(\mathcal{T}_n,\tilde{\mu}_n)}\ge\frac{\mathtt{cost}_{\tilde{\mu}_n}(C_n)}{\mathtt{cost}_{\tilde{\mu}_n}(T_n)}=\frac{\mathtt{cost}_{\mu_n}(C_n)}{\mathtt{cost}_{\mu_n}(T_n)}\rightarrow 2.\)

<tbc>We also have

\(\mathtt{cost}_{\tilde{\mu}_n}(C_n)=\frac{\mathtt{cost}_{\mu_n}(C_n)}{2^{n+1}-1}\rightarrow\infty,\)

therefore, using Theorem 1.1, also \(\mathtt{OPT}(\mathcal{T}_n,\tilde{\mu}_n)\rightarrow\infty\). This concludes the proof.

## 4 Approximation guarantees for trees with bounded degrees

In this section we show the upper and lower bounds on the approximation quality of centroid trees when the underlying tree T has bounded degree.

### 4.1 Upper bound

**Theorem 1.3.** _Let_ T _be a tree,_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\)_, and let_ \(\Delta\) _be the_ maximum degree _of_ T _. Then_

\(\mathtt{cent}(\mathcal{T},w)\le\left(2-\frac{1}{2^\Delta}\right)\cdot\mathtt{OPT}(\mathcal{T},w).\)

For simplicity, in what follows we omit the weight function _w_ from notations.

**Lemma 4.1.** _Let C be a centroid tree of_ T _such that_ cost(_C_)=`cent`(T)_. Let P_=(_v_<sub>0</sub>_,v_<sub>1</sub>_,...,v<sub>p</sub>_) _be any path in C. Then_<tbc>

\(\mathtt{cent}(\mathcal{T})\le\left(2-\frac{1}{2^p}\right)m+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-P)}\mathtt{cent}(\mathcal{H}).\)

<tbc>_Proof._ By induction on _p_. For _p_=0 we have

\(\mathtt{cent}(\mathcal{T})=m+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-v_0)}\mathtt{cent}(\mathcal{H}),\)

as required.

Assume now _p\>_0. Denote by \(\tilde{\mathcal{T}}\) the connected component of T-_v_<sub>0</sub> where _v_<sub>1</sub> is. Denote \(\tilde{P}=(v_1,\dots,v_p)\), and \(\tilde{m}=w(\tilde{\mathcal{T}})\). Observe that \(\tilde{m}\le m/2\) and that \(\mathbb{C}(\mathcal{T}-P)=\mathbb{C}(\tilde{\mathcal{T}}-\tilde{P})\cup(\mathbb{C}(\mathcal{T}-v_0)-\{\tilde{\mathcal{T}}\})\). By the induction hypothesis we have<tbc>

\(\mathtt{cent}(\tilde{\mathcal{T}})\le\left(2-\frac{1}{2^{p-1}}\right)\tilde{m}+\sum_{\mathcal{H}\in\mathbb{C}(\tilde{\mathcal{T}}-\tilde{P})}\mathtt{cent}(\mathcal{H}),\)

