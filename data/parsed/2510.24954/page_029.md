<tbc>a pair of vertices (_s,t_) in the transitive closure of path _P_. We conclude that \(G_+^S\neq G_+^{S^\prime}\), as claimed. This implies that there are 2<sup>|P|</sup> distinct, vertex-labeled graphs in graph family G.

Finally, we observe that there are at most (_x+n_)<sup>2_x_</sup> distinct subgraphs of the universal graph \(\hat{G}\) with at most _x+n_ vertices and at most _x_ edges, so \((x+n)^{2x}\ge 2^{|\mathcal{P}|}\). Taking the log of both sides, we get \(xlog(x+n)\ge|\mathcal{P}|\), which implies that \(x\ge|\mathcal{P}|/log(|\mathcal{P}|)=\tilde{\Omega}(m^{1-\epsilon})\). Then by the definition of _x_, one of the Steiner shortcut graphs \(G_+^S\), where \(S\subseteq\mathcal{P}\), has size at least \(x=\tilde{\Omega}(m^{1-\epsilon})\). This completes the proof.

## B Reachability Shortcuts as OR-circuit Depth Reduction

In this section we will show that the existence of Steiner shortcuts for reachability is equivalent to the existence of a depth reduction for a certain class of Boolean circuits.

**Theorem B.1.** _Conjecture 2 is equivalent to Conjecture 3._

### Preliminaries.

A Boolean circuit is a directed acyclic graph with a set of source nodes _S_, called input gates, and a set of sink nodes _T_, called output gates. The input gates are labeled with binary variables _x_<sub>1</sub>_,...,x<sub>n</sub>_, and the output gates are labeled with binary variables _y_<sub>1</sub>_,...,y<sub>n</sub>_.

Each non-source/sink node in the circuit computes a Boolean function (e.g., AND, OR, NOT). We will restrict our attention to circuits with only OR gates, which we refer to as OR-circuits. Our OR gates will have unbounded fan-in. We measure the size of a Boolean circuit by the number of edges it has. We define the depth of a circuit as the length of the longest path in the directed acyclic graph. We define the _diameter_ of a circuit as the largest distance between an input gate and an output gate in the directed acyclic graph.

The connection between reachability and OR-circuits can be summarized by the following observation.

**Observation B.2.** _Let C be an OR-circuit with input gates_ \(S\subseteq V(C)\) _and output gates_ \(T\subseteq V(C)\)_. Let_ \(t\in T\) _be an output gate labeled with binary variable_ \(y\in\{0,1\}\)_. Then output gate t returns the value y_=1 _if and only if there exists an input gate_ \(s\in S\) _such that s can reach t in C, and input gate s is labeled with a binary variable_ \(x\in\{0,1\}\) _that has the value x_=1.

We can now prove an equivalence between diameter-reducing Steiner shortcuts and the existence of diameter-reductions for OR-circuits.

**Lemma B.3.** _Let s(m_) _and d(m_) _be functions such that s(m),d(m_)=_O_(poly(_m_))_. Then the following two statements are equivalent:_

(_1)_ _Every directed graph on n nodes and m edges admits a Steiner reachability shortcut with s(m_)+_O(m+n_) _additional edges and diameter d(m_)+_O_(1).<tbc>

_(2)_ _Let_ \(f:\{0,1\}^n\mapsto\{0,1\}^n\) _be a multi-output Boolean function that can be computed by a Boolean_ OR_-circuit with m edges. Then f can be computed by an_ OR_-circuit with s(m_)+_O(m+n_) _edges and diameter d(m_)+_O_(1).

_Proof._ We will prove each direction separately.

