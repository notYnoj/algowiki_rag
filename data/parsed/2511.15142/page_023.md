## 5.3 Proof of the Structure Primitives Theorem

Finally, we turn to the proof of the Structure Primitives result in Theorem 5.1. We will provide a proof sketch here for the query complexity bounds; see Section D for the full proof including the running time bounds.

_Proof sketch of Theorem 5.1._ Recall that we want to identify the edges coming out of _u_. The key observation is that, for any set _S_ not containing _u_, the sign of \(\partial(S+u)-\partial(S)\) tells us whether less, equal to, or more than half of the edges incident to _u_ go into _S_ (if the sign is positive, zero, or negative).

Suppose we find a set _S_ such that _just below_ half of the edges from _u_ go into _S_ (so that expression has a positive sign)--such an _S_ is called a _median set for u_. Now if we add _v_ to the median set _S_, and the sign of \(\partial(S+v+u)-\partial(S+v)\) changes, we know that _v_ is a neighbor of _u_. In summary, once we have a median set _S_, we can find all the neighbors of _u_ not in _S_.

How do we find a median set for _u_? Order all the vertices other than _u_ (say this is _v_<sub>1</sub>_,v_<sub>2</sub>_,...,v_<sub>_n_-1</sub>, define _S<sub>i</sub>_ to be the first _i_ elements. If _u_ has at least one edge incident to it, the query \(\partial(S_0+u)-\partial(S_0)\) has a positive sign, whereas \(\partial(S_{n-1}+u)-\partial(S_{n-1})\) has a negative sign (note that we use \(S_0=\emptyset\) and _S_<sub>_n_-1</sub>+_u=U_ here for the sake of exposition, but such trivial cuts are not allowed in the actual comparison model. The full proof in Section D handles this correctly and with full rigor). So we can perform binary search to find a point where the sign changes, which can be used to find a median set in log<sub>2</sub>_n_ comparisons. (In fact, we can find two disjoint median sets--a prefix and a suffix of this ordering--and use the two to find all the neighbors in some _k_-sized set with _k+O_(log_n_) queries.)

For part (ii), the argument builds on the use of such a median set _S_. Given an ordered set _T_={_v_<sub>1</sub>_,...,v<sub>r</sub>_} where _v<sub>j</sub>_ is the first neighbor of _u_ in the ordering, we first compute a median set _S_ that is guaranteed to exclude the prefix {_v_<sub>1</sub>_,...,v<sub>j</sub>_}. Then, we binary search over the chain

\(S\subseteq S\cup\{v_1\}\subseteq\cdots\subseteq S\cup(T\backslash S)\)

to locate the point at which the marginal changes sign. This transition occurs precisely at the set \(S\cup\{v_1,\dots,v_{j-1}\}\), thus identifying _v<sub>j</sub>_ as the first neighbor of _u_ in _T_.

## 5.4 Sparsifiers for Heavy Subgraph Problems

The work of \[EHW15\] considers a broad class of graph optimization problems, which they call _heavy subgraph_ problems; these include densest subgraph, densest bipartite subgraph, and _d_-max cut. For these problems, they show that uniformly sampling \(\widetilde{O}(n/\varepsilon^2)\) edges without replacement from the underlying graph _G_ produces a subgraph _H_ such that running any \(\alpha\)-approximation algorithm for the problem on _H_ yields (after appropriate rescaling) an \((\alpha-\varepsilon)\)-approximate solution for the original graph, with high probability. In other words, the sampled subgraph preserves the structure of the problem up to a small loss in accuracy, and approximate solutions on the sparsifier _H_ translate to approximate solutions on the full graph _G_. We show how to sample a fixed number of edges from _G_ uniformly using the following lemma:

**Lemma 5.5** (Sampling Lemma)**.** _When_ \(n\ge 4\)_, given cut comparison queries, for any_ \(k=\widetilde{\Omega}(1)\)_, we can sample k edges uniformly without replacement using_ \(\widetilde{O}(n+k)\) _queries and_ \(\widetilde{O}(n^2)\) _time with high probability._

_Proof._ Consider the process that at time step _t_ (starting from _t_=0) samples _G(p<sub>t</sub>_) for _p<sub>t</sub>_:=2_<sup>t</sup>/n_<sup>2</sup> until the sample _G(p<sub>t</sub>_) at _t=r_ has at least _k_ edges. Then, subsample _k_ edges uniformly from the sample _G(p<sub>r</sub>_).

