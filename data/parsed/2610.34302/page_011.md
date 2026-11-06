By Claim 2.4, for each fixed level _i_, at most one pair (_i,p_) is mapped to any given edge of \(E_s^\star\). By Claim 2.5, such pairs occur at no more than 5 levels for each edge. Therefore,

\(|E_s|\le\sum_{i=0}^L|E_s^i|\le 5|E_s^\star|.\)

Summing over all sources \(s\in P\) gives \(|E|\le 5|E^\star|\).

## 2.5 Logarithmic Bicriteria Approximation.

**Lemma 2.6.** _Let_ (_P,_d) _be a metric space of n points and let_ \(\alpha\ge 1\)_. Let G_=(_P,E_) _be the graph returned by Algorithm 2.4. Then G is an_ \((\alpha,\beta')\)_-bicriteria_ 8(ln_n_+1)_-approximation, where_

\(\beta'=(1+\delta)(\alpha+2)+2=\alpha+5+\frac{2}{\alpha}.\)

_Proof._ Let _G<sup>⋆</sup>_=(_P,E<sup>⋆</sup>_) be a sparsest \(\beta'\)-navigable graph. Fix a source point \(s\in P\) and a level _i_. Write \(E_s^\star=\{(s,x)\in E^\star\}\) for the outgoing edges of _s_ in _G<sup>⋆</sup>_. Write \(\rho_i=r_i/(\alpha+2)\), and let \(\mathcal{G}_i=\{(C_j,p_j)\}_j\) be the greedy ball cover at level _i_ in the order in which the clusters are produced.

Define

\(\mathcal{U}_{i,s}=\bigcup\{C_j|(C_j,p_j)\in\mathcal{G}_i,p_j\in A_i(s)\}.\)

Let \(\mathcal{F}_{i,s}=\{B(c,\rho_i)\cap\mathcal{U}_{i,s}|c\in P\}\), and let OPT<sub>_i,s_</sub> be the optimum set-cover value for the instance (U<sub>_i,s_</sub>,F<sub>_i,s_</sub>).

**Claim 2.7.** _For every source s and level i,_<tbc>

\(|E_s^i|\le(lnn+1)\text{OPT}_{i,s}.\)

<tbc>_Proof of claim._ Write the output of Algorithm 2.2 at level _i_ as<tbc>

\((C_1,p_1),(C_2,p_2),\dots,(C_m,p_m),\)

<tbc>in the order in which the clusters are produced. Let _U_<sup>(_j_)</sup> be the set of points that remain uncovered immediately before the _j_-th greedy step. Thus<tbc>

\(C_j=U^{(j)}\cap B(p_j,\rho_i),\)

<tbc>and the greedy choice of _p<sub>j</sub>_ implies that, for every center \(c\in P\),

\(|C_j|=|U^{(j)}\cap B(p_j,\rho_i)|\ge|U^{(j)}\cap B(c,\rho_i)|.\) (2.1)

Define \(J_{i,s}=\{j\in[m]|p_j\in A_i(s)\}\). Then \(E_s^i\) contains exactly one edge (_s,p<sub>j</sub>_) for each \(j\in J_{i,s}\), and<tbc>

\(\mathcal{U}_{i,s}=\bigcup_{j\in J_{i,s}}C_j.\)

<tbc>For every point \(v\in C_j\), define its weight by<tbc>

\(y_v=\frac{1}{|C_j|}.\)

