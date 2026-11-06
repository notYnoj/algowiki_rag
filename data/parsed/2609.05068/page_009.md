• **Object vertices:** a first layer of _n_ vertices \(\{u_i\}_{i\in I}\), where each vertex corresponds to an object in the 3-Partition instance.<tbc>

• **Triplet vertices:** a second layer of _m=n/_3 vertices \(\{v_j\}_{j\in J}\), where each vertex corresponds to a target triplet \(j\in J\).<tbc>

• **Chains of vertices:** for each \(j\in J\), a sequence of vertices \(\{v_j^l\}_{l\in\{1,\dots,N\}}\). We will prove that the subpath traversing these vertices is accessible to exactly one commodity, which will force its routing and flow.

The set of arcs _A_ contains the following elements (colors refer to Figure 1):

• **Source-objects arcs (purple):** \(\forall i\in I\), an arc (_s,u<sub>i</sub>_) with capacity _c_<sub>(_s,u<sub>i</sub>_)</sub>=_mw<sub>i</sub>_+(_m_-1)_W_+2.<tbc>

• **Partition arcs (blue):** \(\forall i\in I\), \(j\in J\), an arc (_u<sub>i</sub>,v<sub>j</sub>_) with capacity _c_<sub>(_u<sub>i</sub>,v<sub>j</sub>_)</sub>=_w<sub>i</sub>_+2_W_.<tbc>

• **Triplet completion arcs (red):** \(\forall j\in J\), an arc (_v<sub>j</sub>,t_) with capacity \(c_{(v_j,t)}=\frac{W}{m}+2\).<tbc>

• **Chain arcs (red):** \(\forall j\in J\), an entry arc \((v_j,v_j^1)\) and internal arcs \((v_j^l,v_j^{l+1})\) for \(l\in\{1,\dots,N-1\}\), each with capacity \(W\frac{(n+1)(n-3)}{n}+1\). An exit arc \((v_j^N,t)\) is added with capacity \(W\frac{(n+1)(n-3)}{n}+2\).<tbc>

u1
Wi + 2W
mwi + (m - 1)W + 2
Wi + 2W
v1
W(n + 1)(n - 3)
+ 1
n
wi + 2W
w + 2
v1
w + 2
m
n -1
vj
w + 2
W(n + 1)(n - 3)
S
ui
m
n
vj
v1
v1
n
2
n -1
vn
t
2
w + 1
w + 2W
w + 2
m
mwn + (m - 1)W + 2
w + 2W
w + 2W
vm
un

Figure 1: Instance of the DCMCF problem associated with the 3-Partition problem of a set \(\{w_i\}_{i\in I}\). Only selected arcs, vertices, and capacities are shown. All dashed arcs have a capacity of 2.

