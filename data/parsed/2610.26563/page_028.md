<tbc>For a prior square base of dimension _b_ and multiplication count _r<sub>b</sub>_, we use the padding-free recursive model

\(\xi\big(p,q,pq^{log_br_b}\big)=q^{3-log_br_b}.\) (152)

It agrees with _k_ tensor levels at _q=b<sup>k</sup>_ and provides an optimistic comparison at other dimensions. The base algorithms and their sources are listed in  4. The model applies the base separately to each of the _p_ products, giving the reference count _pq_<sup>log<sub>_b_</sub>_r<sub>b</sub>_</sup>.

## Search algorithm.

We searched for constructions using several algorithms: randomized greedy selection, replacement of tripartitions, search over discretized exponents, and linear and mixed-integer programming. We retain the feasible constructions found by these algorithms. The following describes the joint search over tripartition sets and exponents used for the comparisons.

For balanced families, the candidates are the (3_N_)!/(_N_!)<sup>3</sup> tripartitions in _B<sub>N,N,N</sub>_. A local update removes a random subset of the current family and scans the candidates in random order to refill it. A candidate is accepted only when the three part projections remain injective and a feasible pair of grid exponents (_a<sub>t</sub>,b<sub>t</sub>_) is available, with _c<sub>t</sub>_=-_a<sub>t</sub>-b<sub>t</sub>_. The procedure periodically starts from the empty family and occasionally accepts a lower-scoring family to explore other choices. Stored constructions also supply starting families.

For a nonexact construction and a requested retained fraction \(0<\vartheta<1\), we use \(\mathcal{Q}=\mathcal{Q}_{\le 0}\) from Definition 19 and maximize \(pn^{3N}/\rho_{\mathcal{S},\mathcal{Q}}(n)\). For each candidate, we recompute _c_<sub>Q</sub>(R_<sub>ijk</sub>_) for every mixed product not annihilated by centering. Let _g_ be the smallest remaining degree and _h_<sub>0</sub>=-min_<sub>t</sub>a<sub>t</sub>_-min_<sub>t</sub>b<sub>t</sub>_-min_<sub>t</sub>c<sub>t</sub>_. A candidate with remaining mixed products is eligible when

\(\theta=\frac{g}{g+h_0}\ge\vartheta.\) (153)

Updating an exponent pair changes the required correction sets, each of which is counted only once. With the tripartitions fixed, linear and mixed-integer programming provide further exponent choices. After each such refinement, we recompute \(\mathcal{Q}_{\le 0}\) and check the attained fraction before accepting the candidate.

The weighted search instead maximizes _p_, since one aggregate always costs (_n_+2)<sup>3_N_</sup>. Weighting eliminates all replicated products, so only nonreplicated mixed products constrain its grading. Each tripartition set is evaluated with both embeddings, and each construction remains eligible at all weaker accuracy requirements. For incomplete tripartitions, the code also supports local replacement with objective \(\sum_tn^{\omega|G_t|/3}\) at trial values of \((n,\omega)\), and mixed-integer selection from an explicitly enumerated candidate set.

## Exploration budget.

The systematic weighted exploration covers _N_=1,2,3,4, exactness, and target fractions 1/2,1/3,1/4, together with an unrestricted class explored at height bounds 6 and 12. Each height bound uses two grid spacings, 1 and 1/2, and two random restarts, with 160 local updates per start. For corrected constructions, we use _N_=2,3,4, the same two grids, and target fractions 1/2,1/3,1/4,1/7,1/13; the last two explore the unrestricted comparison. The local dimensions used in the objective are (3,12,126), (3,8,25), and (3,7,11), respectively. A standard start has 80 local updates; additional optimization of selected families uses up to 600.

## Verification and selection.

Every saved construction uses exactly represented rational exponents and is checked against all centered mixed products. An independent set-based enumeration checks the selected tripartitions and inclusion-exclusion coefficients. The factor-generation tests compare the resulting trilinear forms with the target and the predicted residual; small cases additionally admit a full dense coefficient- tensor comparison. The figure checks independently recompute multiplication counts, attained accuracy fractions, and plotted coordinates from the saved tripartitions, exponents, and corrections. Reproducing the comparisons therefore does not require repeating the search. All saved feasible constructions remain available, and the selected ones are evaluated at every integer local dimension in the plotted range.

If a grading suppresses every non-diagonal product surviving centering, including replicated products, no corrections are needed:

\(\underline{R}\left(\oplus_{t=1}^m\left\langle n^{|V_t|},n^{|W_t|},n^{|U_t|}\right\rangle\right)\le(n+1)^d.\) (154)

