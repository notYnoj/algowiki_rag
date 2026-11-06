_The algorithm runs in O(n_<sup>4/3</sup>/log<sup>(_i_)</sup>_n_) _time for i_=1,2_, and in O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>) _time for_ \(i\ge 3\).

_Proof._ Compute \(\hat{\kappa}(I)\) using Theorem 1. If \(\hat{\kappa}(I)+c_0n^{4/3}(log^{(i)}n)^4<K\), then \(\kappa(I)<K\). If \(\hat{\kappa}(I)-c_0n^{4/3}(log^{(i)}n)^4>K\), then \(\kappa(I)>K\). Otherwise, report "unsure". The correctness follows immediately from the error guarantee of Theorem 1.

In the remainder of this section, we prove Theorem 1. The proof naturally splits into two cases. For _i_=1,2, the algorithm follows directly from repeated applications of Lemma 1. The case \(i\ge 3\) is substantially more difficult and new techniques are required.

## 3.1 The cases _i_=1,2

For _i_=1,2, the approximate counting algorithm follows directly from the balanced recurrence (3). For convenience, we restate the recurrence here in the symmetric case _m=n_:

\(T(n,n)=O(nrlogr)+O(r^4)\cdot T\big(\frac{n}{r^3},\frac{n}{r^3}\big).\) (4)

The algorithm computes an approximate count \(\hat{\kappa}(I)\) by recursively applying Lemma 1. At each recursive step, we add to \(\hat{\kappa}(I)\) the number of certified pairs recorded by the bicliques in \(\Gamma\). Since every certified pair has distance in _I_, the only source of error comes from the uncertain pairs represented by \(\Pi\). Consequently, \(|\hat{\kappa}(I)-\kappa(I)|\) is bounded by the total number of uncertain pairs in the remaining recursive subproblems.

For _i_=1, we apply Lemma 1 once with _r=n_<sup>1/3</sup>/log<sup>2</sup>_n_. The runtime is _O(nr_log_r_), which is _O(n_<sup>4/3</sup>/log_n_), and the number of uncertain pairs is _O(n_<sup>2</sup>_/r_<sup>2</sup>)=_O(n_<sup>4/3</sup>log<sup>4</sup>_n_). This proves Theorem 1 for _i_=1.

For _i_=2, we apply Lemma 1 recursively twice. The first application again uses _r=n_<sup>1/3</sup>/log<sup>2</sup>_n_. For each biclique \(A'_s\times B'_s\in\Pi\), we apply Lemma 1 again with _r_=log<sup>2</sup>_n/_log<sup>2</sup>log_n_. The total runtime is _O(n_<sup>4/3</sup>/loglog_n_), while the total number of uncertain pairs after the second recursive step is _O(n_<sup>4/3</sup>/log<sup>4</sup>log_n_). This proves Theorem 1 for _i_=2.

## 3.2 The case \(i\ge 3\)

For \(i\ge 3\), one might try to continue applying Recurrence (4). However, every application of the recurrence introduces a constant-factor loss. After _i_ recursive levels, both the running time and the error bound would incur an extra factor 2<sup>_O(i_)</sup>. Consequently, this approach is sufficient only when _i=O_(1). To obtain the bounds stated in Theorem 1 for general _i_, a different approach is needed.

The key observation is that for approximate counting we do not need to construct all bicliques explicitly. Instead, it is sufficient to know, for each cell of the last cutting, how many annuli completely contain the cell. This allows us to count certified pairs implicitly through cutting cells rather than explicitly through bicliques.

The remaining difficulty is point location. To compute the contribution of a cell, we need to determine, for every point of _B_, the cell of the last cutting that contains it. A straightforward implementation would require logarithmic time per point. To avoid this overhead, we use the \(\Gamma\)- framework of Chan and Zheng \[10\]. The framework becomes applicable because, after two levels of recursion, the remaining subproblem size is already extremely small. The details are given below.

We consider a general \(i\ge 3\).

We first apply Recurrence (4) twice with _r=n_<sup>1/3</sup>/log<sup>2</sup>_n_, exactly as in the case _i_=2. This takes _O(n_<sup>4/3</sup>/loglog_n_) time and produces _O(n_<sup>4/3</sup>/log<sup>8</sup>_n_) certified bicliques together with _O(n_<sup>4/3</sup>/log<sup>8</sup>_n_) uncertain bicliques. We add \(\sum_t(|A_t|\cdot|B_t|)\) over all certified bicliques to \(\hat{\kappa}(I)\) (initially, \(\hat{\kappa}(I)=0\)). Note that the total size of all certified bicliques satisfies \(\sum_t(|A_t|+|B_t|)=O(n^{4/3}/loglogn)\).

