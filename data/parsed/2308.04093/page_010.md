• Can our techniques be useful for other related problems, such as scheduling \[BFH<sup>+</sup>22, ABHS22a, KPR23\] or low-dimensional integer linear proramming \[EW20\]?

### Paper organization

Section 2 contains definitions, notations, and some lemmas from previous works, which are essential for understanding Section 3. Then, in Section 3 we describe our algorithm for 0-1 Knapsack. A key subroutine of our algorithm is deferred to Section 4.

## 2 Preliminaries

### 2.1 Notations and definitions

We use \(\widetilde{O}(f)\) to denote _O(f_ polylog_f_). Let \[_N_\]={1,2_,...,N_}.

#### Multisets and subset sums.

For an integer multiset _X_, and an integer _x_, we use \(\mu_X(x)\) to denote the multiplicity of _x_ in _X_. For a multiset _X_, the _support_ of _X_ is the set of elements it contains, denoted as \(\mathrm{supp}(X):=\{x:\mu_X(x)\ge 1\}\). We say a multiset _X_ is _supported on_ \[_N_\] if \(\mathrm{supp}(X)\subseteq[N]\). For multisets _A,B_ we say _A_ is a subset of _B_ (and write \(A\subseteq B\)) if for all \(a\in A\), \(\mu_B(a)\ge\mu_A(a)\). We write \(A\unknown B\) as the union of _A_ and _B_ by adding multiplicities.

The _size_ of a multiset _X_ is \(|X|=\sum_{x\in\mathbb{Z}}\mu_X(x)\), and the _sum of elements_ in _X_ is \(\Sigma(X)=\sum_{x\in\mathbb{Z}}x\cdot\mu_X(x)\). The set of all _subset sums_ of _X_ is \(\mathcal{S}(X):=\{\Sigma(Y):Y\subseteq X\}\). We also define \(\mathcal{S}^*(X):=\{\Sigma(Y):Y\subseteq X,Y\neq\emptyset\}\) to be the set of subset sums formed by _non-empty_ subsets of _X_.

The _r-support_ of a multiset _X_ is the set of items in _X_ with multiplicity at least _r_, denoted as \(\mathrm{supp}_r(X):=\{x:\mu_X(x)\ge r\}\).

#### Vectors and arrays.

We will work with vectors in Z<sup>I</sup> where I is some index set. We sometimes denote vectors in boldface, e.g., \(\mathbf{x}\in\mathbb{Z}^\mathcal{I}\), and use non-boldface with subscript to denote its coordinate, e.g., \(x_i\in\mathbb{Z}\) (for \(i\in\mathcal{I}\)). Let \(\mathrm{supp}(\mathbf{x}):=\{i\in\mathcal{I}:x_i\neq 0\}\), \(\|\mathbf{x}\|_0:=|\mathrm{supp}(\mathbf{x})|\), and \(\|\mathbf{x}\|_1:=\sum_{i\in\mathcal{I}}|x_i|\). Let **0** denote the zero vector. For \(i\in\mathcal{I}\), let **_e_**_<sub>i</sub>_ denote the unit vector with _i_-th coordinate being 1 and the remaining coordinates being 0.

We use \(A[\ell\dots r]\) to denote an array indexed by integers \(i\in\{\ell,\ell+1,\dots,r\}\). The _i_-th entry of the array is _A_\[_i_\]. Sometimes we consider arrays of vectors, denoted by \(\mathbf{x}[\ell\dots r]\), in which every entry \(\mathbf{x}[i]\in\mathbb{Z}^\mathcal{I}\) is a vector, and we use _x_\[_i_\]_<sub>j</sub>_ to denote the _j_-th coordinate of the vector **_x_**\[_i_\] (for \(j\in\mathcal{I}\)).

#### 0-1 Knapsack.

In the 0-1 Knapsack problem with _n_ input items (_w_<sub>1</sub>_,p_<sub>1</sub>)_,...,(w<sub>n</sub>,p<sub>n</sub>_) (where _weights_ \(w_i\le w_\mathrm{max}\) and _profits_ \(p_i\le p_\mathrm{max}\) are positive integers) and knapsack capacity _t_, an _optimal knapsack solution_ is an item subset \(X\subseteq[n]\) that maximizes the total profit<tbc>

\(P(X):=\sum_{i\in X}p_i,\) (1)

<tbc>subject to the capacity constraint

\(W(X):=\sum_{i\in X}w_i\le t.\) (2)

We will frequently use the following notations:

