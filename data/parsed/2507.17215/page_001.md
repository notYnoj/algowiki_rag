# Triadic First-Order Logic Queries in Temporal Networks

### Abstract

Motif counting is a fundamental problem in network analysis, and there is a rich literature of theoretical and applied algorithms for this problem. Given a large input network _G_, a motif _H_ is a small "pattern" graph indicative of special local structure. Motif/pattern mining involves finding all matches of this pattern in the input _G_. The simplest, yet challenging, case of motif counting is when _H_ has three vertices, often called a _triadic_ query. Recent work has focused on _temporal graph mining_, where the network _G_ has edges with timestamps (and directions) and _H_ has time constraints. Such networks are common representations for communication networks, citation networks, financial transactions, etc.

Inspired by concepts in logic and database theory, we introduce the study of _thresholded First Order Logic (FOL) Motif Analysis_ for massive temporal networks. A typical triadic motif query asks for the existence of three vertices that form a desired temporal pattern. An _FOL_ motif query is obtained by having both existential and thresholded universal quantifiers. This allows for a query semantics that can mine richer information from networks. A typical triadic query would be "find all triples of vertices _u,v,w_ such that they form a triangle within one hour". A thresholded FOL query can express "find all pairs _u,v_ such that for half of _w_ where (_u,w_) formed an edge, (_v,w_) also formed an edge within an hour".

We design the first algorithm, FOLTY, for mining thresholded FOL triadic queries. The theoretical running time of FOLTY matches the best known running time for temporal triangle counting in sparse graphs. Specifically, FOLTY runs in time \(O(ma\mathrm{log}\sigma_\mathrm{max})\). Here, _m_ is the number of temporal edges in the input graph, \(\alpha\) is the maximum core number (degeneracy), and \(\sigma_\mathrm{max}\) is the maximum edge multiplicity. We give an efficient implementation of FOLTY using specialized temporal data structures. FOLTY has excellent empirical behavior, and can answer triadic FOL queries on graphs with nearly 70M edges is less than hour on commodity hardware. Our work has the potential to start a new research direction in the classic well-studied problem of motif analysis.

### CCS Concepts

• **Theory of computation** \(\rightarrow\) **Graph algorithms analysis**; • **Information Systems** \(\rightarrow\) _Data Mining;Social Networks._

### Keywords

Motif counting, temporal network, First Order Logic, subgraph counting, triangle counting

**ACM Reference Format:**

Omkar Bhalerao, Yunjie Pan, C. Seshadhri, and Nishil Talati. 2018. Triadic First-Order Logic Queries in Temporal Networks. In _Proceedings of Make sure to enter the correct conference title from your rights confirmation email (Conference acronym ’XX)_. ACM, New York, NY, USA, 18 pages. https://doi. org/XXXXXXX.XXXXXXX

### 1 Introduction

Triangle counting is a fundamental problem in network analysis, that has been extensively studied in the literature [2, 17, 18, 20, 21, 24, 40, 41, 47, 48, 54, 56, 60]. This problem has found many applications in network analysis [19], synthetic graph generation [46], indexing graph databases [23], and discovering communities [18, 36]. Many real-world networks are _temporal_, meaning that edges have timestamps. For instance, consider the financial network of a bank, in which the nodes represent bank accounts, and directed edges represent transfer of money between accounts [10, 13, 25]. Over the past few years, there has been research on defining and counting temporal motifs, which incorporate time and ordering constraints on edges [12, 25-27, 31, 38, 50-52]. Temporal triangle/motif counts have proven to be useful in a multitude of applications such as network classification [55], temporal text network analysis [57], analyzing financial networks [16, 29], etc.

Motif (especially triangle) counting is an extremely powerful technique in graph mining. Yet, it is unable to capture richer patterns such as the following. Suppose we want to find edges (_u,v_) of the network where: whenever _u_ makes a transaction to _w_, then _w_ makes a transaction to _v_ within an hour. Clearly, this is related to triangles involving _u,v,w_, but observe that _w_ is not a fixed vertex. _How can we express such richer patterns in terms of motifs?_

### 1.1 First Order Logic Motifs

We take inspiration from the concept of First Order Logic (FOL) statements in logic and database theory. The study of this concept is ubiquitous in database theory and parameterized graph theory [1, 5, 7, 11, 14], logic and designing AI expert systems [33, 35, 42].

Omkar Bhalerao<br> University of California, Santa Cruz<br> Santa Cruz, USA<br> obhalera@ucsc.edu

C. Seshadhri<br> University of California, Santa Cruz<br> Santa Cruz, USA<br> sesh@ucsc.edu

Yunjie Pan<br> University of Michigan, Ann Arbor<br> Ann Arbor, USA<br> panyj@umic.edu

Nishil Talati<br> University of Michigan, Ann Arbor<br> Ann Arbor, USA<br> talatin@umich.edu

arXiv:2507.17215v1 [cs.DB] 23 Jul 2025

