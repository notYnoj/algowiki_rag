<tbc>and in line with statistical expectations. It remains the case that even some simple graphs are challenging for enumeration of maximum cliques.

## 4 Quantum tion

As a first step in creating an efficient quantum version of this algorithm, we start by attempting to solve this embedded combinatorial optimisation problem using quantum approaches. First, let us formalise the problem.

**Definition 1** (The Maximum Weighted Clique Enumeration Problem)**.** Given a graph _G_=(_V,E_) and a function \(w:V\rightarrow\mathbb{R}\), the _Maximum Weighted Clique Enumeration Problem_ is to find all subsets \(C\subseteq V\) that maximises \(\sum_{i\in C}w(i)\) subject to the constraint that \((i,j)\in E\) for all \(i,j\in C\).

This differs slightly from the most common variant of this problem in two main ways: firstly, we have a weighted graph, and secondly, our desired output is all MWCs, rather than a single example.

The most common way for solving combinatorial optimisation problems on a quantum computer is using Quantum Approximate Optimisation Algorithm (QAOA) \[8\]. This algorithm takes a cost Hamiltonian with at most quadratic interactions and in its limit, outputs a ground state of the Hamiltonian. QAOA is an example of a solver for Quadratic Unconstrained Binary Optimisation (QUBO) problems, and we start by developing MWC solvers using this approach. In general, quantum implementations of these solvers are typically sampling-based, and hence we use this to our advantage to attempt to enumerate all optima via this sampling.

Whereas the number of edges within a clique changes with the size, \(\frac{n(n-1)}{2}\) edges for a _n_- vertex clique, the number of pairs of vertices that does not share an edge does not change, it is always 0. Hence, rather than counting the number of edges in a potential solution which requires comparing a non-trivial expression, it is much simpler to count the number of missing edges. This inspires us to take the complement of the graph and instead find a maximum weighted subset of vertices that do not have any edges between any pair of vertices. This is the Maximum Weighted Independent Set (MWIS) Enumeration Problem.

**Definition 2** (The Maximum Weighted Independent Set Enumeration Problem)**.** Given a graph _G_=(_V,E_) and a function \(w:V\rightarrow\mathbb{R}\), the _Maximum Weighted Independent Set Problem_ is to find all subsets \(C\subseteq V\) that maximises \(\sum_{i\in C}w(i)\) subject to the constraint that \((i,j)\notin E\) for all \(i,j\in C\).

First, let us describe the general QUBO approach. The main step involves constructing a cost function representing the specific input problem. In the broadest terms, we simply want to choose a subset of the vertices that maximises the total weight, subject to some constraints given by the edges. Since the optimisation methods we wish to employ solve unconstrained optimisation problems, we utilise a Lagrange multiplier to express the constraints. Then for a (now complement) graph _G_=(_V,E_), the cost function that we want to maximise takes<tbc>

