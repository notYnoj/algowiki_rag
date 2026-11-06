<tbc>data structure of Lemma 4.6. We spend time \(O(n')\) to populate it initially, and overall the number of operations performed is \(O(|w|+m')\) (and note that each state is only pushed at most once). In particular, it is important to efficiently access the roots of the DAG _S<sub>i</sub>_, and then start the exploration of _S<sub>i</sub>_ from these states; the fact that we can retrieve these states in time proportional to their number is ensured by the usage of the data structure of Lemma 4.6. Therefore, our statement holds.

## 5 Quantitative Problem Variants

For every \(x\in\{\text{in},\text{pre},\text{ext},\text{lext},\text{sub},\text{sup}\}\), we consider now the min- and max-variant of the \(\unknown_x\)- matching problem, i.e., computing a shortest or longest string \(u\in\mathsf{L}(A)\) with \(u\unknown_xw\). We show an upper bound of _O_(|_w|m_) for all these problem variants.<sup>4</sup>

**Theorem 5.1.** _The min- and max-variant of the matching problem can be solved in time O_(|_w|m_) _for all relations_ \(\unknown_x\) _with_ \(x\in\{\text{in},\text{pre},\text{ext},\text{lext},\text{sub},\text{sup}\}\).

In Section 7 we show that the _O_(|_w|m_) upper bound for all the considered variants is conditionally tight, i.e., \(O((|w|m)^{1-\epsilon})\) is not possible unless SETH fails. The rest of this section is devoted to the proof of Theorem 5.1. Before giving this proof, we need some preliminaries.

Recall that a path in a directed graph may traverse the same vertex multiple times (a simple path is a path where each vertex is traversed once). An _st-path_ is a path from a vertex _s_ to a vertex _t_. When the edges of a directed graph are weighted, let weight(_e_) be the _weight_ of edge _e_ and let the weight of a path be the sum of weights of the successive edges that it traverses (if an edge is traversed multiple times then the weight is added as many times as the edge is traversed). In the case where the edges are labelled, the _label_ of a path is the concatenation of the labels of the successive edges that it traverses (if the edges carry labels in \(\Sigma\cup\{\varepsilon\}\) then the label of the path is a string in \(\Sigma^*\)). We show the following ancillary result:

**Lemma 5.2.** _Let G be a directed graph with edges weighted by_ 0 _and_ 1_, and let s and t be two distinguished vertices. We can check in time O_(|_G_|) _whether there is an st-path in G, and if an st-path exists, then we can compute in time O_(|_G_|):

• _an st-path with minimum weight._<tbc>

• _whether there exist st-paths of unbounded weight in G._<tbc>

• _an st-path with maximum weight, provided that the weight of st-paths is not unbounded._

Note that the lemma is stated for edge weights 0 and 1, but applies more generally to weights bounded by a constant, as we can split every edge of weight larger than 1 into a constant number of length-1 edges connecting auxiliary nodes. Note that the lemma also applies to labelled directed graphs: in this case, when we obtain a path by applying the lemma, then we can retrieve its label (in \(\Sigma^*\)) from its sequence of edges. Let us prove the lemma:

_Proof of Lemma 5.2._ We first eliminate all graph vertices that do not have a path from _s_, as well as those that do not have a path to _t_. This is akin to automaton trimming, and can be done in _O_(|_G_|) with two graph traversals. The resulting graph is empty if and only if there is no _st_-path. Let us now assume that the trimmed graph is not empty and, for simplicity, let us denote this trimmed graph by _G_.

_Minimum weight st-path._ To compute an _st_-path of minimum weight, we simply use Dijkstra’s algorithm with a priority queue implemented with a table of |_G_| buckets. This makes it possible to insert vertices with a given priority in _O_(1), lower their priority in _O_(1), and retrieve a vertex of lowest priority in time _O_(1) per call plus an _O_(|_G_|) total cost throughout the entire algorithm<tbc>

<sup>4</sup>Of course, these upper bounds also give upper bounds on the corresponding (non-quantitative) matching problems for \(\unknown_\text{in}\), \(\unknown_\text{pre}\), \(\unknown_\text{ext}\) and \(\unknown_\text{lext}\); see  1.

