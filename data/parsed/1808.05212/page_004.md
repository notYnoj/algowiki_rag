The networks, depicted in Figure 2 and identical under mirror symmetry, substantially improve the average cost of exchange. More striking is a reduction in maximum exchange, which was lowered from 3 to 2! Moreover, the average number of swaps was lowered from 3/2=1.5 to 7/6≈1.167. This is unexpected and serves as the basis of non-interfering concurrent exchange. Clearly, the first link may exchange without restriction. The remaining cost of one exchange must be shared between the two remaining links: _at most one_ may occur. This in turn implies that the central element cannot be rewritten by both links, allowing both the upper and lower link concurrent execution.

We now create a new fused dual-link element, which we name a "2-_op_" (borrowing from mathematical nomenclature used for such occurrences), depicted below:

The circle at the common link joint 2 indicates non-interference.

## 2 9-element networks and medians

The 2-op exchange on three elements yields immediate gains in lowering costs of traditional networks. For example, Paeth [5] described a median on a \(3\times 3\) box (see Figure 4),

3
2
1.167
0
3
2
1.167
0
1
X
1
X
2
X
2
X
3
X
3
X
1
0.5
1
0.5
2
0.333333
2
0.333333
3
0.333333
3
0.333333
(a)
(b)

3
2
1.167
0
1
X
2
X
3
X

Figure 2: Two sorting networks: (a) corresponds to the comparisons (13), (12), (23), at stages 1, 2, 3, respectively; (b) corresponds to the comparisons (13), (23), (12), at stages 1, 2, 3, respectively.

Figure 3: At stage 1, we have the comparison (13), while at stage 2, we have the new 2-op (123) which will execute at most one of the exchanges {(12), (23)}.

