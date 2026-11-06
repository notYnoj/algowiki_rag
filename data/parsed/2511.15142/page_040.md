components _E_<sub>1</sub>_,...,E<sub>k</sub>_ (note that these are the edge sets of the components); the edge set of the minimum-weight spanning tree (MST) for _E_ is the union of those for the _E<sub>i</sub>_’s, so it suffices to focus on a 2-connected component induced by the edges in some _E<sub>i</sub>_. We claim we can simulate Kruskal’s algorithm for MST in each of these components, which just compares weights of edges: indeed, if this algorithm compares edges \(e,e'\in E_i\), we can find a base _B_ containing _e_, such that \(B':=(B\backslash e)\cup e'\) is also a base. (We defer the proof, since it follows from the result below.) Now comparing \(e,e'\) has the same answer as comparing \(B,B'\).

The same argument holds for arbitrary matroids, where we recall that the notion of 2-vertex connectivity in graphs extends to matroids \[Oxl11\]:

**Lemma E.2.** _For any matroid_ M=(I_,U), let_ B(M) _and_ C(M) _be the collection of all bases and circuits in the matroid._

1. _If elements_ \(e,e'\in E\) _share a circuit_ \(C\in\mathcal{C}(\mathcal{M})\)_, then there exist bases_ \(B,B'\in\mathcal{B}(\mathcal{M})\) _such that_ \(B'=B+e'-e\)_. Call such pair of elements_ \(e,e'\) **_comparable_**.<tbc>

_2._ _The binary relation_ \(\gamma_\mathcal{M}\) _on the elements of the matroid such that_ \((e,e')\in\gamma_\mathcal{M}\) _iff either_ \(e=e'\) _or_ \(e,e'\) _are comparable is an equivalence relation._

_Proof._ For the first part, let _B_ be the basis that extends the independent set \(C-e'\). This means that the fundamental circuit in \(B+e'\) is _C_ implying that \(B':=B+e'-e\) is also a basis. The second part is proved in \[Oxl11, Proposition 4.1.2\]. The equivalence classes in lemma E.2(2) are called the _connected components_ of M.

Now we can run the analog of Kruskal’s greedy algorithm for matroids on the connected components of M; this uses _O_(|_U<sub>i</sub>_|log|_U<sub>i</sub>_|) element (and hence base) comparisons for each component; summing over all components gives us _O_(|_U_|log|_U_|), as claimed.

We now give details on efficient algorithms for decomposition of the matroid into connected components and obtaining two bases \(B,B'\) such that \(B\Delta B'=\{x,y\}\) for every pair _x,y_ compared by the algorithm, and overall running time bounds: The running time consists of the time taken to decompose the matroid into its connected components, and obtaining two bases \(B,B'\) such that \(B\Delta B'=\{x,y\}\) for every pair _x,y_ compared by the algorithm. For this, we use the results from \[Kro77\] that connect the _basis exchange graph_ with the connected components of the matroid. The following are a definition and a lemma:

For any basis _B_ of M, the basis exchange graph _H(B_) is defined as the bipartite graph with color classes _B_ and _U_\\_B_. For \(x\notin B,y\in B\), we have \(\{x,y\}\in H\) iff _B+x-y_ is also a basis. The following lemma connects this exchange graph with matroid connectivity:

**Lemma E.3** (Section 6, \[Kro77\])**.** _For any basis_ \(B\in\mathcal{M}\),

1. _The nodes in the connected components (in the graphic sense) of H(B_) _are the connected components (in the matroid sense) of matroid_ M.<tbc>

_2._ _For x,y in the same connected component of H(B_) _(or equivalently_ M_) such that_ \(x\notin B\) _and_ \(y\in B\)_, if P is the shortest path connecting x and y in H(B), then_ \(B':=B\Delta P\) _is a basis such that_ \(B'+y-x\) _is a basis._

Given Lemma E.3, the matroid decomposition step requires _O(n_<sup>2</sup>) matroid independence calls (in fact, the calls are always about whether a set is a basis or not) to build the exchange graph using Lemma E.3 part 1 and _O(n_<sup>2</sup>) time to identify connected components.

Next, to simulate any pairwise comparison between elements _x,y_, we obtain the two bases \(B\unknown x,B'\unknown y\) such that \(B\Delta B'=\{x,y\}\) using part 2 of Lemma E.3. The implementation of Kruskal’s<tbc>

