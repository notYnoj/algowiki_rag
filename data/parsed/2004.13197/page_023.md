and so on). Thus, it is intuitively clear how to achieve the upper bound if one were allowed, say \(\genfrac(){pt}{2}{k}{B}\) preprocessing. This is huge, and the main question is whether we can reduce it to _O_((_k_log_k)/B+kw/B_).

To describe our algorithm, we will need a smaller data structure first, which we explain next.<br>
2_<sup>B</sup>_ **Tree:** A 2_<sup>B</sup>_ tree for \(\alpha\) levels on a sorted set A of _A_ unit-sized elements (denoted as \(T(\mathcal{A},2^B,\alpha)\)) is a tree that performs the following : Assume _B_ long elements have to find their positions among elements in A, and that they are in memory. Initially they could be anywhere (so their search space size is _A_). \(T(\mathcal{A},2^B,\alpha)\) is a data structure that reduces their search spaces to size \(A/(2^\alpha B)\) using \(\alpha+1\) short block I/Os. We briefly describe how to build this tree. In the first step, we bring in the root block of the _B_-tree on A, achieving a fan-out of _B_ for every long element. Partition the set A:={_e_<sub>1</sub>_,...e<sub>A</sub>_} into _B_ equally sized (sorted) subsets \(\mathcal{A}_i=\{e_{(iA/B)+1},\dots e_{(i+1)A/B}\}\) (\(0\le i\le B-1\)). Put the _B_ middle elements ,\(\{e_{(2j+1)A/2B}\}_{j=0}^{B-1}\), into a block, which serves as the root of \(T(\mathcal{A},2^B,\alpha)\). Assume that the _i_th long element points to _A<sub>i</sub>_ (so _A<sub>i</sub>_ is its current search space). Upon comparison of this root block with the _B_ long elements in memory, each long element’s search space is reduced by a factor of 2, the total fan-out being 2_<sup>B</sup>_. In each such permutation a long element’s search space is now either the left half or the right half of its original. For each of the 2_<sup>B</sup>_ permutations, make a block of _B_ short elements comprising of the middle pivots of the new search spaces corresponding to the permutation. These are the immediate children of the root node. We recurse on these nodes now and stop when we have built \(\alpha\) levels of this tree.

## Preprocessing Phase

1. Define<tbc>

<tbc>\(j=\frac{loglog_{M/B}k/B-logB}{B-1}\)<tbc>

<tbc>and _g_=(log_k-j)/j_.<tbc>

<tbc>Build _T(k,_2_<sup>B</sup>,j_) on the sorted set of the _k_ short elements._For the algorithm to work,_ \(j=\omega(1)\)_, which automatically puts a restriction on k. This is the k_<sub>0</sub> _referred to in the statement of the observation, and the algorithm works only if k\>k_<sub>0</sub>. Also, we will assume that _k_ is sufficiently large that _Bw\<_loglog<sub>_M/B_</sub>_k_.<tbc>

2. Let \(\{\mathcal{U}_i\}_{i=1}^g\) be a collection of sets, where U_<sub>i</sub>_ is the (sorted) set of all nodes at depth _i.j_ (so _i.j_ levels from the root) in the binary tree on _k_<tbc>

