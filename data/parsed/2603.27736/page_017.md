That is, in a potential adjustment, one is allowed to "delete edges" and to add "node weights" in such a way that _A_\[_i,k_\]+_B_\[_k,j_\]-_C_\[_i,j_\] remains unchanged for all surviving triangles. This use of potential adjustments is akin to that in several shortest-path problems, e.g., the well-known Johnson trick \[71\].

**Definition 2.14** (Potential-Adjusting Reduction)**.** _A_ potential-adjusting 1-to-_N_ reduction in time _T is an algorithm that runs in time T, takes as input a (possibly constrained) Exact Triangle instance_ (_A,B,C_) _of size_ \(n_1\times n_2\times n_3\)_, and returns as output a pair_ (I,T) _where_

• I _is a set of N (possibly constrained) potential adjustments of_ (_A,B,C), and_<tbc>

• \(\mathcal{T}\subseteq[n_1]\times[n_2]\times[n_3]\) _with size_ \(|\mathcal{T}|\le T\),

_so that, for each exact triangle_ (_i,k,j_) _in_ (_A,B,C),_ (_i,k,j_) _appears as an (exact) triangle in an instance in_ I_, or_ \((i,k,j)\in\mathcal{T}\) .

**Remark 2.15.** _An even stricter notion would be to enforce that each exact triangle appears_ either _in_ T _or in_ exactly one _instance in_ I_. This would directly imply reductions between counting versions of the problems as well. It can be checked that all of our reductions can actually achieve this stricter constraint (with some minor modifications here and there)--however, since the reductions are already quite involved we have decided to stick to the simpler Definition 2.14._

## 2.4 Additive Combinatorics

Let \(X,Y\subseteq\mathbb{Z}\) be two finite sets. We write \(X+Y=\{x+y:x\in X,y\in Y\}\) to denote their _sumset_. We also set \(X-Y=\{x-y:x\in X,y\in Y\}\) and \(-X=\{-x:x\in X\}\), and for an integer _x_ we write _X+x=X_+{_x_}. Let _r_<sub>_X+Y_</sub>(_z_) denote the _multiplicity_ of _z_ in the sumset _X+Y_, i.e., the number of representations _z=x+y_ with \(x\in X,y\in Y\), or equivalently, \(r_{X+Y}(z)=|X\cap(z-Y)|\). We occasionally rely on the following two basic facts from additive combinatorics; see e.g. the textbooks \[94, 103\].

**Lemma 2.16** (Plünnecke-Ruzsa Inequality \[81, 84\])**.** _Let X,Y be finite sets with_ \(|X+Y|\le K|X|\)_. Then, letting nY denote the n-fold sumset_ \(Y+\cdots+Y\)_, it holds for all nonnegative integers n,m that:_

\(|nY-mY|\le K^{n+m}|X|.\)

**Lemma 2.17** (Ruzsa’s Triangle Inequality \[85\])**.** _For all finite sets X,Y,Z:_

\(|X+Y|\le\frac{|X+Z||Y+Z|}{|Z|}.\)

We also need the following algorithm to efficiently compute sumsets:

**Lemma 2.18** (Sparse Convolution \[22\])**.** _There is an algorithm that, given sets_ \(X,Y\subseteq\{-u,\dots,u\}\)_, com putes their sumset X+Y along with the multiplicities_ \(r_{X+Y}(\cdot)\) _in deterministic time_ \(|X+Y|\cdot(\mathrm{log}u)^{O(1)}\).

## 2.5 Machine Model

Throughout we consider the Word RAM model with logarithmic word size \(\Theta(\mathrm{log}n)\), where _n_ is the input size. Moreover, for all graph and matrix problems we always only consider weights that are polynomially (i.e., _n_<sup>_O_(1)</sup>) bounded and can thus be stored in _O_(1) machine words. As is the standard in fine-grained complexity, we allow randomized algorithms (that succeed with high probability 1-_n_<sup>-_c_</sup> for an arbitrarily large constant _c_) in hypotheses and reductions.

