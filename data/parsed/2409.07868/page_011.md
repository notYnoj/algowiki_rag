As our main tool, we make use of the fact that for an arbitrary set of permutations there exists a decision tree whose height matches the information-theoretic lower bound up to an extra linear term.

**Theorem 4.2** (Fredman \[Fre76\])**.** _For every set_ \(\Gamma\) _of permutations of length n, there exists a decision tree of height at most_ \(log|\Gamma|+2n\) _that correctly sorts every_ \(\pi\in\Gamma\).

It follows by the Marcus-Tardos theorem \[MT04\] and the results of Cibulka \[Cib09\] that the number of \(\pi\)-avoiding permutations of length _n_ is bounded by \(c_\pi^{O(n)}\). Therefore, there is a decision tree of height \(O((logc_\pi+1)\cdot n)\) that correctly sorts every \(\pi\)-avoiding permutation of length _n_.

We construct an algorithm that receives several sequences of length _k_ on input and sorts each of them asymptotically in the same time as given by Theorem 4.2, without explicit knowledge of \(\Gamma\). The only caveat is that it needs an additional overhead that is roughly doubly exponential in _k_.

**Lemma 4.3.** _Let S_<sub>1</sub>_,...,S<sub>m</sub> be a set of permutation sequences, each of length k, and let_ \(\Gamma\) _be the set of all permutations order-isomorphic to some sequence S<sub>i</sub>. Algorithm 3 sorts all S<sub>i</sub>’s in time_ \(O((log|\Gamma|+k)\cdot m)+2^{2^{O(klogk)}}\).

We first provide an upper bound on the total number of decision trees of given height for sorting a sequence of length _k_. Note that we are neglecting here any optimization of the lower-order terms.

**Lemma 4.4.** _The number of decision trees of height at most h for sorting a sequence of length k is at most_ 2<sup>_h+o(k_)+_o(h_)</sup>.

_Proof._ Let us first count the number of such decision trees of height exactly _h_. Since the shape of the tree is given, the decision tree is completely determined by its labels. There are \(2^h-1\le 2^h\) internal nodes, each labeled by one of _k_<sup>2</sup> possible ordered pairs. Additionally, there are exactly 2_<sup>h</sup>_ leaves, each marked with a permutation of length _k_. Together, that makes the number of such decision trees of height _h_ at most<tbc>

\((k^2)^{2^h}\cdot(k!)^{2^h}\le 2^{2\cdot logk\cdot 2^h}\cdot 2^{k\cdot logk\cdot 2^h}\le 2^{2^{h+o(k)}}.\)

<tbc>We obtain the promised bound by summing over all heights up to _h_

\(h\cdot 2^{2^{h+o(k)}}\le 2^{2^{h+o(k)+o(h)}}.\)

(1,2)
(2,3)
(1,3)
(2,3)
(1,3)
(1,3)
(2,3)
1,2,3
1,2,3
1,3,2
3,1,2
2,1,3
2,1,3
2,3,1
3,2,1

Figure 2: A decision tree _T_ for sorting a sequence of length 3. A run on input sequence (_s_<sub>1</sub>_,s_<sub>2</sub>_,s_<sub>3</sub>)=(7,2,3) is highlighted and it reaches a leaf labeled by the permutation 2,3,1. Indeed, we have \(s_2\le s_3\le s_1\) and _T_ correctly sorts _S_. Notice that the tree contains many unnecessary branches since we require the decision trees to be full binary trees.

