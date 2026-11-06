comparison based algorithms, thus settling the complexity of integer sorting under the conjecture by Li and Li.

## 1.1 Network Coding

The field of network coding studies the following communication problem over a network: Given a graph _G_ with capacity constraints on the edges and _k_ data streams, each with a designated source-sink pair of nodes (_s<sub>i</sub>,t<sub>i</sub>_) in _G_, what is the maximum rate at which data can be transmitted concurrently between the source-sink pairs? A simple solution is to forward the data as indivisible packages, effectively reducing the problem to Multicommodity Flow (MCF). The key question in network coding, is whether one can achieve a higher rate by using coding/bit-tricks. This question is known to have a positive answer in directed graphs, where the rate increase may be as high as a factor \(\Omega(|G|)\) (by sending XOR’s of carefully chosen input bits), see e.g. [1]. However the question remains wide open for undirected graphs where there are no known examples for which network coding can do anything better than the Multicommodity Flow rate. The lack of such examples resulted in the following central conjecture in network coding:

**Conjecture 1 (Undirected** _k_**-pairs Conjecture [15])** _The coding rate is equal to the Multicommodity Flow rate in undirected graphs._

Despite the centrality of this conjecture, it has so forth resisted all attempts at either proving or refuting it. Adler et al. [1] made an exciting connection between the conjecture and lower bounds for algorithms. More concretely, they proved that if Conjecture 1 is true, then one immediately obtains non-trivial lower bounds for all of the following:

• _Oblivious_ external memory algorithms.<tbc>

• _Oblivious_ word-RAM algorithms.<tbc>

• _Oblivious_ two-tape Turing machines.

In the above, _oblivious_ means that the memory access pattern of the algorithm (or tape moves of the Turing machine) is fixed and independent of the input data. Thus proving Conjecture 1 would also give the first non-trivial lower bounds for all these classes of algorithms. One can view this connection in two ways: Either as exciting conditional lower bounds for (restricted) algorithms, or as a strong signal that proving Conjecture 1 will be very difficult.

In this paper, we revisit these complexity theoretic implications of Conjecture 1. Our results show that the restriction to oblivious algorithms is unnecessary. In more detail, we show that Conjecture 1 implies non-trivial (and in fact tight) lower bounds for external memory sorting of integers and for external memory matrix transpose algorithms. We also obtain tight lower bounds for word-RAM sorting algorithms when the word size is much larger than the key size, as well as tight lower bounds for transposing a \(b\times b\) matrix on a word-RAM with word size _b_ bits. The striking thing is that our lower bounds hold without _any_ extra assumptions such as _obliviousness_, _indivisibility_, _comparison-based_ or the like. Thus proving Conjecture 1 is as hard as proving superlinear algorithm lower bounds in the full generality word-RAM model, a barrier far beyond current lower bound techniques! Moreover, we show that the assumption from previous papers about algorithms being oblivious makes a huge difference for integer sorting: We prove an \(\Omega(nlgn)\) lower bound for sorting \(\Theta(lgn)\) bit integers using an oblivious word-RAM algorithm with word size \(\Theta(lgn)\) bits. This is in sharp contrast to the classic (non-oblivious) Radix Sort algorithm, which solves the problem in _O(n_) time. Thus the previous restriction to oblivious algorithms may be very severe for some problems.

