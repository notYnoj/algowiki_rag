for \(j\neq j'\), then we say that \((p,p')\) is a type-2 crossing. If either instance _X<sup>j,i</sup>_ or \(X^{j^\prime,i}\) is a bad instance for _L_, then the crossing is of type (2a); otherwise it is of type (2b).

We now bound the total number of crossings of each of these types separately.

### Type-1 Crossings

We bound the total number of all type-1 crossings exactly like in Section 4.5.1. We note that the proof does not use the vertical locations of the points in the sub-instances _X<sup>j,i</sup>_, and only relies on two properties of instance \(\hat{X}\): (i) the points in the first instance _X_<sub>0</sub> (corresponding to instance _X_<sup>0_,i_</sup>) are exponentially spaced horizontally, so the _x_-coordinates of the points are integral powers of 2, and they are all distinct; and (ii) each subsequent instance _X<sub>s</sub>_ (corresponding to instance _X<sup>s,i</sup>_) is a copy of _X_<sub>0</sub> that is shifted horizontally by _s_ units. Therefore, the same analysis applies, and the total number of type-1 crossings in \(\hat{X}_i\) can be bounded by _O(N_log_N_loglog_N_) as before.

### Type-(2a) Crossings

As before, we charge each type-(2a) crossing to one of the corresponding bad instances, to conclude that the total number of type-(2a) crossings is bounded by the total number of type-1 crossings, which is in turn bounded by _O(N_log_N_logloglog_N_).

### Type-(2b) Crossings

Recall that in order to bound the number of type-(2b) crossings, we have collapsed, for every instance _X<sub>s</sub>_, all rows of _X<sub>s</sub>_ into a single row. If we similarly collapse, for every instance _X<sup>s,i</sup>_, all rows of this instance into a single row, we will obtain an identical set of points. This is because the only difference between instances _X<sub>s</sub>_ and _X<sup>s,i</sup>_ is vertical position of their points. Therefore, the total number of type-(2b) crossings in \(\hat{X}_i\) is bounded by _O(N_log_N_) as before.

This finishes the proof of Lemma 5.7. We conclude that \(\sum_{i=1}^N\mathsf{WB}(X_i^*)\le O(N^2logNloglogN)=O(N^*loglogN^*)\).

## 5.3.2 Bounding Wilber Bound for the Compressed Instance

In this subsection, we prove the following lemma.

**Lemma 5.8** \(\mathsf{WB}(\tilde{X})\le O(N^*)\).

We denote the active columns of \(\tilde{X}\) by _C_<sub>1</sub>_,...,C<sub>N</sub>_. Recall that each column _C<sub>i</sub>_ contains exactly _N_log_N_ input points. Let R be the set of all rows with integral coordinates, so |R|=_N_<sup>2</sup>log_N_. Let B<sub>1</sub>,B<sub>2</sub>_,...,_B<sub>_N_<sup>2</sup></sub> be a partition of the rows in R into blocks containing log_N_ consecutive rows each, where the blocks are indexed in their natural bottom-to-top order. Recall that each such block B_<sub>i</sub>_ represents some active row of instance \(\hat{X}\), and the points of \(\tilde{X}\) that lie on the rows of B_<sub>i</sub>_ form an increasing sequence. We also partition the rows of R into super-blocks, \(\hat{\mathcal{B}}_1,\dots,\hat{\mathcal{B}}_N\), where each superblock is the union of exactly _N_ consecutive blocks. For each subinstance \(X^{s,s^\prime}\), the points of the subinstance lie on rows that belong to a single super-block.

Let L be the set of all columns with half-integral coordinates for \(\tilde{X}\), so \(|\mathcal{L}|\le N\). We fix any permutation \(\sigma\) of L, and prove that \(\mathsf{WB}_\sigma(\tilde{X})\le O(N^*)\). Let _T_ be the partitioning tree associated with the permutation \(\sigma\).

Consider any vertex \(v\in V(T)\), its corresponding vertical strip _S=S(v_), and the vertical line _L=L(v_) that _v_ owns. Let \((p,p')\) be a crossing of _L_, so _p_ and \(p'\) both lie in _S_ on opposite sides of<tbc>

