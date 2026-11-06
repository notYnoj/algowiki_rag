<tbc>that sink _t<sub>i</sub>_ must recover. The source messages are mutually independent, and the rate vector is **r**=(_r_<sub>1</sub>_,...,r<sub>W</sub>_).

Under _fractional routing_, each session may use several source-sink paths. Assign nonnegative flow to the paths of session _i_ so that their sum is _r<sub>i</sub>_. For every edge, the total flow on all paths using it must not exceed its capacity; this sum includes both directions and all sessions.

_Network coding_ allows nodes to transmit functions of their source messages and previously received information. Each sink must recover its required message for every source input, giving a zero-error requirement. For fixed network, capacities, and source-sink pairs, the simultaneously achievable rate vectors and their limits form the corresponding _capacity region_. The multiple- unicast conjecture asserts that the coding and fractional routing capacity regions coincide. A rate vector achievable by coding but not by routing therefore refutes it.

All edges in our counterexample have unit capacity. We use a finite-round binary linear protocol: every transmitted bit is an exclusive-or (XOR), or sum modulo two, of bits already available at the transmitting node, and transmission times and directions are fixed in advance. In each round, each edge carries at most one bit in one direction, computed only from initial messages or information received in earlier rounds. Local computation and storage are unrestricted. If a protocol delivers _k_ bits from each source to its sink in _T_ rounds, its _common rate_ is _k/T_. Let _R_route be the maximum common rate under fractional routing, and let _R_code be the supremum of common rates achievable by these binary linear protocols.

The finite construction used in this paper also yields the following communication result.

**Theorem 3.2** (A strict coding advantage in undirected networks)**.** There is a finite undirected network with unit edge capacities and independent source messages such that

\(R_\text{route}\le 1-\frac{33}{338432}<1=R_\text{code}.\) (3)

A finite binary linear block code achieves a common rate strictly above this routing upper bound. The network can also be chosen to be a simple graph, with no loops or parallel edges.

## 4 Proof Overview

The central idea is to use a coding circuit for data rearrangement. The same circuit can deliver independent messages to their destinations and break a large array-movement task into subtasks that each handle less data. We first explain the movement needed for sorting, then show why a coding counterexample provides an implementation using fewer block transfers.

### 4.1 Rearrangement in sorting

Arrange the input integers in a table, storing each column contiguously on disk. Sorting every column does not necessarily remove inversions between columns. Classical Columnsort alternates sorting columns with prescribed rearrangements that redistribute the data among new columns. These movements bring integers from different original columns together for comparison. Executing the column sorts and movements in the prescribed order produces a sorted sequence.

A _rearrangement_ moves data from their original positions to other positions while preserving every value. Figure 1 illustrates a row-column interchange: each destination is determined by the original row and column indices, independently of the data values. The new columns contain<tbc>

