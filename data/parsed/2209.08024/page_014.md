(_ii)_ _There is a sequence of instances_ (T_<sub>n</sub>,w<sub>n</sub>_) _such that_ T_<sub>n</sub> has maximum degree at most_ \(\Delta\), \(lim_{n\rightarrow\infty}\mathsf{OPT}(\mathcal{T}_n,w_n)=\infty\), _w<sub>n</sub>_(T_<sub>n</sub>_)=1_, and for every centroid tree C<sub>n</sub> of_ (T_<sub>n</sub>,w<sub>n</sub>_)<tbc>

<tbc>\(\mathsf{cost}_{w_n}(C_n)\ge\left(2-\frac{4}{2^\Delta}\right)\cdot\mathsf{OPT}(\mathcal{T}_n,w_n)-1.\)<tbc>

<tbc>**Part (i).** As in the proof of Theorem 1.2, it will suffice to prove Theorem 1.4(i) for _some_ centroid tree _C<sub>n</sub>_. Using Lemma 2.4, we can then add arbitrarily small perturbation to _w<sub>n</sub>_, making _C<sub>n</sub>_ the unique centroid tree.

The sequence (T_<sub>n</sub>,w<sub>n</sub>_) of Theorem 1.4(i) is constructed recursively as follows. For the sake of the construction we regard T_<sub>n</sub>_ as a rooted tree. T<sub>0</sub> is simply a single vertex _v_ (which is the root) and _w_<sub>0</sub>(_v_)=1. For _n\>_0, T_<sub>n</sub>_ is constructed from \(\Delta\) copies of T<sub>_n_-1</sub> and \(\Delta+1\) additional vertices, \(v_1,\dots,v_{\Delta+1}\), as shown in Figure 5 (left). The _i_’th copy of T<sub>_n_-1</sub> gets the weight function _w_<sub>_n_-1</sub>/2_<sup>i</sup>_. We set _w<sub>n</sub>(v<sub>i</sub>_)=0 for \(1\le i\le\Delta\) and \(w_n(v_{\Delta+1})=1/2^\Delta\). Finally, we set root(T_<sub>n</sub>_)=_v_<sub>1</sub>. By induction, T_<sub>n</sub>_ has maximal degree \(\Delta\) and _w<sub>n</sub>_ is a distribution on _V_(T_<sub>n</sub>_).

Let _C<sub>n</sub>_ be a search tree on T_<sub>n</sub>_ defined recursively as follows. Connect the vertices \(v_1,\dots,v_{\Delta+1}\) to form a path and set _v_<sub>1</sub> as the root of _C<sub>n</sub>_. Continue recursively on each connected component of \(\mathcal{T}-\{v_1,\dots,v_{\Delta+1}\}\). (See Figure 5 (middle).) Observe that _C<sub>n</sub>_ is a centroid tree of (T_<sub>n</sub>,w<sub>n</sub>_).

Tp
Tp
Tp+1
KP = Kj
KO
KO = Kj
r
Sp
r
Sp
vj
Tp - Tp+1
vp-1
vp
Tp - Tp+1
vp-1
vp

V1
V1
V2
V3
V1
V2
V3
V4
Cn-1
Cn-1
V4
Tn-1
Tn-1
Tn-1
Tn-1
Tn-1
Tn-1
(wn-1/2)
(wn-1/2)
(wn-1/4)
(wn-1/4)
(wn-1/8)
(wn-1/24)
Cn-1
Cn-1
(wn-1/8)
(wn-1/8)
(wn-1/24)
Cn-1
(wn-1/24)

Figure 4: Case 3 in the proof of Claim 4.1. (_Left._) Sub-case where _v<sub>p</sub>_ is in the path in T between _r_ and _v<sub>j</sub>_. (_Right._) Complementary sub-case. Connected components of T-_P_ are represented by light gray circles. In both sub-cases, vertices in T_<sub>p</sub>_-T<sub>_p_+1</sub> have both _r_ and _s<sub>p</sub>_ as ancestors.

Figure 5: Illustration of Theorem 1.4(i). (_Left._) The underlying tree T_<sub>n</sub>_. (_Middle._) The centroid tree _C<sub>n</sub>_. (_Right._) The search tree _T<sub>n</sub>_.

