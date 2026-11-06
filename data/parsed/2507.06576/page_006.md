\(\sum_{F\in\mathcal{F}}y_F\ge 1\) (3a)

\(\sum_{F\in\mathcal{F}e\in F}y_F\le\alpha\cdot x(e)\forall e\in E(G)\)<br>
\(y_F\ge 0\forall F\in\mathcal{F}\)

By reversing the inequality (3a), we obtain that the following system (4) is also infeasible:

\(\sum_{F\in\mathcal{F}}(-y_F)\le-1,\)<br>
\(\sum_{F\in\mathcal{F}e\in F}y_F\le\alpha\cdot x(e)\forall e\in E(G),\) (4)

\(y_F\ge 0\forall F\in\mathcal{F}.\)

Now, we use the following variant of Farkas Lemma (See \[Sch98\] for a proof).

**Lemma 1.** \(\{x\in\mathbb{R}^n|Ax\le b,x\ge 0\}=\emptyset\) _iff there exists a vector u such that_ \(A^Tu\ge 0,u\ge 0\) _and b<sup>T</sup>u\<_0.

For a feasible multicut _F_, let \(\chi_F\in\{0,1\}^E\) denote its indicator vector. By Lemma 1, there exists \(u\ge 0\) and \(c\ge 0\) such that \(c^T\chi_F-u\ge 0\) for all \(F\in\mathcal{F}\) and \(-u+\alpha\cdot c^Tx<0\). This means that \(c^T\chi_F\ge u\) for all \(F\in\mathcal{F}\), and \(\alpha\cdot c^Tx<u\). Thus, \(c^T\chi_F\ge u>\alpha\cdot c^Tx\) for all \(F\in\mathcal{F}\). Therefore with respect to the cost function _c_, \(OPT_{LP}\le\frac{u}{\alpha}\) and OPT_<sub>IP</sub>\>u_. This implies that integrality gap of the multicut instance _M_ is \(>\alpha\), a contradiction.

To connect this with the notion of small diameter decompositions, we now give the formal definition.

**Definition 2** (Small Diameter Decomposition (SDD))**.** _Given an unweighted graph G, an integer parameter_ \(k\in\mathbb{N}\)_, and a probability parameter_ 0_\<p\<_1_, the small diameter decomposition (SDD) problem asks whether there exists a probability distribution_ \(\mathcal{D}=\{y_F\}_{F\in\mathcal{F}_k(G)}\) _over_ F_<sub>k</sub>(G), the family of k-diameter decompositions of G, such that every edge_ \(e\in E(G)\) _is included in a random k-diameter decomposition sampled from_ D _with probability at most p, that is,_<tbc>

\(\sum_{F\in\mathcal{F}_k(G)e\in F}y_F\le p\text{\textit{for all}}e\in E(G).\)

<tbc>_If such a distribution exists, we denote it by SDD(G,k,p_) _(See Figure 1). Moreover, a family of graphs_ G _is said to be SDD(k,p)-acceptable if for every_ \(G\in\mathcal{G}\) _there exists an SDD(G,k,p)._

In the following Theorem 2, we make explicit the relation between the integrality gap \(\alpha_{\mathcal{M}(\mathcal{G})}\) and the existence of suitable SDDs for graph families G closed under minors and edge subdivisions. The forward implication is a direct consequence of Theorem 1, which itself follows straightforwardly from the work of Carr and Vempala \[CV02\] in the context of the minimum multicut problem, and is therefore not our contribution. The backward<tbc>



Figure 1: _G_ is a simple path with 3 edges, and _k_=2. Let _F_<sub>1</sub>={_e_<sub>1</sub>_,e_<sub>2</sub>}_,F_<sub>2</sub>={_e_<sub>2</sub>}_,F_<sub>3</sub>={_e_<sub>2</sub>_,e_<sub>3</sub>}_,F_<sub>4</sub>={_e_<sub>1</sub>_,e_<sub>3</sub>}. One can see that F<sub>2</sub>(_G_)={_F_<sub>1</sub>_,F_<sub>2</sub>_,F_<sub>3</sub>_,F_<sub>4</sub>_,E(G_)}. Let _y_<sub>_F_<sub>1</sub></sub>=_y_<sub>_F_<sub>3</sub></sub>=_y_<sub>_E(G_)</sub>=0, and \(y_{F_2}=y_{F_4}=\frac{1}{2}\). This distribution is a \(SDD(G,2,\frac{1}{2})\).

