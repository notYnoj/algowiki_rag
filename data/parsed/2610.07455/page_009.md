dummy variables so that _x_ must receive the image of \(\alpha(x)\) under the same automorphism. Thus all original variables follow one common symmetry of _R_.

Every assignment \(\pi\circ\alpha_j\) satisfies and violates exactly the same _R_-constraints as \(\alpha_j\). Bob can therefore append the instance from the informal lemma in the ideal reduction above. If _b<sub>j</sub>_=0, an automorphic image of \(\alpha_j\) satisfies the final instance. If _b<sub>j</sub>_=1, every assignment satisfying Bob’s constraints violates _C<sub>j</sub>_. A streaming algorithm for satisfiability would therefore give a one-way protocol for INDEX_<sub>m</sub>_, proving the \(\Omega_R(\text{NRD}_n(R))\) lower bound for core relations. Reducing an arbitrary relation to its core gives the characterization in Section 5.

For the sake of brevity, we next discuss the techniques that underlie the Exact-CSP results. For a discussion of the sparsification and minimization results, we encourage the reader to look at Section 6.

## 2.3 Exact-CSP

We now explain why exact optimization requires a stronger pinning construction than satisfiability. Let _d_ be the _degree_ of the indicator function of the core relation. Informally, this is the largest number of coordinates that occur together in a monomial of its polynomial representation. Our result gives an _O<sub>R</sub>(n<sup>d</sup>_log_n_) upper bound and a matching \(\Omega_R(n^d)\) lower bound up to the logarithmic factor. The formal statement is Theorem 7.1, and the formal definition of degree is in Section 3.5.

As before, we first reduce the relation to its core. The upper bound stores the coefficients of the low-degree polynomial representing the value of the instance. For the lower bound, the ideal reduction again asks Bob to hard-pin complete assignments. It is tempting to use Lemma 4.4 for this purpose. But that lemma is not strong enough here. It describes assignments that satisfy every pinning constraint, whereas an optimal assignment may violate some pinning constraints in order to satisfy more of Alice’s constraints. We therefore first describe the ideal reduction and then explain how a stronger pinning construction ensures that such a violation cannot improve the objective.

**Example 2.4** (Degree of CUT)**.** For CUT on the domain {0,1}, the indicator is **1**<sub>CUT</sub>(_x,y_)=_x+y_-2_xy_. Its degree is therefore 2.

**Example 2.5** (Degree of NAE)**.** Let \(R_\text{NAE}\subseteq\{0,1\}^3\) contain the tuples whose three entries are not all equal. Its indicator is **1**<sub>_R_NAE</sub>(_x,y,z_)=_x+y+z-xy-xz-yz_. Thus _R_NAE has degree 2 even though its arity is 3.

### Upper bound.

The upper bound follows directly from the polynomial representation. Kol, Paramonov, Saxena, and Yu \[KPSY23\] give the Boolean version. They write the value of an instance as a polynomial in the variables and store its coefficients. Each arriving constraint adds one fixed low-degree polynomial to this coefficient table. We use the same idea over an arbitrary finite domain, using the value indicators from Section 3.5 in place of Boolean variables.

**Example 2.6** (The upper bound for CUT)**.** Consider a stream of edges defining a CUT-instance. By the expansion above, an arriving edge {_x<sub>u</sub>,x<sub>v</sub>_} contributes _x<sub>u</sub>+x<sub>v</sub>_-2_x<sub>u</sub>x<sub>v</sub>_ to the value of every assignment. The algorithm adds these three coefficients to its table. After the stream, the sum of the stored terms is exactly the number of edges cut by every assignment. There are only _O(n_<sup>2</sup>) possible terms, and their coefficients use _O_(log_n_) bits on a simple instance. The algorithm may then try every assignment, evaluate the stored polynomial, and return its maximum. Thus Exact-CSP(CUT) uses _O(n_<sup>2</sup>log_n_) space.

