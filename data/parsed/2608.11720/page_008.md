<tbc>X with outputs in a _finite_ set \(\Sigma\) produces a random element in \(\Sigma\). Formally, a measurement on X is described by a Positive Operator-Valued Measure, henceforth _POVM_: a tuple of positive semi-definite matrices \(\Pi_a\) for \(a\in\Sigma\) such that \(\sum_{a\in\Sigma}\Pi_a=\mathbb{1}\). The output probability distribution is given by _Born’s rule_: the probability of output \(a\in\Sigma\) is \(\mathrm{Tr}(\Pi_a\rho)\).

## 3.2. The quantum-LOCAL and quantum-PN models.

The quantum-LOCAL model is a model of distributed quantum computing. The network is represented by a graph where each vertex is a quantum processor, and each edge allows quantum communication between neighboring nodes. Computation proceeds in synchronous rounds. In each round, every node may perform arbitrary local quantum computation and exchange quantum messages of unbounded size with its neighbors. After the last round, each node performs a quantum measurement and outputs a classical string. Thus, quantum-LOCAL is a natural quantum analogue of the classical LOCAL model of distributed algorithms3, obtained by replacing local classical computation and communication with their quantum counterparts.

In LOCAL, hence also in quantum-LOCAL, the nodes are given unique identifiers, usually of _O_(log_n_) bits. When nodes are not provided unique identifiers, the classical model is called the _port-numbering_ model, henceforth PN. Randomized PN algorithms that err with probability at most 1/poly(_n_) can sample random identifiers before the first round, hence randomized PN was heavily used to prove lower bounds in the LOCAL model (e.g., in \[BFHKLRSU16; BBHORS19\]). In this paper, our focus is the _quantum-PN_ model, i.e., the quantum-LOCAL model in which nodes are not provided unique identifiers. As the lower bound from Theorem 1 applies only to zero-error protocols, it does _not_ imply a lower bound in the quantum-LOCAL model.

In this paper, the underlying communication graph is always a _directed cycle_, hence the adjacency relations are implicit in the following definition. Each node has three registers -- left, middle, and right -- to which it can apply a local quantum transformation, and a round of communication swaps the content of the left and right registers between adjacent nodes. To specify an algorithm, it therefore suffices to give a sequence of local quantum transformations and the final measurement.

In full generality, a quantum transformation is described by a Completely Positive Trace Preserving (CPTP) map, see \[Wat18, Eq. 1.124 and 1.125\] for the definition. By Stinespring dilation (\[Wat18, Proposition 2.20\]), any CPTP map can be implemented by a unitary transformation on a larger Hilbert space. Since the local dimension in the quantum-PN model is arbitrary, this enlarged space can be embedded in the model. Thus, quantum-PN algorithms can be defined in terms of unitary transformations without loss of generality. The final measurement is formally described by a POVM as defined in Section 3.1. See Figure 1 for an illustration.

**Definition 3.1.** A _T_-round quantum-PN algorithm with output alphabet \(\Sigma\) consists of

\(\bullet\) unitary matrices _U_<sub>0</sub>_,U_<sub>1</sub>_,U_<sub>2</sub>_,...,U<sub>T</sub>_ on \(\mathbb{C}^d\otimes\mathbb{C}^d\otimes\mathbb{C}^d\) for some \(d\in\mathbb{N}\), and<tbc>

\(\bullet\) a POVM \(\Pi=(\Pi_a:a\in\Sigma)\) on the same space.

For a given integer \(n\ge 1\), a quantum-PN algorithm induces a distribution on \(\Sigma^n\) representing the joint output of the nodes. The nodes correspond to integers of \[_n_\] and if the output is \((x_1,x_2,\dots,x_n)\in\Sigma^n\), then _x<sub>p</sub>_ corresponds to the output of node _p_. The (global) output distribution is obtained by running the following process.

**Definition 3.2.** Let \(n\in\mathbb{N}_{\ge 1}\). On the _n_-cycle, each vertex \(p\in[n]\) has registers

\(\mathsf{L}(p)\otimes\mathsf{M}(p)\otimes\mathsf{R}(p)\cong\mathbb{C}^d\otimes\mathbb{C}^d\otimes\mathbb{C}^d,\)

3In the classical setting, there exist two equivalent descriptions of the LOCAL model: one based on message- passing and one based on mapping local neighborhoods to outputs (see, e.g., \[HS20, Chapter 4\]). When nodes of the network in the former description have access to qubits, no formulation akin to the latter is known.

