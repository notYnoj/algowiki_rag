Evaluating QAOA expectation values can be as hard as counting optimal solutions

**Abstract**

Evaluating expectation values is a critical task for variational quantum eigensolvers, parameterized quantum circuits, and many other quantum algorithms. We consider the well-studied case of the Quantum Approximate Optimization Algorithm (QAOA) for the MaxCut problem. Recent work of Wang et al. [arXiv:2511.20212] showed this task to be NP-hard in general for any QAOA depth \(p\ge 2\), complementing past results showing efficiently computable formulas for _p_=1 with arbitrary problem graphs. We sharpen this dichotomy showing that for \(p\ge 2\) exact or exponentially precise cost expectation value evaluation is #P-hard under deterministic polynomial-time Turing reductions. Hardness at \(p\ge 2\) is shown to remain even for evaluating single pairwise correlators \(\langle Z\otimes Z\rangle\), as well as for highly restricted sets of algorithm parameters. Our proof refines the NP-hardness construction of Wang et al. that recovers the maximum cut value from the largest exponent of a QAOA Laurent polynomial, utilizing a distinct and simpler construction that extracts a value proportional to the total number of maximum cuts, in addition to the optimal cut value. Thus we show that the QAOA expectation value hardness transition from _p_=1 to _p_=2 is not only from tractability to optimization hardness, but to that of counting optimal solutions. As an application we show our results imply analogous hardness results for computing gradients and Hessians of QAOA circuits.

## 1 Introduction

Quantum computing has attracted much interest toward enabling novel approaches to NP-hard combinatorial optimization problems, in both exact and approximate optimization settings [1]. At the same time, rigorous results characterizing their power or limitations remain relatively sparse, impeding our assessment of their true utility or potential for quantum advantage here. A popular paradigm is the Quantum Approximate Optimization Algorithm (QAOA) [2,3], in particular applied to the prototypical NP-hard MaxCut problem. For analyzing quantum algorithms such as QAOA it is common to bound its expected approximation ratio in terms of the expectation value of a quantum observable encoding the cost function. This corresponds to the expected cost value of samples obtained from repeated preparation and measurement of a fixed QAOA state. For QAOA April 8, 2025 DRAFT

<sup>∗</sup>shadfield@usra.edu

Stuart Hadfield<sup>∗</sup>

Quantum Artificial Intelligence Laboratory (QuAIL), NASA Ames Research Center, Moffett Field, CA 94035, USA

USRA Research Institute for Advanced Computer Science, Mountain View, CA 94043, USA

October 5, 2026

