We next prove that one of the dual nodes _f<sub>i</sub>_ is balanced.

**Claim 2.** _Let f<sub>j</sub> be the lowest node on P(f_) _whose subtree weighs more than_ \(\frac{3}{4}\cdot w_F(T^*)\) _but its children in T_<sup>∗</sup> _have subtrees weighing at most_ \(\frac{3}{4}\cdot w_F(T^*)\)_. The child f_<sub>_j_+1</sub> _of f<sub>j</sub> is_ \((\frac{1}{4},\frac{3}{4})\)_-balanced._

_Proof of Claim 2._ First we prove that such _f<sub>j</sub>_ exists. Recall that _f_ was chosen such that it is a \((\frac{1}{4},\frac{3}{4})\)- critical node. This means that \(w(T_f^*)>\frac{3}{4}\cdot w(T^*)\), but all its children in _T_ have subtrees of weight smaller than \(\frac{1}{4}\cdot w(T^*)\). After we replace the face _f_ with the path _P(f_), the total weight of all nodes _f<sub>i</sub>_ in _P(f_) is the same as the original weight of _f_, and the weight of all other nodes is the same. Therefore, we have that \(w(T_{f_1}^*)>\frac{3}{4}\cdot w(T^*)\). On the other hand, consider the last node _f_<sub>_k_-2</sub> on _P(f_). We show that \(w(T_{f_{k-2}}^*)<\frac{3}{4}w(T^*)\). For this, first note that each face _f<sub>i</sub>_ has three vertices, which means that in the dual graph the node _f<sub>i</sub>_ has at most three neighbors. One of the neighbors of _f_<sub>_k_-2</sub> is the node _f_<sub>_k_-3</sub> of _P(f_) (the parent of _f_<sub>_k_-2</sub> in _T_<sup>∗</sup>) and it has at most two children not in _P(f_). Since _f_ is a critical node, each one of these neighbors _g_ not in _P(f_) has \(w(T_g^*)<\frac{1}{4}\cdot w(T^*)\), as explained above. Also, as the weights of the nodes _f<sub>i</sub>_ are \(\frac{1}{4}\)-proper (Claim 1), we get that \(w(T_{f_{k-2}}^*)<\frac{1}{4}\cdot w(T^*)+2\cdot\frac{1}{4}\cdot w(T^*)=\frac{3}{4}\cdot w(T^*)\).

Hence, there exists a node _f<sub>j</sub>_ in _P(f_) whose subtree weighs more than \(\frac{3}{4}\cdot w_F(T^*)\) but its children in _T_<sup>∗</sup> have subtrees weighing at most \(\frac{3}{4}\cdot w_F(T^*)\) (note that the children not on _P(f_) weigh less than \(\frac{1}{4}\cdot w(T^*)\) as explained above, and we are looking for the first _f<sub>j</sub>_ in _P(f_) where this condition holds). Note that \(f_j\neq f_{k-2}\) as we showed that \(w(T_{f_{k-2}}^*)<\frac{3}{4}\cdot w(T^*)\). Hence, _f<sub>j</sub>_ has a child _f_<sub>_j_+1</sub>. By definition, we have that \(w(T_{f_{j+1}}^*)\le\frac{3}{4}\cdot w(T^*)\). To show that _f_<sub>_j_+1</sub> is balanced we will show that \(w(T_{f_{j+1}}^*)>\frac{1}{4}\cdot w(T^*)\). Recall that \(w(T_{f_j}^*)>\frac{3}{4}\cdot w(T^*)\). Recall, _f<sub>j</sub>_ has at most one child _g_ not on _P(f_), in addition to the child _f_<sub>_j_+1</sub> on _P(f_). The child _g_ not on _P(f_) has \(w(T_g^*)<\frac{1}{4}\cdot w(T^*)\) as explained above. And since the weights are \(\frac{1}{4}\)-proper we have that \(w_F(f_j)\le\frac{1}{4}\cdot w(T^*)\). On the other hand \(w(T_{f_{j+1}}^*)=w(T_{f_j}^*)-w_F(f_j)-w(T_g^*)>\frac{3}{4}\cdot w(T^*)-\frac{1}{4}\cdot w(T^*)-\frac{1}{4}\cdot w(T^*)=\frac{1}{4}\cdot w(T^*)\). Hence, _f_<sub>_j_+1</sub> is indeed a \((\frac{1}{4},\frac{3}{4})\)-balanced node as needed.

By the above claim, Case 2 indeed reduces to Case 1. That is, the edge _e_=(_f<sub>j</sub>,f_<sub>_j_+1</sub>) in the new dual tree defines two nodes \(u,v\in G\) s.t. the _u_-to-_v_ path _P_ in _T_ is a 3/4-balanced path separator (in<tbc>

V1
V10
V2
f
V9
V3
V4
V5
V6
V7
V8

f1
f2
f8
f3
f4
f5
f6
f7

