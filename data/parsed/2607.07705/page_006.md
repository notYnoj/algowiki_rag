leave the complexity for complete digraphs as an open question. There is also a related line of works \[CGJ<sup>+</sup>10, CFG<sup>+</sup>11, CGJY12\] on weighted CSPs for linear systems over F<sub>2</sub>, parameterized above or below guarantees, where the parameter _k_ is also the excess weight.

### Organization of the paper.

In the next section, we introduce the notation used throughout the paper and provide some preliminary results. In Section 3, we introduce definitions and properties of edges around MaxST(_G,_**w**) that are fundamental to our approach. In Section 4, we provide our proof of Theorem 1, supporting it with necessary intuition and discussion. In Section 5, we give the proof of Theorem 2 in the same way.

## 2 Preliminaries

### Notation.

We use standard graph terminology and notation (we refer the reader to the book of Diestel \[Die17\]). We also use several additional notions. We use _G-S_ to denote a graph obtained by deleting all edges of _S_ from _G_. We write _G+S_ to denote a graph obtained by adding all edges of _S_ to _G_. We refer to both undirected and directed edges as just _edges_, the actual variant is always clear from the context.

For a graph (_G,_**w**) with edge weights, we always assume that **w** is additively extended to all subsets of edges. That is, for each \(S\subseteq E(G)\), we have \(\mathbf{w}(S)=\sum_{e\in S}\mathbf{w}(e)\). For a subgraph \(X\subseteq G\), we also shorten the notation **w**(_E(X_)) to just **w**(_X_).

For the comprehensive introduction to parameterized algorithms and terminology of parameterized complexity, we refer the reader to the Parameterized Algorithms book \[CFK<sup>+</sup>15\].

### Partially ordered sets.

A _partially ordered set_ (poset for short) is an ordered pair \(\mathcal{P}=(X,\unknown)\) where _X_ is a set and \(\unknown\) is a partial order on _X_. A relation \(\unknown^*\) is called a _linear extension_ of P if it is a total order on _X_ that is compatible with \(\unknown\), that is, for all \(x,y\in X\), \(x\unknown y\) implies \(x\unknown^*y\).

The _order dimension_ of a poset \(\mathcal{P}=(X,\unknown)\) is the least integer _t_ for which there exists a family \((\unknown_1,\unknown_2,\dots,\unknown_t)\) of linear extensions of P with the following property: for each \(x,y\in X\), it holds that \(x\unknown y\) if and only if \(x\unknown_iy\) for all _i_. This concept was introduced by Dushnik and Miller in \[DM41\]. We will use the following result on the order dimension.

**Proposition 1** (\[TM77\], \[AS26\])**.** _Let T be an oriented tree, and let_ \(\mathcal{P}=(V(T),\unknown)\) _be a poset such that for each_ \(u,v\in V(T)\), \(u\unknown v\) _if and only if there exists a directed path from u to v in T. Then the order dimension of_ P _is at most three, and the corresponding linear extensions_ \((\unknown_1,\unknown_2,\unknown_3)\) _of_ P _can be constructed in polynomial time._

Trotter and Moore \[TM77\] proved that the order dimension of such posets is at most three, but they did not explicitly state the existence of a polynomial-time algorithm that constructs the corresponding linear extensions. Although such an algorithm follows from their proof, we refer to a recent work of Abram and Segovia for a more direct construction (see Corollary 6.3 in \[AS26\]).

## 3 Classification of directed edges and their basic properties

In this section, we introduce the basic toolbox that we use extensively throughout our proof. Our tools are mostly related to classification of edges of _G_ relative to its MaxST and several useful properties surrounding this classification for _arbitrary positive edge weights_.

