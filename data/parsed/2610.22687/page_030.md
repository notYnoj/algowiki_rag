## 6. Executable graph

First, define the following:

• \(S_p=[p]_{G\backslash A(p)}=\{k\in N\backslash A(p):k\sim_{G\backslash A(p)}p\}\): the cycle of a problem _p_ with all its nesting ancestors removed (i.e. what it should iterate).<tbc>

• \(O(S)=\bigcup_{k\in S}O_k\) for a set of nodes _S_: all owned variables in that set _S_, and similarly for \(I(S)=\bigcup_{k\in S}I_k\).

The driver contract is that it iterates \(U_p\rightarrow C_p\) with the additional inputs and outputs used only at the start and at the end. In other words:

• **Read** _I<sub>p</sub>_\\_C<sub>p</sub>_: driver input data such as tolerances or initial guesses.<tbc>

• **Iterate** \(U_p\rightarrow C_p\): until conditions are met.<tbc>

• **Output** _O<sub>p</sub>_\\_U<sub>p</sub>_: driver output data such as iteration history.

Additional data (e.g. inverse Jacobian approximations) is driver-internal and not in the graph.

A nested graph is executable if additionally the following checks hold:

(A.13) **No bare conditions**: all have unknowns.<tbc>

<tbc>_N<sub>P</sub>=N<sub>C</sub>_<tbc>

<tbc>(A.14) **No functional nodes have feedback**: only conditional nodes are allowed to have feedback.<tbc>

<tbc>_G_\\_N<sub>P</sub>_ is acyclic<tbc>

(A.15) **Conditions determined on the cycle**: a problem iterates something and every condition it holds is produced on that cycle.<tbc>

<tbc>\(|S_p|>1\text{and}C_p\subseteq O(S_p)\forall p\in N_P\)<tbc>

<tbc>(A.16) **One problem per level**: nodes cannot be cyclic if they answer on the same nesting level (i.e. have the same upwards nesting edge, such that \(A(q)=A(q')\)).<tbc>

<tbc>\(q\unknown_{G\backslash A(q)}q'\forall q\neq q'\in N_P\text{with}A(q)=A(q')\)<tbc>

<tbc>(A.17) **Driver data not produced or read on cycle**: the inputs of a driver (e.g. tolerance) cannot be produced on its cycle and its outputs (e.g. iteration history) cannot be read on its cycle. The driver iterates \(U_p\rightarrow C_p\) only.

\((I_p\backslash C_p)\cap O(S_p)=\emptyset\forall p\in N_P\)<br>
\((O_p\backslash U_p)\cap I(S_p)=\emptyset\forall p\in N_P\)

Furthermore, for the execution layer of `cottax`, the driver should be assigned and compatible with the problem; these are not graph checks but rather implementation.

In  IV the correspondence between the checks given in Section III and the checks given in the appendix is given. The checks that have no version in the main text of Section III are the definitions of the node kinds and the check that driver data are not produced or read on the cycle; these are assumed in the main text to be valid in all cases.

## 7. Comparison with existing graph-based framework

The graph-based formulation of MDAO problems in KADMOS \[26\] similarly has defined several checks that have to be passed in order to define an MDAO problem.

First, it has a somewhat broader and different scope: it also concerns the earlier stages before a particular selection of models is chosen, has special roles for the outer problem formulation (with specifically named objective, constraints, and design variables in the graph checks), and is in general tailored for MDAO problem specification rather than<tbc>

