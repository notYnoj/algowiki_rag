<tbc>triangulation represents a way to add edges to some graph _G_ in order to make it chordal. Treewidth and triangulations are very close concepts: computing the treewidth of a graph amounts to finding a triangulation with the smallest clique size.

**Definition 13** (Triangulation \[20\])**.** _Let G_=(_V,E_) _be any graph. We say that a graph H is a_ triangulation _of G if both H is chordal and is obtained by adding edges to G,_ i.e. \(H=(V,E\cup F)\)_, where_ \(E\cap F=\emptyset\).

_A_ minimal triangulation _H of G is a triangulation of G for which H_\\{_e_} _is not chordal, for any_ \(e\in F\).

PMCs are exactly the maximal cliques of the minimal triangulations of _G_.

**Definition 14** (Potential Maximal Clique (PMC))**.** _A set_ \(\Omega\subseteq V(G)\) _is a_ potential maximal clique _(PMC) of G if_ \(\Omega\) _is an inclusion-wise maximal clique of some minimal triangulation of G._

**Theorem 4** (\[6\])**.** _Let G be a graph and_ \(\Omega\subseteq V(G)\)_. Set_ \(\Omega\) _is a PMC iff it satisfies the two following properties:_

• \(\Omega\) _is a shy set._<tbc>

• \(\Omega\) _has the reachability property._

From now on, this latter characterization will be the main method used to identify PMCs. Thanks to it, we can check whether some set is a PMC or not in polynomial time.

**Lemma 7** (PMC identification \[6\])**.** _Given a set_ \(\Omega\subseteq V(G)\)_, we can decide in O(nm_) _whether_ \(\Omega\) _is a PMC of G or not._

In the literature, many properties of PMCs were identified. Most of them concern the case where _G_ is not a complete graph. Indeed, if _G_ is a clique, then it admits a unique PMC _V(G_), as any other vertex set is not shy. For this reason, we focus in this paper only on graphs _G_ which are not complete, to skip this trivial but specific case. On other graphs, PMCs and minimal separators admit strong connections.

A first property of PMCs is that none of their proper subset is a PMC.

**Lemma 8** (\[6\])**.** _Any_ \(PMC\Omega'\) _of G cannot be strictly included into another_ \(PMC\Omega\) _of G._

This comes from the fact that, as PMCs have the reachability property, any proper subset admits at least one full component - the one which contains a removed vertex. Observe that this statement also holds for minimal (_a,b_)-separators with fixed (_a,b_), but not for minimal separators in a broad sense.

Second, an interesting fact is that the neighborhood of any connected component of \(G\backslash\Omega\), for any \(PMC\Omega\), is a minimal separator of _G_.

**Lemma 9** (\[6\])**.** _For any_ \(PMC\Omega\) _of G, the minimal separators of G which are included into_ \(\Omega\) _are exactly the sets N<sub>G</sub>(C), for any connected component C of_ \(G\backslash\Omega\)_. Those sets are called_ neighbor separators.

Many efforts in the study of PMCs are dedicated to the structural features of these neighbor separators \(S\subseteq\Omega\). We pursue with a property of sets \(\Omega\backslash S\), which are PMCs without one of its neighbor separator.

