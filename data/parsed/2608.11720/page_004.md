<tbc>must use _T\>n/_2-1 rounds, as if not, it could be used to produce a 1-round quantum-PN algorithm in which any \(2T+2\le n-2\) consecutive nodes never all output the same value.

This work was assisted by modern AI tools: the key idea of the first part, the one-round lower bound, was discovered by OpenAI GPT 5.4, while the key idea of part (2) was discovered by us. However, we emphasize that this paper was fully written (and verified) by humans, for humans.

**The quantum-PN model (Section 3).** Since nodes are in a cycle, we identify them using integers from 1 to n understood cyclically modulo _n_. In the quantum-PN model, communications rounds are seen as swap gates in a quantum circuit, see Figure 1. Each node manipulates three local registers, local computation steps correspond to unitary matrices, and that the output colors are obtained by a final projective measurement. Using a standard Stinespring dilation, by increasing the dimension of the local registers, one can verify that this model captures the more general definition of quantum-PN in which unitary matrices can be any local quantum transformation (i.e., any CPTP map).

**The One-Round Lower Bound (Section 5).** The proof proceeds by contradiction. Assume that there exists a one-round, identical nodes quantum algorithm which breaks symmetry, i.e., such that the probability that any _n_-2 consecutive nodes output the same color is zero. First, we express the global state after the communication round as a translation-invariant Matrix Product State (MPS) [FNW92; PVWC07; CPSV21]. Two structural properties of this MPS are then derived. One follows from the symmetry-breaking requirement, while the other follows from the fact that the algorithm uses a single communication round. Finally, we show that these two properties are incompatible.

For the sake of intuition, we consider here a simplified case where the number of nodes _n_ is even, the number of colors is equal to the dimension of each local quantum state and each node produces its output by a measurement in the computation basis. Using MPS, the global state \(|\psi\rangle\) of the network after the communication round can be written as

\(|\psi\rangle=\sum_{x_1,\dots,x_n\in[c]^n}\mathrm{Tr}\left(\prod_{p=1}^nL(x_p)\right)|x_1,\dots,x_n\rangle,\)

U0 U0 U0 ROUND 1 U1 U1 U1 ROUND 2 U2 U2 U2 POVM ap-1 ap ap+1

**Figure 1.** The normal form of a 2-round quantum-PN algorithm. It interleaves local computations, in the form of unitary matrices _U_<sub>0</sub>, _U_<sub>1</sub>, and _U_<sub>2</sub> and register swaps with the left and right neighbors. The final outcome is the result of a measurement (formalized as a POVM). See Section 3 for formal definitions.

