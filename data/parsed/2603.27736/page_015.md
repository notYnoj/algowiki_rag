<tbc>into two matrices _A_<sub>1</sub>_,A_<sub>2</sub> of the same size, denoted by \(A=A_1\sqcup A_2\), if each entry \(A[i,j]\neq\perp\) appears in _exactly one_ of the two matrices (i.e., _A_<sub>1</sub>\[_i,j_\]=_A_\[_i,j_\] and \(A_2[i,j]=\perp\), or \(A_1[i,j]=\perp\) and _A_<sub>2</sub>\[_i,j_\]=_A_\[_i,j_\]).

Let MM(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>) denote the time complexity of multiplying an \(n_1\times n_2\) with an \(n_2\times n_3\) integer matrix. Let \(2\le\omega<2.372\) \[8\] denote the exponent of square matrix multiplication.

## 2.1 APSP, Min-Plus Product and Exact Triangle

**Definition 2.1** (APSP)**.** _The_ All-Pairs Shortest Paths (APSP) _problem is to compute the u-v-distances for all pairs of nodes u,v in a given directed edge-weighted n-vertex graph._

**Definition 2.2** (Min-Plus Product)**.** _The_ min-plus product _of_ \(A\in(\mathbb{Z}\cup\{\perp\})^{n_1\times n_2},B\in(\mathbb{Z}\cup\{\perp\})^{n_2\times n_3}\) _is the matrix_ \(A*B\in(\mathbb{Z}\cup\{\perp\})^{n_1\times n_3}\) _defined by_

\((A*B)[i,j]=min_{k\in[n_2]}(A[i,k]+B[k,j]).\)

_The_ Min-Plus Product _problem is to compute the min-plus product A∗B of two given matrices A,B._

**Definition 2.3** (Exact Triangle)**.** _Let_ \(A\in(\mathbb{Z}\cup\{\perp\})^{n_1\times n_2},B\in(\mathbb{Z}\cup\{\perp\})^{n_2\times n_3}\) _and_ \(C\in(\mathbb{Z}\cup\{\perp\})^{n_1\times n_3}\). _A_ triangle _is a triple_ \((i,k,j)\in[n_1]\times[n_2]\times[n_3]\) _such that_ \(A[i,k]\neq\perp,B[k,j]\neq\perp,C[i,j]\neq\perp\)_, and an_ exact triangle _is a triangle_ (_i,k,j_) _such that A_\[_i,k_\]+_B_\[_k,j_\]=_C_\[_i,j_\].<sup>11</sup> _The_ (All-Edges) Exact Triangle<sup>12</sup> _problem is, given A,B,C, to decide for each edge_ \((i,k)\in[n_1]\times[n_2]\) _and_ \((k,j)\in[n_2]\times[n_3]\) _and_ \((i,j)\in[n_1]\times[n_3]\) _if it is involved in an exact triangle_ (_i,k,j)._

It is long-known that the APSP and Min-Plus Product problems have the same complexity up to logarithmic factors. Vassilevska W. and Williams \[97\] further proved that Min-Plus Product reduces to All-Edges Exact Triangle by a scaling trick that only incurs an overhead logarithmic in the universe size.

## 2.2 Parameters

We study the Min-Plus Product and Exact Triangle problems constrained by various parameters, often by multiple parameters at the same time. To simplify notation, we propose a systematic naming scheme. For any Min-Plus Product instance (_A,B_) or any Exact Triangle instance (_A,B,C_), consider the following six parameters:

**Parameter 2.4** (_r_-Rank)**.** _The select-plus rank of A or B (or C) is at most r. We assume that as part of the input we additionally receive a rank-r decomposition of that respective matrix._

**Parameter 2.5** (_d_-Slice-Uniform)**.** _The rows or columns in A or B (or C) have at most d distinct non-_\(\perp\) _entries each._<sup>13</sup>

**Parameter 2.6** (_D_-Uniform)**.** _The total number of distinct non-_\(\perp\) _entries in all matrices A and B (and C) is at most D._

**Parameter 2.7** (\(\rho\)-Regular)**.** _In every row and column of A and B (and C), no non-_\(\perp\) _entry appears in more than a_ \(\rho\)_-fraction of the respective row or column._

**Parameter 2.8** (_K_-Doubling)**.** _Let X be the set of integer entries in A and B (and C). Then X has doubling_ \(|X+X|\le K|X|\).

**Parameter 2.9** (_u_-Universe)**.** _All non-_\(\perp\) _entries in the matrices A and B (and C) are from_ {0_,...,u}._

<sup>11</sup>Of course, one could equivalently define an exact triangle to satisfy that _A_\[_i,k_\]+_B_\[_k,j_\]+_C_\[_i,j_\]=0; in this case the problem is typically called the _Zero Triangle_ problem. We stick to the version in Definition 2.3 which is nicer to relate to the Min-Plus Product problem. <sup>12</sup>The established name in the fine-grained literature is "All-Edges" Exact Triangle. However, in this paper we are exclusively concerned with the All-Edges version and so we will usually drop the "All-Edges" prefix for the sake of brevity. <sup>13</sup>In \[4\] this constraint was instead called _d-weights_.

