## 13:10 Tight Energy Lower Bounds for Distributed Graph Algorithms

predicates _P_, such that IC(_P_) corresponds to IC(_f_) of the function _f_ that exhibits the highest information cost of all functions that can be computed by simulating an algorithm for _P_ on some \(\ell\)-separated graph family. We obtain Theorem 4, which, intuitively speaking, states that a graph predicate with a high information cost entails a corresponding lower bound on its energy complexity. To see why Theorem 4 holds, we observe that, when simulating an algorithm for _P_ for a given cut \((V_{\le i},V_{>i})\), the nodes on one side of the cut must learn at least \(\frac{\mathsf{IC}(P)}{2}\ge\frac{\mathsf{IC}(f)}{2}\) bits. Consequently, we can instantiate Lemma 1 for obtaining a lower bound on the expected total number of awake rounds of the corresponding nodes. By summing over the \(\ell-1\) possible cuts, the lower bound on the expected total energy complexity follows. Figure 2 shows the general setup used in Theorem 4 for the special case \(\ell=3\).

\(\blacktriangleright\) **Definition 2** (\(\ell\)-Separated Family of Lower Bound Graphs; see Def 2.1 in [25])**.** _Let_ \(f:X\times Y\rightarrow\{\mathsf{true},\mathsf{false}\}\) _be a function and P be a graph predicate. For an integer_ \(\ell>1\)_, a family of graphs_ \(\{G_{x,y}=(V,E_{x,y})|x\in X,y\in Y\}\) _is said to be an_ \(\ell\)-separated family of lower bound graphs w.r.t. _f_ and _P if V can be partitioned into_ \(\ell\) _disjoint subsets_ \(V_1,V_2,\dots,V_{\ell-1},V_\ell\) _such that the following properties hold:_

(_a)_ _Only the existence or the weight of edges in_ \(V_1\times V_1\) _depend on x;_

(_b)_ _Only the existence or the weight of edges in_ \(V_\ell\times V_\ell\) _depend on y;_

(_c)_ _For all_ \(1\le i\le\ell\)_, the vertices in V<sub>i</sub> are only connected to vertices in_ \(V_{i-1}\cup V_i\cup V_{i+1}\) _(where_ \(V_0=V_{\ell+1}=\emptyset\)_)._

_(d)_ _G<sub>x,y</sub> satisfies the predicate P iff f(x,y_)=true.

The equivalence captured by (d) motivates simulating a distributed algorithm for the predicate _P_ in the two-party model of communication complexity, where Alice and Bob want to compute the value of _f(X,Y_). As the simulation follows the standard approach used in previous work, we provide only a high-level overview; additional details can be found in [25, 11].

Simulation Protocol. For an index \(i\in[\ell-1]\), we obtain the _simulation protocol for cut_ \((V_{\le i},V_{\ge i+1})\), by instructing Alice to construct the edges of _G[V_<sub>1</sub>], according to her input _X_, whereas Bob is responsible for constructing \(G[V_\ell]\) according to _Y_ . The rest of _G_ does not depend on their inputs and hence can be (locally) constructed by both. Then, they jointly simulate algorithm A round by round, whereby Alice simulates all nodes in \(V_{\le i}\), and Bob simulates the remaining nodes given by \(V_{\ge i+1}\). Alice and Bob only need to communicate for the messages that cross the cut \((V_{\le i},V_{\ge i+1})\). It is straightforward to verify that the simulation protocol has the same error probability as A.

Maximum Cut Degree and Cut Size. For each \(i\in[\ell]\), we define subsets \(V_i^-,V_i^+\subseteq V_i\) as follows: \(V_i^-\) contains all nodes in _V<sub>i</sub>_ that have a neighbor in _V_<sub>_i_-1</sub> and \(V_i^+\) consists of all nodes having a neighbor in _V_<sub>_i_+1</sub>. We call _s_ the _cut set size_ of the graph family and define \(s=max_{1\le i\le\ell}\left(|V_i^-|,|V_i^+|\right)\). We also define the _maximum cut degree_

\(d_{cut}=max_{1\le i\le\ell-1}\left(max_{u\in V_i}e(u,V_{i+1}),max_{v\in V_{i+1}}e(v,V_i)\right).\) (4)

Information Cost. A common way to quantify how much information the transcript \(\Pi\) of all messages leaks to the players in the two-party model about each other’s input is the _(internal) information cost [8] of the protocol_ \(\pi\) _on distribution_ \(\mu\), defined as

\(\mathsf{IC}_\mu(\pi)=\mathbf{I}[X:\Pi|Y]+\mathbf{I}[Y:\Pi|X].\)

