## 1.2 Universe Reductions for APSP

The main goal of this paper is to establish that these three hypotheses are actually equivalent. It is reasonable to expect that such an equivalence result hinges on the assumption that \(\omega=2\); we will later comment on this issue in detail, but for now assume that \(\omega=2\). The two missing "hard" directions can both be seen as _universe reductions_ for APSP: from large (polynomially bounded) weights to weights bounded by _n_ (_large- universe reduction_), and from weights bounded by _n_ to no weights at all (_small-universe reduction_). We start with the latter task which turns out to be the slightly simpler one.

### 1.2.1 Small-Universe Reduction: From Small to No Weights

There has been partial progress towards a small-universe reduction. In the same paper that introduces the Strong APSP Hypothesis, Chan, Vassilevska W., and Xu \[35\] develop an exciting technique called "Fredman’s trick meets dominance product" and thereby establish a non-tight reduction: Directed Unweighted APSP cannot be solved in time \(O(n^{7/3-\epsilon})\) unless the Strong APSP Hypothesis fails. Ultimately, they left open if the two hypotheses are equivalent, but their technique is inspiring. We propose a new approach, _low-rank APSP_, and based on this new technique we successfully prove the desired equivalence result:

**Theorem 1.7** (Strong APSP Implies Directed Unweighted APSP)**.** _APSP in directed unweighted graphs cannot be solved in time_ \(O(n^{2.5-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong APSP Hypothesis fails. In particular, conditioned on_ \(\omega=2\)_, the Strong APSP and Directed Unweighted APSP Hypotheses are equivalent._

Theorem 1.7 constitutes one of the very rare cases that two fine-grained hypotheses are shown to be equivalent--in fact, we are not aware of any prior case where two explicitly established fine-grained assumptions have later been shown to be equivalent. Moreover, Theorem 1.7 constitutes an equivalence result of two problems with the same input and output size but _different_ complexities (_n_<sup>3</sup> versus _n_<sup>2.5</sup>). This, too, is quite exceptional; there are only few other examples such as the Mono-Convolution problem by Lincoln, Vassilevska W., and Polak \[73\].

More generally, our universe reduction correctly interpolates between unweighted and \[_n_\]-weighted graphs, both in the directed and undirected settings. Specifically, for directed graphs with weights {0_,...,u_} Zwick’s algorithm \[104\] takes time \(\tilde{O}(n^{2+1/(4-\omega)}u^{1/(4-\omega)})\). If \(\omega=2\) then this running time becomes \(\tilde{O}(n^{2.5}\sqrt{u})\). For undirected graphs with weights {0_,...,u_} the Shoshan-Zwick algorithm \[90\] takes time \(\tilde{O}(n^\omega u)\). We show both algorithms are best-possible if \(\omega=2\), for all values of _u_:

**Theorem 1.8** (Zwick’s Algorithm is Optimal)**.** _Let_ \(0\le\delta\le 1\) _be a constant. APSP in directed graphs with weights_ \(\{0,\dots,n^\delta\}\) _cannot be solved in time_ \(O(n^{2.5+\delta/2-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong APSP Hypothesis fails._

**Theorem 1.9** (Shoshan-Zwick Algorithm is Optimal)**.** _Let_ \(0\le\delta\le 1\) _be a constant. APSP in undirected graphs with weights_ \(\{0,\dots,n^\delta\}\) _cannot be solved in time_ \(O(n^{2+\delta-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong APSP Hypothesis fails._

### 1.2.2 Large-Universe Reduction: From Large to Small Weights

Next, focus on the universe reduction from polynomially large weights to weights bounded by _n_. This reduction appears even more difficult. In fact, we are neither aware of any prior progress on this question, nor are we aware of any other (exact) graph distance problem where a similar weight reduction is known. In the related, more restricted setting where one graph has to be mapped one-to-one to a graph with smaller weights such a reduction turns out to be impossible \[18\].

Our approach involves two steps. The first builds on the new _low-rank APSP_ technique from before. The second builds on _additive combinatorics_. In fact, the _low-rank APSP_ technique also relies on some additive combinatorics, so this work should be seen as part of a recent trend to exploit additive combinatorics in fine-grained complexity and algorithm design \[32, 27, 50, 29, 28, 1, 35, 70, 39, 20, 69, 41, 38, 40, 23, 52, 53, 4\].

