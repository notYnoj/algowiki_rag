## 5.3. Reaching _H_

At time \(T=(1-n^{-\alpha_\mathrm{gr}})n\) we have reached a graph _H_<sub>gr</sub> on 4_n_<sub>gr</sub>:=|_V_(0)|-4(\(n-n^{1-\alpha_\mathrm{gr}})=n^{1-\alpha_\mathrm{gr}}(1\pm bn^{\alpha_\mathrm{gr}})\) vertices, where \(bn^{\alpha_\mathrm{gr}}=o(1)\) (with _n_<sub>gr</sub> vertices in each part). From now on we write \(p_\mathrm{gr}:=n^{-\alpha_\mathrm{gr}}\). Then in addition, we have that \(V_O^{X+Y}(H_\mathrm{gr})=(1\pm 2b^{1/3}p_\mathrm{gr}^{-1})np_\mathrm{gr}/2\) and \(V_O^{X-Y}(H_\mathrm{gr})=(1\pm 2b^{1/3}p_\mathrm{gr}^{-1})np_\mathrm{gr}/2\). With out loss of generality, we may assume that \(|V_O^{X+Y}(H_\mathrm{gr})|\le V_O^{X-Y}(H_\mathrm{gr})\). Then we obtain _H_ from _H_<sub>gr</sub> by removing a matching _M_<sub>gr</sub> so that \(|V_O^{X+Y}(H)|=|V_O^{X-Y}(H)|\) and \(|V_E^{X+Y}(H)|=|V_E^{X-Y}(H)|\). (Note that this step is only necessary when _n_ is odd. Indeed, since T<sup>-_A_<sup>∗</sup></sup> satisfies these parity requirements whp by Theorem 4.11, and going from T<sup>-_A_<sup>∗</sup></sup> to _H_<sub>gr</sub> only removes a matching, when _n_ is even the parity requirements are not modified by this process.) In particular, we want to take wrap-around edges with an even vertex in _X+Y_ and an odd vertex in _X-Y_ , and we need to take at most 2_b_<sup>1/3</sup>_n_ edges of this type to achieve equality. Note that in T choosing any vertex \(v\in X-Y\) with coordinate of modulus at least _t_<sub>0</sub>/4 there are at least _t_<sub>0</sub>/4 vertices in _Y_ whose coordinate dictates a wrap-around edge with _v_ such that the _X+Y_ and _X-Y_ coordinates both have modulus at least _t_<sub>0</sub>/4. Half of these will use an even vertex in _X+Y_ and an odd vertex in _X-Y_ . So in T every vertex \(v\in[-t_0,-t_0/4]^X\cup[t_0/4,t_0]^X\) is in at least _t_<sub>0</sub>/8 edges of the required type. It follows, since this is a degree-type property, that in _H_<sub>gr</sub> every such vertex is in at least \((1-2b^{1/3})\frac{t_0p_\mathrm{gr}^3}{8}\) such edges. Since this process is only required for odd _n_ we have that pair degrees are at most one and so the choice of one such edge for a particular vertex in _X_ destroys at most three choices for a different vertex in _X_. Thus since \(2b^{1/3}n\checkmark(1-2b^{1/3})\frac{3t_0p_\mathrm{gr}^3}{8}\) we may greedily choose edges to fix the parity disparity. By restricting to edges that only contain vertices with modulus _t_<sub>0</sub>/4 or larger, this does not affect any of the properties we maintained during the random greedy matching process too much. In particular, following the discussion above we are now in the position to prove Theorem 3.28.

Proof of Theorem 3.28. We start by recalling (as per Section 3.1.1) that \(\alpha_G=n^{-10^{-8}}\), _p_<sub>gr</sub>=_n_<sup>-10<sup>-25</sup></sup> and _b=O(n_<sup>-10<sup>-7</sup></sup>). From the random greedy matching process, with high probability we obtain _H_<sub>gr</sub> such that the following all hold:

(i) every T -valid subset \(S\subseteq V(\mathcal{T})\) satisfies<tbc>

<tbc>\(|V(H_\mathrm{gr}[S])|=(1\pm 2b^{1/3}p_\mathrm{gr}^{-1})|S|p_\mathrm{gr},\)<tbc>

(ii) for every \(v\in V(H_\mathrm{gr})\) and every open or closed T -valid tuple (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>), we have<tbc>

<tbc>\(|E_{H_\mathrm{gr}}(v,S_1,S_2,S_3)|=(1\pm 2b^{1/3}p_\mathrm{gr}^{-3})|E_\mathcal{T}(v,S_1,S_2,S_3)|p_\mathrm{gr}^3,\)<tbc>

(iii) for every \(i\in[c_g]\),

<tbc>\(|\mathcal{Z}_{i,e,H_\mathrm{gr}}^+(\alpha,\beta,\gamma)|:=\left\{\begin{array}{ c c }
(1\pm 2b^{1/3}p_\mathrm{gr}^{-12})|\mathcal{Z}_{i,e,\mathcal{T}}^+(\alpha,\beta,\gamma)|p_\mathrm{gr}^{12} & \text{if}e\text{is a bad edge,} \\
O\left(k_it_1p_\mathrm{gr}^{12}\right) & \text{if}\alpha=0,\beta=1,\gamma=3, \\
0 & \text{otherwise.}
\end{array}\right.\)<tbc>

