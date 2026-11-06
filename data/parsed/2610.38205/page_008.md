SetOf\((p_k,\ell\in[n])\) returns the \(\ell\)th set \(S_{i\rightarrow j}\) containing _p<sub>k</sub>_ (in some order), assuming \(\ell\le\mathrm{FreqOf}(p_k)\).

Suppose we fix the set cover instance, that is, we fix _i_. Supporting MemberOf queries is straightforward. By definition, \(p_k\in S_{i\rightarrow j}\) if and only if \(d(p_j,p_k)<\frac{1}{\alpha}\cdot d(p_i,p_k)\), which can be determined by only two distance accesses.

To support the other two queries, we first preprocess a **_distance-based permutation matrix_**. This is an \(n\times n\) matrix \(\Pi\) where the _i_th row stores the sorted order of all points by increasing distance from _p<sub>i</sub>_. That is, \(p_{\Pi_{i,j}}\) is the _j_th closest point to _p<sub>i</sub>_. This matrix can be constructed in _O(n_<sup>2</sup>log_n_) time by simply sorting each row.

Using the permutation matrix, we observe that, because \(p_k\in S_{i\rightarrow j}\Longleftrightarrow d(p_j,p_k)<\frac{1}{\alpha}\cdot d(p_i,p_k)\), all of the sets \(S_{i\rightarrow j}\) containing _p<sub>k</sub>_ are associated with the closest points to _p<sub>k</sub>_ and can therefore be found within some prefix of the _k_th row of \(\Pi\). We can find the length of the prefix by binary search on row _k_ for the last point _j_ satisfying \(d(p_j,p_k)<\frac{1}{\alpha}d(p_i,p_k)\). We can precompute these prefix lengths for all instances _i_ and targets _p<sub>k</sub>_ in _O(n_<sup>2</sup>log_n_) time total, then perform a simple lookup of these prefix lengths to answer FreqOf queries. SetOf queries follow the same principle; the \(\ell\)th set containing _p<sub>k</sub>_ is simply \(S_{i\rightarrow\Pi_{k,\ell}}\).

From this point on, we assume we have access to these three operations. We state this as a lemma.

**Lemma 2.3** (due to \[12\])**.** _Given a sparsest_ \(\alpha\)_-navigable graph construction problem specified by an input point set P and distance function_ \(d:P\times P\rightarrow\mathbb{R}^+\)_, there exists a data structure which supports_ MemberOf, FreqOf_, and_ SetOf _queries for the induced set cover instances in O_(1) _time. This data structure is constructed in O(n_<sup>2</sup>log_n_) _time and requires O(n_<sup>2</sup>) _space._

## 2.5 Batched Verification of Navigability Constraints via Matrix Multiplication

As in \[25\], a key component of our new algorithm for constructing sparse \(\alpha\)-navigable graphs is a routine for using fast matrix multiplication to verify the \(\alpha\)-navigability of a graph. Concretely, given a graph over _P_, we’d like to identify which source-target \(\alpha\)-navigability constraints are satisfied. We first describe how to verify all constraints at a single distance scale, then use distance discretization to verify all constraints.

**Lemma 2.4** (due to \[25\])**.** _Let G_=(_P,E_) _be a directed graph,_ \(\alpha\ge 1\)_, and r\>_0_. In_ \(O(n^\omega)\) _time, we can identify every pair_ (_s,t_) _such that there exists some edge_ \((s,v)\in E\) _satisfying d(v,t)\<r._

_Proof._ Let _A_ be the adjacency matrix of _G_, and define the matrix \(B^{(r)}\in\{0,1\}\) by

\(B_{j,k}^{(r)}=\left\{\begin{array}{ c c }
1 & \text{if}d(p_j,p_k)<r \\
0 & \text{otherwise}
\end{array}\right.\)

We construct _B_<sup>(_r_)</sup> using _O(n_<sup>2</sup>) distance queries and compute the matrix product _C_<sup>(_r_)</sup>=_AB_<sup>(_r_)</sup>. For any (_i,k_), \(C_{i,k}^{(r)}>0\) if and only if there exists some _j_ such that \((p_i,p_j)\in E\) and _d(p<sub>j</sub>,p<sub>k</sub>)\<r_. Consequently, we can identify all pairs described in the lemma above by scanning through _C_<sup>(_r_)</sup> and outputting (_p<sub>i</sub>,p<sub>k</sub>_) whenever \(C_{i,k}^{(r)}>0\).

Constructing the matrices and inspecting the product take _O(n_<sup>2</sup>) time, while computing the product takes \(O(n^\omega)\) time. Since \(\omega\ge 2\), the total running time is \(O(n^\omega)\).

