**Input:** _A_, _b_, basis _F_ with circuit _F<sub>q</sub>_, sampling times _T_<sub>1</sub>_,...,T<sub>d</sub>_, shots _M_, tolerance \(\varepsilon\), expansion size _m_, maximum size _S_<sub>max</sub>

\(\hat{b}\leftarrow Fb;\mathcal{S}\leftarrow\emptyset\)

**For** _k_=1_,...,d: (Phase 1: quantum sampling)_

prepare _e_<sup>-_iAT<sub>k</sub>_</sup>|_b_〉, apply _F<sub>q</sub>_, and measure _M/d_ times; let B be the observed indices

\(\mathcal{S}\leftarrow\mathcal{S}\cup\text{FILTER}(\mathcal{B})\)

solve \(\hat{A}[\mathcal{S},\mathcal{S}]y=\hat{b}[\mathcal{S}];r\leftarrow\hat{b}-\hat{A}\text{Embed}(y,\mathcal{S})\)

**If** \(\|r\|\le\varepsilon\)**: return** _F_<sup>†</sup>Embed(_y,_S) **End if**

**End for**

**While** \(\|r\|>\varepsilon\) and |S|_\<S_<sub>max</sub>_: (Phase 2: classical expansion)_

add to S the _m_ admissible indices outside S with the largest |_r<sub>z</sub>_|

solve \(\hat{A}[\mathcal{S},\mathcal{S}]y=\hat{b}[\mathcal{S}];r\leftarrow\hat{b}-\hat{A}\text{Embed}(y,\mathcal{S})\)

**End while**

**return** _F_<sup>†</sup>Embed(_y,_S)

_Proof._ By substituting _b=Ax_<sup>∗</sup> into the Galerkin condition, we obtain \(\langle v,A(x^*-x_\mathcal{S})\rangle=0\) for all \(v\in V_\mathcal{S}\). Hence _x_<sub>S</sub> is the _A_-orthogonal projection of _x_<sup>∗</sup> onto _V_<sub>S</sub>. The second statement follows because \(V_\mathcal{S}\subseteq V_{\mathcal{S}^\prime}\).

Lemma 1 is the classical Céa property \[14\]. For general Hermitian systems one can instead minimize a projected cost function on _V_<sub>S</sub>, as in variational formulations \[4, 15\] and in the solver of Ref. \[9\]. For positive-definite systems the Galerkin solution is simpler: it minimizes the energy-norm error, requires only the principal submatrix \(\hat{A}[\mathcal{S},\mathcal{S}]\), and its error does not increase on nested sets.

### 2.4 A practical solver for positive-definite systems

Algorithm 1 summarizes the variant used in Secs. 4 and 5. Phase 1 measures Krylov states in the basis _F_ with a classical Galerkin solve after each state. Phase 2 is an optional classical expansion that adds the indices with the largest residual components. The function FILTER removes indices at which the solution vanishes by symmetry or constraint, such as a parity rule or a zero mode. A filter must retain every potentially nonzero solution coefficient; discarding physically admissible modes invalidates the coverage bounds. The sampling times may be taken from a uniform grid, whose outcome law approaches the dephased law of Theorem 7 at the rate given by Lemma 9, or from the heuristic schedule of Algorithm 2. The latter is motivated in Sec. 3.2 but carries no separate guarantee.

## 3 Energy-norm guarantees for Galerkin reconstruction

For the positive-definite case of Sec. 2.3, an expectation bound in the energy norm follows directly from Lemma 1. Throughout this section the measurement basis is {|_z〉<sub>F</sub>_}, _x_<sup>∗</sup>=_A_<sup>-1</sup>_b_ with \(\|b\|=1\), \(\hat{x}_z=\langle z|_Fx^*\rangle\), and \(\lambda_\mathrm{min}\), \(\lambda_\mathrm{max}\) are the extreme eigenvalues of _A_. For sampling times _T_<sub>1</sub>_,...,T<sub>d</sub>_ with _M/d_<tbc>

**Algorithm 1:** Sample-based Krylov solver for positive-definite systems

