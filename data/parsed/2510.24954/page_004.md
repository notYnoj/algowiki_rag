**Conjecture 2** (Steiner Shortcut Conjecture)**.** _Let G_<sup>∗</sup>=(_V,E_<sup>∗</sup>) _be the transitive closure of a directed graph G_=(_V,E). There exists a graph_ \(G_+=(V\cup V_+,E\cup E_+)\) _such that_

• _G_<sub>+</sub> _captures the transitive closure of G, i.e., for all_ \((u,v)\in V\times V\)_, v is reachable from u in G iff it is reachable from u in G_<sub>+</sub>.<tbc>

• \(|E_+|=\widetilde{O}(|E|)\);<tbc>

• _G_<sub>+</sub> _has_ polylog(_n_) _diameter, i.e.,_ \(\forall(u,v)\in E^*\), dist<sub>_G_<sub>+</sub></sub>(_u,v_)=polog(_n_).

We are not the first to propose the use of Steiner points. Berman, Bhattacharyya, Grigorescu, Raskhodnikova, Woodruff, and Yaroslavtsev \[BBG<sup>+</sup>14\] proved that if _G_ is a DAG with dimension _d_, meaning there is a reachability-preserving embedding into the oriented hypergrid \[_n_\]_<sup>d</sup>_, then it has a diameter-2 graph _G_<sub>+</sub> with _O(n_log_<sup>d</sup>n_) shortcuts. However, the prior work on Steiner shortcuts \[BBG<sup>+</sup>14, Ras10\] has no bearing on Conjecture 2.

## 1.2 Contributions

The purpose of this paper is to explore Conjecture 2 and the power of Steiner vertices more generally in constructing shortcuts. We are _uncertain_ about the truth of Conjecture 2 and our goal is to raise it as an open problem. Although Conjecture 2 can be refuted using known techniques when the size of the Steiner shortcut is limited to \(|E_+|\le|E|^{1-\epsilon}\) for a constant \(\epsilon\) (see Section A), once we permit \(|E_+|=\widetilde{O}(|E|)\), all known techniques become ineffective.

Indeed, our main contribution is to carefully demonstrate why the lower bounds of Hesse \[Hes03\], Huang and Pettie \[HP21\], Lu, Williams, Wein, and Xu \[LVWX22\], Williams, Xu, and Xu \[VXX24\], and Hoppenworth, Xu, and Xu \[HXX25\] fail catastrophically when Steiner vertices are allowed. These results are presented in Section 2.

Our second result, presented in Section 3, can be viewed as either partially refuting Conjecture 2 or identifying the crucial property that the shortcut for Conjecture 2 must satisfy. Specifically, we show that the shortcut must have a sufficiently large _thickness_, defined as follows.

**Definition 1.2** (Thickness)**.** Let \(G_+=(V\cup V_+,E\cup E_+)\) be a Steiner shortcut graph for _G_=(_V,E_). We say _G_<sub>+</sub> has _thickness t_ (or is _t-thick_) if every path in _G_<sub>+</sub> has at most _t_-1 consecutive Steiner vertices from _V_<sub>+</sub>.

\begin{tabular}{cccc}
Shortcut Size & Diameter & Construction Time & Notes/Citation \\
\multirow{5}{*}{\(\widetilde{O}(n)\)} & \(O(\sqrt{n})\) & \(\widetilde{O}(m\sqrt{n})\) & \[UY91\] \\
 & \(\widetilde{O}(n^{2/3})\) & \(\widetilde{O}(m)\) & \[Fin20\] \((\widetilde{O}(n^{2/3})\) depth) \\
 & _n_<sup>1/2+_o_(1)</sup> & \(\widetilde{O}(m)\) & \[JLS19\] (_n_<sup>1/2+_o_(1)</sup> depth) \\
 & _O(n_<sup>1/3</sup>) & \(\widetilde{O}(mn^{1/3})\) & \[KP23, KP22a, KP22b\] \\
 & \(\widetilde{\Omega}(n^{1/6})\) & & \[HP21\]; see also \[Hes03\] \\
 & \(\widetilde{\Omega}(n^{1/4})\) & & \[BH23b\] \\
\multirow{5}{*}{\(\widetilde{O}(m)\)} & \(O(n/\sqrt{m})\) & \(\widetilde{O}(m^{3/2})\) & \[UY91\] \\
 & _O(n_<sup>2/3</sup>_/m_<sup>1/3</sup>) & \(\widetilde{O}(m^{7/6}n^{1/6})\) & \[KP23, KP22a, KP22b\] \\
 & \(\widetilde{\Omega}(n^{1/11})\) & & \[HP21\]; see also \[Hes03\] \\
 & \(\widetilde{\Omega}(n^{1/8})\) & & \[LVWX22\] \\
 & \(\widetilde{\Omega}(n^{1/5})\) & & \[VXX24\] \\
 & \(\widetilde{\Omega}(n^{2/9})\) & & \[HXX25\] \\
\end{tabular}

1: Upper and lower bounds on diameter specialized to \(\tilde{O}(m)\)- and \(\tilde{O}(n)\)-size shortcuts.

