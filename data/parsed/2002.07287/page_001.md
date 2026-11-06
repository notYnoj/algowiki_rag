# Sorting and Ranking of Self-Delimiting Numbers with Applications to Outerplanar Graph Isomorphism

**Frank Kammer** \(\unknown\)<br> THM, University of Applied Sciences Mittelhessen, Giessen, Germany

**Johannes Meintrup** \(\unknown\)<br> THM, University of Applied Sciences Mittelhessen, Giessen, Germany

**Andrej Sajenko** \(\unknown\)<br> THM, University of Applied Sciences Mittelhessen, Giessen, Germany

**Abstract**

Assume that an _N_-bit sequence _S_ of _k_ numbers encoded as Elias gamma codes is given as input. We present space-efficient algorithms for sorting, dense ranking and competitive ranking on _S_ in the word RAM model with word size \(\Omega(logN)\) bits. Our algorithms run in \(O(k+\frac{N}{logN})\) time and use _O(N_) bits. The sorting algorithm returns the given numbers in sorted order, stored within a bit-vector of _N_ bits, whereas our ranking algorithms construct data structures that allow us subsequently to return the dense/competitive rank of each number _x_ in _S_ in constant time. For numbers \(x\in IN\) with _x\>N_ we require the position _px_ of _x_ as the input for our dense-/competitive-rank data structure. As an application of our algorithms above we give an algorithm for tree isomorphism, which runs in _O(n_) time and uses _O(n_) bits on _n_-node trees. Finally, we generalize our result for tree isomorphism to forests and outerplanar graphs, while maintaining a space-usage of _O(n_) bits. The previous best linear-time algorithms for trees, forests and outerplanar graph isomorphism all use \(\Theta(nlogn)\) bits.

**2012 ACM Subject Classification** Mathematics of computing \(\rightarrow\) Graph algorithms

**Keywords and phrases** space efficient, sorting, rank, dense rank, tree isomorphism, forest isomorphism, outerplanar graph isomorphism

**Related Version** This is the full version of the paper [1], which includes proofs and result to forest and outerplanar graph isomorphism.

**Funding** J. Meintrup and A. Sajenko are funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 379157101.

### 1 Introduction

Due to the rapid growth of input data sizes in recent years, algorithmic solutions that optimize both run time and memory usage have become increasingly important. For this reason, we focus on _space-efficient_ algorithms, i.e., algorithms that run (almost) as fast as standard solutions for the problem under consideration, while decreasing the required space by more than an asymptotic constant.

Graphs are often used to encode structural information in many fields, e.g., in chemistry or electronic design automation. Isomorphism testing on these graphs can then be used for identifying a chemical compound within a large chemical database [2]. Moreover, it is the basis for a verification whether large electric circuits represented by a circuit schematic and an integrated circuit layout correspond [3].

**Model of Computation.** Our model of computation is the word RAM, where we assume to have the standard operations to read, write as well as arithmetic operations (addition, subtraction, multiplication, modulo, bit shift, **AND** and **OR**) take constant time on words of size \(w=\Omega(logN)\) bits where _N_ is the input size in bits. (In our paper log is the

