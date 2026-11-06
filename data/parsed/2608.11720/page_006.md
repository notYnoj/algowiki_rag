<tbc>Repeating this procedure for all \(t\in[T]\) simulated rounds gives each node a list of teleportation keys. After the simulation, each node _p_ performs the final measurement prescribed by A and obtains _a(p_). The output of _p_ in B is then

\(\big(k_{1,L}(p),k_{1,R}(p),\dots,k_{T,L}(p),k_{T,R}(p),a(p)\big).\)

Now consider the output of any block of 2_T_+2 consecutive nodes. If every teleportation guess inside the block is correct, then A is simulated faithfully on its two central nodes, which receive different colors because by assumption \(a(p)\neq a(p+1)\) in A . Otherwise, some teleportation guess is incorrect. This means that at least one condition in Eq (3) fails somewhere inside the block, thus at least one pair of guessed teleportation keys differ between two nodes in that block. Since these keys are included in the output, the outputs on the block cannot all be identical. Hence, B breaks symmetry in a single communication round.

## Finitely many qubits and error probability.

Our analysis of one-round algorithms only rules out the existence of a finite-dimensional quantum algorithm, with local systems of dimension _d_<sup>3</sup>, that solves 3-coloring in _O_(1) rounds with success probability 1. Since the error probability of an algorithm can be written as a polynomial with integer coefficients and real variables, once it is known to be non-zero, results from optimization (see \[JPT13, Theorem 1.1\]) provide a lower bound on the error probability: for each fixed _d_, the success probability is upper bounded by \(1-\varepsilon(d)\), for some \(\varepsilon(d)>0\) that may go to zero as \(d\rightarrow\infty\). Because our argument for the one-round impossibility (Section 5) uses an MPS representation, where the local dimension plays a central role, it is not clear how to obtain a dimension-independent bound \(1-\varepsilon\) with \(\varepsilon>0\) independent of _d_.

Such a dimension-independent lower bound on the error probability would concern infinite- dimensional quantum strategies as defined by the _tensor-product_ model of quantum theory (see e.g. Def. 1 and Def. 1, 4 of \[LG23\]). This model extends finite-dimensional quantum theory<tbc>

