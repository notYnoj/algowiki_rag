## 4 Polynomial Multiplication and the Complete Graph Bound

We now use the entropy inequality to prove the complete graph bound. The proof compares two estimates for a symmetric spectral profile of polynomial multiplication: interpolation gives an upper bound, while two degenerations force growth as the input lengths increase. We first define the tensors and their profiles, then establish discrete concavity and shifted tripling. A coordinate-by-coordinate growth argument will turn these inequalities into the upper bound of Theorem 1.1.

### 4.1 Polynomial tensors and spectral profiles

We extend the polynomial tensor and symmetrized profile used by OpenAI \[Ope26a, Section 4\] from two polynomial inputs to _n_-1 independent inputs. The interpolation rank bound remains linear in the sum of their lengths. We describe the value of a spectral point on each edge tensor, then average over permutations of all _n_ legs. This gives a symmetric numerical profile whose growth controls the spectral value of the complete graph tensor. Each input remains a separate tensor leg throughout the construction.

**Definition 4.1** (polynomial multiplication tensor)**.** Let \(n\ge 3\) be an integer, and let _a_<sub>1</sub>_,...,a_<sub>_n_-1</sub> be positive integers. Put \(D=1+\sum_{j=1}^{n-1}(a_j-1)\). The _polynomial multiplication tensor_ is the complex _n_-th order tensor

\(\mathcal{C}_n(a_1,\dots,a_{n-1})=\sum_{i_1=0}^{a_1-1}\cdots\sum_{i_{n-1}=0}^{a_{n-1}-1}e_{i_1}^{(a_1)}\otimes_C\cdots\otimes_Ce_{i_{n-1}}^{(a_{n-1})}\otimes_Ce_{i_1+\cdots+i_{n-1}}^{(D)}.\)

Its first _n_-1 legs are the input legs, and its last leg is the output leg. Thus its dimension vector is (_a_<sub>1</sub>_,...,a_<sub>_n_-1</sub>_,D_).

For \(1\le j\le n-1\), write an input polynomial as \(f_j(x)=\sum_{i=0}^{a_j-1}u_{j,i}x^i\). Contracting the first _n_-1 tensor legs against these coefficient vectors gives the coefficient vector of \(\prod_{j=1}^{n-1}f_j(x)\). This interpretation keeps every input in a separate leg.

The next lemma is the many-input version of the interpolation and output-flattening argument in \[Ope26a, Equation (4.2)\].

**Lemma 4.2** (rank of polynomial multiplication)**.** _For every integer_ \(n\ge 3\) _and all positive integers a_<sub>1</sub>_,...,a_<sub>_n_-1</sub>,<tbc>

\(\mathrm{R}\big(\mathcal{C}_n(a_1,\dots,a_{n-1})\big)=1+\sum_{j=1}^{n-1}(a_j-1).\)

<tbc>_Proof._ Put \(D=1+\sum_{j=1}^{n-1}(a_j-1)\), and choose distinct complex numbers \(\xi_1,\dots,\xi_D\). For every integer \(1\le r\le D\), let<tbc>

\(L_r(x)=\prod_{1\le s\le Ds\neq r}\frac{x-\xi_s}{\xi_r-\xi_s},\)

<tbc>and let \(c_r\in\mathbb{C}^D\) be its coefficient vector, in increasing order of degree. Lagrange interpolation states that every polynomial _f_ of degree at most _D_-1 satisfies \(f(x)=\sum_{r=1}^Df(\xi_r)L_r(x)\). Apply this identity to \(f=\prod_{j=1}^{n-1}f_j\), whose degree is at most _D_-1. For \(1\le j\le n-1\) and \(1\le r\le D\), define the evaluation vector<tbc>

\(v_{j,r}=\sum_{i=0}^{a_j-1}\xi_r^ie_i^{(a_j)}.\)

