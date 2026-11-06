## 1 Introduction

If we invest in heavy-duty computation on prior data, can we avoid repeating this effort for similar future inputs? In an era defined by data abundance, this has become a central algorithmic challenge. There is a pressing need for data-driven algorithms that exploit knowledge of existing instances, fundamentally departing from the traditional worst-case design paradigm where inputs are analyzed without any prior context.

In this paper, we explore this question theoretically by proposing a new computational model for graphs and related objects. While this motivation is shared by existing paradigms, such as average- case analysis over input distributions or learning-augmented algorithms with oracles, our model uniquely grants direct access to raw prior data without relying on learned oracles or distributions.

### Model: Algorithms with Isomorphic Priors.

Solving a graph problem \(\Pi\) in our model proceeds in two phases. In the _preprocessing_ phase, the algorithm is given a set of _prior graphs G_<sub>1</sub>_,...,G<sub>k</sub>_ along with their exact optimal values _OPT(G<sub>i</sub>_), which may have been computationally expensive to obtain. Subsequently, in the _query_ phase, the algorithm receives a new _query graph H_. The algorithm must either output _OPT(H_) if _H_ is isomorphic to some _G<sub>i</sub>_, or correctly report that _H_ is not isomorphic to any prior graph.<sup>2</sup> Throughout, we let _n_ and _m_ denote the number of vertices and edges in _H_, respectively. We assume without loss of generality that all prior graphs _G_<sub>1</sub>_,...,G<sub>k</sub>_ also contain exactly _n_ vertices and _m_ edges (because graphs of different sizes cannot be isomorphic).

For concreteness, let us consider two examples of problems \(\Pi\):

1. Negative Triangle: Given a weighted undirected graph _G_, we want to know if _G_ contains a negative triangle, i.e., three vertices _a,b,c_ such that the sum of the weights of edges (_a,b_), (_b,c_), and (_c,a_) is less than zero. This problem can be easily solved in _O(n_<sup>3</sup>) time. Breaking this cubic barrier would be a major breakthrough in fine-grained complexity \[VW10, Vas18\].<tbc>

<tbc>In our model, the algorithm is given weighted undirected graphs _G_<sub>1</sub>_,...,G<sub>k</sub>_ alongside binary indicators _OPT(G<sub>i</sub>_) denoting whether each _G<sub>i</sub>_ contains a negative triangle. After preprocessing this information, the algorithm is given another graph _H_ and must either return whether _H_ contains a negative triangle, or report that _H_ is not isomorphic to any _G<sub>i</sub>_.<tbc>

2. Constrained Shortest Path (CSP): The input consists of a directed graph _G_ where each edge _e_ has a non-negative length \(\ell(e)\) and a non-negative cost _c(e_), two designated vertices _s_ and _t_, and a budget _B_. We want to find a path from _s_ to _t_ whose total cost is at most _B_ and whose total length is minimized. Let _OPT(G_) denote the length of the optimal path.<tbc>

<tbc>CSP is NP-hard \[GJ79, Han80\] and has been extensively studied under various names, such as Restricted Shortest Path or Resource Constrained Shortest Path, from both the theoretical \[ABK25, Ber12, PY00, LR01, MZ00, Has92\] and applied \[YRZ<sup>+</sup>24, WW23, ATHK21, WXYL16, Sto12, MZ01, Xue00, LT92, BC89, AAN83, HZ80\] perspectives.<tbc>

<tbc>In our model, the algorithm is given a budget<sup>3</sup> _B_ and preprocesses prior input graphs _G_<sub>1</sub>_,...,G<sub>k</sub>_ with their respective length and cost functions, along with their precomputed solutions _OPT(G_<sub>1</sub>)_,...,OPT(G<sub>k</sub>_). After preprocessing this information, the algorithm receives a query<tbc>

<sup>2</sup>Recall that graphs _G_ and _H_ are isomorphic (denoted \(G\cong H\)) if one graph can be obtained simply by renaming the vertices of the other; i.e., there exists a bijection \(\pi:V(G)\rightarrow V(H)\) such that \((u,v)\in E(G)\) if and only if \((\pi(u),\pi(v))\in E(H)\). Furthermore, if the edges carry additional attributes (such as weights, lengths, or costs), the bijection must preserve these values; i.e., every attribute \(\alpha\) satisfies \(\alpha_G(u,v)=\alpha_H(\pi(u),\pi(v))\) for all \((u,v)\in E(G)\). <sup>3</sup>We assume for simplicity that the budget is the same for all input instances. Algorithms for this case can be trivially extended to handle varying budgets since, naturally, two instances are isomorphic if and only if their input graphs are isomorphic and their budgets are identical.

