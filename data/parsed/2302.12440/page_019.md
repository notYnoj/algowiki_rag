## 4 Noisy Sorting Lower Bound

In this section, we show the lower bound of noisy sorting.

**Theorem 2** (Noisy Sorting Lower Bound)**.** _Any (deterministic or randomized) algorithm for_ NoisySorting(_n_) _with error probability o_(1) _must make at least_

\((1-o(1))\left(\frac{1}{I(p)}+\frac{1}{(1-2p)log\frac{1-p}{p}}\right)nlogn\)

_noisy comparisons in expectation, even if the input is a uniformly random permutation._

The following problem serves as an intermediate step towards the lower bound.

**Definition 25** (Group Sorting Problem)**.** For some integers _k|n_, we define problem GroupSorting(_n,k_) as follows: Given a list _L_ of _n_ elements, divided into _n/k_ groups _A_<sub>1</sub>_,...,A<sub>n/k</sub>_ of _k_ elements each, satisfying the property that for all \(1\le i<j\le n/k\), \(x\in A_i,y\in A_j\), we have _x\<y_. An algorithm needs to output an ordered list of sets _A_<sub>1</sub>_,...,A<sub>n/k</sub>_ by asking the following type of queries GroupQuery(_x,y_):

• If the two elements are in the same group, then the query result is ∗.<tbc>

• Otherwise, suppose \(x\in A_i\), \(y\in A_j\) with \(i\neq j\). Then the query result is NoisyComparison(_i,j_).

The following lemma relates GroupSorting and NoisySorting.

**Lemma 26.** _Fix any algorithm_ A _for_ NoisySorting(_n_) _with error probability o_(1)_. Let k|n. Let L be the input list of_ NoisySorting(_n). Suppose we partition L into n/k groups A_<sub>1</sub>_,...,A<sub>n/k</sub> where for all_ \(1\le i<j\le n/k\)_, for all_ \(x\in A_i\), \(y\in A_j\)_, we have x\<y. Let_ \(U^\neq\) _denote the number of queries_ A _makes to elements in different groups._

_Then there exists an algorithm for_ GroupSorting(_n,k_) _with error probability o_(1) _which makes at most_ \(\mathbb{E}[U^\neq]+(n-n/k)\) _queries in expectation._

_Proof._ Given A, we design an algorithm \(\mathcal{A}'\) for GroupSorting(_n,k_) as follows.

Given input _L_, Algorithm \(\mathcal{A}'\) picks an arbitrary strict total order _\<<sub>T</sub>_ on all the elements. \(\mathcal{A}'\) also maintains which elements are known to be in the same group, implied by queries that return ∗. Then, it simulates Algorithm A on the same input _L_ as follows:

• When A attempts to make a comparison between _x_ and _y_:

– If _x,y_ are not known to be in the same group, call GroupQuery(_x,y_). If the query returns ∗, which means _x_ and _y_ are in the same group, return BSC\(_p(\unknown\{x<_Ty\})\) to A. Otherwise, return the result of GroupQuery(_x,y_) to A.<tbc>

– If _x,y_ are known to be in the same group, return BSC\(_p(\unknown\{x<_Ty\})\) to A.<tbc>

• When A outputs a sequence _x_<sub>1</sub>_,...,x<sub>n</sub>_: Let _A<sub>i</sub>_={_x_<sub>(_i_-1)_k_+1</sub>_,...,x<sub>ik</sub>_} for \(i\in[n/k]\) and output _A_<sub>1</sub>_,...,A<sub>n/k</sub>_.

Let us analyze the error probability and number of queries made by algorithm \(\mathcal{A}'\).

