due to Lemma 3.4, in some top-left region of _C_, the values are equal to the corresponding values of _C<sup>L</sup>_, and in the remaining bottom-right region of _C_, the values are equal to the corresponding values of _C<sup>R</sup>_; see Figure 2. We find the boundary between these two regions by starting in the bottom-left corner of _C_ and traversing it towards the top-right corner along this boundary. We use lco(_C<sup>L</sup>_) and lco(_C<sup>R</sup>_) to sequentially compute the subsequent entries along the boundary. Having determined the boundary, we construct the core of _C_ by picking the core elements of _C<sup>L</sup>_ located to the top-left of this boundary, picking the core elements of _C<sup>R</sup>_ located to the bottom-right of this boundary, and computing the \(C^\square\) values on the boundary from scratch. The values in the topmost row and the leftmost column of _C_ can be trivially obtained as element-wise minima of the corresponding values in _C<sup>L</sup>_ and _C<sup>R</sup>_. This concludes the recursive procedure; see Algorithm 1 for the pseudocode. This algorithm follows the classical divide-and-conquer framework, and thus its time complexity can be easily derived from Theorem 1.1. The full description of the algorithm, the proof of its correctness, and the formal analysis of its time complexity are deferred to Appendix A. \(\blacktriangleleft\)

If the (min,+)-product of matrices represents the lengths of the shortest paths in a graph, the corresponding witness matrix allows computing the underlying shortest paths themselves. For that, we extend the presented algorithm to allow witness reconstruction.

\(\blacktriangleright\) **Theorem 4.7.** _The algorithm of Theorem 1.2 can be extended so that, within the same time complexity, it also builds a data structure that takes_ \(\mathcal{O}(n_1+n_2+n_3+\delta(M_1)+\delta(M_2))\) _space and provides_ \(\mathcal{O}(log(2+\delta(M_1)+\delta(M_2)))\)_-time oracle access to_ W<sup>_M_<sub>1</sub>_,M_<sub>2</sub></sup>.

**Proof Sketch.** We slightly modify the algorithm of Theorem 1.2. For the leaf recursive calls with _p=r_=1, we explicitly store the minimal witness of the only entry of _C_. In the non-leaf recursive calls, we store the correspondence between the indices in the compressed matrices _A,B,C_ and the decompressed matrices _A_<sup>∗</sup>_,B_<sup>∗</sup>_,C_<sup>∗</sup>, as well as the border separating the values of _C<sup>L</sup>_ and _C<sup>R</sup>_ in _C_ (the blue curve of Figure 2). Naively, this data takes space proportional to the time complexity of Theorem 1.2. Nevertheless, using bit-masks equipped with rank/select functionality, the total space complexity can be brought down to be linear in terms of the size of the input. To answer a query, we descend the recursion tree. In constant time we can find an entry of _C_ corresponding to the queried entry of _C_<sup>∗</sup> and decide on which side of the border separating the values of _C<sup>L</sup>_ and _C<sup>R</sup>_ the queried entry of _C_ is. After that, we recurse into either \(A^L\otimes B^L\) or \(B^L\otimes B^R\). In the terminal recursion call with _p=r_=1 we return the minimal witness that is stored explicitly. The time complexity of the

0 0
0 0
0 0
0 0
0 0
0 0
0 1
1 1
3 3
2 2
2 2
3 3
2 2
0 0
5 4
3 2
0 0
5 4
3 2
2 2
5 4
3 2
0 0
7 6
4 2
0 0
8 7
6 4
4 4
8 7
5 3
1 1
8 7
5 3
1 1
9 8
7 5
5 8
7 4
2 0
0 8
7 4
2 0
0 10 8
6 3
2 2
9 7
4 2
0 0
9 7
4 2
0 0
CL C
CR

**Figure 2** An example of how _C_ is obtained from _C<sup>L</sup>_ and _C<sup>R</sup>_. The blue ladder represents the border between the values that are inherited from _C<sup>L</sup>_ and the values that are inherited from _C<sup>R</sup>_. Ticks correspond to the core elements: the green ticks are inherited from _C<sup>L</sup>_, the red ticks are inherited from _C<sup>R</sup>_, and the blue ticks represent the core element computed from scratch.

