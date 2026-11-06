we still maintain the invariant, while the added redundancy (i.e., the non-existing edges) allows us to pre-allocate a set of edges that could potentially be added to G in the future, ensuring that the cut value of (_S,T_) remains at most \(f-k'-1\).

**Definition 3.6** (Witness)**.** _Let_ G=(_V,E_) _be an unweighted undirected graph with two designated terminals s and t. A tuple_ W=(_S,T,Y_) _is called a_ witness _of_ G _if the following conditions hold:_

1. (_S,T_) _is an s-t cut of_ G _with value_ \(|E_\mathcal{G}(S,T)|\le f-k'-1\).<tbc>

_2._ \(Y\subseteq S\times T\) _such that_ \(|Y|=f-k'-1\) _and_ \(E_\mathcal{G}(S,T)\subseteq Y\).

_Finally, let_ W(G) _denote the set of all witnesses of_ G.

Notice that the notion of _Y_ here is consistent with \(E_\mathcal{G}(S,T)\cup X\) as explained in the previous paragraph. For clarity, we may relax the notation and write a witness as \((S,T,E_\mathcal{G}(S,T)\cup X)\) if needed. However, it is crucial to view _Y_ as a union of _E_<sub>G</sub>(_S,T_) and _X_ rather than two individual sets _E_<sub>G</sub>(_S,T_) and _X_.

**Invariant 3.7** (Witness Invariant)**.** _For any graph_ G_, we have_ \(\nu(\mathcal{G})\ge f-k'\) _if and only if_ \(\mathcal{W}(\mathcal{G})=\emptyset\).

The second question is how quickly we can decrease the number of witnesses. Following the above definition of witnesses, we can naturally describe how a witness is removed upon an insertion of (_a,b_): say a pair of vertices \((a,b)\notin E\) _ kills_ W iff W is _not_ a witness of \(\mathcal{G}\cup(a,b)\). <sup>5</sup>

Following this description, observe that if \(a\notin S\) or \(b\notin T\), then (_a,b_) can never kill W. Furthermore, even if \(a\in S\) and \(b\in T\) but \((a,b)\in Y\) , then W remains a witness of \(\mathcal{G}\cup(a,b)\). This leads us to the following equivalent interpretation of invalidating a witness.

**Definition 3.8** (Killing a witness)**.** _Let_ G=(_V,E_) _be an unweighted and undirected graph with terminals s and t, and let_ W=(_S,T,Y_) _be one of its witnesses. We say a pair of vertices_ (_a,b_) kills _witness_ W=(_S,T,Y_) _if and only if_ \(a\in S\), \(b\in T\)_, and_ \((a,b)\notin Y\) .

In other words, these conditions together mean that (_a,b_) are on the different side of (_S,T_) and does _not_ belong to the pre-allocated cut _Y_ of (_S,T_), thereby invalidating the witness.

With this definition, we can establish an upper bound _n_<sup>_O(n_)</sup> on the initial number of witnesses. To see this, there are up to 2_<sup>n</sup>_ possible choices of (_S,T_), and for each fixed value of (_S,T_), there are up to \(n^{2(f-k^\prime-1)}\le n^{2n}\) choices of _Y_ . Due to our greedy-like approach, we assert that each iteration reduces the number of witnesses by a fraction of \(\gamma\). Therefore, we only need \(\widetilde{O}(n/\gamma)\) iterations to eliminate all witnesses, thereby terminating the algorithm.

Finally, for this argument to go through, we need to determine an appropriate value of \(\gamma\) such that a \(\gamma\)-good edge always exists in _G_\\_H<sub>i</sub>_ in every iteration _i_. Depending on the computation model, we also need to be able to find such edge efficiently. Without these guarantees, our algorithm may spend too much resource in finding a \(\gamma\)-good edge, or even worse may fail horribly if such edge did not exists at all. This is where the "promise" that \(\nu(G)\ge f\) and the "redundancy" of witness’s definition comes into rescue. Under these assumptions, by setting \(\gamma=\Omega\left(\frac{k'}{n\sqrt{k}}\right)\), a \(\gamma\)-good edge always exists.

<sup>5</sup>Notice that this is defined with respect to a _pair_ of vertices (_a,b_) rather than an _edge_ (_a,b_). This is due to a technical reason that in the cut-query model, we (as an algorithm designer) do not know if (_a,b_) exists in the underlying graph until we somehow "learn" it. For the ease of understanding, it is helpful to think of (_a,b_) as an actual edge in _G_ that is not presented in _H_ yet.

