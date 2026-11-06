Applying theorem 4.1 to (_R,z_) gives \(m(R)\le 2m(F)\) and hence \(\mathbb{P}_\mathsf{U}(y\in I)\ge 1/3\). Therefore, if _z_ exists and \(r\ge 2\),

\(\mathbb{P}_\mathsf{G}(y\text{selected})<\frac{1}{r+1}\le\frac{1}{3}\le\mathbb{P}_\mathsf{U}(y\in I).\)

If there is no nonleaf neighbour, _T_ is a star with centre _y_. Its only maximal independent sets are {_y_} and _L_, so the uniform marginal of _y_ is 1/2, while the greedy marginal is 1/(_r_+1)_\<_1/2.

The remaining case is a support vertex with exactly one pendant leaf. This is where we compare exact permutation fibres.

**Lemma 4.4** (One pendant leaf)**.** _Assume the diameter is at least_ 3 _and r_=1_. Let x be the unique leaf neighbour of y, so locally x-y-z and_ deg(_y_)=2_. Then the greedy law on T is not uniform on_ M(_T)._

_Proof._ Let<tbc>

\(R=T-\{x,y\},F=R-z=T-N[y].\)

<tbc>Fix any \(A\in\mathcal{M}(F)\) and set \(I_y=\{y\}\cup A\). Define

\(I_x=\left\{\begin{array}{ c c }
\{x\}\cup A, & \text{if}A\text{contains a neighbour of}z\text{in}R, \\
\{x,z\}\cup A, & \text{otherwise.}
\end{array}\right.\)

Both are maximal independent sets. Indeed, _I<sub>y</sub>_ is maximal because _A_ is maximal in _F_ and _y_ dominates _x_ and _z_. If _A_ dominates _z_, then _A_ is maximal in _R_, so \(\{x\}\cup A\) is maximal in _T_; if _A_ does not dominate _z_, then \(A\cup\{z\}\) is independent and maximal in _R_, so \(\{x,z\}\cup A\) is maximal in _T_.

Let \(\sigma\) be the transposition of the vertex labels _x_ and _y_, applied entrywise to an order. It is a bijection on all vertex orders. We compare fibres using theorem 2.1.

Suppose first that _A_ dominates _z_, so \(I_x=\{x\}\cup A\). For every \(\pi\in\mathcal{F}_T(I_x)\), the swapped order \(\sigma\pi\) lies in F_<sub>T</sub>(I<sub>y</sub>_). To see this, note first that in \(\pi\) the outside vertex _y_ can only be certified by its target neighbour _x_ among \(\{x\}\cup A\), so \(x\prec_\pi y\); after swapping, \(y\prec_{\sigma\pi} x\), certifying the outside leaf _x_ for target _I<sub>y</sub>_. The outside vertex _z_ is certified in \(\pi\) by some neighbour in _A_ because _x_ is not adjacent to _z_; that same witness remains earlier after the swap. Every other outside vertex lies in _F_\\_A_ and is certified by a vertex of _A_, all of which are fixed by \(\sigma\). Thus<tbc>

\(\sigma(\mathcal{F}_T(I_x))\subseteq\mathcal{F}_T(I_y).\)

<tbc>The inclusion is strict. Consider an order beginning _y,z_, then listing all vertices of _A_, then the remaining vertices. By theorem 2.1 it lies in F_<sub>T</sub>(I<sub>y</sub>_). Its swapped order begins _x,z_; both _x_ and _z_ are then accepted, so it cannot have output _I<sub>x</sub>_, which excludes _z_. Since \(\sigma\) is an involution,<tbc>

\(|\mathcal{F}_T(I_x)|<|\mathcal{F}_T(I_y)|.\)

<tbc>Now suppose that _A_ does not dominate _z_, so \(I_x=\{x,z\}\cup A\). The reverse inclusion holds:<tbc>

\(\sigma(\mathcal{F}_T(I_y))\subseteq\mathcal{F}_T(I_x).\)

<tbc>Indeed, for an order in the fibre of _I<sub>y</sub>_, the outside leaf _x_ is certified only by _y_, so after swapping the target vertex _x_ precedes and certifies the outside vertex _y_. Every vertex in _F_\\_A_ is certified by a fixed vertex of _A_, while _z_ is now itself in the target. Again the inclusion is strict. An order beginning _z,y_, then listing _x_, the vertices of _A_, and the remaining vertices belongs to F_<sub>T</sub>(I<sub>x</sub>_); after swapping it begins _z,x_, so _z_ is accepted although \(z\notin I_y\). Hence

\(|\mathcal{F}_T(I_y)|<|\mathcal{F}_T(I_x)|.\)

In either case two maximal independent sets have different fibre cardinalities, so their greedy probabilities differ.

