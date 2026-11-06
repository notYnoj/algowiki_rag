<tbc>demands of the Coupled Arcs Gadget and is thus not available for routing _s<sub>x</sub>t<sub>x</sub>_. If _x<sub>i</sub>_ occurs positively in _C_, this means that _f(P<sub>x<sub>i</sub></sub>_)=0, and so \(\phi(x_i)=true\), satisfying the clause. On the hand, if _x<sub>i</sub>_ occurs negatively in _C_, this means that _f(N<sub>x<sub>i</sub></sub>_)=0 and _f(P<sub>x<sub>i</sub></sub>_)=1, and so \(\phi(x_i)=false\), satisfying the clause. As this holds for any clause, \(\phi\) is a satisfying assignment, concluding the proof of reduction.

### C.4 Exists-Embedding Uncrossed Multiflow

**Theorem C.6.** _It is NP-hard to determine whether there is an embedding of G in which_ (_G,H_) _has a fractional uncrossed multiflow._

_Proof._ We reduce from the fixed-embedding version of fractional uncrossed multiflow. Start with a fixed embedding of _G_. Consider the following operation: add an edge _e_=(_u_<sub>1</sub>_,u_<sub>2</sub>) between two nodes _u_<sub>1</sub>_,u_<sub>2</sub> on the same face, then subdivide it into a path _P=u_<sub>1</sub>_,v_<sub>1</sub>_,v_<sub>2</sub>_,u_<sub>2</sub>, and add demand edges _u_<sub>1</sub>_v_<sub>1</sub>_,u_<sub>2</sub>_v_<sub>2</sub>. The new supply and demand edges have unit weight.

**Claim C.7.** (_G,H_) _has an uncrossed solution (in the original embedding) if and only if the new instance has an uncrossed solution._

_Proof._ It is straightforward to verify that if (_G,H_) has an uncrossed solution, then so does the new instance. We show the converse, that if the new instance has an uncrossed solution, so too does (_G,H_). Consider an arbitrary uncrossed solution _f_ for the new instance. It suffices to show that there is an uncrossed solution where the demand _u<sub>i</sub>v<sub>i</sub>_ is routed entirely on the supply edge _u<sub>i</sub>v<sub>i</sub>_ for _i_=1,2.

Observe that, in _f_, all flow for _u_<sub>1</sub>_v_<sub>1</sub> that is not routed through _u_<sub>1</sub>_v_<sub>1</sub> must be routed through _u_<sub>2</sub>_v_<sub>2</sub>. So, _f_<sup>_u_<sub>1</sub>_v_<sub>1</sub></sup>(_u_<sub>1</sub>_v_<sub>1</sub>)+_f_<sup>_u_<sub>1</sub>_v_<sub>1</sub></sup>(_u_<sub>2</sub>_v_<sub>2</sub>)=1. Similarly, _f_<sup>_u_<sub>2</sub>_v_<sub>2</sub></sup>(_u_<sub>2</sub>_v_<sub>2</sub>)+_f_<sup>_u_<sub>2</sub>_v_<sub>2</sub></sup>(_u_<sub>1</sub>_v_<sub>1</sub>)=1. So, between the two new demands, all capacity on the new supply edges _u_<sub>1</sub>_v_<sub>1</sub>_,u_<sub>2</sub>_v_<sub>2</sub> is used. Therefore, the demands of the original demand graph _H_ are routed (uncrossed) inside the original supply graph _G_. So (_G,H_) has an uncrossed solution.

\(\diamond\)

We then repeat this operation until the supply graph is a (subdivision of) a 3-connected graph, which has a unique embedding. The claim implies that the original instance (_G,H_) has an uncrossed solution (in its given embedding) if and only if the new instance has an uncrossed solution in its embedding, which by the uniqueness of the embedding is equivalent to the new instance having an uncrossed solution in some embedding.

## D Colouring Uncrossed String Graphs

In this section, we prove the following result.

**Theorem D.1.** _Let U be an uncrossed string graph arising from a realization with at most k paths on any edge. Then_ \(\chi(U)=O(k^2log|E(U)|)\).

The following is the key lemma.

**Lemma D.2.** _Let U be an uncrossed string graph with a load k realization_ (_G,_P)_. Then U is the union of O(k_<sup>2</sup>log|_E(U_)|) _planar graphs._

_Proof._ We generate a random subgraph _H_=(_S,F_) of _U_ as follows. First, we select random subset \(S\subseteq\mathcal{P}\) by drawing each \(P\in\mathcal{P}\) independently and uniformly at random with probability \(q=\frac{1}{k}\). Now, for each \(e\in E(G)\) such that \(|S\cap\mathcal{P}_e|=2\) exactly, we add to _F_ an edge between the two members of \(S\cap\mathcal{P}_e\). Note that _H_ is planar.

Let \(PP'\in E(U)\), and consider the event that \(PP'\in E(H)\). This event happens if there exists some _e_ with \(P,P'\in\mathcal{P}_e\) where \(P\in S\), \(P'\in S\), and no other path in P_<sub>e</sub>_ is in _S_. Clearly there is at least one _e_ such that \(P,P'\in\mathcal{P}_e\), and we lower bound the probability that \(PP'\) is included due to this particular edge. Then,<tbc>

\(Pr\left[PP'\in E(H)\right]\ge q\cdot q\cdot(1-q)^{k-2}\ge\frac{1}{k^2}\left(1-\frac{1}{k}\right)^{k-2}\ge\frac{1}{ek^2},\)

