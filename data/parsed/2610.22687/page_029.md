<tbc>In other words, _p∼<sub>G</sub>q_ intuitively means that _p_ and _q_ are in the same strongly connected component of the graph _G_.

By definition, the graph obtained by condensing the strongly connected components (taking each component as a single node) is acyclic (if there is a cycle between them, the nodes would be in the same component instead of two) and can be topologically sorted (TOSCC in the main text).

Acyclic means that each strongly connected component has size 1.

## 4. Node kinds

Two types of nodes are defined:

\(\text{\textbf{Functional node:}}n=(I_n,O_n)n\in N_F\)<br>
\(\text{\textbf{Conditional node:}}n=(I_n,O_n,U_n,C_n)n\in N_C\)

where _U<sub>n</sub>_={_p<sub>k</sub>_} are the unknowns and _C<sub>n</sub>_={_p<sub>l</sub>_} are the variables participating in a condition. Thus, \(N=N_F\sqcup N_C\) (a node is either conditional or functional). These have the following validity checks:

(A.5) **_N_**_<sub>F</sub>_ **has outputs**:<tbc>

<tbc>\(O_n\neq\emptyset\forall n\in N_F\)<tbc>

(A.6) **_N_**_<sub>C</sub>_ **outputs contain all unknowns**:<tbc>

<tbc>\(U_n\subseteq O_n\forall n\in N_C\)<tbc>

(A.7) **_N_**_<sub>C</sub>_ **inputs contain all conditions**:<tbc>

<tbc>\(C_n\subseteq I_n\forall n\in N_C\)<tbc>

(A.8) **_N_**_<sub>C</sub>_ **cannot be both without unknowns and without conditions**:

<tbc>\(U_n\neq\emptyset\text{or}C_n\neq\emptyset\forall n\in N_C\)

A conditional node has additional inputs and outputs beyond its conditions and unknowns because a driver implementation might use those; the above checks are by construction true in the implementation.

## 5. Nested graph

A nested graph _G<sub>N</sub>_=(_G,W_) is an extension of a valid graph _G_ that adds explicit nesting edges _W_={(_p,q_)} with \(p,q\in N\); _p_ is nested within _q_.

Define the _set of problems_ of the set _N_ as \(N_P=\{n\in N_C:U_n\neq\emptyset\}\). Furthermore, the directed graph (_N<sub>P</sub>,W_) can be defined, as well as the set \(A(q)\subseteq N_P\) all problems that a problem _q_ is transitively nested in (all problems with a path from _q_ in (_N<sub>P</sub>,W_), except itself).

The following checks are then required for a valid nesting:

(A.9) **Nesting edges refer to problems**: bare conditions (without unknowns) cannot be nested.

<tbc>\(W\subseteq N_P\times N_P\)<tbc>

<tbc>(A.10) **One outer**: a problem is nested in at most one outer problem.

<tbc>\((n,m),(n,m')\in W\Longrightarrow m=m'\)<tbc>

<tbc>(A.11) **No nesting loops**: cannot nest problems within themselves.<tbc>

<tbc>(_N<sub>P</sub>,W_) is a forest<tbc>

(A.12) **Nesting ends are on a cycle**: can only nest problems that are cyclic (using each other’s outputs indirectly or directly).

<tbc>\(p\sim_{G\backslash A(q)}q\forall(p,q)\in W\)<tbc>

<tbc>The latter check is somewhat more complex: it means that in the subgraph obtained by removing all problems _q_ is nested in, the remaining inner (_p_) and outer problem (_q_) lie on the same component.

