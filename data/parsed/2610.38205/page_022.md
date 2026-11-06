Based on the answer, for each _i,j_ we update the search space and _C<sub>i,j</sub>_ accordingly before the next query. Observe that the entries of \([R\star N]\) are in \([n]\cup\{\infty\}\) and thus the searches converge in _log(n_) steps.

Conversely, suppose we are given an oracle for Boolean min-plus product, and let \(A\in\{0,1\}^{n\times n}\) and \(B,C\in\mathbb{R}_{\ge 0}^{n\times n}\) be an instance of threshold testing. Compute _D_=(_B<sup>T</sup>⋆A<sup>T</sup>)<sup>T</sup>_. Then, for every _i,j_,

\(D_{i,j}=min\{B_{k,j}:A_{i,k}=1\}.\)

Hence we can obtain the answer by comparing _D<sub>i,j</sub>_ with _C<sub>i,j</sub>_ entrywise.

We next relate threshold testing to \(\alpha\)-navigability testing.

**Lemma 4.8.** _Boolean min-plus threshold testing and_ \(\alpha\)_-navigability testing have equivalent running times - if one of the two can be solved in T(n_) _time, the other can be solved in T(n_)+_O(n_<sup>2</sup>) _time._

_Proof._ We begin with the reduction from \(\alpha\)-navigability testing to Boolean min-plus threshold testing.

Let _G_=(_P,E_) be a directed graph on _P_={_v_<sub>1</sub>_,...,v<sub>n</sub>_}, and let _d_ be a metric on _P_. Define matrices \(A\in\{0,1\}^{n\times n}\) and \(B,C\in\mathbb{R}_{\ge 0}^{n\times n}\) by<tbc>

\(A_{i,k}=1\Longleftrightarrow(v_i,v_k)\in E,B_{k,j}=d(v_k,v_j),C_{i,j}=\frac{1}{\alpha}d(v_i,v_j).\)

<tbc>Then, for every _i,j_, we have \(min\{B_{k,j}:A_{i,k}=1\}\le C_{i,j}\) if and only if there exists _k_ such that

\((v_i,v_k)\in E\text{and}d(v_k,v_j)\le\frac{1}{\alpha}d(v_i,v_j),\)

which is exactly \(\alpha\)-navigability constraint for (_v<sub>i</sub>,v<sub>j</sub>_).

For the converse direction, let \(A\in\{0,1\}^{n\times n}\) and \(B,C\in\mathbb{R}_{\ge 0}^{n\times n}\) be an instance of Boolean min- plus threshold testing. Let _S_={_s_<sub>1</sub>_,...,s<sub>n</sub>_}, _U_={_u_<sub>1</sub>_,...,u<sub>n</sub>_}, and _T_={_t_<sub>1</sub>_,...,t<sub>n</sub>_}, and set \(P=S\unknown U\unknown T\).

Define a directed graph _G_=(_P,E_) by: \((s_i,u_k)\in E\) if and only if _A<sub>i,k</sub>_=1.

We now define a metric on _P_. Let \(W>\alpha max_{i,j}C_{i,j}+max_{k,j}B_{k,j}\). Let _H_ be the undirected weighted graph on _P_ containing the following edges:

• for every \(k,j\in[n]\), an edge {_u<sub>k</sub>,t<sub>j</sub>_} of weight _W+B<sub>k,j</sub>_;<tbc>

• for every \(i,j\in[n]\), an edge {_s<sub>i</sub>,t<sub>j</sub>_} of weight \(\alpha\cdot(W+C_{i,j})\).

Let _d_ be the shortest-path metric of _H_.

We claim that, for all _k,j_, _d(u<sub>k</sub>,t<sub>j</sub>_)=_W+B<sub>k,j</sub>_, and, for all _i,j_, \(d(s_i,t_j)=\alpha W+\alpha C_{i,j}\). Indeed, each of these values is realized by a direct edge. Any alternative path from _u<sub>k</sub>_ to _t<sub>j</sub>_ uses at least two edges between _U_ and _T_ or two edges between _S_ and _T_ and therefore has weight at least 2_W\>W+B<sub>k,j</sub>_. Likewise, any alternative path from _s<sub>i</sub>_ to _t<sub>j</sub>_ has at least one edge connecting _S_ and _T_ and at least one edge connecting _U_ and _T_ and therefore has weight at least \(\alpha\cdot W+W>\alpha\cdot(W+C_{i,j})\).

Therefore, for every _i,k,j_,

\(d(u_k,t_j)\le\frac{1}{\alpha}d(s_i,t_j)\Longleftrightarrow W+B_{k,j}\le W+C_{i,j}\Longleftrightarrow B_{k,j}\le C_{i,j}.\)

It follows that the \(\alpha\)-navigability oracle reports (_s<sub>i</sub>,t<sub>j</sub>_) if and only if there exists _k_ such that

\(A_{i,k}=1\text{and}B_{k,j}\le C_{i,j},\)

which is exactly the threshold-testing condition.

