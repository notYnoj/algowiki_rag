is just \(O(2^k\lambda n^{1+o(1)})\). Note that the total space used is bounded by \(O(2^k\lambda n^2)\). Therefore, we have the following theorem.

\(\blacktriangleright\) **Theorem 23.** _Given any directed graph_ G=(_V,E_) _on n vertices, and any positive constants_ \(\lambda,k\ge 1\)_, we can preprocess G in polynomial time to build an O(n_<sup>2</sup>) _size data structure that, given any query vertex-pair_ (_x,y_) _and any set F of k edges, can determine the_ \((x,y)\)-\(\lambda\)_-reachability in_ G\\_F in O(n_<sup>1+_o_(1)</sup>) _time._

## 6.2 FT-BFPs for graphs with non-unit capacities

We have shown till now that for any digraph G with unit capacities, one can compute a \((\lambda,k)\)-FT-BFP with \(O(2^k\lambda n)\) edges. We shall now show how to extend this result to a digraph with integer edge capacities such that flow values up to \(\lambda\) are preserved under bounded capacity decrement.

Let us first formalize the notion of FT-BFP under capacity decrement function.

\(\blacktriangleright\) **Definition 24.** _Let_ G=(_V,E,c_) _be a directed flow graph such that capacity of any edge is a positive integer, and let_ \(s\in V\) _be a designated source vertex. A subgraph_ \(\mathcal{H}=(V,E_0\subseteq E)\) _of_ G _is said to be a_ \((\lambda,k)\)_-Fault-Tolerant Bounded-Flow-Preserver if for any capacity decrement function_ \(I:E(G)\rightarrow\mathbb{N}\) _satisfying_ \(\sum_{e\in E(G)}I(e)\le k\)_, the following holds for the capacity function c_<sup>∗</sup> _defined as c_<sup>∗</sup>(_e_)=_c(e_)-_I(e), for_ \(e\in E\)_: For every_ \(t\in V\) ,

\(max-flow(s,t,\mathcal{H}|c^*)=\left\{\begin{array}{ c c } max-flow(s,t,\mathcal{G}|c^*) & \text{\textit{if}}max-flow(s,t,\mathcal{G}|c^*)\le\lambda, \\ At least\lambda, & \text{\textit{otherwise}}; \end{array}\right.\)

_where,_ H|_c_<sup>∗</sup> _and_ G|_c_<sup>∗</sup> _are respectively the graphs_ H _and_ G _with capacity function c_<sup>∗</sup>.

Let us now discuss the construction of \((\lambda,k)\)-FT-BFPs. Let G=(_V,E,c_) be a digraph with integer edge capacities. We first transform G into a multigraph G<sup>∗</sup> by replacing an edge (_x,y_) of capacity _c(x,y_) by exactly _c(x,y_) copies of edge (_x,y_) of unit-capacity. Thus, for vertex \(v\in V\) , the _s_ to _v_ max-flow in graphs G and G<sup>∗</sup> are identical.

Now, let H<sup>∗</sup> be a \((\lambda,k)\)-FT-BFP of multigraph G<sup>∗</sup>. Then, a \((\lambda,k)\)-FT-BFP of G, say H=(_V,E_<sub>0</sub>_,c_), can be obtained by simply retaining all those edges whose multiplicity in H<sup>∗</sup> is non-zero. The graph H will indeed be a \((\lambda,k)\)-FT-BFP of G since a bounded capacity decrement in G corresponds to _k_-edge failures in G<sup>∗</sup>.

## References

1 Amir Abboud, Loukas Georgiadis, Giuseppe F. Italiano, Robert Krauthgamer, Nikos Parotsidis, Ohad Trabelsi, Przemysław Uznanski, and Daniel Wolleb-Graf. Faster algorithms for all-pairs bounded min-cuts. In Christel Baier, Ioannis Chatzigiannakis, Paola Flocchini, and Stefano Leonardi, editors, _46th International Colloquium on Automata, Languages, and Programming, ICALP 2019, July 9-12, 2019_, volume 132 of _LIPIcs_, pages 7:1-7:15, 2019. 2 Surender Baswana, Koustav Bhanja, and Abhyuday Pandey. Minimum+1 (s, t)-cuts and dual edge sensitivity oracle. In Mikolaj Bojanczyk, Emanuela Merelli, and David P. Woodruff, editors, _49th International Colloquium on Automata, Languages, and Programming, ICALP 2022, July 4-8, 2022, Paris, France_, volume 229 of _LIPIcs_, pages 15:1-15:20. Schloss Dagstuhl - Leibniz-Zentrum für Informatik, 2022. 3 Surender Baswana, Shreejit Ray Chaudhury, Keerti Choudhary, and Shahbaz Khan. Dynamic DFS in undirected graphs: Breaking the o(m) barrier. _SIAM J. Comput._, 48(4):1335-1363, 2019.

