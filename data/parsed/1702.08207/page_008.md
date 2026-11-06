Our construction consists of two main building blocks. First, we design an algorithm based on a bottom-up (dynamic programming) approach, which considers exhaustively feasible sequence assignments and query schedules over a carefully restricted state space of size _n_<sup>_O_(log_n_)</sup> for each node. The output of the algorithm provides us both with a lower bound on OPT(_T_), and with a sequence assignment-based strategy A_<sub>S</sub>_ for solving the tree search problem. The performance of this strategy A_<sub>S</sub>_ is closely linked to the performance of OPT(_T_), however, there is one type of query, namely a query on a vertex of small weight leading to a ‘down’ response, due to whose repeated occurrence the eventual cost difference between COST<sub>A<sub>_S_</sub></sub>(_T_) and OPT(_T_) may eventually become arbitrarily large. To alleviate this difficulty, we introduce an alternative measure of cost which compensates for the appearance of the disadvantageous type of query.

We start by introducing some additional notation. Let \(\omega\in\mathbb{R}_+\), be an arbitrarily fixed value of weight and let \(c\in\mathbb{N}\). The choice of constant \(c\in\mathbb{N}\) will correspond to an approximation ratio of \((1+\varepsilon)\) of the designed scheme for \(\varepsilon=168/c\).

We say that a query to a vertex _v_ is a _light down query_ in some strategy if \(w(v)<c\omega\) and \(x\in V(T_v)\), i.e., it is also a ‘down’ query, where _x_ is the target vertex.

For any strategy A, we denote by \(\mathsf{COST}_\mathcal{A}^{(\omega,c)}(T,x)\) its modified cost of finding target _x_, defined as follows. Let _d<sub>x</sub>_ be the number of light down queries when searching for _x_:<tbc>

\(d_x=\left|\left\{i:w(\mathsf{Q}_{\mathcal{A},i}(T,x))<c\omega\text{and}x\in V(T_{\mathsf{Q}_{\mathcal{A},i}(T,x)})\right\}\right|.\)

<tbc>Then, the modified cost \(\mathsf{COST}_\mathcal{A}^{(\omega,c)}(T,x)\) is:

\(\mathsf{COST}_\mathcal{A}^{(\omega,c)}(T,x)=\mathsf{COST}_\mathcal{A}(T,x)-(2c+1)\omega d_x.\) (3.1)

and by a natural extension of notation:

\(\mathsf{COST}_\mathcal{A}^{(\omega,c)}(T)=max_{x\in V}\mathsf{COST}_\mathcal{A}^{(\omega,c)}(T,x).\)

The technical result which we will obtain in Section 4 may now be stated as follows.

**Proposition 3.1.** _For any_ \(c\in\mathbb{N}\), \(L\in\mathbb{N}\)_, there exists an algorithm running in time_ (_cn_)<sup>_O(L_)</sup>_, which for any tree T constructs a stable sequence assignment S and computes a value of_ \(\omega\) _such that_ \(\omega\le\frac{1}{L}\mathsf{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)\) _and:_

\(\mathsf{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)\le\left(1+\frac{12}{c}\right)\mathsf{OPT}(T).\)

In order to convert the obtained strategy A_<sub>S</sub>_ with a small value of \(\mathsf{COST}^{(\omega,c)}\) into a strategy with small COST, we describe in Section 5 an appropriate strategy conversion mechanism. The approach we adopt is applicable to any strategy based on a stable sequence assignment and consists in concatenating, for each vertex \(v\in V\) , a prefix to the query sequence _S(v_) in the form of a separately computed sequence _R(v_), which does not depend on _S(v_). The considered query sequences are thus of the form \(R(v)\circ S(v)\), where the symbol "\(\circ\)" represents sequence concatenation. Intuitively, the sequences _R_, taken over the whole tree, reflect the structure of a specific solution to the unweighted tree search problem on a contraction of tree _T_, in which each edge connecting a node to a child with weight at least \(c\omega\) is contracted. We recall that the optimal number of queries to reach a target in an unweighted tree is _O_(log_n_), and the goal of this conversion is to reduce the number of light down queries in the combined strategy to at most _O_(log_n_).

