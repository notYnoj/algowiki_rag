**Algorithm 2**

Require: Hypergraph H on vertices V with cut and edge oracles and tolerance \(\varepsilon>0\)<br>
Ensure: \((1+\varepsilon)\)-approximation for DSH(G)<br>
\(C\leftarrow 240nlogn/\varepsilon^2\)<br>
for all \(v\in V\) do<br>
\(deg(v)\leftarrow\text{cut}(\{v\})\triangleright n\text{\textit{cut queries}}\)<br>
\(\hat{H}\leftarrow(V,E,\hat{w}=0)\)<br>
for i=1...C do<br>
\(e\leftarrow\perp\)<br>
while \(e=\perp\) do \(\triangleright Vol(H)/2w(H)\) iterations in expectation<br>
Sample \(e\leftarrow\) a random hyperedge of H using Rand<sub>H</sub> \(\triangleright\) one edge query per iteration<br>
\(e\leftarrow\perp\) with probability 1-2/|e|<br>
\(\hat{w}(e)\leftarrow\hat{w}(e)+1\)<br>
return \(\mathcal{P}(\hat{H})\)

<tbc>to be ‘overkill’ for Max Cut. Intuitively, the maximum cut is always at least m/2 and so concentrates well with uniform sampling, whereas minimum cuts can lie on a much smaller scale, thus requiring strength-based sampling techniques to properly capture.

## 3.2 \((1+\varepsilon)\)-Approximation for Densest Subhypergraph

Unfortunately, cut queries alone do not suffice to learn any nontrivial approximations for Densest Subhypergraph, which we discuss further in Section 4.1. As in \[14\], we augment our query algorithms with the edge oracle, giving us access to the sampling primitive Rand<sub>H</sub>. Recall that Rand<sub>H</sub> outputs hyperedge e with probability \(w(e)\cdot|e|/Vol(H)\); this |e| bias prevents us from directly using Theorem 3.1 with this primitive as our sampling oracle. To avoid oversampling high cardinality hyperedges, we will therefore perform rejection sampling on Rand<sub>H</sub>: when we sample hyperedge e with Rand<sub>H</sub>, we will only put e into our sparsifier with probability proportional to |e|<sup>-1</sup>, discarding it otherwise. This eliminates the |e| bias, outputting each hyperedge with probability w(e)/Vol(H) (proportional to w(e)). To generate a sample of O, we will call our Rand<sub>H</sub> rejection sampler until it outputs a hyperedge, which in expectation requires \(O(Vol(H)/w(H))\le O(r)\) samples. By the sampling complexity result of Theorem 3.1, this approach can be used to uniform sparsify hypergraphs.

**Theorem 3.7.** Let H=(V,E) be a weighted hypergraph, with rank r unknown. There is a randomized algorithm that makes \(O(nrlogn/\varepsilon^2)\) cut and edge queries and returns a \((1+\varepsilon)\)- approximation to the densest subhypergraph of H.

_Proof._ The correctness of Algorithm 2 follows immediately from the observation that the Rand<sub>H</sub> rejection sampler outputs each hyperedge e with probability w(e)/w(H_) after conditioning that the hyperedge is not discarded. To bound the number of queries, a simple application of the Chernoff bound eq. (1b) suffices. Letting X be the total number of edge queries we make, we have \(\mathbb{E}[X]=CVol(H)/2w(H)\le Cr/2\), using \(2w(H)\le Vol(H)\le rw(H)\). Now,

\(Pr[X>Cr]\le Pr[X-\mathbb{E}[X]\ge 1\cdot\mathbb{E}[X]]\le exp(-\mathbb{E}[X]/3)\ge exp(-240nlogn/3)\le n^{-n}.\)

We implicitly use \(\mathbb{E}[X]\ge C\) in the third inequality. Thus, algorithm 2 requires more than \(n+240nrlogn/\varepsilon^2=O(nrlogn/\varepsilon^2)\) queries with negligible probability, completing the proof.

We note that the 2 factor in the term 2/|e| is a stand-in for the minimum hyperedge cardinality, r<sub>min</sub>, so that we always keep a minimum-cardinality hyperedge with probability 1. While<tbc>

