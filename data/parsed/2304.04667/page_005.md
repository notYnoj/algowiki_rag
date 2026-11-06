## 1.2.1 Unit Node-Capacities

For undirected graphs with unit node-capacities, we obtain the following non-reducibility bound by combining Theorem 1.2 with the natural _O(n_) flow volume bound and the algorithm in Theorem 1.1.

**Theorem 1.3.** _Under NSETH, for any fixed_ \(\varepsilon>0\) _there is no deterministic fine-grained reduction_ <sup>13</sup> _proving an_ \(\Omega(n^{\omega(log_nm,1,1)+\varepsilon})\) _SETH-based lower bound for All-Pairs Max-Flow on undirected graphs with unit node-capacities._

For \(\omega=2\), the bound becomes \(\Omega(mn^{1+\varepsilon})\). A question posed by \[HLSW23\] is whether conditional lower bounds for general algorithms could match their _m_<sup>2-_o_(1)</sup> lower bounds against combinatorial algorithms. Theorem 1.3 conditionally answers this question negatively, for SETH-based results. That said, we observe a SETH lower bound for this setting, which is obtained by a straightforward adaptation of the conditional lower bound in \[AKT20b\] for general node-capacities to the unit node-capacities case, together with a recently developed source-sink isolating gadget \[HLSW23\].

**Theorem 1.4.** _If for some fixed_ \(\varepsilon>0\) _All-Pairs Max-Flow on undirected graphs with unit node- capacities can be solved in time_ \(O(n^2+m^{3/2-\varepsilon})\) _then SETH is false._

## 1.2.2 General node-capacities.

For directed graphs with general node-capacities<sup>14</sup>, we obtain the following non-reducibility bound by combining Theorem 1.2 with the naive algorithm and our new flow volume bounds.

**Theorem 1.5.** _Under NSETH, for any fixed_ \(\varepsilon>0\) _there is no deterministic fine-grained reduction proving an_ \(\Omega(n^{\omega(2,1,1)+\varepsilon})\) _SETH-based lower bound for All-Pairs Max-Flow on directed graphs with node-capacities._

For \(\omega=2\), the bound becomes \(\Omega(n^{3+\varepsilon})\). This result indicates that even when the input graph is dense and directed, the existing _n_<sup>3-_o_(1)</sup> SETH lower bound \[AKT20b\], designed for sparse undirected graphs, is unlikely to be improved.

<sup>13</sup>Similar to existing literature, we rule out black-box Turing reductions. See \[CGI<sup>+</sup>16\] and Section 1.4 in this paper for more formal definitions. <sup>14</sup>The running times of all our algorithms do not depend on the numerical values of the capacities in the input.

\begin{tabular}{ccccccc}
Setting & Dir. & Capacities & SETH

Lower Bounds & Combinatorial

Lower Bounds & Algorithms & Nondeterministic

Algorithm \\
node-cap & no & unit & _m_<sup>3/2</sup>+_n_<sup>2</sup>, **Thm 1.4** & _m_<sup>2</sup> \[HLSW23\] & \(m\cdot T(m)\), **Thm 1.1** & _mn_, **Lma 2.7** \\
 & yes & unit & _mn_ \[KT18\] & _m_<sup>2</sup> \[AGI<sup>+</sup>19\] & \(m^\omega\) \[CLL13\], \(n^2\cdot T(m)\) & _n_<sup>3</sup>, **Lma 2.8** \\
 & no & general & _n_<sup>3</sup> \[AKT20b\] & _m_<sup>2</sup> \[ " \] & \(n^2\cdot T(m)\) & _n_<sup>3</sup>, **Lma 2.8** \\
 & yes & general & _n_<sup>3</sup> \[ " \] & _m_<sup>2</sup> \[ " \] & \(n^2\cdot T(m)\) & _n_<sup>3</sup>, **Lma 2.8** \\
edge-cap & yes & unit & _mn_ & _m_<sup>2</sup> \[ " \] & \(m^\omega\) \[CLL13\], \(n^2\cdot T(m)\) & \(n^{5/2}\sqrt{m}\), **Lma 2.9** \\
 & yes & general & _n_<sup>3</sup> \[KT18\] & _m_<sup>2</sup> \[ " \] & \(n^2\cdot T(m)\) & \\
 & no & general & & & _m_<sup>1+_o_(1)</sup> \[ALPS23\] & \\
\end{tabular}

1: Known algorithms and lower bounds for hard variants of All-Pairs Max-Flow, ignoring subpolynomial factors, and where _T(m_) represents the time of a Max-Flow query. All presented bounds for nondeterministic algorithms are under the assumption that \(\omega=2\).

