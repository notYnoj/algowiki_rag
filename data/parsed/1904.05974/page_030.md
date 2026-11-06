Set \(\alpha_{a_0}=\alpha_{b_0}=0\). It is easy to check that \(\alpha_u+\alpha_v=0\) for every \((u,v)\in M_S\). Hence \(\sum_{u\in A\cup B}\alpha_u=0\). We prove in Claim 5 below that \(\alpha_u+\alpha_v\ge\mathsf{wt}_{M_S}(u,v)\) for every edge (_u,v_) in _G_. Also, \(\alpha_u=0=\mathsf{wt}_{M_S}(u,u)\) for \(u\in\{a_0,b_0\}\) and \(\alpha_u\ge-1=\mathsf{wt}_{M_S}(u,u)\) for all other vertices _u_. Thus \(\alpha\) is a witness of _M<sub>S</sub>_’s popularity. \(\sqcap\sqcup\)

**Claim 5** \(\alpha_u+\alpha_v\ge\mathsf{wt}_{M_S}(u,v)\) _for every edge_ (_u,v_) _in G._

_Proof._ It is easy to check that we have \(\alpha_u+\alpha_v=\mathsf{wt}_{M_S}(u,v)\) when _u_ and _v_ belong to the same gadget, i.e., when \(u,v\in Z_i\) for some \(i\in[n_H]\) or \(u,v\in Y_e\) for some \(e\in E_H\). What we need to check now is that for any _e_=(_i,j_) and _i\<j_, the edges (_a<sub>i</sub>,t<sub>e</sub>_) and (_s<sub>e</sub>,b<sub>j</sub>_) are _covered_.

Suppose \(i\in S\). Then \((s''_e,t_e)\in M_S\). So \(\alpha_{a_i}+\alpha_{t_e}=0-1=-1>-2=\mathsf{wt}_{M_S}(a_i,t_e)\), since _t<sub>e</sub>_ is matched to its top choice \(s''_e\) and so wt_<sub>M<sub>S</sub></sub>(a<sub>i</sub>,t<sub>e</sub>_)=-2. Since \(i\in S\), it follows that \(j\notin S\) and so we have \(\alpha_{a_j}=\alpha_{b_j}=1\). Thus \(\alpha_{s_e}+\alpha_{b_j}=-1+1=0=\mathsf{wt}_{M_S}(s_e,b_j)\) since _s<sub>e</sub>_ is matched to \(t''_e\) and _s<sub>e</sub>_ prefers _b<sub>j</sub>_ to \(t''_e\).

If \(i\notin S\) then \(\alpha_{a_i}=1\). So we have \(\alpha_{a_i}+\alpha_{t_e}=1-1=0=\mathsf{wt}_{M_S}(a_i,t_e)\) since \((s'_e,t_e)\in M_S\) and _t<sub>e</sub>_ prefers _a<sub>i</sub>_ to \(s'_e\). Also, _s<sub>e</sub>_ is matched to its top choice \(t'_e\) and so \(\mathsf{wt}_{M_S}(s_e,b_j)=-2<\alpha_{s_e}+\alpha_{b_j}\) since \(\alpha_{b_j}\ge 0\). Thus the edges (_a<sub>i</sub>,t<sub>e</sub>_) and (_s<sub>e</sub>,b<sub>j</sub>_) are covered in all cases. \(\sqcap\sqcup\)

**Extension Complexity.** The max-size popular matching polytope of _G_ is a face \(F'\) of the popular matching polytope P. Our goal is to define a linear surjective map _f_ from \(F'\) to I_<sub>H</sub>_. Hence, given an extension \(\mathcal{T}'\) for P, we obtain that

\(\mathcal{I}_H=\{x:x=f(z),(z,y)\in\mathcal{T}',|z|=\frac{n}{2}-1\}.\)

Therefore, an extension of small size for P would imply the existence of an extension of small size for I_<sub>H</sub>_. The lower bound on the extension complexity of I_<sub>H</sub>_ will therefore imply a lower bound on the extension complexity of P.

We will need the following properties:

1. Let _M_ be a max-size popular matching. Consider the following 0-1 assignment **_x_** to the vertices of _H_. For \(i\in[n_H]\):<tbc>

<tbc>\(x_i=\left\{\begin{array}{ c c }
1 & \text{if}(a_i,b_i)\in M; \\
0 & \text{otherwise}.
\end{array}\right.\)<tbc>

<tbc>It follows from Lemma 9 that **_x_** is the incidence vector of an independent set in _H_.<tbc>

2. Let **_x_** be the incidence vector of an independent set in _H_. It follows from the proof of Lemma 10 that there is a max-size popular matching _M_ with the following properties:

<tbc>\(\text{for}i\in[n_H]:(a_i,b_i)\in M\Longleftrightarrow x_i=1.\)<tbc>

<tbc>Define the mapping _f_ from \(F'\) to I_<sub>H</sub>_ as: for \(z\in F'\), let _f_(**_z_**)=**_x_** where _x<sub>i</sub>=z_<sub>(_a<sub>i</sub>,b<sub>i</sub>_)</sub> for \(i\in[n_H]\). Part 1 above implies that, if **_z_** is a vertex of \(F'\), then _f_(**_z_**) is the incidence vector of an independent set in _H_. Together with part 2, we deduce \(f(F')=\mathcal{I}_H\). Thus we can conclude that \(xc(\mathcal{P})\ge 2^{\Omega(n_H/logn_H)}=2^{\Omega(m/logn)}\) where _m_ is the number of edges in _G_ (note that \(m=\Theta(n_H+m_H)=\Theta(n_H)\) since graphs _H_ have bounded degree). This finishes the proof of the first part of Theorem 3.

## 6.2 A Lower Bound on the Extension Complexity of Q

We now prove the second part of Theorem 3. Given a SAT formula \(\psi\) on _n_ variables, let \(C(\psi)\) be the convex hull of all vectors \(x\in\{0,1\}^n\) such that \(\psi(x)=1\) where, as usual, for \(i\in[n]\), _x<sub>i</sub>_=1 corresponds to the _i_-th variable being set to true. It is now easy to construct a family of 2SAT instances \(\psi\) with _n_ variables and _O(n_) clauses such that \(xc(C(\psi))=2^{\Omega(n/logn)}\): indeed, every independent set instance _H_=(_V,E_) can be formulated as a 2SAT instance \(\psi\) with _n_=|_V_| variables _x_<sub>1</sub>_,...,x<sub>n</sub>_ and clauses \((\neg x_i\vee\neg x_j)\) iff \((i,j)\in E\).<tbc>

