**Algorithm 3** Algorithm for sorting \(\pi\)-avoiding sequences S<sub>1</sub>,...,S<sub>m</sub> of length k.

\(T\leftarrow\) first decision tree in the enumeration sequence<br>
for \(i\in\{1,\dots,m\}\) do<br>
   \(\sigma\leftarrow\) the result of applying T on \(S_i=s_1^i,\dots,s_k^i\)<br>
   while \(s_{\sigma_1}^i,\dots,s_{\sigma_k}^i\) is not sorted do<br>
   \(T\leftarrow\) next decision tree in the enumeration sequence<br>
   \(\sigma\leftarrow\) the result of the run of T on S<sub>i</sub><br>
   \(S_i\leftarrow s_{\sigma_1}^i,\dots,s_{\sigma_k}^i\triangleright\) Sorting S<sub>i</sub>.

Let us take a brief detour and sketch how a prior knowledge of \(\pi\) can be used to efficiently sort many \(\pi\)-avoiding sequences of length k. Knowing \(\pi\), we first compute the set of all \(\pi\)-avoiding permutations of length k by enumerating all permutations of length k and testing for pattern- avoidance. Afterwards, we enumerate all the decision trees of height \(O((\mathrm{log}c_\pi+1)\cdot k)\) and for each of them, we test whether it successfully sorts all the precomputed \(\pi\)-avoiding permutations of length k. All of this can be done in \(2^{O((\mathrm{log}c_\pi+1)\cdot k)}\) time. Once we find a suitable decision tree guaranteed by Theorem 4.2, we simply apply it on every input sequence in \(O((\mathrm{log}c_\pi+1)\cdot k)\) time for a total of \(O((\mathrm{log}c_\pi+1)\cdot n)\). Note that this approach follows closely the use of decision trees in the celebrated asymptotically optimal algorithm for minimum spanning tree by Pettie and Ramachandran \[PR02\].

However, we propose a more elegant solution that does not require prior knowledge of \(\pi\) and additionally works for sets of permutations defined through different means than pattern avoidance. Rather than computing the optimal decision tree upfront, we work with a candidate tree instead. For each sequence S<sub>i</sub> on input, we try applying the current decision tree T on S<sub>i</sub> and test in O(k) time whether T sorts S<sub>i</sub>. If that is the case, we move on to the next sequence with the same decision tree. Otherwise, we throw away the current decision tree, replace it with a different one, and try sorting S<sub>i</sub> again.

## Description of the algorithm.

Now, we describe the algorithm in full detail. Recall that we are given m sequences S<sub>1</sub>,...,S<sub>m</sub> of length k on input. For now, assume that each S<sub>i</sub> is a permutation sequence.

Let T<sub>1</sub>,T<sub>2</sub>,... be an arbitrary enumeration of all the decision trees for sorting a sequence of length k in the increasing order given by their heights, starting with the decision trees of height exactly k. For now, we just assume that we can efficiently enumerate them in this order, leaving the implementation details for later. The algorithm keeps a current candidate for the optimal decision tree T. At the beginning, we set \(T\leftarrow T_1\).

Now, for each S<sub>i</sub>, we do the following. The algorithm computes the result \(\sigma\) of the run of the tree T on S<sub>i</sub>. If T sorts S<sub>i</sub>, i.e. we have \(s_{\sigma_1}\le\cdots\le s_{\sigma_k}\), the algorithm accordingly rearranges S<sub>i</sub> and moves on to the next sequence on input. Otherwise, the algorithm changes T to the next decision tree in the enumeration sequence and repeats the previous step. See Algorithm 3.

If the algorithm terminates, it clearly sorts all the input sequences, since it moves to the next sequence only after it verifies that the current sequence is sorted. Moreover, all sequences of length k can be sorted by a decision tree of height O(klogk), and thus the algorithm must eventually reach a decision tree capable of sorting all input. It follows that the algorithm always terminates and correctly sorts all the sequences on input. It remains to bound its running time.

