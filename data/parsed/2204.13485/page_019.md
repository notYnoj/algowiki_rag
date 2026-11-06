• the preference lists of agents \(a_i(1\le i\le 3n)\) and \(s_j(1\le j\le 2n)\) are not fixed,<tbc>

• if _C<sub>j</sub>_=(_a_<sub>_j_<sub>1</sub></sub>_,a_<sub>_j_<sub>2</sub></sub>_,a_<sub>_j_<sub>3</sub></sub>) is the _j_-th set in _I_, then:<tbc>

\(x_j:[S]>c_j^1>c_j^2>c_j^3>d_j^1>\dots\)<br>
\(c_j^1:a_{j_1}>x_j>c_j^2>d_j^1>c_j^3>\dots\)<br>
\(c_j^2:a_{j_2}>x_j>c_j^3>c_j^1>\dots\)<br>
\(c_j^3:a_{j_3}>x_j>c_j^1>c_j^2>\dots\)

where \[_S_\] denotes \(s_1>\cdots>s_{2n}\) and ‘_\>\dots_’ means that the rest of the agents are ranked in an arbitrary order.

We claim that there is an exact 3-cover in _I_ if and only if the preferences of the remaining agents can be set in a way such that there is a stable matching _M_ in _G_. Suppose there is an exact 3-cover \(\mathcal{C}'\subseteq\mathcal{C}\). Then, we make construct a matching _M_ as follows. We match the agents in _S_={_s_<sub>1</sub>_,...,s_<sub>2_n_</sub>} to the agents _x<sub>j</sub>_ that correspond to the 3-sets not in \(\mathcal{C}'\). In the gadgets for these sets, we add the edges \(c_j^2c_j^3,d_j^2d_j^3\) and \(c_j^1d_j^1\) to the matching. In the gadgets of the sets in \(\mathcal{C}'\), we add the edges \(a_{j_1}c_j^1\), \(a_{j_2}c_j^2\), \(a_{j_3}c_j^3\), \(xd_j^1\), and \(d_j^2d_j^3\) to the matching. Finally, we set the preferences of the _a<sub>i</sub>_s and _s<sub>j</sub>_s such that each prefers its partner in _M_ the most.

Suppose there is a blocking edge _uv_. It is clear that both _u_ and _v_ must be from the same set gadget, since each _a<sub>i</sub>_ and _s<sub>j</sub>_ is with their best partner, everyone is matched, and each agent in a set gadget prefers everyone in their gadget to anyone from another gadget. If _u_ and _v_ are in a gadget for a set \(C_j\in\mathcal{C}'\), then each \(c_j^i\) and \(d_j^1\) is with their best partner, so they cannot block. Moreover, _x<sub>j</sub>_ is with the best partner from the gadget that is not a \(c_j^i\). Therefore, only \(d_j^2d_j^3\) could block, but it is in _M_. If _u_ and _v_ are in a gadget for a set \(C_j\notin\mathcal{C}'\), then _x<sub>j</sub>_ is matched with its best partner, so it cannot block with anyone. It is straightforward to check that the edges \(c_j^1c_j^2\), \(c_j^3c_j^1\), \(d_j^1d_j^2\), and \(d_j^3d_j^1\) are all dominated, so no edge can block.

Now suppose that there are preferences for the elements and selectors such that there exists a stable matching _M_ in _G_. We can assume that the elements and selector agents like their partner the most if there exists one. If a gadget for a set _C<sub>j</sub>_ would get no selector and no element agent from outside, then \(c_j^1\) and _x<sub>j</sub>_ must be matched together. However, then there is no stable matching among the vertices \(d_j^1\), \(d_j^2\) and \(d_j^3\). If the gadget for _C<sub>j</sub>_ gets a selector, then we may assume that it is matched with _x<sub>j</sub>_. In this case, there is a stable matching inside the gadget consisting of the edges \(c_j^2c_j^3\), \(c_j^1d_j^1\), and \(d_j^2d_j^3\). If the gadget for _C<sub>j</sub>_ gets no selector, then it must get all three of the corresponding element agents, as otherwise neither _x<sub>j</sub>_ nor \(c_j^1\) is matched to \(d_j^1\), implying that there is no stable matching among the vertices \(d_j^1\), \(d_j^2\) and \(,d_j^3\). Indeed, if only one or two element agents would get matched, then the preferences of _x<sub>j</sub>_ imply that it must be matched to a remaining \(c_j^i\) since the remaining \(c_j^i\) prefers _x<sub>j</sub>_ the most, and _x<sub>j</sub>_<tbc>

d2 j
aj1
d1
d3
dj
Xj
S1
aj2
C1 j
C3 j
S2n
aj3
C2

Figure 5: Gadget corresponding to set _C<sub>j</sub>_={_a_<sub>_j_<sub>1</sub></sub>_,a_<sub>_j_<sub>2</sub></sub>_,a_<sub>_j_<sub>3</sub></sub>} in Theorem 26 with the first few edges on the preference lists of the vertices.

