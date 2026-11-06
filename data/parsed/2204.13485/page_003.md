interchanging any two of them would count as only one swap. In addition, this approach also makes possible to have ties among agents. We show that the problem is solvable in bipartite graphs in the capacitated setting, even when upper and lower bounds are given on the changes and the compensation cost differs for each agent. We also consider the roommate case which has not yet been investigated before. We show that the problem is NP-hard, but it admits a 2-approximation.

Finally, we investigate problems where the preferences are manipulated by the agents themselves in order to force or avoid certain contracts to form. While previous papers only considered manipulations with respect to the outcome of the Gale-Shapley algorithm, we investigate more general cases. Our goal is to ensure that there exists a stable matching with respect to the modified preferences. This can be practically important, for example when a stable matching is chosen randomly, not by the Gale-Shapley algorithm. We also study cases where there are forbidden edges instead of forced ones, or some places in the preferences are fixed and cannot be manipulated. We show that almost all problems arising this way are NP-complete even in rather restricted settings. On the positive side, we give an algorithm for the case when certain places in the preference lists are not allowed to be manipulated by the agents.

The rest of the paper is organized as follows. Basic notation and definitions are introduced in Section 2. Section 3 focuses on problems where the goal is to ensure the existence of a stable matching through the deletion of a subset of vertices. Preference modifications in order to make a given outcome stable are discussed in Section 4. Finally, in Section 5, we investigate preference extension problems.

## 2 Preliminaries

### Basic notations.

We denote the sets of _real_, _nonnegative real_, _integer_, and _nonnegative integer_ numbers by R, R<sub>+</sub>, Z, and Z<sub>+</sub>, respectively. For a positive integer _k_, we use \[_k_\]:={1_,...,k_}.

Given a ground set _S_ and subsets \(X,Y\subseteq S\), the _difference_ of _X_ and _Y_ is denoted by _X_\\_Y_ . If _Y_ consists of a single element _y_, then _X_\\{_y_} and \(X\cup\{y\}\) are abbreviated by _X-y_ and _X+y_, respectively. We call a 3-element subset a 3_-set_ for short. Some hardness proofs in Section 5 will be based on the following NP-complete problems, see \[14\].

Let _G_=(_V,E_) be an undirected graph, \(S\subseteq V\) be a subset of vertices, and \(F\subseteq E\) be a subset of edges. The graphs obtained by _deleting the vertices in S_ (together with the edges incident to them) or _the edges in F_ are denoted by _G-S_ and _G-F_, respectively. We call _S_ a _vertex cover_ if _G-S_ has no edges. For a vertex \(u\in V\) , the _set of neighbors of u_ is denoted by \(N(u)=\{v\in V|uv\in E\}\). The _set of edges in F incident to a vertex_ \(v\in V\) is denoted by _F(v_). The following is a well-known NP-hard problem.

x3c
Input: A family C = {C1,...,C3n} of 3-sets of a ground set a1,..., a3n.
Question: Does there exist n 3-sets in C that partition {a1,..., a3n}?
3sat
Input: A Boolean formula Φ in conjunctive normal form where each clause is limited to at most three literals.
Question: Does there exist a truth assignment to the variables for which Φ is true?

