<tbc>in Figure 1 for _m_=3, where distinct 4-tuples are colored in red, green, and blue, respectively. The crucial property of the gadget is that if we wish to take 4 edge-disjoint shortest cycles from _F_, then because of the overlap of the shortest cycles, the only option is to choose cycles of the same color. This choice corresponds to the selection of an edge in the instance of Multicolored Clique between two color classes.

The construction of the vertex selection gadget _H_ exploits the same idea. We assume that each color class contains _n_ vertices. Then _H_ is composed of _n_ pairs of cycles of length _L_. We use Figure 2 to explain the construction for _n_=3; the 3 pairs of cycles are shown in red, green, and blue. For the vertex selection gadget, the crucial property is that if we are required to take 2 shortest cycles from _H_, then the only possibility is to select cycles of the same color. The choice naturally corresponds to a selection of a vertex in the color class of the instance of Multicolored Clique.

We use the paths _Q<sub>s</sub>_ in the vertex selection gadget (see Figure 2) constructed for a color class _V<sub>i</sub>_ and roots of the edge selection gadgets (see Figure 1) constructed for the pairs _V<sub>i</sub>,V<sub>j</sub>_ for \(j\neq i\). Namely, we identify edges of _Q<sub>s</sub>_ corresponding to \(v\in V_i\) without common endpoints with the roots<tbc>

root
root
l
L - 5
L - 5
root
root
l
root
root

Q1
Q2
Q3
l

Figure 1: Construction of the edge selection gadget _F_ for _m_=3. The paths in the left and in the right parts are of length _L_-5, and the paths in the middle part are of length \(\ell=L/2\). The middle vertices of the paths in the left and in the right parts are _roots_ that are used to connect the edge selection gadget with the corresponding vertex selection gadgets. For _F_ constructed for the pair of color classes _V<sub>i</sub>,V<sub>j</sub>_ with _i\<j_, the roots from the left part are used to connect the edge selection gadget with the vertex selection gadget constructed for _V<sub>i</sub>_, and the roots from the right part are used for the connection with the vertex selection gadget constructed for _V<sub>j</sub>_.

Figure 2: Construction of the vertex selection gadget for _n_=3. The paths in the middle part are of length \(\ell=L/2\). The paths _Q_<sub>1</sub>_,Q_<sub>2</sub>_,Q_<sub>3</sub> correspond to the vertices of a color class and are used to connect the vertex selection gadget with the edge selection gadgets.

