<tbc>with indices understood cyclically, i.e., L(_n_+1)=L(1) and R(0)=R(_n_). Initially, the global state is \(\otimes_{p=1}^nU_0|000\rangle_{\mathsf{L}(p)\mathsf{M}(p)\mathsf{R}(p)}\). For _t_=1,2_,...,T_, each vertex _p_ does

(1) swap the content of L(_p_) with R(_p_-1), and<tbc>

(2) apply _U<sub>t</sub>_ to \(\mathsf{L}(p)\otimes\mathsf{M}(p)\otimes\mathsf{R}(p)\).

Finally, each vertex _p_ measures \(\Pi\) on \(\mathsf{L}(p)\otimes\mathsf{M}(p)\otimes\mathsf{R}(p)\) and outputs the observed label.

Each iteration of Steps 1 and 2 is called a _round_. This model assumes that vertices have a consistent orientation of the _n_-cycle, i.e., they agree on which side is the left one. An algorithm that uses this information can only be faster than an undirected algorithm, therefore lower bounds within Definitions 3.1 and 3.2 also hold for undirected models.

## 4. Proof of Theorem 1

In this section, we formally state our two main technical contributions, Theorems 2 and 3, and use them to prove Theorem 1: any _T(n_)-round quantum-PN algorithm that _c_-colors _n_-cycles with \(T(n)\le n/2-2\) must produce a monochromatic edge with non-zero probability. The choice of the quantum-PN algorithm can depend on _n_, in other words the nodes have knowledge of _n_.

Let us introduce some terminology first. For a quantum-PN algorithm A , the _support_ of A is the set of vectors \(\vec{a}\in\bigcup_{n\ge 3}\Sigma^n\) that A outputs with non-zero probability. For \(r\in\mathbb{N}\), an _r-block_ is a set of _r_ consecutive natural numbers. We say that the _r_-block _B_ is _monochromatic_ in \(\vec{a}=(a_1,\dots,a_n)\in\Sigma^n\) if and only if all _a<sub>i</sub>_ for \(i\in B\) have the same value. In particular, a coloring algorithm that errs with zero probability is such that all output vectors containing a monochromatic 2-block have probability zero.

First, we prove that any 1-round quantum-PN algorithm produces a monochromatic (_n_-2)- block with non-zero probability, no matter the number of output labels.

**Theorem 2.** _Let_ \(n\ge 4\) _an integer. Any 1-round quantum-PN algorithm has a monochromatic_ (_n_-2)_-block in its support._

Then, we prove that any _T(n_)-round _c_-coloring algorithm can be turned into a 1-round algorithm where nodes output values from \([d]^{4T}\times[c]\) and produces no monochromatic (2_T(n_)+2)- block.

**Theorem 3.** _Let_ \(r\in\mathbb{N}\) _and_ \(n\ge 4\) _and_ \(T\le\lfloor\frac{n-r}{2}\rfloor\)_. Suppose there is a T-round quantum- PN algorithm_ \(\mathscr{A}=(U_0,U_1,\dots,U_T,\Pi)\) _of local dimension_ \(d\in\mathbb{N}\) _with outputs in_ \(\Sigma\) _and no monochromatic r-block in its support. Then there exists a 1-round algorithm_ B _with outputs in_ \([d]^{4T}\times\Sigma\) _and no monochromatic_ (2_T+r)-block in its support._

_Proof of Theorem 1._ Fix \(n\ge 4\), and let A be a quantum-PN algorithm that properly _c_-colors the directed _n_-cycle in \(T(n)\le n/2-1\) rounds, i.e., it has \(\Sigma=[c]\) and no monochromatic 2-block in its support. By Theorem 3, there is a one-round quantum-PN algorithm B with output \([d]^{4T}\times[c]\) with no monochromatic (2_T(n_)+2)-block in its support. By Theorem 2, the algorithm B produces a monochromatic _r_-block with non-zero probability, where _r=n_-2 when _n_ is even, and _r=n_-3 when _n_ is odd. In particular, B has a monochromatic _r_-block in its support for all \(r\le n-2\). Hence, we must have 2_T(n_)+2_\>n_-2, meaning that \(T(n)>\lfloor n/2\rfloor-2\).

## 5. No One-Round Quantum Symmetry Breaking (Theorem 2)

In this section, we prove that symmetry breaking is not possible with probability one in one-round of quantum-PN. Recall that _n_, the number of nodes in the cycle, is fixed first and the one-round quantum-PN can depend on it, i.e., nodes know the length of the cycle.

