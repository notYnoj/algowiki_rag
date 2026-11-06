<tbc>which ordering is meant.

This is in the form of a _nesting edge_ added to the dependency graph between two conditional nodes. It states the first node is nested within the second, with the first conditional node being fully satisfied for each iteration of the second. For a valid dependency graph with nesting edges, it has to additionally satisfy:

**Check G3 (No nesting loops)** _No conditional node is nested within itself, not even through other conditional nodes (no_ \(A\rightarrow B\rightarrow A\)_)._

and for that graph to be executable, it has to hold that:

**Check E4 (Valid nesting)** _Every component with multiple conditional nodes has exactly one outermost conditional node, the same holding within that component’s subgraph after removing the outermost conditional node. Nesting edges also only connect conditional nodes sharing a component, as nesting is meaningless otherwise._

In Figure 7 the three options for making Figure 6(b) executable are shown: either the fixed point is Nested within the optimiser, or vice versa, or the two conditional nodes are Combined together, adding their conditions. This may change the combined node’s condition type: here, the fixed point becomes a constraint on the optimiser. (a) and (c) will yield the same solution set while (b) will in general not.

In nested figures, the ordering is still from top-left to bottom-right. If an iterated component (indicated by a solid line outline) is encountered, that is first fully converged before moving on. As an example, in Figure 7(a), the purple box indicates it will be iterated. The top-left node is the optimiser, then comes the green solid box: the fixed-point node is top-left within that, so it is first converged fully (by iterating _N_<sub>3</sub> and _N_<sub>4</sub>) before moving to the next node _N_<sub>1</sub> and then _N_<sub>2</sub>.

X
X
X
X
FP
y2
y1
y1
y2
N4
y2
N1
f
N2
g
g
min g
0
(a)
(b)

Opt
X
X
X
min
0
FP
y2
y1
y1
y2
N4
y2
f
N1
g
N2

FP
y2
y2
min
0
0
y2
y1
y1
y1
y2
N4
y2
f
N1
g
N2

Opt
X
X
X
X
X
X
X
N3
y1
y1
y1
y1
y2
N4
y2
f
N1
g
N2

Figure 6: The Sellar problem in Figure 4(c), with an added optimality condition (a), which then determines the design variable _x_, resulting in one strongly connected component with two conditional node types (b).

(a) NEST(FP in Opt)

(b) NEST(Opt in FP)

(c) Combine(Opt, FP)

Figure 7: Three ways to make Figure 6(b) executable: in (a) the fixed-point conditional node is nested such that the optimiser executes it in each iteration, in (b) the fixed point is outer and executes the optimiser per iteration, and in (c) the two conditional nodes are combined. (a) and (c) have the same solution sets; (b) a different one.

