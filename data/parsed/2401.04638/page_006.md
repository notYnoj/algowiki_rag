\(\bullet\) There are _k_ paralleling links between _a_ and _o_, i.e., \(E_{a,o}=\{\{a,o\}_i:1\le i\le k\}\).<tbc>

\(\bullet\) Finally, let \(E=E_1\cup E_2\cup E_3\cup E_A\cup E_o\cup E_{a,o}\), and \(\forall\{u,v\}\in E_1\cup E_2\cup E_3:c((u,v))=c((v,u))=1\), otherwise _c_((_u,v_))=_c_((_v,u_))=3.

Moreover, we define demands _D_ as follows: for each \(i\in\{1,\dots,n\}\), it has demands \(D\left(v_i,b_i\right)=\delta_{v_i}\) and _D(v<sub>i</sub>,a<sub>i</sub>_)=3, where \(\delta_{v_i}=3\) denotes the degree of _u<sub>i</sub>_ in _G<sub>U</sub>_ of _I_. We note that the graph _G<sub>D</sub>_ induced by demands _D_ in our construction is also a 3D-matching.

Finally, for every \(u,v\in V\) , there is a reconfigurable (bi- directed) link {_u,v_} with capacities: _c_((_u,v_))=_c_((_u,v_))=3. However, due to the splittable and segregated model (\(\tau=\) SS), only reconfigurable links {_u,v_} that have _D(u,v_)+_D(v,u)\>_0 need to be considered for reconfiguration.

Next, we will prove:

\(\bullet\) If _G<sub>U</sub>_ has a vertex cover \(U^*\subseteq U\) with \(|U^*|\le k\), then the constructed instance \(I'\) has the minimized congestion \(\lambda\le 1\);<tbc>

\(\bullet\) If any vertex cover \(U^*\subseteq U\) in _G<sub>U</sub>_ has \(|U^*|\ge\rho\cdot k\), where the ratio \(\rho\in(1,2)\), then the constructed instance \(I'\) has the minimized congestion \(\lambda\ge min\{\rho,1.2\}\).

We first do some analysis of the constructed instance \(I'\). Due to _b_=1 and |_V_<sub>1</sub>|=_n_, the reconfiguration (matching) _M_ can contain at most _n_ reconfigurable links. Let \(M_1\subseteq M\) denote the selected reconfigurable links between _V_<sub>1</sub> and _A_ and \(M_2\subseteq M\) denote the selected reconfigurable links between _V_<sub>1</sub> and _B_, where \(M_1\cap M_2=\emptyset\) and \(M_1\cup M_2=M\).

We first claim that the set of nodes \(V^*\subseteq V_1\) contained in _M_<sub>2</sub> must imply a vertex cover _U_<sup>∗</sup> in the graph _G<sub>U</sub>_, where \(\forall v_i\in V^*\Longrightarrow u_i\in U^*\), otherwise, the maximum load factor is \(\lambda\ge 1.2\).

If _V_<sup>∗</sup> implies a vertex cover \(U^*\subseteq U\) in _G<sub>U</sub>_, it is easy to note that the maximum load on the static edges in \(E_1\cup E_2\cup E_3\) is at most one. If \(v_i\in V^*\), then its demand _D(v<sub>i</sub>,b<sub>i</sub>_)=3 is sent on the reconfigurable (directed) link (_v<sub>i</sub>,b<sub>i</sub>_) with _c_((_v<sub>i</sub>,b<sub>i</sub>_))=3 , otherwise _D(v<sub>i</sub>,b<sub>i</sub>_)=3 must go through the corresponding three paralleling paths consisting of static links: \((v_i,v_{ij},v'_{ij},b_i)\), where each _j_ indicates an edge \(\{u_i,u_j\}\in E_U\) in _G<sub>U</sub>_.

Reverversely, we assume that _V_<sup>∗</sup> does not imply a vertex cover in the graph _G<sub>U</sub>_. We know at least one edge {_u<sub>i</sub>,u<sub>j</sub>_} is not covered in _G<sub>U</sub>_, which also means \(v_i,v_j\notin V^*\). There are at most 5 edge-disjoint paths between {_v<sub>i</sub>,v<sub>j</sub>_} and {_b<sub>i</sub>,b<sub>j</sub>_} on static network _G_, which provides total capacities of 5. Since _D(v<sub>i</sub>,b<sub>i</sub>_)=3 and _D(v<sub>j</sub>,b<sub>j</sub>_)=3, then 6 units of demands need to be sent on these 5 edge-disjoint paths, which indicates the maximum load \(\lambda\ge 1.2\).

After showing that _M_<sub>2</sub> must imply a vertex cover _U_<sup>∗</sup> in _G<sub>U</sub>_, otherwise \(\lambda\ge 1.2\), then we discuss the relationship between the size |_M_<sub>2</sub>| and the maximum load \(\lambda\). If _G<sub>U</sub>_ has a minimum vertex cover _U_<sup>∗</sup> of the size _k_, then the load on any static link in \(E_o\cup E_a\cup E_{a,o}\) is at most one, which implies the congestion \(\lambda\le 1\). But if all vertex covers having size \(\ge\rho\cdot k\) in _G<sub>U</sub>_, where \(\rho\in(1,2)\), then it must have the congestion \(\lambda\ge\rho\).

Given an arbitrary vertex cover \(U^*\subseteq U\) in _G<sub>U</sub>_, where \(|U^*|\ge\rho\cdot k\), let \(V^*\subseteq V\) denote the corresponding nodes in _G_<tbc>

<tbc>with \(|V^*|\ge\rho\cdot k\). Since each \(v_i\in V^*\) must be included in the reconfigurable links _M_<sub>2</sub> not _M_<sub>1</sub>, then its demand _D(v<sub>i</sub>,a<sub>i</sub>_)=3 must be sent through static links. Thus, there are at least \(3\cdot\rho\cdot k\) units of demands that must be transferred from _o_ to _a_. Furthermore, there are _k_ paralleling static links _E<sub>a,o</sub>_ between _a_ and _o_, where \(c:\vec{E}_{a,o}\mapsto 3\). Clearly, the maximum load \(\lambda\) on directed links in _E<sub>a,o</sub>_ is at least \(\rho\).

Since the minimum vertex cover problem on cubic graphs is APX-complete \[33\], there must exist a \(\rho\in(1,2)\) s.t., the minimum vertex cover problem on cubic graphs cannot be approximated better than \(\rho\) unless _P=NP_. Therefore, the above reduction implies that our problem cannot be approximated better than \(min\{1.2,\rho\}\), which further implies APX-hardness. Since our problem can be approximated by two, then it is in APX-complete.

It remains to investigate the approximation lower bound for unsplittable and segregated routing. In Theorem 2, we reduce the MCRN problem with \(\tau=\) US into a sub-problem, which belongs to the min-congestion multi-commodity unsplittable flow problem. Now, we can formally show the connection between these two problems in terms of approximability.

**Theorem 5.** _There is an approximation factor-preserving reduction from the min-congestion of multi-commodity unsplittable flow problem to the MCRN problem with_ \(\tau=\) _US. Thus, the lower bound_ \(\Omega\left(logm/loglogm\right)\) _\[34\] on approximating the min-congestion of multi-commodity unsplittable flow problem is also an approximation lower bound for the MCRN problem with_ \(\tau=\) _US._

_Proof:_ We prove it by giving a factor-preserving reduction. Given an instance _I_=(_V,E,c,D_) of the min-congestion of multi-commodity unsplittable flow problem (Definition 2), we will construct an instance \(I'=(V',E',\mathcal{E}',c',D')\) of the MCRN problem with \(\tau=\) US. W.L.O.G., we assume that the minimum value in the capacity function _c_ is one.

We first construct a copy of _I_ contained in \(I'\), s.t., \(V\subset V'\), \(E\subset E'\), \(c\subset c'\) and \(D\subset D'\). In addition, for each node \(v_i\in V\) , we create a node \(v_{i^\prime}\in V'\) and a demand \(d_{i,i^\prime}\in D'\) with \(d_{i,i^\prime}=\alpha\), where \(\alpha>0\) is a very large number. For each node \(v_i\in V\) , we construct a reconfigurable edge \(\{i,i'\}\in\mathcal{E}'\) with capacities \(c'\left((i,i')\right)=\alpha\) and \(c'\left((i',i)\right)=1\), and a static link \(\{i,i'\}\in E'\) having the capacity one on both directions. We finish the construction of \(I'\) after setting the capacities of other unmentioned reconfigurable links in \(\mathcal{E}'\) by one.

Since \(\alpha\) is very large in the instance \(I'\), for each node \(v_i\in V\) , its reconfigurable edge \(\{i,i'\}\in\mathcal{E}\) must be included in the matching _M_, otherwise the min-congestion in \(I'\) after reconfiguration can be as large as \(\alpha\). After that, we cannot add any reconfigurable link into the matching _M_ of \(I'\). Now, the instance \(I'\) equals to the given instance _I_ of the multi- commodity flow problem. Therefore, \(I'\) cannot be approximated better than _I_. \(\blacksquare\)

## IV. NON-SEGREGATED ROUTING MODEL

In this section, we study the MCRN problem under non- segregated routing, where we are particularly interested in un<tbc>

