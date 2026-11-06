## 3 General Preferences

In this section we consider convergence to stable matchings in the two-sided case with general preferences that may be incomplete and have ties. For locally stable matching it is known that in this case there are instances and initial states such that no locally stable matching can be reached using local blocking pair resolutions. Moreover, deciding the existence of a converging sequence of resolutions is NP-hard \[19\].

We here study the problem for socially, considerate, and friendship matching. Our positive results are based on the following procedure from \[2\] that is known to construct a sequence of polynomial length for unconstrained stable matching. The only modification of the algorithm for the respective scenarios is to resolve "social", "considerate" or "perceived blocking pairs" in both phases.

**Phase 1** Iteratively resolve only blocking pairs involving a matched vertex \(w\in W\). Phase 1 ends when for all blocking pairs {_u,w_} we have \(w\in W\) unmatched.

**Phase 2** Choose an unmatched \(w\in W\) that is involved in a blocking pair. Resolve one of the blocking pairs {_u,w_} that is most preferred by _w_. Repeat until there are no blocking pairs.

It is rather straightforward to see that the algorithm can be applied directly to build a sequence for socially stable matching.

**Theorem 4.** _In every bipartite instance of socially stable matching_ \(G=(V=U\dot{\cup}W,E)\) _with general preference lists and social network L, for every initial matching M_<sub>0</sub> _there is a sequence of polynomially many improvement steps that results in a socially stable matching. The sequence can be computed in polynomial time._

For extended settings the algorithm still works for somewhat restricted social networks. For considerate matching we assume that the link set is only within \(L\subseteq(U\times U)\cup(U\times W)\), i.e., no links within partition _W_.

**Theorem 5.** _In every bipartite instance of considerate matching_ \(G=(V=U\dot{\cup}W,E)\) _with general preference lists and social network L such that_ \(\{w,w'\}\notin L\) _for all_ \(w,w'\in W\)_, for every initial matching M_<sub>0</sub> _there is a sequence of polynomially many improvement steps that results in a considerate matching. The sequence can be computed in polynomial time._

We also apply the algorithm to friendship matching in case there can be arbitrary friendship relations \(\alpha_{u,u^\prime},\alpha_{u^\prime,u}\ge 0\) for each pair \(u,u'\in U\). Here we allow asymmetry with \(\alpha_{u,u^\prime}\neq\alpha_{u^\prime,u}\). Otherwise, for all \(u\in U,w,w'\in W\) we assume that \(\alpha_{u,w}=\alpha_{w,u}=\alpha_{w,w^\prime}=0\), i.e., friendship only exists within _U_.

**Theorem 6.** _In every bipartite instance of friendship matching_ \(G=(V=U\dot{\cup}W,E)\) _with benefits b and friendship values_ \(\alpha\) _such that_ \(\alpha_{u,u^\prime}>0\) _only for_ \(u,u'\in U\)_, for every initial matching M_<sub>0</sub> _there is a sequence of polynomially many improvement steps that results in a friendship matching. The sequence can be computed in polynomial time._

