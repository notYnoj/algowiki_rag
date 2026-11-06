### BSTs and dynamic optimality.

Arguably, the most famous open question related to sorting is the _dynamic optimality conjecture_ \[ST85\] asking whether the splay tree is an instance-optimal online BST balancing strategy. More recently, the conjecture is usually rephrased as asking whether there exists _any_ instance-optimal online BST strategy with GreedyFuture being the other prime candidate alongside splay trees. Observe that any instance-optimal balancing strategy must also work within the bounds proved for GreedyFuture \[CGK<sup>+</sup>15, CGJ<sup>+</sup>23, CPY24\] and thus, any such strategy can be used to sort pattern-avoiding sequences in near-linear time. However, none of these results implies that an instance-optimal BST strategy must sort pattern-avoiding sequences in linear time, and it has been raised as an open question \[CGK<sup>+</sup>15\] whether this is, in fact, a corollary of dynamic optimality. Berendsohn, Kozma and Opler \[BKO24\] resolved this question positively by showing that any instance-optimal BST balancing strategy sorts \(\pi\)-avoiding sequences in time \(O(c_\pi^2n)\). They construct an offline sequence of BST modifications that accommodates a given \(\pi\)- avoiding input with linear cost. However, an \(\Omega(nlogn)\) time is still needed for the computation of this sequence and therefore, this result in itself does not imply the existence of a linear-time algorithm for sorting pattern-avoiding sequences.

### Twin-width.

Lastly, there is a close connection between pattern avoidance and the recently emerging notion of twin-width. Without going into too much detail, twin-width is a structural parameter introduced for permutations by Guillemot and Marx \[GM14\], and later extended to graphs and arbitrary relational structures by Bonnet, Kim, Thomassé and Watrigant \[BKTW22\]. Guillemot and Marx \[GM14\] showed that the twin-width of any \(\pi\)-avoiding permutation is at most \(O(c_\pi)\) and conversely, any permutation of twin-width _d_ avoids a certain pattern \(\pi\) with \(c_\pi=2^{O(d)}\). As a result, bounded twin-width can been exploited to prove properties of pattern-avoiding permutations and sequences \[BBGT24, BKO24\].

## 1.1 Our result

Our main result is an asymptotically optimal sorting algorithm for pattern-avoiding sequences that matches the information-theoretic lower bound for each \(\pi\) up to a global constant.

**Theorem 1.1.** _There is an algorithm that sorts a_ \(\pi\)_-avoiding sequence S of length n in_ \(O((logc_\pi+1)\cdot n)\) _time even if_ \(\pi\) _is a priori unknown._

The algorithm is built from two components. The first one is an efficient multi-way merge procedure capable of merging up to \(\frac{n}{logn}\) sequences with _n_ elements in total, as long as the sequences originate from a \(\pi\)-avoiding input. Its analysis is heavily based on the Marcus-Tardos theorem \[MT04\].

The second component is an efficient algorithm to sort a large set of short sequences. Naturally, many sequences in such a set must be pairwise order-isomorphic, which suggests that we could try grouping them into equivalence classes and then actually sorting only one sequence from each class. Unfortunately, computing the equivalence classes is in some sense as hard as sorting itself. Instead, we take a different approach of guessing a shallow decision tree for sorting \(\pi\)-avoiding permutations guaranteed by the result of Fredman \[Fre76\].

Theorem 1.1 follows by first cutting up the input into sequences of length roughly logloglog_n_ which we can efficiently sort using the optimal decision tree. The sorted sequences then serve as a basis for a bottom-up merge sort using the efficient multi-way merge.

Furthermore, let us point out that Theorem 1.1 achieves the information-theoretic lower bound for arbitrary \(\pi\)-avoiding sequences, not only permutations. This is in sharp contrast with previous works \[CGK<sup>+</sup>15, BKO24\] where the generalization beyond permutations comes with a price of<tbc>

