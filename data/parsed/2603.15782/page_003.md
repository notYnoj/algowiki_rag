<tbc>following conclusions.

• Taking any fixed \(\varepsilon>0\), we obtain \(O(\sqrt{logn})\)-approximation in \(O(m^{1+\varepsilon})\) time. This approximation factor is the best known for both vertex- and edge balanced separators.<tbc>

• Taking \(\varepsilon=\Theta(1/logn)\), we obtain an _O_(log_n_)-approximation in \(O(T_{maxflow}(m,m)\cdot\text{polylog}(n))\) time. This will be useful if _T_<sub>maxflow</sub>(_m,m_) is ever improved to be near-linear.

## 1.1 Padding bound

**Definition 2.** _Graph_ (_V,E_) _has padding bound_ \(\beta\ge 1\) _if, for every nonnegative edge length vector_ \(\xi\in\mathbb{R}_{\ge 0}^E\) _and every D\>_0_, the shortest-path pseudometric_ \(d(\cdot,\cdot)\) _with edge lengths_ \(\xi_{xy}\) _admits a distribution of partitions into sets of diameter at most D such that_

\(\mathtt{Pr}\left[B(x,\Gamma D)\subseteq P(x)\right]\ge e^{-\Gamma\beta}(x\in V)\)

_where_ \(B(x,r)=\{y\in V:d(y,x)\le r\}\) _is the ball of radius r centered at x, and P(x_) _is the part containing x. Here_ \(\Gamma>0\) _is a fixed absolute constant. We write_ \(\beta(G)\) _for the smallest padding bound of G_=(_V,E)._

_If we restrict to the case of edge length vectors_ \(\xi\in\mathbb{R}_{\ge 0}^E\) _arising from vertex lengths_ \(\xi_v\in\mathbb{R}_{\ge 0}^V\) _(so_ \(\xi_{uv}=\frac{1}{2}\xi_u+\frac{1}{2}\xi_v\)_), we obtain an analogous quantity we call_ \(\beta_v(G)\).

Many existing results are known for these padding bounds. Most are implied by the following results.

**Theorem 3** (Conroy-Filtser \[11\], Theorem 2)**.** _Every K<sub>h</sub>-minor-free graph G has_ \(\beta(G)\in O(logh)\).

**Theorem 4** (\[13, Theorem 1.4\])**.** _Every string graph G has_ \(\beta_v(G)\in O(1)\).

We will prove the following algorithmic result in terms of the padding bound.

**Theorem 5.** _For any_ \(\varepsilon\in[\Theta(1/logn),\Theta(1)]\) _and any constant_ \(c\in(0,1/2)\)_, there is a Monte-Carlo randomized algorithm (succeeding w.h.p.) that, given a graph G_=(_V,E_) _with padding bound_ \(\beta\) _(or with_ \(\beta_v(G)\le\beta\) _in the special case of vertex separators) and polynomially-bounded finite integer element weights w, finds a_ \(\Theta(1)\)_-balanced element cut of size at most_ \(O(OPT_c\cdot\sqrt{\beta}/\varepsilon)\)_, where_ OPT_<sub>c</sub> is the minimum size of a c-balanced element cut. The algorithm runs in time_ \(m^{1+o(1)}n^\varepsilon\text{polylog}(n)\)_. For fixed_ \(\varepsilon>0\)_, this is_ \(O(m^{1+\varepsilon})\).

In particular, by taking any fixed \(\varepsilon>0\) we obtain an \(O(\sqrt{\beta})\) approximation in \(O(m^{1+\varepsilon})\) time.

For comparison, when the partitions in Theorem 2 can be sampled efficiently, a standard polynomial-time LP-based approach \[31\] gives a \(O(\beta)\)-approximation (e.g., a _O_(log_h_)-approximation for _K<sub>h</sub>_-minor-free graphs \[11\]). Theorem 5 improves this to \(O(\sqrt{\beta})\). Moreover, it does not require that the partitions can be sampled efficiently. See table 1 for the direct applications to various graph classes.

<sup>1</sup>The history of this bound is nuanced. A \(O(\sqrt{logg})\)-approximation was claimed in \[29\], but a proof was absent, and one of the explicit claimed theorems is false \[42, Appendix B\]. In the same work, a padding bound of _O_(log_g_) was claimed, but this bound also lacks proof. Ratio _O_(log_g_) also follows from a later work that does include a proof \[11\].

\begin{tabular}{cccccc}
**Class** & **Cut** & **Previous ratio** & **Year** & **Ref** & **This paper** \\
_K<sub>h</sub>_-minor-free & edge, vertex & _O_(log_h_) & 2025 & \[11\] & \(O(\sqrt{logh})\) \\
Genus _g_ & edge, vertex & _O_(log_g_) <sup>1</sup> & 2010 & \[29\] & \(O(\sqrt{logg})\) \\
\multirow{2}{*}{Treewidth tw} & vertex & \(O(\sqrt{logtw})\) & 2005 & \[18\] & \multirow{2}{*}{\(O(\sqrt{logtw})\)} \\
 & edge & _O_(logtw) & 2024 & \[19\] & \\
String graphs & vertex & _O_(1) & 2026 & \[13\] & _O_(1) \\
\end{tabular}

1: Class-dependent ratios of polynomial-time pseudo-approximations for balanced separators.

