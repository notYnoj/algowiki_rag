## 4 Asteroidal Triples and Friends in (Likely Necessary) Matrix Multiplication Time

OV and Triangle detection are central problems in fine-grained complexity. Simplicial Vertex has been used only a handful of times as a source of hardness. Nevertheless, it is a very natural problem. In fact, the three hard problems that Kratsch and Spinrad propose are just different quantifications of the following form:

\(Q_1x\in V,Q_2y\in N(x),Q_3z\in N(x):(y,z)\in E.\) (1)

Triangle detection has quantifiers \(Q_1Q_2Q_3=\exists\exists\exists\exists\) in Equation (1), Simplicial Vertex has \(Q_1Q_2Q_3=\exists\forall\forall\), and OV in _n_ dimensions (and dominated vertex) is equivalent to the case \(Q_1Q_2Q_3=\exists\exists\forall\) (this requires a bit of a proof since we need \(y\in N(x)\) - see Section B in the appendix). Kratsch and Spinrad [KS06] provide evidence that tight reductions between these different quantifications might be difficult due to an inherent difference in the non-deterministic complexity of the problems. Nevertheless, we do know that _fine-grained subcubic_ (but non-tight w.r.t. \(n^\omega\)) reductions exist from Simplicial Vertex and Dominated Vertex to Triangle Detection because both these problems can be solved using Boolean Matrix Multiplication (BMM) and BMM is fine-grained equivalent to Triangle Detection [WW10, VW18].

## Our Results

We show that all the problems presented by Spinrad and Kratsch can be solved in \(\tilde{\mathcal{O}}(n^\omega)\) time. <sup>4</sup> Therefore, none of the presented problems fit into the aforementioned category of intermediate problems. If one is willing to believe that _n_-dimensional OV, Simplicial Vertex, and Triangle Detection all require \(n^{\omega-o(1)}\) time, then our algorithms are also optimal.

We start with neighborhood-deleted components, noting that this is equivalent to a more general problem that we call the _induced subgraph connected component_ problem: Given an _n_-vertex graph **G**=(_V,E_) and a family of subsets S of _V_ , compute the connected components of **G**[_S_] for each \(S\in\mathcal{S}\). This equivalence can easily be seen to hold for \(|\mathcal{S}|=\Theta(n)\): in one direction, we choose the sets to be the graphs obtained by deleting the (closed) neighborhoods; in the other direction, we introduce a clique containing one vertex for each \(S\in\mathcal{S}\), where each such vertex’s neighbors are exactly the vertices not in its corresponding set _S_.

We show that the induced subgraph connected component problem is _equivalent_ to multiplying an \(|\mathcal{S}|\times n\) Boolean matrix by an \(n\times n\) Boolean matrix. <sup>5</sup> This equivalence demonstrates that we can compute the connected components of multiple graphs more efficiently, provided they are all induced subgraphs of a single underlying graph.

**Main Theorem 1.** _There is a deterministic algorithm that solves the induced subgraph connected component problem in time_ \(\tilde{\mathcal{O}}(\mathrm{MM}(|\mathcal{S}|,n,n))\) _for an n-node input graph and a non-empty input set_ S.

<sup>4</sup> To be precise, we show this for all problems in the journal version of [KS06]. The conference version contains one additional problem (finding clique cutsets) for which an \(\mathcal{O}(n^\omega)\)-time algorithm was found concurrently [HTV05]. Later, this result was extended to cliqueset decompositions in matrix multiplication time [CD18]. <sup>5</sup> We note that one (perhaps minor) reason we present this result for the induced subgraph connected component problem, as opposed to neighborhood deleted components, is that this equivalence with rectangular Boolean matrix product holds even when \(|\mathcal{S}|=\omega(n)\).

Hard as Triangle-Free Recognition: Recognizing AT-free graphs, finding a dominating pair, verifying a specific vertex pair is a dominating pair, identifying all extremities.
Hard as Testing for a Dominated Vertex/High Dimensional OV: Determining whether a graph has a two-pair, determining whether a graph has a star cutset.
Hard as Testing for a Simplicial Vertex: Determining whether a graph has a clique cutset.

**Figure 1.** Hardness of the problems solved in [KS06].

