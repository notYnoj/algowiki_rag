# A Framework for Parameterized Subexponential-Subcubic-Time Algorithms for Weighted Problems in Planar Graphs

**Abstract**

Many problems are known to be solvable in subexponential parameterized time when the input graph is planar. The bidimensionality framework of Demaine, Fomin, Hajiaghay, and Thilikos [JACM ’05] and the treewidth-pattern-covering approach by Fomin, Lokshtanov, Marx, Pilipczuk, Pilipczuk, and Saurabh [SICOMP ’22] give robust tools for designing such algorithms. However, there are still many problems for which we do not know whether subexponential parameterized algorithms exist. The bidimensionality framework is not able to handle weights or directed graphs and the treewidth-pattern-covering approach only works for finding connected solutions. Building on a result by Nederlof [S ’20], we provide a framework that is able to solve a variety of problems in planar graphs in subexponential parameterized time for which this was previously not known (where the polynomial part of the running time is usually O(_n_<sup>2.49</sup>)). Our framework can handle weights, does not require solutions to contain only few connected components, and applies to cases where the number of potential patterns of a solution is exponential in the parameter.

We then use the framework to show that various weighted problems like Weighted Partial Vertex Cover, Maximum-Weight Induced Forest, Minimum-Weight Rooted Simple Minor, and Maximum-Weight Rooted Parallel Induced Minor allow for subexponential parameterized algorithms. This was previously not known for any of them. Moreover, we present a very easy-to-use fragment of our framework that is still powerful enough to be applicable to problems like Densest _k_-Subgraph, Maximum-Weight Independent Set, Maximum (_k,n-k_)-Cut, and Weighted Partial Vertex Cover. This fragment allows for significantly simpler proofs in the case of Maximum-Weight Independent Set and Maximum (_k,n-k_)-Cut and is able to show a subexponential parameterized algorithm for weighted versions of Densest _k_-Subgraph. Even the unweighted version was not known before and is stated as an open problem in the existing literature.

Matthias Bentert Fedor V. Fomin Petr A. Golovach

arXiv:2604.00891v1 [cs.DS] 1 Apr 2026

