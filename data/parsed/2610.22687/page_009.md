<tbc>First, a copy of _y_<sub>2</sub> (\(\hat{y}_2\)) is made (only read by the function in the cycle that reads it, _N_<sub>3</sub>) and a conditional node in the graph is inserted that requires these to be equal (together, a Cut). This does not change the solution of the graph -- replacing \(\hat{y}_2\rightarrow y_2\) yields the original graph again. Checks E1 and E3 require it to be given unknowns and a driver to make the graph executable. The Determine operation sets the unknowns of the conditional node to \(\hat{y}_2\). The Assign operation then assigns the Picard iteration to the conditional node.

The graph of Figure 4(d) satisfies checks E1 to E3: the Picard iteration node has unknowns, it is the only node receiving feedback (under the diagonal, in contrast to Figure 3c where the functional node _N_<sub>3</sub> receives feedback), and it has been assigned a driver.

The assigned driver may also use external inputs that are not part of its conditions such as an initial guess \(\hat{y}_2^{(0)}\) or a tolerance \(\epsilon\), and output other quantities such as iteration history. These remain part of the dependency graph and can be wired to other functions: an initial guess may come from a low-fidelity variant and its tolerance may be scaled by the other inputs. However, they cannot be part of what a driver iterates: otherwise they _are_ just conditions or unknowns since a driver by definition iterates only those.

Conditional nodes are general: for example, in Figure 5 three condition types are shown in the graph before and after determining. The minimum set of models that they have to iterate immediately follows from the TOSCC. Optimisation, fixed point, and root find are, from the graph’s perspective, all a condition determining a variable (the colouring is for visualisation purposes only) and the executability checks hold in the same way whatever the type of conditions are in the graph. Furthermore, the noted graph operations in Figure 4 apply to all of them (but the type of conditional node determines which drivers can be assigned to it), as well as the nesting and combining of such nodes discussed in the next section.

## C. Nesting and combining

Multiple conditional nodes can be present in the same strongly connected component: for example, adding an optimality condition determining _x_ to the Sellar problem of Figure 4 yields one component containing both the fixed-point node and the optimiser node, as shown in Figure 6.

The TOSCC defines no order within an SCC and as such the graph itself does not define whether the optimiser iterates the fixed-point node or vice versa (in Figure 6 by convention the optimiser is outer, Figure 7(a) and (b) show the two options). This in general leads to different solution sets and as such we have to force an explicit decision on<tbc>

J
x
S
u
M1
a
g
M2
u
r
M3
f
r = 0
0
Determine s
J
x
S
u
M1
a
g
RF
S
r
M2
u
M3
f
O

J
x
S
u
M1
a
g
M2
u
r
M3
f
u = u
0
Determine u
J
x
S
u
M1
a
g
M1
a
g
M2
u
r
M3
f
O

J
x
S
u
M1
a
g
M2
u
r
M3
f
min g < 0
0
Determine x
J
x
S
u
M1
a
g
M2
u
r
M3
f
O

(a)

(b)

(c)

Figure 5: Three different types of conditions each determining a different variable in the same dependency graph: (a) a root find, (b) a fixed point, and (c) an optimisation. The size of the induced cycle depends on the determined variable.

