<tbc>critical shortest paths passing through _v_ is at most as large as this number of such pairs. Using further that \(\mathrm{deg}(v)\le p(v)/\eta\) then implies that<tbc>

\(p(v)\le\mathrm{deg}(v)^2\Delta^{(1+\epsilon^\prime)(t-2)}\le\frac{p(v)^2}{\eta^2}\Delta^{(1+\epsilon^\prime)(t-2)},\)

<tbc>which implies that

\(p(v)\ge\frac{\eta^2}{\Delta^{(t-2)(1+\epsilon^\prime)}}=\Omega(\Delta^{2k-2-(t-2)(1+\epsilon^\prime)-18\epsilon})=\Omega(\Delta^{2k-t(1+3\epsilon^\prime)}).\)

On the other hand, we know that the critical _E_<sup>∗</sup>-respecting shortest paths passing through _v_ correspond to critical paths passing through some \(A\subseteq L_i\) and some \(B\subseteq L_j\) where _L<sub>i</sub>,L<sub>j</sub>_ are the layers shortcut by the component _C_ of _E_<sup>∗</sup> that _v_ belongs to. Due to the maximum degree restriction in _E_<sup>∗</sup>, and the fact that \(v\in M\), we know that \(\sigma:=\mathrm{max}\{|A|,|B|\}\le\Delta^{(\frac{t}{2}+1)(1+\epsilon^\prime)}\). Applying Lemma 3.10, we get that the number of critical paths with one vertex in _A_ and the other in _B_ is \(O((k\ell\sigma\mathrm{log}(n))^{3/2})=O(\Delta^\frac{3t}{4}(1+\epsilon^\prime)+\epsilon^\prime+6\epsilon+1)=O(\Delta^\frac{3t}{4}(1+2\epsilon^\prime))\) since \(\ell=O(r^3)\) and \(r=O(\Delta^{2\epsilon})\). In total, we get that the following inequality must be true<tbc>

\(\Delta^{2k-t(1+3\epsilon^\prime)}\le p(v)\le\Delta^\frac{3t}{4}(1+2\epsilon^\prime).\)

<tbc>This implies that<tbc>

\(2k-t(1+3\epsilon')\le\frac{3t}{4}(1+2\epsilon').\)

<tbc>Rearranging yields that<tbc>

\(\frac{7}{4}(1+3\epsilon')t\ge 2k\Leftrightarrow(1+27\epsilon)t\le\frac{8}{7}k.\)

<tbc>Using \(\epsilon=0.0001\) and assuming that

\(1.01t\le\frac{8}{7}k\)

would imply that the above inequality is violated. Hence, we have proved that no Steiner shortcut of thickness _t_, diameter \(m^{\epsilon^2/k}\), and with \(m^{1+\epsilon^2/k}\) edges can exist if \(1.01\cdot t\le\frac{8}{7}k\) and \(\epsilon=0.0001\).

## 4 Generalized Shortcuts for Congestion and Length

Let us refer to shortcuts in previous sections as _reachability shortcuts_. In this section, we formalize the generalization of reachability shortcut that also preserves congestion and length in Section 4.1. Then, we explain why the construction of these shortcuts would imply algorithmic breakthroughs in parallel algorithms for shortest paths and maximum flow in Section 4.2. For convenience, we assume lengths and capacities are polynomially bounded integers in this section.

### 4.1 Formalization

Here, we define a notion of _length-constrained flow shortcuts_ (LC-flow shortcuts). This is a shortcut added to the graph so that every multi-commodity flow can be routed with approximately the same congestion and length, but all flow paths only require a small number of edges.

To formalize this, we need notation for multi-commodity flows. Let _G_=(_V,E_) be a graph with edge capacity \(c:E\rightarrow\mathbb{R}_{\ge 0}\) and edge length \(\ell:E\rightarrow\mathbb{R}_{\ge 0}\). A _(multi-commodity) flow F_ in<tbc>

