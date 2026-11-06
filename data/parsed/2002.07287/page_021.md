Theorem 5. Parameter _k_ summed over all calls is bounded by \(\sum_udeg(u)=O(n)\) and parameter _N_ over all calls is bounded by \(\sum_udeg(u)logn=O(nlogn)\) since we made sure that the classification number can be stored in _O_(log_n_) bits (a classification number is made up of tuples with values of size _O(n_)). Thus, the total time is bounded by \(O(k+N/\tau)=O(n)\).

We next consider the calls to Theorem 5. Since every node is part of one set _V<sub>h</sub>_, _k_ summed over all calls is bounded as before by _O(n_). Moreover, each node with its classification number is part of one classification vector. Thus, _N_ over all calls is bounded as before by _O(n_log_n_). Due to our choice of \(\tau\), we obtain a total running time of _O(n_). \(\blacktriangleleft\)

We generalize Lemma 17 to unrooted trees by first determining the center of a tree space efficiently, which is a set of constant size that is maximal distance to a leaf. Using each vertex in the center as a (possible) root, we then run our rooted isomorphism algorithm. A _center_ of a tree _T_ is a set consisting of either one node or two adjacent nodes of _T_ such that the distance to a leaf is maximal for these nodes compared to all other nodes of _T_. It is known that every tree has a unique center [47, Theorem 4.2]. If two trees _T_<sub>1</sub> and _T_<sub>2</sub> are isomorphic, then every isomorphism function maps the center nodes of _T_<sub>1</sub> to the center nodes of _T_<sub>2</sub>.

\(\blacktriangleright\) **Lemma 18.** _Given an n-node tree T_=(_V,E_) _there is a linear-time O(n)-bit algorithm that determines the center of T._

**Proof.** Harary [47, Theorem 4.2] determines the center of a tree in rounds where, in each round, all nodes of degree 1 are removed. The algorithm stops if at most two nodes are left, which are selected as the center.

We follow a similar approach, but cannot afford to manipulate the given trees. For our approach we need to be able to read and reduce the degree of a node. We also can not use Lemma 15 since it requires a rooted tree. Alternatively, we store the initial degrees of all nodes as self-delimiting numbers by using static space allocation (Section 2).

Similar to Harary’s algorithm, our algorithm also works in rounds. We use a choice dictionary _C_ consisting of the nodes of degree one, which we initially fill by scanning through the whole tree. Then, while we iterate over each node _u=C.choice_, we delete _u_ from _C_, increment an initial-zero global counter _k_ to be able to determine how many nodes remain in the tree, and decrement the degree of the only node _v_ (neighbor of _u_) with \(deg(v)\ge 2\). Intuitively speaking this simulates the deletion of _u_. If the degree of _v_ is 1 after decrementing, we add _v_ in a second choice dictionary \(C'\). After the iteration over the nodes in _C_ is finished, we swap the meaning of _C_ with \(C'\). If at most two nodes remain (i.e, \(k\ge n-2\)), we output the nodes in _C_ as the center of the tree. Otherwise, we start the next round.

Storing two choice dictionaries and all degrees can be done with _O(n_) bits. Moreover, since the total degree in a tree is bounded by _O(n_), our approach runs in _O(n_) time. \(\blacktriangleleft\)

We can check isomorphism for two given non-rooted trees _T_<sub>1</sub> and _T_<sub>2</sub> by first computing the center _C_<sub>_T_<sub>1</sub></sub> and _C_<sub>_T_<sub>2</sub></sub> of _T_<sub>1</sub> and _T_<sub>2</sub>, respectively. Then, we iterate over the 4 possibilities to choose a root \(r_{T_1}\in C_{T_1}\) and \(r_{T_2}\in C_{T_2}\) and apply Lemma 17. _T_<sub>1</sub> and _T_<sub>2</sub> are isomorphic exactly if one possible rooted versions of _T_<sub>1</sub> and _T_<sub>2</sub> are isomorphic. We thus can conclude the next theorem.

\(\blacktriangleright\) **Theorem 19.** _Given two (unrooted) trees T_<sub>1</sub> _and T_<sub>2</sub> _there is an algorithm that outputs if T_<sub>1</sub> _and T_<sub>2</sub> _are isomorphic in linear-time using O(n_) _bits._

We finally consider isomorphism on node-colored trees. We view node-colored trees as trees where each node has a color assigned in the form of a bit string. Two colored trees

