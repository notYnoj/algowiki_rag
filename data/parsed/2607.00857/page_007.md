\(\blacktriangleright\) **Problem 2** (APSP Certificate Learning)**.** _Given k APSP instances G_<sub>1</sub>_,...,G<sub>k</sub> on the same vertex set V, and parameters p, q, output a certificate C, with_ |_C[u,v_]|=_q for every_ \(u,v\in V\) _, that minimizes the average prediction error_ \(\frac{1}{k}\sum_{i=1}^k\eta(G_i,C,p)\).

In Section 6, we show that this problem is, unfortunately, NP-hard to solve exactly. However, in our context, a constant-factor approximation algorithm would be entirely sufficient, because a constant-factor loss in the prediction error translates to a constant-factor loss in the running time of our APSP algorithm, which anyway vanishes in the big-O notation. We leave it as open problem to find such an approximation algorithm (see Section 1.3).

## 1.3 Open problems

We state two important open problems we are left with. The first is about improving and generalizing our error measure, the second is about learning certificates.

Cleaner prediction error measure. A pair of vertices (_u,v_) can contribute to our error measure \(\eta\) in two ways. The first way is when the computed distance estimate _D[u,v_] from Stage 1 is not the correct distance. The second way is when we cannot verify the distance estimate _D[u,v_] in the second stage of our algorithm.

The second term seems unavoidable, because we need a way to beat cubic time while verifying correctness of the distance matrix. To our best knowledge, the co-nondeterministic algorithm from [12] is the only suitable one among known ways to achieve that. However, we see no apparent reason why it should not be possible to remove the first term entirely from the error.

\(\blacktriangleright\) **Open Problem 1.** _Can we remove the term_ \(|\{(u,v):D[u,v]\neq d(u,v)\}|\) _from the definition of the prediction error_ \(\eta\)?

Notice that if the first term is significantly larger than the second term, there is an incorrect entry _D[u,v_] such that many shortest paths contain a subpath from _u_ to _v_. One approach to solve such a case could be to rerun the first stage of our algorithm once an incorrect entry is corrected. The correction could then propagate to all superpaths, without spending linear time for each of them. Making such an approach work formally could require phrasing the error in a more direct way without a distance estimate matrix. A better understanding of the error term could also help in extending our approach to problems with fine-grained lower bounds based on APSP.

Approximate learning algorithm. Our hardness proof of the learning problem in Section 6 shows that we cannot hope to compute an optimal certificate for a collection of graphs exactly. Naturally, one could resort to looking for an approximately optimal certificate. The first question to answer is what should be approximated; we could aim for approximation of the error, or allow to compute a larger certificate than the optimal one that we compare against. Relaxing both of these conditions is known as bicriteria approximation, which is certainly interesting in our setting, since a certificate that is larger by a factor of _c_ only adds at most the same factor _c_ to the running time.

\(\blacktriangleright\) **Open Problem 2.** _What is the best bicriteria approximation for Problem 2?_

Solving instances like the one in our hardness proof requires computing a set of _k_ vertices in a hypergraph that induces the maximum number of edges, that is, Densest _k_-Subgraph (D_k_S) in hypergraphs. For D_k_S in standard graphs, only an O(_n_<sup>1/4</sup>)-approximation is known [9],

