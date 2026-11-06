**Monotone sets.** We define monotone sets as follows:

**Definition 2.** _We say that a set_ \(P\subseteq\mathbb{N}\times\mathbb{N}\) _is_ monotone _iff for all_ \(((i,k),(j,l))\in P\times P\)_, we have (i)_ \(i=j\Leftrightarrow l=k\)_; and (ii)_ \(i<j\Leftrightarrow k<l\).

One can observe that

\(\mathrm{LCS}(x,y)=\mathrm{max}_{P\subseteq[n]\times[n]P\text{is monotone}}\sum_{(i,j)\in P}\mathbf{1}[x_i=y_j]\)

**The Block-LIS problem.** The Block-LIS problem was defined in \[ANSS21\]<sup>1</sup>. In Block-LIS, the main input consists of _n_ blocks of (at most) _k_ elements each, and each block can contribute at most one of its elements to a subsequence. Formally, for an integer block sequence \(z\in\mathbb{N}^{n\times k}\), Block-LIS(_z_) is the length of a maximal sub-sequence \(\mathsf{OPT}\unknown\{(w_1,z_w)\}_{w\in[n]\times[k]}\) such that OPT is monotone.

**Other notations.** Fix vectors \(a,b\in\mathbb{R}^n\), then min(_a,b_) (respectively max(_a,b_)) is defined, as the vector of minimums (respectively, maximums) for each (_a<sub>i</sub>,b<sub>i</sub>_) pair. Also, the notation \(\oplus\) means the direct sum.

## 2.2 Main technique - Block-LIS reduction

Our construction boils down to a formulation of the LCS problem as a (larger) LIS problem, and solve the LIS problem directly. Our reduction at its core is reminiscent to ideas introduced in \[HS77, AG87\], with two important differences:

1. We provide a simplified approach by direct "black-box" reduction to a LIS problem which is then solved directly. In particular, we reduce to the Block-LIS problem. As a result, the entire construction and proof takes roughly 1.5 pages.<tbc>

2. We show that the number of "matching pairs" is always bounded by \(2n\cdot\mathrm{LCS}(x,y)\) using norm inequalities, implying the linear runtime from Lemma 4.3 in \[ANSS21\].

In particular, we restate the following Definition and Theorem:

**Definition 3.** _\[ANSS21\] For_ \(\alpha\ge 1\) _and_ \(\beta>0\)_, an_ \((\alpha,\beta)\)_-approximation_ \(\hat{q}\) _of a quantity q is an_ \(\alpha\)_- multiplicative and_ \(\beta\) _additive estimation of q, i.e.,_ \(\hat{q}\in[q/\alpha-\beta,q]\).

**Theorem 4.** _\[ANSS21\] Fix_ \(n,k\in\mathbb{N}\) _and_ \(z\in\mathbb{N}^{n\times k}\)_. For any_ \(\lambda=o(1)\)_, there exists a randomized non- adaptive algorithm_ A_<sub>BL</sub> that solves Block-LIS up to_ \((\alpha,\lambda n)\)_-approximation, where_ \(\alpha=\left(\frac{|z|}{\lambda n}\right)^{o(1)}\) _using_ \(\left(\frac{|z|}{\lambda n}\right)\cdot n^{o(1)}\) _time._

**Block-LIS tion for LCS.** To prove Theorem 1, we formulate the LCS problem as a single string Block-LIS. Given \(x,y\in\Sigma^n\), we define an integer block sequence _z_ such that each _z<sub>i</sub>_ is a block of all \(j\in[n]\) indices where _y<sub>j</sub>=x<sub>i</sub>_. Formally:

\(z\unknown\oplus_{i\in[n]}\left\{y^{-1}\left(x_i\right)\right\}.\) (1)

We claim the following equivalence:

**Claim 5.** _Block-LIS(z_)=LCS(_x,y)._

<sup>1</sup>The original definition of Block-LIS included another extension which is not relevant for our reduction, and hence was omitted for exposition.

