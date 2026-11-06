Both dynamic and online locality model a setting with a central algorithm. The difference is that under online locality, once a node is revealed, its final neighborhood is visible to the algorithm, whereas in dynamic locality, the graph can still change at any point later during the execution. As previously shown in figure 1, an algorithm in online-LOCAL is provably stronger than one in dynamic-LOCAL, leading to the following hierarchy [2]:

where \(A\unknown B\) means that for any problem, an algorithm in model _A_ with locality _T<sub>A</sub>_ implies an algorithm in _B_ with locality _T<sub>B</sub>=O(T<sub>A</sub>_), but, in general, not vice-versa.

Another related locality model is SLOCAL [14], which is sequential, similar to the online-LOCAL model, but without a global memory. Instead, each node stores a state and produces its own output and state based on the information previously stored in the local neighborhood. Compared to dynamic-LOCAL, it is stronger on some problems and weaker on others [2]. See figure 1 for an overview of the connections between the models of locality mentioned here.

Finally, a concept similar to dynamic locality is the _mending radius_ [4] of a graph labeling problem. It is the neighborhood radius around unlabeled nodes in any correct partial labeling such that changing labels in this neighborhood makes the labeling completeable. It provides an upper bound for dynamic-LOCAL, but is in general weaker, as it has to complete any possible partial labeling, not only those produced by the same algorithm.

**An LCL separation between dynamic-LOCAL and online-LOCAL?** A class of problems of particular interest to the study of locality is the class of _locally checkable labeling problems_ (LCLs) [17], which are problems that can be defined by a finite set of accepted labeled neighborhoods on bounded-degree graphs. LCLs form a fundamental class of problems that have been studied for a long time in the distributed graph algorithm community [13,17]. Examples of LCLs are vertex coloring, maximal matching and maximal independent set.

As mentioned before, the dynamic-LOCAL model is strictly weaker than online-LOCAL models on general problems. A known separation between the two models occurs in the problem of _component-wise leader election_ [2], which has locality _O_(1) in online-LOCAL and \(\Omega(n)\) in dynamic-LOCAL. This separation relies on the fact that in online-LOCAL an algorithm can tell when a component is completed, whereas in dynamic-LOCAL it is always possible that more edges will be added in the future. It is not clear whether this restriction is relevant for other problems. In fact, component-wise leader election is not an LCL problem. Whether dynamic-LOCAL and online-LOCAL can be separated by an LCL problem is, to the best of our knowledge, an open question.

**3-coloring bipartite graphs.** A bipartite graph is, by definition, always 2-colorable. There exist exactly two 2-colorings for a connected component, and just a single colored

dynamic-LOCAL
LOCAL
online-LOCAL
SLOCAL

**Figure 1** A landscape of distributed models from [2]. A model _A_ pointing to a model _B_ means that any algorithm of _A_ can be simulated in _B_ with locality _T<sub>B</sub>=O(T<sub>A</sub>_).

LOCAL \(\unknown\) dynamic-LOCAL \(\unknown\) online-LOCAL

