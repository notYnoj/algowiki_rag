### 3.2 Schedule mixtures and a multiscale heuristic

A long uniform step aliases the high eigenvalues, while a short step does not dephase the low ones. An explicit mixture of candidate schedules has the following coverage property.

**Lemma 10** (Schedule mixtures)**.** _Let_ T<sub>1</sub>_,...,T<sub>r</sub> be complete time schedules with outcome laws q_<sup>(1)</sup>_,...,q_<sup>(_r_)</sup>_, and allocate equal total shots to each schedule. The outcome law of the mixture satisfies_

\(q^\mathrm{mix}=\frac{1}{r}\sum_{j=1}^rq^{(j)}\ge\frac{q^{(j)}}{r}\text{\textit{for every j}}.\)

By Corollary 3, the sufficient budget of the mixture is at most _r_ times that of its best constituent for the same essential set. This compares sufficient bounds, not observed stopping times. Times that occur in several constituents are kept with multiplicity. Algorithm 2 instead selects isolated, logarithmically spaced times. It does not contain the candidate fixed-step schedules, and Lemma 10 does not apply to it. We use it as an empirical heuristic. Its lower time scale \(\pi/\lambda_\mathrm{max}\) avoids aliasing of the highest eigenvalues, and its upper scale \(2\pi/\lambda_\mathrm{min}\) resolves the lowest eigenvalues, which dominate \(\hat{x}\) through the weights \(1/\lambda\) of Eq. (7).

## 4 Geometric formulation

In this section we formulate the solver for elliptic problems on a general Riemannian cross section. We first state the geometric method as a sequence of steps. We then show that the guarantees of Sec. 3 apply to the resulting matrices and classify the approximations that a realization requires. An interpretation of the sampling in terms of Green’s functions is given in Appendix B. Elliptic, lens-shaped, and curved ducts appear at the end of the section as concrete examples.

### 4.1 The geometric method

Let \(\Omega\) be a cross section, and let \(\Phi:R\rightarrow\Omega\) be a coordinate map from a simple coordinate domain _R_, such as a rectangle, a strip, or a quarter rectangle. The map induces a metric _g<sub>ij</sub>_ on _R_. The geometric method consists of five steps.

1. _Coordinates_. Choose \(\Phi\) such that the wall of \(\Omega\) is mapped to coordinate lines of _R_. Conformal maps are preferred in two dimensions (Proposition 12), and orthogonal tube coordinates in curved vessels.

2. _Weak form_. Write the physical problem in the invariant weak form (18). The metric enters only through \(\sqrt{g}\) and _g<sup>ij</sup>_.

3. _Reference operator and basis_. Split the discrete matrix as _A=A_<sub>0</sub>+_V_ , where _A_<sub>0</sub> is a reference operator whose eigenbasis _F_ has an efficient quantum circuit. For a rectangle in conformal coordinates with a constant stiffness coefficient, _A_<sub>0</sub> is the flat stiffness matrix and _F_ is a sine or cosine transform. All mode coupling is then contained in _V_ .

4. _Sampling and reconstruction_. Measure Krylov states in the basis _F_ (Sec. 2.2) with a schedule of Sec. 3.1 or 3.2, apply a filter that encodes the symmetries of \(\Omega\), and reconstruct by the Galerkin solve of Eq. (5).

5. _Approximation_. Replace the exact metric, domain, or circuit by approximations of Class I or Class II (Sec. 4.7).

Steps 1-3 define a discrete model, which already includes discretization and any coordinate truncation. Step 5 separates further model and sampler approximations. Physical accuracy requires control of all these contributions.

