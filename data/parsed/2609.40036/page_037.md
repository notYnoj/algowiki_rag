## Likelihood ratio.

A valid original trajectory containing _F_ determines its forcing schedule uniquely. At a state with _v_ free vertices and _k_ pending prescribed edges, let<tbc>

\(N=\genfrac(){pt}{2}{v}{2},N^\circ=\genfrac(){pt}{2}{v-2k}{2},A=|\mathscr{A}_t|,A^\circ=\#\{\text{available outside pairs}\}.\) (161)

<tbc>The original-to-planted likelihood ratio on that trajectory is<tbc>

\((T)_s\prod_\text{forced times}\frac{1}{A}\prod_\text{unforced times}\frac{A^\circ}{A}.\) (162)

<tbc>In the complete graph, this product telescopes to

\(p_\text{ref}=\frac{(T)_s2^s}{(n)_{2s}}=(1+o(1))n^{-s},\) (163)

independently of the schedule. For example, the identity follows by writing each outside ratio as (_v_-2_k_)(_v_-2_k_-1)/(_v(v_-1)); its numerator cancels successive outside-vertex counts.

Put \(\Delta=C_Dn^c\). At a forced step, replacing _N_ by _A_ changes the logarithm of the product by \(O_D(\Delta/v)\). At an unforced step write _A=N-M_ and \(A^\circ=N^\circ-M^\circ\). Since<tbc>

\(M-M^\circ\le 2k\Delta,M^\circ\le(v-2k)\Delta/2,\) (164)

<tbc>we have<tbc>

\(\left|log\frac{A^\circ/A}{N^\circ/N}\right|=O_D(k\Delta/v^2).\) (165)

<tbc>Summing these estimates shows uniformly over valid trajectories that<tbc>

\(\frac{Pr_\text{original}(trajectory)}{Pr_\text{planted}(trajectory)}=p_\text{ref}exp(O_D(sn^c/m))=(1+o(1))n^{-s}.\) (166)

<tbc>_Validity of the planted process._ Let _U_ be its unforced matching. For any prescribed matching _U_<sub>0</sub> of _t=O_(log_n_) edges outside _V(F_),

\(Pr_\text{planted}(U_0\subseteq U)\le(1+o(1))n^{-t}.\) (167)

To see this, fix the forcing schedule and apply the matching potential on the _n_-2_s_ outside vertices. Forced steps leave that potential unchanged; every unforced step has missing degree at most \(\Delta\), and at least _m_-2_s_ outside vertices remain. The accumulated error is \(exp(O_D(t\Delta/(m-2s)))=1+o(1)\). Uniform artificial completion of the outside matching gives (167); averaging over schedules preserves it. No assertion about the girth of a possibly invalid trajectory is needed for this degree bound.

Set _J=H+F_. If a forced edge _xy_ is unavailable when inserted, then (_J-xy_)+_U_ contains a simple _x-y_ path of length at most _g_-2. Such a path must use at least one edge of _U_, since \(\text{girth}(J)\ge g\). We bound all these paths by their _last_ unforced edge.

For precision, give each unforced edge in a path weight 1_/n_, and each edge of _J-xy_ weight one. The total weight of nonbacktracking prefixes of length _a_ is at most _C<sub>D</sub>(D_-1)_<sup>a</sup>_. At a vertex outside _V(F_), arrival along an old edge leaves at most _D_-2 old continuations and one unforced port, whose destinations have total weight at most one; arrival along an unforced edge leaves _D_-1 old continuations and no second unforced port. At a vertex of _V(F_) there are at most _D_-1 old<tbc>

