_Proof._ Let F<sub>2_w_</sub>=F<sub>2_w_</sub>(_G_) and \(\mathcal{F}_{2w}^w(r)=\mathcal{F}_{2w}^w(G,r)\) for simplicity. It is sufficient to show that the following LP (6) is feasible and has optimal value 0.

\(\mathrm{min}\sum_{F\in\mathcal{F}_{2w}\backslash\mathcal{F}_{2w}^w(r)}y_F\sum_{F\in\mathcal{F}_{2w}e\in F}y_F\le p\forall e\in E(G)\sum_{F\in\mathcal{F}_{2w}}y_F=1y_F\ge 0\forall F\in\mathcal{F}_{2w}\) (6)

The above LP (6) is feasible since G is _SDD_(2_w,p_)-acceptable. For the sake of contradiction, assume that the optimal value of the above LP is _z\>_0. Let \(m>\frac{1}{z}\) be a natural number. Let _G_<sub>1</sub>_,...,G<sub>m</sub>_ be _m_ disjoint copies of _G_ and _r<sub>i</sub>_ be the vertex of _G<sub>i</sub>_ which corresponds to _r_. Let \(G'\) be formed by taking 1-sum of _G_<sub>1</sub>_,...,G<sub>m</sub>_ at _r_<sub>1</sub>_,...,r<sub>m</sub>_. See the following Figure 5 for an illustration:<tbc>

\(\includegraphics{}\)

<tbc>Note that \(G'\in\mathcal{G}\) since G is closed under the 1-sum operation. Let \(\mathcal{F}'_{2w}=\mathcal{F}_{2w}(G')\) be the set of all 2_w_-diameter decompositions of \(G'\). Since G is _SDD_(2_w,p_)-acceptable, then \(G'\) has a \(SDD(G',2w,p)\). Let \(\{g_{F^\prime}\}_{F^\prime\in\mathcal{F}_{2w}(G^\prime)}\) denote such a distribution for \(G'\). Let _G<sub>i</sub>_=(_V<sub>i</sub>,E<sub>i</sub>_) and F<sub>2_w_</sub>(_G<sub>i</sub>_) be the set of all 2_w_-diameter decompositions of _G<sub>i</sub>_ for _i_=1,2_,...,m_.<sup>2</sup> By Lemma 2, the projection of _g_ onto _G<sub>i</sub>_ induces a distribution _g<sup>i</sup>=g(G<sub>i</sub>_) over F<sub>2_w_</sub>(_G<sub>i</sub>_) for _i_=1_,...,m_. Furthermore, since _G<sub>i</sub>_ is an identical copy of _G_ and _g<sup>i</sup>_ is a feasible solution to the LP 6 mentioned above, we have:<tbc>

\(\sum_{F\in\mathcal{F}_{2w}(G_i)\backslash\mathcal{F}_{2w}^w(G_i,r)}g_F^i\ge z\text{for}i=1,2,\dots,m.\)

<tbc>Recall that \(\mathcal{F}_{2w}^w(G_i,r)\) denotes the set of all 2_w_-diameter decompositions of _G<sub>i</sub>_ in which the distance of every vertex in the connected component containing _r_ is at most _w_-1 from it. Let _T<sub>i</sub>_ be the event that, when sampling \(F'\in\mathcal{F}'_{2w}\) according to the distribution _g_, the intersection \(F'\cap E_i\) does not belong to \(\mathcal{F}_{2w}^w(G_i,r)\). From the above discussion, it follows that \(\mathrm{Pr}[T_i]\ge z\). Since \(m>\frac{1}{z}\), we have<tbc>

\(\sum_{i=1}^m\mathrm{Pr}[T_i]\ge z\cdot m>1.\)

<tbc>This implies that the events _T_<sub>1</sub>_,...,T<sub>m</sub>_ are not disjoint, and there exist indices _i,j_ such that \(\mathrm{Pr}[T_i\cap T_j]>0\). Therefore, there exists a \(F'\in\mathcal{F}'_{2w}\), and vertices \(u\in V_i\), \(v\in V_j\) such that:

1. \(g_{F^\prime}>0\),<tbc>

2. _u_ and _v_ are in the connected component containing _r_ in \(G'\backslash F'\),<tbc>

<sup>2</sup>Note that \(\cap_{i=1}^mV_i=\{r\}\).

