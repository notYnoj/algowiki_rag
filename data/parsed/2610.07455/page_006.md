explanation and concrete examples are given in the technical overview (Section 2).

## AI Disclosure.

Generative AI tools including GPT 5.6 Sol Medium/High were used for language editing, improving exposition, checking the clarity of parts of the manuscript and to assist with routine mathematical tasks that do not require a significant level of innovation or with verifying proofs. They were not used to generate the mathematical results or proofs, and the authors take full responsibility for the contents of the paper.

## 2 Technical overview

In this section, we explain the main structural ideas behind our results. Our central idea is to replace every relation by a reduced form called its _core_, which we define formally in Section 3.4. We first use a relation of Sharma and Velusamy \[SV26a\] to explain why we must reduce to the core. We then explain the satisfiability lower bound using CUT={(0,1),(1,0)} and return to CUT to explain the exact optimization lower bound. As we will show, the satisfiability and exact-optimization lower bounds crucially rely on whether we can _hard-pin_ variables, meaning fix them to chosen values in the domain. _R_-constraints usually cannot do this directly, so we instead build gadgets that simulate such pinnings up to unavoidable symmetries of the relation. The main fact that makes these gadgets possible is that the relation is a core. For satisfiability, we need a gadget whose satisfying assignments give the variables the desired values. For exact optimization, an optimal assignment may violate some gadget constraints, so we need a stronger construction that makes every deviation from the desired values unprofitable.

### 2.1 Reduction to the core

Sharma and Velusamy \[SV26a\] proved that the one-pass space needed to decide satisfiability for CSPs with literals is characterized, up to a logarithmic factor, by the _non-redundancy_ parameter NRD_<sub>n</sub>(R_). This parameter is the maximum number of constraints in an _R_-instance in which every constraint is independently necessary. Equivalently, every constraint has a _witness assignment_ that violates it and satisfies all the other constraints. We give the formal definition in Section 3.3.

They also showed that without literals, NRD_<sub>n</sub>(R_) need not be the right parameter, using the following counterexample<tbc>

\(T=\{(0,1),(1,0),(0,3),(3,0),(1,2),(2,1)\}\subseteq\{0,1,2,3\}^2.\)

<tbc>Using known characterizations of non-redundancy, one can prove that \(\mathsf{NRD}_n(T)=\Theta(n^2)\) \[BŽ20; BCK20; KPS25; SV26a\]. However, satisfiability for _T_ can be checked in _O(n_log_n_) space. To see this, notice that _T(a,b_) holds when _a_ and _b_ have opposite parity and at least one of them belongs to {0,1}. Given a _T_-instance, form its underlying graph whose vertices are the variables and whose edges are the pairs {_x,y_} on which a constraint _T(x,y_) appears. The _T_-instance is satisfiable exactly when this graph is bipartite. Indeed, every satisfying assignment gives a bipartition according to the parity of the assigned values. Conversely, any bipartition can be made satisfying by assigning 0 to one side and 1 to the other. Bipartiteness can be decided in one pass using _O(n_log_n_) bits \[SV26a\].

This suggests that the values 2 and 3 are unnecessary for solving the instance. So, let’s consider the map<tbc>

\(\sigma(0)=\sigma(2)=0\text{and}\sigma(1)=\sigma(3)=1.\)

