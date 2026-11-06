Here it should be stressed that the algorithm in Theorem 3 estimates the size of a stable matching, not just an \(\epsilon\)-stable matching.

### 1.4 Overview

The rest of the paper is structured as follows. In Section 2 we discuss the specific choices that we make in this work, in particular, why and how an almost stable matching differs from a stable matching in a distributed setting. Section 3 reviews related work. Sections 4 and 5 present and analyse the distributed, truncated version of the Gale-Shapley algorithm. Section 6 applies this algorithm to prove Theorems 1-3.

## 2 Motivation and Implications

### 2.1 Local Algorithms

The running time _T_ of the algorithms presented in this work only depends on the degree bound \(\Delta\) and the desired stability or approximation guarantee \(\epsilon\). For a constant \(\Delta\) and \(\epsilon\), these are constant-time algorithms; the running time is independent of the number of nodes in the network, the diameter of the network, or other global properties. Such constant-time distributed algorithms are known as local algorithms [23, 27, 32].

Besides the practical advantage of a low time complexity, our positive results also provide insight into the structure of the stable marriage problem. We mention three interpretations of Theorem 1, from different perspectives; these all follow from the observation that in _T_ synchronous communication steps, information can only be propagated from distance _T_ in the network.

• _Robustness and dynamic graphs_. The \(\epsilon\)-stable matching _M_ from Theorem 1 is robust in a dynamic network. A change in the network only affects _M_ in the radius-_T_ neighbourhood around the point of change.<tbc>

• _Available information_. Information within the radius-_T_ neighbourhood of an edge _e_ is sufficient to determine whether _e_ is part of the globally consistent \(\epsilon\)-stable matching _M_.<tbc>

• _Parallelism and circuit complexity_. For any graph, we can construct a bounded-fan-in Boolean circuit that maps the matching preferences to an \(\epsilon\)-stable matching. The depth of the circuit only depends on the constants \(\Delta\) and \(\epsilon\), not on the size of the graph.

As we will discuss in the next section, these properties highlight a substantial difference between stable and almost stable matchings.

