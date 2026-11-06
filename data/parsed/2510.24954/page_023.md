**Definition 4.10.** A _tree flow sparsifier T_ of _G_ with congestion slack \(\kappa\) is such that

1. The set of leaves of _T_ corresponds to _V(G_).<tbc>

2. Every demand on _V(G_) routable in _G_ is routable in _T_<tbc>

3. Every demand on _V(G_) routable in _T_ is routable in _G_ with congestion \(\kappa\).

Clearly from the definition, a tree flow sparsifier with depth _d_ and congestion slack \(\kappa\) is a congestion shortcut with congestion slack \(\kappa\), hopbound 2_d_, and size _O(n_). There exists a tree flow sparsifier with depth _O_(log_n_) and congestion slack _O_(log<sup>2</sup>_n_loglog_n_) \[HHR03\]. Moreover, there is a parallel algorithm that construct a tree flow sparsifier with depth _O_(log_n_) and congestion slack _O_(log<sup>9</sup>_n_) in \(\tilde{O}(m)\) work and polylog(_n_) depth \[AKL<sup>+</sup>24\].

If this can be generalized to directed graphs even when the shortcut size is \(\tilde{O}(m)\), then Theorem 4.9 would imply an exact max flow algorithm with \(\tilde{O}(m)\) work and polylog(_n_) depth.

**Corollary 4.11.** _Suppose there is an algorithm that, given O(m)-edge O(n)-vertex directed graph, computes a congestion shortcut of hopbound_ polylog(_n), length slack_ polylog(_n), and size_ \(\tilde{O}(m)\)_. Then, there is an algorithm for computing exact max flow in an m-edge n-vertex directed graphs in_ \(\tilde{O}(m)\) _work and_ polylog(_n_) _depth._

Unfortunately, there is no prior work on this and we leave it an interesting open problem.

**Proof of Theorem 4.9**

_Proof._ We first give an algorithm computing approximate max flow which routes a feasible flow whose value is at least \(1/2\kappa\) times the optimal value on the input graph. Then show how to turn it into an exact max flow algorithm.

**Approximate max flow.** We first use A to compute a congestion shortcut on _G_, denoted by \(E'\). Let \(G'=G\cup E'\). We will use Theorem 3.1 (1) of \[HHS23\], stated as follows.

**Lemma 4.12** (Theorem 3.1 (1) of \[HHS23\])**.** _Given a directed graph G with edge capacities and unit edge length, length bound_ \(h\ge 1\)_, approximation parameter_ \(\epsilon>0\)_, and source and sink_ \(s,t\in V\)_, there is an algorithm computing a_ \(1-\epsilon\) _approximate maximum h-length flow, in the sense that the flow value is at least_ \(1-\epsilon\) _times the maximum h-length flow from s to t in G. The algorithm takes_ \(\widetilde{O}\left(m\cdot h^{17}\cdot\frac{1}{\epsilon^9}\right)\) _work and_ \(\widetilde{O}\left(h^{17}\cdot\frac{1}{\epsilon^9}\right)\) _depth._

We use Lemma 4.12 with parameter \(\epsilon=1/2\), _h_ the same as our _h_, and the digraph the same as \(G'\) with unit length. The guarantee for the output is a flow \(F'\), which is a \(1-\epsilon\) approximation for maximum _h_-length flow, which, in our case, is the maximum flow with hop bound _h_ since the graph has unit length. Then, we call the backward mapping algorithm A to turn \(F'\) into a flow _F_ on _G_ with congestion \(\kappa\). To make _F_ feasible, we scale the flow on each edge down by a factor of \(\kappa\), and denote the final flow as \(F/\kappa\). According to Definition 4.1, every flow on _G_ corresponds to a feasible flow on \(G'\) with hop bound _h_ and the same value. Thus, \(F'\) has a value of at least 1/2 times the max flow value on _G_, which implies that \(F/\kappa\) is a \(1/2\kappa\) approximate max flow on _G_.

The algorithm takes an input graph of _m_ edges and _n_ vertices, uses 1 call to A and \(\mathcal{A}'\), and additional \(\widetilde{O}\left(\text{poly}(h)\cdot(m+m')\right)\) work and poly(_h_) depth using Lemma 4.12.

