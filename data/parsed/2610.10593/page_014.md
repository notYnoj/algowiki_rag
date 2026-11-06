_Proof._ Unfold the graph recursively. Its levels strictly decrease, so the resulting tree is finite. An induction from the leaves proves that all copies of a graph node have identical complete split distributions: the recursion uses only its parameters and its children’s distributions. Its local entropies and matrix-size coefficients are therefore also identical. Mass propagation, regional sums before minimization, and leaf contributions are linear in the incoming mass. Summing the masses of these copies consequently gives the same result as their separate evaluation. No tensor variables are identified by this parameter sharing.

## A.2 Rational logarithm enclosures

**Lemma 2** (Outward dyadic logarithms)**.** _The logarithm routine in the accompanying verifier returns rational numbers_ \(L_-(x)\le log_2x\le L_+(x)\) _for every positive rational input x. The enclosure uses only integer arithmetic._

_Proof._ Write _x_=2_<sup>k</sup>z_ with integer _k_ and \(1\le z<2\), using exact comparisons of integers. Let _S_=2<sup>192</sup>, _m_=74, and \(t=(z-1)/(z+1)\in[0,1/3)\). The identity

\(lnz=2\sum_{j=0}^{m-1}\frac{t^{2j+1}}{2j+1}+\mathcal{R}_m,0\le\mathcal{R}_m\le\frac{2t^{2m+1}}{(2m+1)(1-t^2)}\)

follows by integrating the geometric series, and bounding every denominator in its remaining positive terms by 2_m_+1.

The implementation brackets _t_ and _t_<sup>2</sup> on the grid _S_<sup>-1</sup>Z. If \(P_j^-/S\) and \(P_j^+/S\) bracket _t_<sup>2_j_+1</sup>, and _V_<sup>-</sup>_/S,V_<sup>+</sup>_/S_ bracket _t_<sup>2</sup>, the integer updates<tbc>

\(P_{j+1}^-=\left\lfloor\frac{P_j^-V^-}{S}\right\rfloor,P_{j+1}^+=\left\lceil\frac{P_j^+V^+}{S}\right\rceil\)

<tbc>preserve this invariant. Each summand is divided by 2_j_+1 with outward rounding. After _m_ summands, the upper tail in units of _S_<sup>-1</sup> is bounded by<tbc>

\(\left\lceil\frac{2P_m^+S}{(2m+1)(S-V^+)}\right\rceil.\)

<tbc>The denominator is positive since \(t\le 1/3\) and the grid bounds give _V_<sup>+</sup>_\<S_. This produces integers _A_<sub>-</sub>_,A_<sub>+</sub> enclosing _S_ln_z_. The same calculation at _z_=2 produces integers _B_<sub>-</sub>_,B_<sub>+</sub> enclosing _S_ln2, with _B_<sub>-</sub>_\>_0. Therefore

\(k+\frac{1}{S}\left\lfloor\frac{SA_-}{B_+}\right\rfloor\le log_2x\le k+\frac{1}{S}\left\lceil\frac{SA_+}{B_-}\right\rceil.\)

If _z_=1, the routine returns the exact integer _k_.

All subsequent interval operations are exact rational operations with outward endpoints. In particular, if \(x_i\in[a_i,b_i]\), then

\(min_ix_i\in[min_ia_i,min_ib_i].\)

For a nonnegative rational vector _v_ of mass _s_, define \(\mathcal{H}(v)=-\sum_iv_ilog_2v_i\), with 0log<sub>2</sub>0=0. The compatibility calculation uses H(_v_)-H((_s_))=_sH(v/s_) when _s\>_0, and zero when _s_=0. This identity also covers mixtures whose mass exceeds one.

