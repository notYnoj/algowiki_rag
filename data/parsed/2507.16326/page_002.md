## II. PROBLEM CONTEXT

In Quantum Computers, one of the most critical problems to solve is that of data stability. Qbits (Quantum Bits) degenerate very rapidly \[14\] and with error rates many orders of magnitude above classical bits. In the classical world, these errors are often mitigated with some sort of ECC \[15\] (Error Correction ). In essence, more bits than necessary are used to represent the information, so that if one flips, others can be used to recover it.

In the context of quantum computing, LDPC (Low Density Parity Check) quantum codes are used. Given the high error rates inherent to current technologies, these codes often use several physical qbits to just represent a single logical qbit. When checking for errors, the information from many different parity checks is gathered in order to understand what failure might have arrived at that state. How this is done is beyond the scope of this paper, but the general workings of the algorithm are outlined below:

When _solving_ a LDPC, BP is applied first. This algorithm outputs a probability for each qbit, indicating if it experienced (or not) an error. In most cases and under low error rates, this algorithm alone can be 100% confident in which qbits failed and which did not. This information is fed back to the system to correct the errors. In some cases, BP might not be sure of what caused the failure, in which case OSD is applied after. OSD requires the output of BP to be sorted by probability, and mathematically solves the system of parity check equations that involve the most likely qbits to have failed, finding a solution that satisfies them. This information can in turn be use to recover any errors.

To understand why sorting fast is necessary, we now analyze algorithm complexity as a function of three variables involved in the calculations: _n_, which is the number of potential failure points, \(m;m\checkmark n\), which is the number of checks and _k;k\<m_ which is the number of iterations that BP performs. BP works in \(\mathcal{O}(n\cdot k)\) time, but can be fully parallelized over _n_ to work in O(_k)\<_O(_m_). OSD works in O(_m_<sup>2</sup>_n_), and can be parallelized over O(_m_<sup>2</sup>) to work in O(_n_). This would at first suggest that parallelizing BP is unnecessary, but it has been found experimentally that it is probabilistically enough to run OSD in O(_m_) by using only partial information from BP, which makes the latter’s acceleration necessary.

With this in mind, both BP and OSD are working at O(_m_), with an array sorting of \(n\gg m\) elements in between. Our target is to lower this to O(_m_) or below, to match the complexity of the OSD decoder. More specifically, it is sufficient to obtain the _m_ lowest values in O(_m_), matching the rest of the process’s complexity. Classical serial algorithms that work in \(\mathcal{O}(n\cdot log(n))\) will not be fast enough, while parallel algorithms that work in O(log(_n_)) time take resources proportional to at least \(\mathcal{O}(n\cdot log(n))\), which experimentally exceeds resource availability. Furthermore, the input to OSD is serial, so having a fully parallel output is unnecessary.

## III. DESIGN IDEA

Ideally, then, we strive for an algorithm that finds the lower _m_ values in O(_m_), with a hardware complexity of at most O(_n_). Note that, despite \(m\checkmark n\), we find that log(_n)\<m_.

Given that our input (coming from BP) is parallel and our output (going to OSD) is serial, this maps very naturally to a tree-like structure (Figure 1) where the input gets progressively reduced to a single point. Indeed, if we just had a tree of comparators with no registers in between, we would find and delete the minimum value trivially as seen in Algorithm 1.

**Algorithm 1** Unregistered comparator tree algorithm

**Input:** Values _D_<sub>1</sub>, _D_<sub>2</sub>

**Input:** Valid flags _V_<sub>1</sub>, _V_<sub>2</sub>

**Outputs:** _V<sub>out</sub>_; _D<sub>out</sub>_;

**Input:** Reset signal _R<sub>out</sub>_

**Outputs:** Reset signal _R_<sub>1</sub>_,R_<sub>2</sub>

**Ensure:** Values output in ascending order; sorting is stable.

1: \(V_{out}\leftarrow V_1\) **or** _V_<sub>2</sub>

3: **if** _V_<sub>1</sub> **and** _V_<sub>2</sub> **then** {both valid, select lowest}

4: \(D_{out}\leftarrow min(D_1,D_2)\)

5: \(R_{argmin(R_1,R_2)}\leftarrow R_{out}\)

6: **else if** _V_<sub>1</sub> **then** {only _V_<sub>1</sub> valid}

7: \(D_{out},R_1\leftarrow D_1,R_{out}\)

8: **else if** _V_<sub>2</sub> **then** {only _V_<sub>2</sub> valid}

9: \(D_{out},R_2\leftarrow D_2,R_{out}\)

10: **end if**

11: **end for**

For this to work at a rate of a value per cycle, the lowest value has to travel through the tree of comparators to the bottom, going through log(_n_) of them. Furthermore, a reset signal _R_ has to then travel up the tree to delete/disable that value, preventing it from participating in further iterations. As such, even though at first it seems we achieve constant time, the critical path for this design would scale with O(log(_n_)), so extracting _m_ elements would result in a cost of \(\mathcal{O}(log(n))\cdot m\) time wise, an increase over our target of O(_m_).

A first approach to solving this stems from the fact that a signal has to travel back and forth between the root and leaf nodes, resulting in not only long critical paths, but also excessive fan-outs. A direct, yet naive solution appears to be just segmenting the levels in the tree by placing a register after each node. This creates a structure where isolated registered comparators compare the input from two registers, placing the<tbc>

9
1
4
2
6
1
5
3
1
2
1
3
1
1
1
9
4
2
6
1
5
3
9
2
1
3
2
1
1

Fig. 1. Two steps of a naive way of sorting which does not scale well with input size. Registers are shown as light blue, and only exist for the first layer.

