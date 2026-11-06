\(+\lambda_2\big(\frac{527}{1728}-\frac{1}{8}\zeta_{12}^{3n}+\frac{2}{27}\zeta_{12}^{4n}-\frac{13}{64}\zeta_{12}^{6n}+\frac{2}{27}\zeta_{12}^{8n}-\frac{1}{8}\zeta_{12}^{9n}\big)\)<br>
\(+\lambda_3\big(\frac{599}{1600}-\frac{4}{25}\zeta_{20}^{4n}+\frac{1}{8}\zeta_{20}^{5n}-\frac{4}{25}\zeta_{20}^{8n}+\frac{1}{64}\zeta_{20}^{10n}-\frac{4}{25}\zeta_{20}^{12n}+\frac{1}{8}\zeta_{20}^{15n}-\frac{4}{25}\zeta_{20}^{16n}\big)\big](q)_3n^{2q-6},\)

_where_ \(\lambda_1\), \(\lambda_2\)_, and_ \(\lambda_3\) _are as in  7.2._

The symmetry in the coefficients of powers of each \(\zeta_r\) in the last _n_<sup>2_q_-6</sup>-term is due to the coefficients’ being real numbers.

_Proof._ There are four types of subspace, of which only Type \(\EuScript{U}_{3\mathrm{b}}^2\) involves calculations that are substantially different from those in Lemma III.3.4. That is where the \(\lambda_i\) arise.

From Section 6, for a subspace determined by equations involving \(\kappa\) pieces, \(\alpha(\EuScript{U};n)\) is a quasipolynomial of degree \(2\kappa-\mathrm{codim}\EuScript{U}\).

**Type** \(\EuScript{U}_2^2\)**:** The subspace U is defined by two move equations involving the same two pieces. There is one such subspace for each of the \(\genfrac(){pt}{2}{q}{2}\) unordered pairs of pieces and _n_<sup>2</sup> ways to place the attacking pieces in U. Since U lies in _k_ hyperplanes, the Möbius function is \(\mu(\hat{0},\EuScript{U})=k-1\). The contribution to _o_<sub>N_k_</sub>(_q;n_) is \(\frac{k-1}{2}(q)_2n^{2q-2}\) so the contribution to \(q!\gamma_2\) is \(\frac{k-1}{2}(q)_2\).

The one-move partial nightrider is an exception, since there is no subspace of this type when _k_=1. Then instead of multiplying the contribution by \(\mu(\hat{0},\EuScript{U})\), we multiply it by 0=_k_-1; i.e., the same multiplier expression.

**Type** \(\EuScript{U}_{3\mathrm{a}}^2\)**:** The subspace U is defined by two move equations of the same slope involving three pieces. There is one subspace of this type for each of the _k_ slopes. The number of points in each subspace is \(\beta^{1/2}(n)\) from Equation (6.1). There are (_q_)<sub>3</sub>/3! ways to choose three partial nightriders, and the Möbius function is 2. Thus we multiply \(\beta^{1/2}(n)\) by \(\frac{2k}{3!}(q)_3n^{2q-6}\) to find that the contribution to _o_<sub>N_k_</sub>(_q;n_) is

\((q)_3\left\{\frac{k}{16}n^{2q-2}+\frac{7k}{48}n^{2q-4}+\frac{k}{32}n^{2q-6}-(-1)^n\big[\frac{k}{16}n^{2q-4}+\frac{k}{32}n^{2q-6}\big]\right\},\)

so that the contribution to \(q!\gamma_2\) is \(\frac{k}{16}(q)_3\) and that to \(q!\gamma_4\) is \(\big[\frac{7k}{48}-(-1)^n\frac{k}{16}\big](q)_3\).

**Type** \(\EuScript{U}_{3\mathrm{b}}^2\)**:** The subspace U is defined by two move equations of different slopes in volving three pieces, say \(\EuScript{U}=\EuScript{H}_{12}^{d/c}\cap\EuScript{H}_{23}^{d^\prime/c^\prime}\). By symmetry it suffices to find the contributions when _d/c_=1/2 and \(d'/c'\in\{2/1,-2/1,-1/2\}\). The total contribution will depend on the piece’s basic move set. We write \(\EuScript{U}=\EuScript{U}^{d^\prime/c^\prime}\) when we need to mention the slope. The Möbius function is \(\mu(\hat{0},\EuScript{U})=1\).

We choose the piece P<sub>2</sub> in _q_ ways, P<sub>1</sub> in _q_-1 ways, and P<sub>3</sub> in _q_-2 ways.

For each value of \(d'/c'\) we calculated the denominators of all vertex coordinates of \([0,1]^{2q}\cap\EuScript{U}\) using Mathematica. That gave us the denominator \(D([0,1]^{2q}\cap\EuScript{U})\) and hence an upper bound on the period of \(\alpha(\EuScript{U};n)\) in each case. Using Mathematica again we found quasipolynomial formulas for the number of placements of the three nightriders, \(\alpha(\EuScript{U};n)\). These formulas were calculated by varying the position of P<sub>2</sub> in the \(n\times n\) grid as _n_ varied in a residue class modulo \(D([0,1]^{2q}\cap\EuScript{U})\). The calculations were carried out for _n_=1_,...,_100, which covers at least five periods in every case. By Theorem 6.1 and the fact that \(\alpha(\EuScript{U};n)\) has degree \(4=2\cdot 3-\mathrm{codim}\EuScript{U}\), there are 2_p_+1 coefficients to determine in \(\alpha(\EuScript{U};n)\); as the periods are bounded by 20

