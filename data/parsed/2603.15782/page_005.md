In 2024, Lau, Tung, and Wang \[28\] published a result implying a \(O(\sqrt{logn/\varepsilon})\)-approximation for the "vertex expansion" problem in \(O(n^{O(\varepsilon)})\) maximum flow computations, for a parameter \(\varepsilon\) similar to ours. This consequently implies a \(O(\sqrt{logn/\varepsilon})\)-approximation for the balanced vertex separators in \(O(n^{1+O(\varepsilon)})\) maximum flow computations via a standard reduction \[18\]. Unfortunately, their analysis omits consideration of bit-complexity, and so faces the same issue as Arora and Kale’s work (although it is again likely possible to handle with a more careful derivation).

## 1.3 Technical Overview

The overall structure of our algorithm is closest to the methods of Arora and Kale and follow-up works \[3, 40, 24\] for the balanced (edge) separator problem. Accordingly, we first give a brief overview of the latter problem, and discuss the precise point at which the same approach fails, requiring new ideas. Our method also bears some similarities to a slightly different approach of Lau, Tung, and Wang \[28\] for the directed edge expansion problem, and we discuss where this approach fails as well. Both of these previous works, as well as ours, make use of the "Matrix Multiplicative Weights Update" algorithm (MMWU), which is an online learning algorithm for the so-called "Matrix game" \[3, Algorithm 1\]. However, their implementations of this algorithm differ significantly.

### Balanced edge separator

First, the methods of Arora and Kale define an SDP relaxation of the problem that involves vector-valued variables \(v_i\in\mathbb{R}^n\) for each node \(i\in V\) . This relaxation is then approximately solved using a primal-dual Matrix Multiplicative Weights Update **framework** \[3, Algorithm 2\] (called the "Primal-Dual Algorithm for SDPs" in the cited version of their work), which internally runs the MMWU algorithm while maintaining the variables _v<sub>i</sub> explicitly_. The main subroutine of the primal-dual MMWU framework is a procedure called Oracle that does the following: given the current primal solution (i.e. vectors _v<sub>i</sub>_), it either finds a balanced separator of small cost, or finds an inequality violated by this solution (specified by dual variables). This inequality is then used to update vectors _v<sub>i</sub>_. This pair of valid outputs is key to keeping the "width" low, which in turn allows for a fast time complexity.

Different implementations of the oracle are presented in \[3\], \[40\] and in \[24\]. In particular, the oracle in \[24\] works by running a sequence of maximum flow computations, extracting directed matchings from these computations (via flow decompositions), and then "chaining" together these matchings.

### Sparse directed edge cuts

Lau, Tung, and Wang take an alternative approach to integrating the MMWU algorithm into their problem. There is a natural SDP relaxation of their problem as well, but it would naturally involve both a vector-valued variable \(v_i\in\mathbb{R}^n\) and a separate real- valued variable \(r_i\in\mathbb{R}\) for each node \(i\in V\) , with surprisingly challenging inequalities relating these two (see also \[27\] for related SDPs with similar structure). The standard primal-dual MMWU framework has no way to handle this structure, so Lau, Tung, and Wang instead use a min-max form of their problem, with outer vector-valued variables \(v_i\in\mathbb{R}^n\). In their case, the constraints on the vector-valued variables in this min-max form happen to coincide with precisely the guarantees that are maintained by the MMWU algorithm at all times. They then construct another Oracle procedure that either solves the inner problem in a way that has low "width", or outputs a combinatorial solution.

Importantly, their approach to analysis is rather ad-hoc, and only seems applicable to their specific problem, while making constraints like balance much more difficult to handle nicely.

On the technical level, our work introduces two new ideas, which are described below.

### Technical contribution #1: partial variable MMWU framework

For simplicity, let us consider vertex separators. We start by defining an SDP relaxation of the problem which is a variant of the SDP for the balanced edge separator (and distinct from previous SDP relaxations for balanced vertex separators such as the SDP of Feige-Hajiaghayi-Lee \[18\]). Besides variables<tbc>

