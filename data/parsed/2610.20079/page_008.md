one. Let there be _W_ independent messages, and let _S_ be the sum of all edge lengths. The circuit and labels in Section 5 satisfy

\(S<Wm.\) (4)

The matrix differences along any source-sink path sum to the full-rank difference between the sink and source matrices. Subadditivity of rank therefore makes every such path at least _m_ long, including paths that run against the circuit’s time direction. Routing all messages at common rate _r_ requires total length at least _rWm_, while the edge capacities supply only _S_. Hence \(r\le S/(Wm)<1\).

By contrast, pipeline repeated circuit executions so that each edge transmits at most one bit per round. For a fixed startup delay _D_, each source can deliver _k_ bits in at most _k+D_ rounds. The coding rate _k/(k+D_) approaches one and thus eventually exceeds the strictly smaller routing upper bound.

## Where the strict saving comes from.

The local circuit has _v_=111 pairs of data registers and _R_=439 auxiliary registers. Each register holds one bit and is also assigned a subspace of Q<sup>8</sup> for the analysis. A subspace label is not the register’s stored value. Labels on registers present throughout the computation only grow by inclusion. Nine temporary copies require their labels to shrink; the sum of the dimensions lost in these changes is _c_=63.

Section 5.1 combines copies of this circuit in three coordinate directions, giving labels in dimension _m_=8<sup>3</sup>=512. Three copies of the data registers share auxiliary registers, whose values are restored before reuse. Each data pair contributes 2_m_-2 to the total edge length, two less than the full endpoint requirement 2_m_. The auxiliary registers contribute _m_ each; temporary copies add the extra cost counted by _c_. The resulting totals are<tbc>

\(W=3v^2(2v+R),S=Wm-3v^2(2v-3c)<Wm.\)

Execution order
(a) Three registers, six gates
91
92
93
94
95
96
A
x
y
y
y
y
y
x
B
y
+
+
x
C
z
z
Z
Z
Gate node, wire segment edge
(b) The corresponding undirected network
Sx
O ty
91
92
93
94
95
96
Sz
O tx
Sy
O tz

Figure 2: A three-register example and its network. Colors distinguish register wires. Node _g<sub>j</sub>_ below represents gate _j_ above; an edge represents a wire segment between consecutive gates or endpoints.

