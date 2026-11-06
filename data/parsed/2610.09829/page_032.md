<tbc>share an edge with \(\gamma\), i.e., \(\Gamma_{\delta,R,\gamma}=\{\gamma'|\gamma'\in(R\cup\{\delta\})\backslash\{\gamma\},E(\gamma')\cap E(\gamma)\neq\emptyset\}\). We say that \(\Gamma_{\delta,R,\gamma}\) is the \((\delta,R,\gamma)\)_-relevant set_ (see Figure 15). Next we give some simple observations, the first of which immediately follows from Definitions 5.7 and 5.8.

**Observation 5.3.** _Consider a solution_ C _for_ \(\Pi_\mathcal{P}(\alpha,h)\)_, where_ \(\alpha\) _is a non-leaf node of_ T _and h\>_1_. Let_ \(\{\beta_i|i\in[b]\}\) _be the set of solution descendants of_ \(\alpha\) _in_ C_, where for_ \(i\in[b]\), \(\gamma_i\) _is the representative of_ \(\beta_i\).

1. _For distinct_ \(i,j\in[b]\), \(\beta_i\neq\beta_j\) _and_ \(\gamma_i\neq\gamma_j\).<tbc>

_2._ _The set_ \(\{\gamma_i|i\in[b]\}\) _is lineage-free._

The next observation shows that no edge can belong to three cycles in a \(\delta\)-lineage-free set. Consequently, solution descendant descendant \(\beta\) of some cycle \(\gamma\in R\) cannot share the same edge with two distinct cycles in the \((\delta,R,\gamma)\)-relevant set. We will crucially rely on this property in our dynamic programming.

**Observation 5.4.** _Consider_ \(\delta\in V(\mathcal{T})\)_, a_ \(\delta\)_-lineage-free set R, and_ \(\gamma^*\in R\)_. Then for any descendant_ \(\beta^*\) _of_ \(\gamma^*\) _in_ \(\mathcal{T}_\delta\) _and distinct_ \(\gamma,\gamma'\in\Gamma_{\delta,R,\gamma^*}\)_, we have_ \(E(\beta^*)\cap E(\gamma)\cap E(\gamma')=\emptyset\).

_Proof._ Towards a contradiction, suppose there is a descendant \(\beta^*\) of \(\gamma^*\) in \(\mathcal{T}_\delta\) and distinct \(\gamma,\gamma'\in\Gamma_{\delta,R,\gamma^*}\) such that \(E(\beta^*)\cap E(\gamma)\cap E(\gamma')\neq\emptyset\). As \(\gamma\neq\gamma'\), at least one of \(\gamma\) or \(\gamma'\) is different from \(\delta\), say \(\gamma\neq\delta\). As \(E(\beta^*\cap\gamma)\neq\emptyset\), from Proposition 5.1 we can obtain that \(\beta^*\cap\gamma\) is a path in _G_. Note that \(\beta^*\) and \(\gamma\) are not in ancestor-descendant relationship, and thus, from Proposition 5.2 (1), neither \(\beta^*\le\gamma\), nor \(\gamma\le\beta^*\) in the (given) planar embedding of _G_. Now, by the planarity of _G_, if a cycle _C_ contains an edge in \(E(\beta^*)\cap E(\gamma)\), then exactly one of the following holds: i) \(C\le\beta^*\), ii) \(C\le\gamma\), iii) \(\beta^*\le C\), or iv) \(\gamma\le C\). Notice that \(\gamma'\) satisfies none of the above conditions, as argued next. Indeed, neither \(\gamma'\le\beta^*\) nor \(\gamma'\le\gamma\) (recall \(\gamma\neq\delta\)). Also exactly one of \(\beta^*\le\gamma'\) or \(\gamma\le\gamma'\) cannot hold, whether or not \(\gamma'=\delta\) (see Proposition 5.2 (1)). Therefore, \(\gamma'\) cannot contain an edge from \(E(\beta^*)\cap E(\gamma)\), which contradicts our assumption.

The next observation exploits the planarity of _G_ to bound the sum of the sizes of the relevant sets of all representative descendants, which will be useful in obtaining the desired running-time.

**Observation 5.5.** _For_ \(\delta\in V(\mathcal{T})\) _and a_ \(\delta\)_-lineage-free set_ \(R=\{\gamma_i|i\in[b]\}\), \(\sum_{i\in[b]}|\Gamma_{\delta,R,\gamma_i}|\le 7b\).

We remark that the constant 7_b_ is likely not tight, but it is sufficient for our purposes.

_Proof._ Let _G<sub>R</sub>_ be the plane graph obtained from _G_ by deleting each vertex and edge that are not present in any of the cycles in _R_. Furthermore, let \(\widetilde{G}_R\) be the graph with \(V(\widetilde{G}_R)=R\) and for distinct \(\gamma,\gamma'\in R\), \(\{\gamma,\gamma'\}\) is an edge in \(\widetilde{G}_R\) if \(E(\gamma)\cap E(\gamma')\neq\emptyset\). Note the following:

1. For distinct \(\gamma,\gamma'\in R\), \(\{\gamma,\gamma'\}\in E(\widetilde{G}_R)\) if and only if \(\gamma\in\Gamma_{\delta,R,\gamma^\prime}\backslash\{\delta\}\) and \(\gamma'\in\Gamma_{\delta,R,\gamma}\backslash\{\delta\}\). In other words, \(N_{\widetilde{G}_R}(\gamma)=\Gamma_{\delta,R,\gamma}\backslash\{\delta\}\) and \(N_{\widetilde{G}_R}(\gamma')=\Gamma_{\delta,R,\gamma^\prime}\backslash\{\delta\}\).<tbc>

2. The graph \(\widetilde{G}_R\) is a simple graph and it is a subgraph of the dual of _G<sub>R</sub>_. Thus, \(\widetilde{G}_R\) is a planar graph, hence \(|E(\widetilde{G}_R)|<3b\). (The above follows from the fact that a dual of a planar graph is a planar multi-graph, see for instance, Section 4.6 of \[10\]).

Using the above, together with the possibility that \(\delta\in\Gamma_{\delta,R,\gamma_i}\), for each \(i\in[b]\), we can conclude that \(\sum_{i\in[b]}|\Gamma_{\delta,R,\gamma_i}|=2\cdot|E(\widetilde{G}_R)|+b\le 7b\).

