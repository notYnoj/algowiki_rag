Both \[16, 25\] give a (static) algorithm to compute for a given graph _H_ that is associated with a root in R, the DDG for every \(H'\) in R with \(H'\subseteq H\) in total time \(\tilde{O}(r)\); since there are _O(n/r_) pieces _H_, the total preprocessing time is thus \(\tilde{O}(n)\). Further, after an edge weight change to _G_, the algorithm only has to locate the affected root graph _H_ containing the edge, and one can simply recompute the dense distances graphs in the tree rooted at _H_ from scratch, again in \(\tilde{O}(r)\) time.

Thus, previous APSP algorithms maintained the DDGs of the pieces essentially by applying a static algorithm at every update step and obtained a dynamic APSP algorithm rather using the _r_-divisions technique in planar graphs. We ask whether there is a way of maintaining DDGs that does not require recomputation from scratch but rather maintains them dynamically. More concretely, we pose the following question.

**Research Question 2.** _Can a DDG be maintained dynamically with sublinear update time (and small query time)?_

We note that so far, the question about whether there exists an efficient encoding of DDG that can be maintained during updates with only a small number of bits changed over each update is not known either. In particular, for any DDG over an _n_-vertex graph _G_, there is no known encoding that does not have to change \(\Omega(n)\) bits on average for each update.

## 2 Contributions

In this article, we present the first partial progress on this long-standing problem. We give the first algorithm that achieves the desired update/query time in the offline setting<sup>2</sup>. Moreover, if the graph is _incremental_, i.e. the update sequence only consists of edge weight decreases, the data structure works in the online setting. Due to the lower bound of Abboud and Dahlgaard \[1\] that extends for both offline and online incremental setting, our bounds are tight up to polylogarithmic factor.

**Theorem 2.1.** _\[Near-Optimal Dynamic APSP\] There exists a data structure for the planar, dynamic APSP problem in the offline setting, i.e. where the update sequence is accessible from the beginning of the algorithm, that has worst-case update time and query time_ \(\tilde{O}(\sqrt{n})\) _and preprocessing time_ \(\tilde{O}(n)\)_. The data structure is deterministic._

_If the graph is incremental then our data structure works in the online setting._

**Remark 2.2.** _More generally, for any_ \(\delta\in[0,\frac{1}{2}]\)_, we obtain an offline dynamic APSP data structure with worst-case update time_ \(\tilde{O}(n^\delta)\) _and query time_ \(\tilde{O}(n^{1-\delta})\)_. By the lower bound by Abboud and Dahlgaard \[1\] which extends to the offline setting, this is tight for all choices of_ \(\delta\)_. Further, we improve for every constant_ \(\delta\in(0,\frac{1}{2}]\) _on the previous state-of-the-art._

Even more interestingly, we achieve our result by designing a new algorithm that efficiently maintains DDGs. We remind the reader that so far, even maintaining an encoding undergoing a sublinear number of changes in _n_ was not known.

**Theorem 2.3.** _Given a planar embedded graph G along with an r-capped recursive division_ R _of G, there exists a data structure that maintains the DDG of every node H in_ R _in the offline_<tbc>

<sup>2</sup>Here, we only assume that the update sequence is offline, i.e. is initially presented the data structure, while queries can be online.

