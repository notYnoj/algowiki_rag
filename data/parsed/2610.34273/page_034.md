**Corollary 4.13** (edge exponents below two thirds)**.** _For every integer_ \(n\ge 5\),

\(\tau(K_n)\le\frac{n}{2(n-1)}<\frac{2}{3}.\)

_In particular, the existence question in \[CVZ19, Question 1.3.1\] has an affirmative answer for every_ \(n\ge 5\)_. Moreover,_ \(lim_{n\rightarrow\infty}\tau(K_n)=1/2\).

_Proof._ Divide the upper bound in Theorem 4.11 by |_E(K<sub>n</sub>_)|=_n(n_-1)/2. The strict inequality _n/_(2(_n_-1))_\<_2/3 is equivalent to 3_n\<_4_n_-4, or _n\>_4. For the limit, both bounds in the theorem give

\(\frac{\lfloor n^2/4\rfloor}{\genfrac(){pt}{2}{n}{2}}\le\tau(K_n)\le\frac{n}{2(n-1)}.\)

The two bounding quantities tend to 1/2, which proves the claim.

For odd _n_, the upper bound still exceeds the maximum-cut lower bound by 1/4. Section 5 studies whether further combinations of the polynomial constructions can close this gap. It specifies the allowed operations and constructs a numerical certificate that limits every derivation in that system.

## 5 An Operational Barrier for the Polynomial Method

The polynomial constructions in Section 4 give the complete-graph upper bound _n_<sup>2</sup>/4 in Subsection 4.5. We now examine whether their further combinations can improve this threshold. Amanov, van den Berg, and Zuiddam \[ABZ26, Section 5\] proved that the three-leg polynomial ingredients cannot yield a matrix multiplication exponent below 9/4, even when the ingredients are combined repeatedly. We extend their symmetric certificate to _n_ legs. Its threshold is _n_<sup>2</sup>/4, and its growth on polynomial tensors matches the diagonal exponent in Subsection 4.4.

The proof separates the tensor constructions from their numerical analysis. We first define formal expressions and a resource form of simultaneous separation. We then specify the permitted derivations and verify that each rule describes a valid tensor degeneration. A comparison function supplies the numerical inequalities needed by these rules; extending it to expressions gives the barrier. The certificate is monotone for this explicitly generated relation on expressions. It is not asserted to be a spectral point on Tens_<sub>n</sub>_(C). Throughout this section, \(n\ge 3\) is an integer. We allow arbitrary positive integer edge dimensions in the auxiliary expressions, but state the final barrier for GT<sub>2</sub>(_K<sub>n</sub>_), in the same normalization as Theorem 1.1.

### 5.1 Formal expressions and polynomial resources

A formal expression records how a tensor is built, including which coordinates are shared in a partial direct sum. We begin with polynomial atoms whose support treats every leg symmetrically. This convention will allow the tripling rule to retain the original shared coordinates in all three output blocks.

**Definition 5.1** (polynomial atoms)**.** A vector **x**=(_x_<sub>1</sub>_,...,x<sub>n</sub>_) of positive integers is _admissible_ if, with \(M=max_{1\le i\le n}x_i\),<tbc>

\(\sum_{i=1}^nx_i=2M+n-2.\)

