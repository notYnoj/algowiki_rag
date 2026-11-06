<tbc>\[AP72, Sah17, BGHS19\]), RNA Folding \[NJ80, Aku99, ZTZU11, VGF14, Sah17\] and Dyck Edit Distance \[Sah14, BGHS19, DKS22, FGK<sup>+</sup>24\]. All of these problems now have \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) time algorithms.

As TED seems related to APSP and since its unweighted version is now known to have a truly subcubic algorithm, a natural question is:

_Question 3: Can unweighted TED be solved in_ \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) _time?_

Mao’s truly subcubic time algorithm for unweighted TED \[Mao22\] can be viewed as a reduction to Bounded Monotone Min-Plus product which can be solved in \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) time. The reduction, however, is not efficient enough to achieve the same running time for unweighted TED. One way to resolve Question 3 is by presenting a tight reduction. Is such a reduction possible?

## Our Results.

We resolve all three questions above. Similarly to the prior work on TED, we focus on solving the more general edit distance problem on ordered _forests_ (rather than just single trees): collections of rooted trees with a left-to-right ordering. Our first main theorem is a fine-grained reduction from (forest) TED to the Min-Plus product problem mentioned earlier:

\(\text{\textbf{Min-Plus Matrix Multiplication (MUL)Input:} Two}m\times m\text{matrices}A=(a_{i,j})\text{and}B=(b_{i,j})\text{.
\textbf{Output:} The distance matrix}C=A\star B\text{, where}C=(c_{i,j})\text{is defined as}c_{i,j}=min_{k\in[1..m]}\{a_{i,k}+b_{k,j}\}\text{.}\)

Let T<sub>MUL</sub>(_N_) denote the running time for solving MUL on two \(N\times N\) matrices, or equivalently (\[FM71\]) for solving APSP in _N_ node graphs.

The formal theorem for our reduction is as follows:

\(\includegraphics{}\text{\textbf{Main Theorem 1.} \textit{Let}}\mathbf{F},\mathbf{F}'\text{\textit{be forests of size}}n=|\mathbf{F}|,m=|\mathbf{F}'|\text{\textit{with}}n\ge m\text{\textit{. Then, there is an algorithm computing Tree Edit Distance between}}\mathbf{F},\mathbf{F}'\text{\textit{in time}}\tilde{\mathcal{O}}\left((n/m)^{1+o(1)}\cdot\left(\mathsf{T}_{MUL}(m)+m^{2+o(1)}\right)\right)\text{.}\)

If _m=n_, the theorem states that TED on _n_-node forests can be solved in \(\tilde{\mathcal{O}}(\mathsf{T}_{MUL}(n))\). We thus complete the missing direction in establishing the equivalence between TED and APSP, resolving Question 2.

In fact, because our reduction is very efficient and only adds polylogarithmic factors over the APSP running time, we are also able to resolve Question 1 using Williams’ \[Wil18\] \(m^3/2^{\Omega(\sqrt{logm})}\) running time for APSP.

\(\includegraphics{}\text{\textbf{Corollary 1.1.} \textit{Let}}\mathbf{F},\mathbf{F}'\text{\textit{be forests. Then, there is an algorithm for TED running in time}}n^3/2^{\Omega(\sqrt{logn})}\text{\textit{, where}}n=max(|\mathbf{F}|,|\mathbf{F}'|)\text{.}\)

Beyond providing a faster algorithm for TED, Corollary 1.1 underscores once again the difference in nature between ED and TED by demonstrating that, while we (probably) cannot eliminate an arbitrary number of logarithmic factors for the former, we can do so for the latter.

The last several TED algorithms (prior to ours) all use the same dynamic programming approach which was formalized as a decomposition framework for solving TED \[DT03, DT05\]. Formalizing the framework allowed for proving lower bounds on the running time of any algorithm that falls into that framework. The first such lower bound was by \[DT03\] who showed such algorithms must take \(\Omega(n^2log^2n)\) time. The approach culminated in obtaining an \(\Omega(n^3)\) time lower bound \[DMRW10\] for any algorithm that falls within the framework. Since our algorithm runs faster than cubic time, it falls outside the framework.

