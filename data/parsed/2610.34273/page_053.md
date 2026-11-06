_v_. Because \(\mathrm{deg}(v)\ge\ell\), the family \((c_e)_{e\in E(G)\backslash E_v}\) has at most \(m-\ell=d\) members and is linearly independent.

We first select a large set of edge labelings. Fix an integer \(q\ge 2\) and define<tbc>

\(B=\mathrm{max}\left(1,\mathrm{max}_{1\le j\le d}\sum_{e\in E(G)}|c_{e,j}|\right),C=(2B+1)^d.\)

<tbc>The constants _B,C_ depend only on the fixed vectors, not on _q_. We identify each tuple \(\mathbf{a}=(a_e)_{e\in E(G)}\in[q]_0^{E(G)}\) with the labeling \(e\mapsto a_e\), and use _I<sub>v</sub>_(**a**) for its coordinate at vertex _v_ from Definition 2.20. Each coordinate of \(\sum_{e\in E(G)}c_ea_e\) is an integer in \[-_B(q_-1)_,B(q_-1)\]. There are therefore at most \((2Bq+1)^d\le Cq^d\) possible values of this sum. There are _q<sup>m</sup>_ labelings. By the pigeonhole principle, some \(g\in\mathbb{Z}^d\) has a fiber

\(\mathcal{F}_g=\left\{\mathbf{a}\in[q]_0^{E(G)}\middle|\sum_{e\in E(G)}c_ea_e=g\right\}.\)

Writing _R_=|F_<sub>g</sub>_|, this choice satisfies \(R\ge C^{-1}q^{m-d}=C^{-1}q^\ell\).

We next construct a degeneration that keeps exactly this fiber. Order the edges lexicographically, and for an edge _e_=(_u,v_) with _u\<v_, put _o(e_)=_u_. For each vertex _v_, assign the following integer weight to its basis vector with incident labels \((a_e)_{e\in E_v}\):

\(w_v((a_e)_{e\in E_v})=\mathbf{1}_{\{v=1\}}\langle g,g\rangle+\sum_{e\in E(G)o(e)=v}\big(\langle c_e,c_e\rangle a_e^2-2\langle g,c_e\rangle a_e\big)\)<br>
\(+2\sum_{e,f\in E_ve<f}\langle c_e,c_f\rangle a_ea_f.\)

Here **1**<sub>{_v_=1}</sub> is 1 when _v_=1 and 0 otherwise. Each summand depends only on labels incident to _v_, so it is a valid local weight. Distinct edges of a simple graph share at most one endpoint. Also, \(\langle c_e,c_f\rangle=0\) when _e_ and _f_ are disjoint, by orthogonality in the line graph. Consequently, summing these local weights gives<tbc>

\(\sum_{v=1}^kw_v((a_e)_{e\in E_v})=\left\langle\sum_{e\in E(G)}c_ea_e-g,\sum_{e\in E(G)}c_ea_e-g\right\rangle.\)

<tbc>This is a nonnegative integer and is zero exactly for \(\mathbf{a}\in\mathcal{F}_g\). Multiplying each local basis vector by \(\varepsilon\) to its assigned weight therefore degenerates GT_<sub>q</sub>(G_) to

\(T_g=\sum_{\mathbf{a}\in\mathcal{F}_g}e_{I_1(\mathbf{a})}^{(q^{\mathrm{deg}(1)})}\otimes_C\cdots\otimes_Ce_{I_k(\mathbf{a})}^{(q^{\mathrm{deg}(k)})}.\)

Individual weights can be negative; Definition 2.15 allows the resulting Laurent-polynomial local maps.

We next show \(\mathsf{I}_k(R)\unknown T_g\) by deleting unused coordinates and relabeling the remaining coordinates on each leg. Suppose that \(\mathbf{a},\mathbf{b}\in\mathcal{F}_g\) agree on all edges incident to a vertex _v_. Subtracting their two fiber equations yields \(\sum_{e\in E(G)\backslash E_v}c_e(a_e-b_e)=0\). The vectors in this sum are linearly independent, as observed above. Thus _a<sub>e</sub>=b<sub>e</sub>_ for every \(e\in E(G)\backslash E_v\), and the labelings agree on all edges. Hence distinct labelings in F_<sub>g</sub>_ give distinct basis vectors at every<tbc>

