We view an instance _G_=(_V,E,c,P_), where _P=v_<sub>1</sub>_v_<sub>2</sub>_...v<sub>k</sub>_, of Replacement Path as an attributed graph with edge attributes \(\alpha_E(e)=c(e)\) for all \(e\in E\) and vertex attributes \(\alpha_V(v_i)=i\) for all \(i\in\{1,\dots,k\}\), and \(\alpha_V(w)=0\) for all other vertices \(w\in V\backslash\{v_1,\dots,v_k\}\).

**Theorem A.6** (Replacement Path in the Isomorphic-Priors Model)**.** _There is an algorithm that solves_ Replacement Path _with k prior instances each having at most n vertices and m edges in O(k(n+m_)log_n_) _preprocessing time and O_((_n+m_)log_n_) _query time. Additionally, if each prior G<sub>i</sub> is equipped with a set of replacement paths, then the algorithm can also compute a set of replacement paths for H in O_((_n+m_)log_n_) _time._

In the following theorem, we prove that Replacement Path is invariant under 1-WL equivalence.

**Theorem A.7.** _Let_ \(G=(V,E,c:E\rightarrow\mathbb{R},P)\) _and_ \(G'=(V',E',c':E'\rightarrow\mathbb{R},P')\) _be two instances of_ Replacement Path_. If_ \(G\equiv_{1\text{-WL}}G'\)_, then G and_ \(G'\) _have the same optimal replacement path vector._

_Proof._ Let _P=v_<sub>1</sub>_,...,v<sub>k</sub>_ and \(P'=v'_1,\dots,v'_k\) be the designated shortest paths in _G_ and \(G'\), respectively. Observe that the initial coloring \(\chi_0\) assigns color _i_ to _v<sub>i</sub>_ and to \(v'_i\) for every \(i\in\{1,\dots,k\}\), and assigns color 0 to all remaining vertices. Let _OPT_ and \(OPT'\) be the optimal replacement vectors for _G_ and \(G'\), respectively. We show that for every \(i\in\{1,\dots,k-1\}\), \(OPT_i=OPT'_i\).

Fix \(i\in\{1,\dots,k-1\}\). Let _Q=u_<sub>1</sub>_,...,u<sub>m</sub>_ be a shortest _v_<sub>1</sub>_,v<sub>k</sub>_-path in _G<sub>i</sub>_=(_V,E_\\{(_v<sub>i</sub>,v_<sub>_i_+1</sub>)}). We construct a \(v'_1,v'_k\)-walk \(Q'=u'_1,\dots,u'_m\) in \(G'_i=(V',E'\backslash\{(v'_i,v'_{i+1})\})\) with the same sequence of stable colors as _Q_, and hence with the same total cost.

We define \(Q'\) inductively. Since _u_<sub>1</sub>=_v_<sub>1</sub>, its initial color is 1. Because \(G\equiv_{1\text{-WL}}G'\), there exists a vertex \(u'_1\in V'\) with \(\chi_\infty^G(u_1)=\chi_\infty^{G^\prime}(u'_1)\). By the Refinement property of 1-WL (see Lemma 7.6), \(u'_1\) has the same initial color as _u_<sub>1</sub>, and therefore \(\chi_0^{G^\prime}(u'_1)=1\), so \(u'_1=v'_1\).

Now suppose that \(u'_j\) has already been chosen so that \(\chi_\infty^G(u_j)=\chi_\infty^{G^\prime}(u'_j)\). Since \((u_j,u_{j+1})\in E\), by Neighborhood Preservation (see Lemma 7.6), there exists an outgoing edge \((u'_j,u'_{j+1})\in E'\) such that \(\chi_\infty^G(u_{j+1})=\chi_\infty^{G^\prime}(u'_{j+1})\) and (_u<sub>j</sub>,u_<sub>_j_+1</sub>) and \((u'_j,u'_{j+1})\) have the same edge label, i.e., the same cost under _c_ and \(c'\), respectively. Continuing in this way, we obtain a walk \(Q'\) in \(G'\) from \(v'_1\) to some vertex \(u'_m\) with \(\chi_\infty^G(v_k)=\chi_\infty^{G^\prime}(u'_m)\). By Refinement, \(\chi_0^{G^\prime}(u'_m)=\chi_0^G(v_k)=k\), and hence \(u'_m=v'_k\).

Thus, \(Q'\) is a \(v'_1,v'_k\)-walk in \(G'\) and \(c'(Q')=c(Q)\). We claim that \(Q'\) does not use the edge \((v'_i,v'_{i+1})\). Suppose otherwise. Then there exists _j_ such that \((u'_j,u'_{j+1})=(v'_i,v'_{i+1})\). Since \(v'_i\) and \(v'_{i+1}\) are the unique vertices of initial colors \(\chi_0^{G^\prime}(v'_i)=i\) and \(\chi_0^{G^\prime}(v'_{i+1})=i+1\), it follows from \(\chi_\infty^G(u_j)=\chi_\infty^{G^\prime}(u'_j)\) and \(\chi_\infty^G(u_{j+1})=\chi_\infty^{G^\prime}(u'_{j+1})\), together with another application of Refinement, that _u<sub>j</sub>=v<sub>i</sub>_ and _u_<sub>_j_+1</sub>=_v_<sub>_i_+1</sub>. Hence (_u<sub>j</sub>,u_<sub>_j_+1</sub>)=(_v<sub>i</sub>,v_<sub>_i_+1</sub>), contradicting the fact that _Q_ is a path in _G<sub>i</sub>_.

Therefore, \(Q'\) is a valid \(v'_1,v'_k\)-walk in \(G'_i\), and so, by Remark A.5, \(OPT'_i\le c'(Q')=c(Q)=OPT_i\). By symmetry, \(OPT_i\le OPT'_i\). Hence \(OPT_i=OPT'_i\), as required.

_Proof of Theorem A.6._ The first part follows directly from Theorems A.7 and 8.4. For the second part, observe that Theorem A.7 provides an explicit method for constructing replacement paths on _H_ given replacement paths for a prior graph _G<sub>i</sub>_ such that \(G_i\equiv_{1\text{-WL}}H\).

## A.4 Maximum Flow

Next, we show that Maximum Flow can be solved in near-linear time in our model, slightly improving over existing worst-case algorithms \[CKL<sup>+</sup>22, vdBCP<sup>+</sup>23, vdBLL<sup>+</sup>21, vdBLN<sup>+</sup>20\]. Towards this end, we again argue that 1-WL equivalent graphs admit the same maximum flow. We note that this also improves over a result from \[AM13\] where the same is shown for 2-WL.

