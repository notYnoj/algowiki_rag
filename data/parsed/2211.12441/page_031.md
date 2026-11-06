<tbc>exactly those whose affected items fall within the same partition class. In the case of the problem \(\Pi_T\), the partition classes _X<sub>i</sub>_ correspond to the leaf child sets LC(_v_) from Definition 7, where _v_ ranges over the leaf parents.

Let us investigate the size of the connected components of \(G(\Pi)\) when \(\Pi\) satisfies the partition property. Consider a walk in \(G(\Pi)\). As the only steps we can take correspond to adjacent-rank transpositions \(\tau\) that swap elements in the same partition class, the sets _X<sub>i</sub>_ remain invariant, irrespective of the ranking \(\rho\) we start from. Depending on \(\rho\), there may be more structure inside each partition class _X<sub>i</sub>_; the set _X<sub>i</sub>_ may be broken up into smaller subsets that are each invariant. For our analysis, we list the elements of each partition class in order of increasing rank under \(\rho\), and include an edge between elements that have successive ranks. We introduce the term "successor graph" to capture this structure, viewed as a graph with the ranks as vertices.

**Definition 47 (successor graph,** \(S(\cdot,\cdot)\)**).** _Let_ \(\Pi\) _be a computational problem in the comparison- query model on a set X of n items, and_ \(\rho\) _a ranking of X. The successor graph of_ \(\Pi\) _on_ \(\rho\)_, denoted_ \(S(\Pi,\rho)\)_, has vertex set_ \[_n_\] _and contains all edges of the form_ (_r,r_+1) _with_ \(r\in[n-1]\) _such that_ \(\Pi(\rho)=\Pi(\tau\rho)\)_, where_ \(\tau\) _denotes the adjacent-rank transposition_ (_r,r_+1).

We have the following connection.

**Proposition 48.** _Let_ \(\Pi\) _be a computational problem in the comparison-query model on the set X, and let_ \(\rho\) _be a ranking of X. If_ \(\Pi\) _has the partition property, then the connected component of_ \(\rho\) _in_ \(G(\Pi)\) _has size_ \(\prod_j(n_j!)\)_, where the n<sub>j</sub>’s denote the sizes of the connected components of_ \(S(\Pi,\rho)\).

_Proof._ The connected components of the successor graph \(S(\Pi,\rho)\) correspond to subsets of the classes _X<sub>i</sub>_ that each remain invariant under walks in \(G(\Pi)\). Within each of the subsets, independently for each subset, every possible ordering can be realized by such walks. This is because for any adjacent-rank transposition \(\tau\), the successor graphs \(S(\Pi,\rho)\) and \(S(\Pi,\tau\rho)\) are the same, and every ordering can be realized by a sequence of swaps of adjacent elements. It follows that the number of rankings that can be reached from \(\rho\) in \(G(\Pi)\) equals the product over all connected components of \(S(\Pi,\rho)\) of the number of possible orderings of the elements in the connected component.

Figure 10 depicts an example for a problem of type \(\Pi_T\) and a partition consisting of 4 classes, namely the leaf child sets LC<sub>1</sub>,LC<sub>2</sub>,LC<sub>3</sub> and LC<sub>4</sub>. The tree _T_ and ranking \(\rho\) are represented in Figure 10a. Figure 10b represents the part of the successor graph \(S(\Pi_T,\rho)\) involving the leaf child set LC<sub>3</sub> and illustrates the subpartitioning into invariant subsets.

LC4
1
13
LC1
4
12
6
5
10
LC3
11
2
3
9
14
7
8

r
2
3
7
8
9
11
14
P(r)

(a) Leaf child sets and leaf ranks under \(\rho\)

(b) Inside leaf child set LC<sub>3</sub>

Figure 10: Connected component analysis

