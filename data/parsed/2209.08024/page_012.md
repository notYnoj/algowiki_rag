therefore

\(\mathtt{cent}(\mathcal{T})=m+\mathtt{cent}(\tilde{\mathcal{T}})+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-v_0)\mathcal{H}\neq\tilde{\mathcal{T}}}\mathtt{cent}(\mathcal{H})\)<br>
\(\le m+\left(2-\frac{1}{2^{p-1}}\right)\tilde{m}+\sum_{\mathcal{H}\in\mathbb{C}(\tilde{\mathcal{T}}-\tilde{P})}\mathtt{cent}(\mathcal{H})+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-v_0)H\neq\tilde{\mathcal{T}}}\mathtt{cent}(\mathcal{H})\)<br>
\(\le m+\left(2-\frac{1}{2^{p-1}}\right)\frac{m}{2}+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-P)}\mathtt{cent}(\mathcal{H})\)<br>
\(=\left(2-\frac{1}{2^p}\right)m+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-P)}\mathtt{cent}(\mathcal{H}),\)

as required.

_Proof of Theorem 1.3._ The proof is by induction on |_V_(T)|. Let _T_ be any search tree on T . We will show that \(\mathtt{cent}(\mathcal{T})\le\left(2-\frac{1}{2^\Delta}\right)\mathtt{cost}(T)\).

Denote _r_=`root`(_T_). Let _C_ be a centroid tree on T with `cost`(_C_)=`cent`(T). Denote by _v_<sub>0</sub>_,v_<sub>1</sub>_,...,v<sub>d</sub>=r_ the vertices along the path to _r_ in _C_. Denote T_<sub>i</sub>_=T\[_V(C<sub>v<sub>i</sub></sub>_)\]. Observe that \(r\in V(\mathcal{T}_d)\subseteq\cdots\subseteq V(\mathcal{T}_0)=V(\mathcal{T})\). For _i\<d_, denote by K_<sub>i</sub>_ the connected component of T-_r_ where _v<sub>i</sub>_ is. Denote by _s<sub>i</sub>_ the unique child of _r_ in _T_ such that \(s_i\in V(\mathcal{K}_i)\), i.e., _V(T<sub>s<sub>i</sub></sub>_)=_V_(K_<sub>i</sub>_). Finally, denote by _p_ the minimal _i_ for which one of the following holds:

1. _v<sub>i</sub>=r_, i.e., _i=d_,<tbc>

2. \(s_i\in V(\mathcal{T}_{i+1})\), or<tbc>

3. there exists _j\<i_ such that K_<sub>j</sub>_=K_<sub>i</sub>_, i.e., _s<sub>j</sub>=s<sub>i</sub>_.

Note that from the third condition above it follows that \(p\le\Delta\). Denote _P_=(_v_<sub>0</sub>_,...,v<sub>p</sub>_). We will prove the following.

**Claim 4.1.**<tbc>

\(\mathtt{cost}(T)\ge m+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-P)}\mathtt{cost}(T|_\mathcal{H}).\)

<tbc>Assume for now that Claim 4.1 holds. Using Lemma 4.1, the fact that \(p\le\Delta\), the induction hypothesis and Claim 4.1, we have

\(\mathtt{cent}(\mathcal{T})\le\left(2-\frac{1}{2^p}\right)m+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-P)}\mathtt{cent}(\mathcal{H})\)<br>
\(\le\left(2-\frac{1}{2^\Delta}\right)m+\sum_{\mathcal{H}\in\mathbb{C}(\mathcal{T}-P)}\left(2-\frac{1}{2^\Delta}\right)\mathtt{cost}(T|_\mathcal{H})\)<br>
\(\le\left(2-\frac{1}{2^\Delta}\right)\mathtt{cost}(T),\)

as required. It remains to prove Claim 4.1.

_Proof of Claim 4.1._ The proof breaks into three cases according to the defining condition of _p_.

**Case 1.** Assume _v<sub>p</sub>=r_. For every \(\mathcal{H}\in\mathbb{C}(\mathcal{T}-P)\) and \(v\in V(\mathcal{H})\) we have \(\mathtt{Path}_T(v)\supseteq\{r\}\cup\mathtt{Path}_{T|_\mathcal{H}}(v)\). The contribution of such _v_ to `cost`(_T_) is therefore at least _w(v_)(1+|`Path`<sub>_T_|<sub>H</sub></sub>(_v_)|). The contribution of each _v<sub>i</sub>_ to `cost`(_T_) is at least _w(v<sub>i</sub>_). Summing the contribution of all vertices yields the required result. See Figure 3.

