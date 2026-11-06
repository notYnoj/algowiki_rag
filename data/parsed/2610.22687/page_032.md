\begin{tabular}{cc}
Pate et al. / KADMOS \[26\] & This work \\
_Data graph_ (base class of RCG, FPG, MDG) & \\
1-2 nodes are functions or variables; edges connect a variable and a function & -- (by construction: nodes are always functions or conditions: edges implied) \\
_Repository connectivity graph (RCG)_ & \\
-- (no checks beyond base data graph) & -- \\
_Fundamental problem graph (FPG)_ & \\
1-2 functions and variables are in the RCG, or instances/merges of RCG nodes & -- (no RCG) \\
3 no _collisions_ (\(\delta^-(v)\le 1\)); no _circular_ variables (cir(_v_)=0); no isolated variables & Checks (A.1) and (A.3); Check (A.2); (isolated variables not representable) \\
4 functions have outputs (\(\delta^+>0\)) & Check (A.5) \\
5 functions have a problem role & -- (follows from TOSCC) \\
6 design variables are inputs (\(\delta^-=0\)) & -- (no special role for optimiser) \\
7 quantities of interest have one producer (\(\delta^-=1\)) & Check (A.3) but we require for every node in the graph \\
8 objective and constraints are outputs (\(\delta^+=0\)) & -- only that they are read by a conditional node: Check (A.7) \\
9 every node lies on a path to a QOI, objective or constraint & -- (trimming not relevant for executability) \\
_MDAO data graph (MDG)_ & \\
1 contains all FPG nodes & -- \\
2 a single coordinator & -- (top level is _G_\\_N<sub>P</sub>_, ordered by TOSCC, multiple are fine) \\
3 every node lies on a cycle through the coordinator & -- (no single top-level) \\
4-6 architecture roles of functions (optimiser, converger, ...) and variables (initial guess, copy, final value) & -- (architecture is not enforced) \\
_MDAO process graph (MPG)_ & \\
1 nodes are the MDG functions & -- \\
2-4 starts and ends at the coordinator; every node on a cycle through it & -- (order follows from TOSCC and nesting) \\
5 a cycle with continuously increasing step numbers & -- (idem) \\
_Dynamic workflows_ \[56\] & \\
a design variable is defined at one workflow level only & Check (A.3) (unknown owned once, across nesting) \\
a subworkflow is a function node holding its own graph & similar to Checks (A.10) and (A.11) \\
subworkflow inputs (incl. initial guesses) supplied by, outputs returned to, the parent & Check (A.17) for initial guesses \\
switches activate one of several mutually exclusive branches & -- (graph fixed during execution) \\
_Not checked in KADMOS_ (checks of this work) & \\
-- (coupling allowed in the FPG; resolved by a converger with copy variables in the MDG algorithm) & Check (A.14) no functional feedback \\
_Not expressible in KADMOS_ (checks of this work) & \\
-- (variable places are not hierarchical) & Check (A.4) exact reads: a read is exactly an owned place \\
-- (no conditional nodes: drivers are function nodes with an architecture role, inserted by the architecture algorithms) & Check (A.6) conditional nodes own their unknowns \\
-- (no nesting relation: loop nesting is implicit in process step numbers) & Check (A.8) conditional nodes have unknowns or conditions Check (A.13) every condition has unknowns Check (A.15) conditions determined on the cycle Check (A.9) only problems can be nested Check (A.12) nested problems share a cycle with their outer problem Check (A.16) one problem per nesting level \\
\end{tabular}

V: Checks from earlier graph-based MDAO formulations, grouped by graph type, beside the corresponding checks of this work.

