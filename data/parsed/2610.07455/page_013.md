## 3.1 CSPs

Throughout the paper, _D_ is a fixed finite nonempty domain and \(R\subseteq D^k\) is a fixed relation of arity \(k\ge 1\). We work with ordinary _R_-constraints, without literals or shifts. We refer to this as the general finite-domain setting, since the finite domain and relation are arbitrary. We call _R non-trivial_ if \(\varnothing\unknown R\unknown D^k\). The asymptotic symbols _O<sub>R</sub>_, \(\Omega_R\), and \(\Theta_R\) hide constants that may depend on _R_.

Let _V_={_x_<sub>1</sub>_,...,x<sub>n</sub>_} be a set of variables. An _R-constraint_ is an expression _R(x_<sub>_i_<sub>1</sub></sub>_,...,x<sub>i<sub>k</sub></sub>_), and its _scope_ is the ordered variable tuple (_x_<sub>_i_<sub>1</sub></sub>_,...,x<sub>i<sub>k</sub></sub>_). The order matters unless _R_ is symmetric. Variables may repeat within a scope. An assignment \(\alpha:V\rightarrow D\) satisfies this constraint if \((\alpha(x_{i_1}),\dots,\alpha(x_{i_k}))\in R\).

An unweighted _R_-instance _I_ is a finite multiset of _R_-constraints. Thus the same constraint may occur more than once, and |_I_| counts constraints with multiplicity. A weighted instance gives every occurrence of a constraint _C_ a nonnegative rational weight _w(C_) represented in binary. Unweighted instances are the special case in which every weight is 1. The support of a weighted instance is the set of constraint occurrences with nonzero weight. A weighted subinstance \(H\subseteq I\) uses only occurrences from _I_, but it may give them new nonnegative weights.

An instance is _simple_ if no ordered scope occurs more than once. The degree of a variable is the number of constraint occurrences whose scopes contain it. A constraint contributes once to this degree even if the variable appears more than once in its scope. The maximum variable degree is denoted by \(\Delta(I)\). A relation is _symmetric_ if membership in _R_ is unchanged by permuting the _k_ coordinates. For a symmetric relation, we also use the stronger notion of _unordered simplicity_. This means that no two scopes become the same multiset of variables after their coordinates are reordered.

**Example 3.1.** Let _D_={0,1} and CUT={(0,1),(1,0)}. A CUT-constraint CUT(_x,y_) requires _x_ and _y_ to receive different values. Thus a CUT-instance is a graph, with one variable at each vertex and one constraint at each edge.

## 3.2 Objectives and streaming space

We next define the three objectives studied in the paper. We state them for a weighted _R_-instance, which is the more general setting. The inputs to our three problems are unweighted unless we say otherwise. Let _I_ be a weighted _R_-instance and let \(\alpha\) be an assignment to its variables. We write<tbc>

\(\text{val}_I(\alpha)=\sum_{C\in I\alpha\text{satisfies}C}w(C)\text{and}\text{unsatval}_I(\alpha)=\sum_{C\in I\alpha\text{violates}C}w(C).\)

<tbc>Thus \(\text{val}_I(\alpha)\) is the weight of the satisfied constraints and \(\text{unsatval}_I(\alpha)\) is the weight of the violated constraints. We define

\(\text{OPT}_\text{max}(I)=max_\alpha\text{val}_I(\alpha)\text{and}\text{OPT}_\text{min}(I)=min_\alpha\text{unsatval}_I(\alpha).\)

The set of satisfying assignments is \(\text{Sat}(I)=\{\alpha:\text{unsatval}_I(\alpha)=0\}\).

The problem SAT(_R_) asks whether Sat(_I_) is nonempty. The problem Min-CSP(_R_) asks for OPT<sub>min</sub>(_I_), and a \(\gamma\)-approximation must return a number between OPT<sub>min</sub>(_I_) and \(\gamma\text{OPT}_\text{min}(I)\). We write \(\text{Min-CSP}_\gamma(R)\) for this approximation problem. Finally, Exact-CSP(_R_) asks for the exact value OPT<sub>max</sub>(_I_). Instances are unweighted unless we explicitly say otherwise.

We will also use a stronger guarantee than merely approximating OPT<sub>min</sub>(_I_). A weighted subinstance \(H\subseteq I\) is a \((1\pm\varepsilon)\) _sparsifier_ of _I_ if \((1-\varepsilon)\text{unsatval}_I(\alpha)\le\text{unsatval}_H(\alpha)\le(1+\)<tbc>

