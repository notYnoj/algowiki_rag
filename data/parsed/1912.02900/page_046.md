#### Type-2 crossings

In order to bound the number of type-2 crossings, observe that \(|\mathcal{L}|\le N\). If \(L\in\mathcal{L}\) is a vertical line, and _S_ is a strip that _L_ splits, then there are _N_ superblocks of rows that can contribute type-2 crossings to cost(_L_), and each such superblock may contribute at most one crossing. Therefore, the total number of type-2 crossings charged to _L_ is at most _N_, and the total number of all type-2 crossings is _O(N_<sup>2</sup>).

#### Type-3 crossings

In order to bound the number of type-3 crossings, observe that every column contains _N_log_N_ points. Therefore, if \(L\in\mathcal{L}\) is a vertical line, then the number of type-3 crossings charged to it is at most 2_N_log_N_. As \(|\mathcal{L}|\le N\), we get that the total number of type-3 crossings is _O(N_<sup>2</sup>log_N_).

To conclude, we have shown that \(\mathsf{WB}_\sigma(\tilde{X})=O(N^2logN)=O(N^*)\), proving Lemma 5.8. By combining Lemmas 5.7 and 5.8, together with Theorem 3.6, we conclude that WB(_X_<sup>∗</sup>)=_O(N_<sup>∗</sup>logloglog_N_<sup>∗</sup>), proving Theorem 5.6.

### 5.4 Handling Horizontal Cuts

We show the following analogue of Theorem 5.6.

**Theorem 5.11** \(\mathsf{WB}'(X^*)\le O(N^*loglogN^*)\).

The proof of the theorem is virtually identical to the proof of Theorem 5.6. In fact, consider the instance _X_<sup>∗∗</sup>, that is obtained from _X_<sup>∗</sup>, by rotating it by 90 degrees clockwise. Consider the sequence \(\mathsf{BRS}'(\ell,\mathcal{R},\mathcal{C})\) that is obtained by rotating the point set \(\mathsf{BRS}(\ell,\mathcal{R},\mathcal{C})\) by 90 degrees. Consider now the following process. Our starting point is the rotated Bit Reversal Sequence. We then follow exactly the same steps as in the construction of the instance _X_<sup>∗</sup>. Then the resulting instance is precisely (a mirror reflection of) instance _X_<sup>∗∗</sup>. Notice that the only place where our proof uses the fact that we start with the Bit Reversal Sequence is in order to show that OPT(_X_<sup>∗</sup>) is sufficiently large. In fact we could replace the Bit Reversal Sequence with any other point set that is a permutation, and whose optimal solution cost is as large, and in particular the Bit Reversal Sequence that is rotated by 90 degrees would work just as well. The analysis of the Wilber Bound works exactly as before, and Theorem 5.11 follows.

## 6 The Algorithms

In this section we provide the proof of Theorem 1.3. Both the polynomial time and the sub- exponential time algorithms follow the same framework. We start with a high-level overview of this framework. For simplicity, assume that the number of active columns in the input instance _X_ is an integral power of 2. The key idea is to decompose the input instance into smaller sub-instances, using the split instances defined in Section 3.1. We solve the resulting instances recursively and then combine the resulting solutions.

Suppose we are given an input point set _X_ that is a semi-permutation, with |_X_|=_m_, such that the number of active columns is _n_. We consider a _balanced_ partitioning tree _T_, where for every vertex \(v\in V(T)\), the line _L(v_) that _v_ owns splits the strip _S(v_) in the middle, with respect to the active columns that are contained in _S(v_). Therefore, the height of the partitioning tree is log_n_.

