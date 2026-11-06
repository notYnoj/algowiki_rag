Let _C<sub>n</sub>_ denote the search tree on T_<sub>n</sub>_ obtained by setting _c_ as the root and recursing. Observe that _C<sub>n</sub>_ is a centroid tree of (T_<sub>n</sub>,w<sub>n</sub>_).

**Lemma 3.2.** _The following hold_

(_a)_ `cost`_<sub>w<sub>n</sub></sub>(C<sub>n</sub>_)=_n_+1,<tbc>

(_b)_ \(lim_{n\rightarrow\infty}\mathtt{OPT}(\mathcal{T}_n,w_n)=\infty\).

_Proof._ Let _c<sub>n</sub>_=`cost`_<sub>w<sub>n</sub></sub>(C<sub>n</sub>_). Clearly, _c_<sub>0</sub>=1. Assume _n\>_0. Let _C_<sub>A</sub> and _C_<sub>B</sub> be search trees on A and B respectively, each a copy of _C_<sub>_n_-1</sub>. By construction of _C<sub>n</sub>_ we have

\(c_n=1+\frac{1}{2}\mathtt{cost}_{w_\mathcal{A}}(C_\mathcal{A})+\frac{1}{2}\mathtt{cost}_{w_\mathcal{B}}(C_\mathcal{B})=1+c_{n-1},\)

and (a) follows by induction.

Using (a) and Theorem 1.1, part (b) follows:

\(\mathtt{OPT}(\mathcal{T}_n,w_n)\ge\frac{c_n+1}{2}=\frac{n}{2}+1\rightarrow\infty.\)

Next, in order to bound `OPT`(T_<sub>n</sub>,w<sub>n</sub>_) from above, we construct a sequence of search trees _T<sub>n</sub>_ on T_<sub>n</sub>_. For _n_=0, tree _T_<sub>0</sub> is a single vertex. Assume _n\>_0. Let A, B, and _c_ be as in the definition of T_<sub>n</sub>_. Let _T_<sub>A</sub> and _T_<sub>B</sub> be search trees over A and B respectively, each a copy of _T_<sub>_n_-1</sub>. Denote _r_<sub>A</sub>=`root`(A) and _r_<sub>B</sub>=`root`(B). Tree _T<sub>n</sub>_ is obtained by adding an edge from _r_<sub>A</sub> to _r_<sub>B</sub> and an edge from _r_<sub>B</sub> to _c_, and setting `root`(_T<sub>n</sub>_)=_r_<sub>A</sub>.

**Lemma 3.3.** \(\mathtt{cost}_{w_n}(T_n)=\frac{n}{2}+1\).

_Proof._ Denote _t<sub>n</sub>_=`cost`_<sub>w<sub>n</sub></sub>(T<sub>n</sub>_). Clearly _t_<sub>0</sub>=1. Assume _n\>_0. The contribution of vertices of A to _t<sub>n</sub>_ is exactly \(\frac{1}{2}\mathtt{cost}_{w_\mathcal{A}}(T_\mathcal{A})=\frac{t_{n-1}}{2}\) . Since _r_ is an ancestor of all vertices in B, the contribution of these vertices to _t<sub>n</sub>_ is exactly \(\frac{1}{2}(1+\mathtt{cost}_{w_\mathcal{B}}(T_\mathcal{B}))=\frac{1+t_{n-1}}{2}\) . Summing the contribution of all vertices, we get \(t_n=t_{n-1}+\frac{1}{2}\) and the claim follows.

_Proof of Theorem 1.2(i)._ By Lemma 3.3, \(\mathtt{OPT}(\mathcal{T}_n,w_n)\le\frac{n}{2}+1\). Together with Lemma 3.2, the claim follows.

## Part (ii).

Let T_<sub>n</sub>_, _C<sub>n</sub>_ and _T<sub>n</sub>_ be as in the proof of Theorem 1.2(i). Let \(\mu_n:V(\mathcal{T}_n)\rightarrow\mathbb{R}_{\ge 0}\) be the constant function \(\mu_n(v)=1\). Let A, B and _c_ be as in the construction of T_<sub>n</sub>_. Observe that _c_ is the unique centroid of \((\mathcal{T}_n,\mu_n)\). By induction, _C<sub>n</sub>_ is the unique centroid tree of \((\mathcal{T}_n,\mu_n)\).

**Lemma 3.4.** _The following hold_

(_a)_ \(\mathtt{cost}_{\mu_n}(C_n)=2^{n+1}n+1\),<tbc>

_(b)_ \(\mathtt{cost}_{\mu_n}(T_n)=2^nn+2^{n+1}-1\).<tbc>

r
c
c
r
Tn-1
c
Tn-1
r
Tn-1
Tn-1
Cn-1
Cn-1
Tn-1

Figure 2: Illustration of the proof of Theorem 1.2(i). Vertex _r_ is the root of T_<sub>n</sub>_. (_Left._) The underlying tree T_<sub>n</sub>_. (_Middle._) The entroid tree _C<sub>n</sub>_ of T_<sub>n</sub>_. (_Right._) The search tree _T<sub>n</sub>_.

