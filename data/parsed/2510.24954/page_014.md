However, according to the definition of \(\vec{u}_j,\vec{u}'_j,\vec{v}_{i^\star}\in\mathcal{B}(r,d)\) (they are the extreme points of a convex hull), we must have \(\vec{u}_j=\vec{u}'_j=\vec{v}_{i^\star}\) for every \(j\in[0,\ell)\), for otherwise \(\vec{v}_{i^\star}=\frac{1}{2\ell}\sum_{j\in[0,\ell)}(\vec{u}_j+\vec{u}'_j)\), contradicting the fact that \(\vec{v}_{i^\star}\) is a extreme point, and contradicting the fact that \(a_{i^\star}\neq b_{i^\star}\).

This section is intended to prove that a normalized Steiner shortcut cannot have a large efficiency.

**Lemma 3.8.** _Fix a_ \(k\ge 2,\epsilon>0\)_. Let_ \(G\in\mathcal{G}_k\) _and_ \(G'=(V\cup V',E\cup E')\) _be a t-thick Steiner shortcut for G, where_ \(t\le(1-\epsilon)k\)_. Any normalized shortcut set_ \(E'_{i,j}\subseteq E'\) _has efficiency at most_ \(\Delta^{k-1-\epsilon}\).

_Proof._ Suppose that \(E'_{i,j}\) has efficiency greater than \(\Delta^{k-1-\epsilon}\). Begin by deleting all Steiner vertices from \(E'_{i,j}\) whose degrees are at least \(\Delta^{1+\epsilon}\), and let \(E''_{i,j}\) be the resulting edge set. Notice that according to Lemma 3.7, these vertices have efficiency at most \(\Delta^k/\Delta^{1+\epsilon}=\Delta^{k-1-\epsilon}\). According to Lemma 3.6, the efficiency of \(E''_{i,j}\) is at least as large as that of \(E'_{i,j}\).

Recall that the efficiency of \(E''_{i,j}\) is the ratio of the number of \(E''_{i,j}\)-respecting critical shortest paths to \(|E''_{i,j}|\). Thus, there must exist an edge \(e\in E''_{i,j}\) such that at least \(\Delta^{k-1-\epsilon}\) different \(E''_{i,j}\)-respecting critical shortest paths use _e_, and moreover, use _e_ as the _first_ edge in \(E''_{i,j}\). Due to the _t_-thickness of \(E''_{i,j}\), every path in \(E''_{i,j}\) has length at most \(t\le(1-\epsilon)k\), which, with the degree bound \(\Delta^{1+\epsilon}\), implies that the total number of paths in \(E''_{i,j}\) using _e_ as the first edge is at most

\(\Delta^{(t-1)(1+\epsilon)}\le\Delta^{((1-\epsilon)k-1)(1+\epsilon)}<\Delta^{k-1-\epsilon}.\)

By the pigeonhole principle, there must be two \(E''_{i,j}\)-respecting critical shortest paths \(\Pi_1,\Pi_2\) that take the same route through \(E''_{i,j}\), beginning with edge _e_. This implies that \(\Pi_1,\Pi_2\) share the same vertices \(v_i\in L_i\) and \(v_j\in L_j\). Notice that _v<sub>i</sub>,v<sub>j</sub>_ must also be in the two corresponding critical paths in _G_, which follows from the uniqueness of critical paths (Lemma 2.5). By the definition of the normalized Steiner shortcut \(E'_{i,j}\), \(j\ge i+k\), and by the limited intersection property of Lemma 2.5, this implies that \(\Pi_1,\Pi_2\) are not distinct paths, but associated with the _same_ critical pair in _P_, a contradiction.

## 3.2 G_<sub>k</sub>_ Needs Thick Steiner Shortcuts--Proof of Theorem 3.1

_Proof of Theorem 3.1._ Select \(G\in\mathcal{G}_k=\mathcal{G}_k(c,d)\), where _c_=3_,d_=20000. Let _m_ and _n_ be the number of edges and vertices in _G_, where \(m=exp(\omega(klogk))\). Suppose there exists a Steiner shortcut \(G_+=(V\cup V_+,E\cup E_+)\) for _G_ with \(|E_+|\le m^{1+\epsilon_0^2/k}\) edges and diameter \(m^{\epsilon_0/k}\), for a sufficiently small constant \(\epsilon_0=\epsilon_0(c,d)\). We will deduce a contradiction. Recall from Definition 2.6 that we have<tbc>

\(m=O(Nk\ell\Delta)\le r^{k\cdot f(c,d)},\)

<tbc>where _f(c,d_) is a constant depending on _c,d_. We set \(\epsilon_0<1/f(c,d)\), so<tbc>

\(|E_+|=m^{1+\epsilon_0^2/k}\le m\cdot r^{\epsilon_0}.\)

<tbc>We now substitute for _G_<sub>+</sub> a normalized shortcut graph \(G'=(V\cup V',E\cup E')\), where \(E'\bigcup_{i,j}E'_{i,j}\) is the union of less than \((k\ell)^2\) normalized shortcuts \(E'_{i,j}\) from _L<sub>i</sub>_ to _L<sub>j</sub>_. By Lemma 3.4, \(|E'|<(k\ell)^2|E_+|\) and \(G'\) has diameter upper bounded<tbc>

\(k\cdot m^{\epsilon_0/k}=O(k\cdot r^{\epsilon_0\cdot f(c,d)})\le O(k\cdot r^{c/2})<k\ell.\)

<tbc>Since the diameter is less than the number of layers of _G_ (which is \(k\ell\)), every critical pair must be connected by a critical shortest path \(\Pi\) that uses some \(E'\) edge, and therefore must be \(E'_{i,j}\)-respecting for at least one \(E'_{i,j}\). Recall from Definition 2.6 that the number of critical pairs is<tbc>

\(\Omega\left(\frac{N\Delta^kr^{dk}}{(r+1)^{dk}}\right)=\Omega(m/k\ell)\cdot\Delta^{k-1}=\Omega(m)\cdot\Delta^{k-1-\frac{2c}{d}}.\)

