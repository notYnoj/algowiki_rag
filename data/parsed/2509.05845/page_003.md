## 3. Transfer Matrix Framework and Main Results

The fundamental observation underlying our approach is that for fixed (_k,q_), the chromatic counts \(P(\mathcal{C}_n^{(k)},q)\) can be expressed as traces of powers of a finite transfer matrix.

**Theorem 3.1.** _For fixed parameters_ (_k,q), there exists a finite matrix A<sub>k,q</sub> such that_ \(P(\mathcal{C}_n^{(k)},q)=\mathrm{tr}(A_{k,q}^n)\)_. Consequently, the sequence_ \(n\mapsto P(\mathcal{C}_n^{(k)},q)\) _satisfies a linear homogeneous recurrence with constant coefficients._

_Proof._ We use a window automaton of length _k_: a state is a legal _k_-tuple \((c_i,\dots,c_{i+k-1})\in\{0,\dots,q-1\}^k\) with \(c_{j+1}\neq c_j\) for all _j_. A transition \((c_i,\dots,c_{i+k-1})\rightarrow(c_{i+1},\dots,c_{i+k})\) is allowed if and only if \(c_{i+k}\notin\{c_{i+k-1},c_i\}\). This yields a finite directed graph with adjacency matrix _A<sub>k,q</sub>_. On a cycle, _q_-colorings correspond to closed walks of length _n_, hence \(P(\mathcal{C}_n^{(k)},q)=\mathrm{tr}(A_{k,q}^n)\). Since _A<sub>k,q</sub>_ is fixed, the power-sum sequence \(\mathrm{tr}(A_{k,q}^n)\) is a finite C-linear combination of \(\lambda^n\) over the distinct eigenvalues \(\lambda\) of _A<sub>k,q</sub>_, establishing the linear recurrence property. □

_Remark_ 3.1. For _q_=3 and general _k_, the window has at most \(3\cdot 2^{k-1}\) states since adjacent entries must differ, and color-rotation symmetry often reduces the effective order substantially.

Before presenting the main results for _k_=3, we establish the foundational theorems upon which our analysis depends.

**Theorem 3.2** (Cayley-Hamilton theorem)**.** _Let A be an_ \(n\times n\) _matrix over any commutative ring, and let_ \(\chi_A(\lambda)=\mathrm{det}(\lambda I-A)\) _be its characteristic polynomial. Then_ \(\chi_A(A)=0\).

**Theorem 3.3** (Skolem-Mahler-Lech theorem)**.** _Let_ \((u_n)_{n\ge 0}\) _be a linear recurrence sequence over a field of characteristic zero. Then the zero set_ \(Z=\{n\ge 0:u_n=0\}\) _is the union of a finite set and finitely many arithmetic progressions._

The Skolem-Mahler-Lech theorem follows from the foundational work of Skolem (1934) \[20\], Mahler (1935) \[15\], and Lech (1953) \[14\], with modern expositions available in Everest et al. \[9\].

For the specific case _k_=3 and _q_=3, we obtain detailed results depending on the parity of _n_. For odd _n_ (no diameter edges), the transfer matrix block-diagonalizes under color-rotation symmetry. The characteristic polynomial factors as

\(\chi_A(\lambda)=(\lambda^2-\lambda-1)(\lambda^2+\lambda+1)(\lambda^3+\lambda^2+1)^2,\)

yielding seven distinct eigenvalues with some occurring at higher algebraic multiplicities due to the squared cubic factor.

This spectral structure allows us to derive an exact closed-form expression for the chromatic counts when _n_ is odd, as established in the following theorem.

**Theorem 3.4** (Exact closed form for odd _n_)**.** _For k_=3 _and odd n,_<tbc>

\(P(\mathcal{C}_n^{(3)},3)=L_n+2\mathrm{cos}\big(\frac{2\pi n}{3}\big)+2s_n+2,\)

<tbc>_where L<sub>n</sub> is the Lucas sequence L_<sub>0</sub>=2_,L_<sub>1</sub>=1_,L<sub>n</sub>=L_<sub>_n_-1</sub>+_L_<sub>_n_-2</sub>_, and the sequence_ \((s_n)_{n\ge 0}\) _is defined by_

\(s_n:=r^n+u^n+\bar{u}^n,\)

