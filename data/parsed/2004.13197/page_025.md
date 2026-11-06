### Preprocessing Analysis

**Lemma 21.** _Starting with a binary tree on_ A, \(T(\mathcal{A},2^B,\alpha)\) _can be built in_ \(O(B.2^{\alpha B})I/Os\).

_Proof._ There are \(O(2^{\alpha B})\) blocks in \(T(\mathcal{A},2^B,\alpha)\). Each block takes a maximum of _B_ I/Os, since all the levels of the binary tree are already built and one only needs to go one level down the binary tree in order to bring the middle pivot.

The number of trees of type _T_(A,2_<sup>B</sup>,j_) built by our algorithm can be bounded by the last level. There are (_k/B)/_2_<sup>j</sup>_ nodes in the last level on which this data structure is built. Thus the total cost is bounded by

\((B.2^{jB})\frac{k}{2^jB}=k2^{j(B-1)}=\frac{k}{B}log_{M/B}\frac{k}{B},\)

where the last inequality follows by the definition of \(j=\frac{loglog_{M/B}k/B-logB}{B-1}\) . This finishes the proof of the preprocessing claim.

## 7 Conclusion and Open Problems

We derived upper and lower bounds on sorting and batched predecessor in the RAM and DAM models, when comparison or I/O costs depend on the length of the items being compared. In many settings, we show that the optimal sorting algorithm involves the optimal batched predecessor problem as a subroutine, and develop algorithms for the batched predecessor problem.

While our results are for the two-size setting, we would like to point out that our algorithms generalize to the multiple-sizes setting. However, generalizing our lower bound techniques to the multiple-size setting requires more ideas.

## References

