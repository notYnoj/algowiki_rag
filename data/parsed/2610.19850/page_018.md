<tbc>with the sets to be enumerated. Internal nodes of the binary tree represent a _partial solution_, in other words, a subset of a solution to be enumerated. For each internal node at depth _i_, we check whether it is possible to _extend_ the current partial solution with element _e<sub>i</sub>_. We potentially create two branches below: one leading to a node representing the partial solution extended with _e<sub>i</sub>_, the other leading to the same partial solution without _e<sub>i</sub>_. We stop extending a branch when no solution hides beneath. At each depth, to prune the tree, the _extension version_ of the enumeration problem needs to be answered. Below is the extension version of PMC enumeration.

PMC Extension<br>
**Input:** A graph _G_=(_V,E_), a subset \(M\subseteq V\) of _mandatory_ vertices, a subset \(F\subseteq V\) of _forbidden_ vertices such that \(M\cap F=\emptyset\).<br>
**Question:** Is there, a set \(\Omega\) of vertices with \(M\subseteq\Omega\), \(\Omega\cap F=\emptyset\) and such that \(\Omega\) is a PMC?

Let us focus now on the possible application of Flashlight Search for PMC enumeration. The root of the tree is labeled \(\emptyset\). Consider any ordering _v_<sub>1</sub>_,...,v<sub>n</sub>_ of _V(G_). Given a node of the tree, if the answer of the extension problem considering the add-on of _v<sub>i</sub>_ (or resp. its exclusion) into the current mandatory (resp. forbidden) set is yes, then one can see that there will be at least one PMC satisfying our current restriction (_M,F_), and it is worth continuing the exploration. It follows that if the answer is no, then there is no PMC below, and we can cut the branch.

Figure 4 provides an example of exploration using Flashlight Search, considering the very simple input graph: path (_v_<sub>2</sub>_,v_<sub>1</sub>_,v_<sub>3</sub>). Starting from the root of the binary tree, we ask the extension problem whether there is a PMC including _v_<sub>1</sub> (_M_={_v_<sub>1</sub>} and \(F=\emptyset\)). If the answer is yes, we create a branch labeled _v_<sub>1</sub>. We do the same for the exclusion of _v_<sub>1</sub>. Deeper in the tree, at a depth _i_, we may arrive in a situation where we can still add a vertex _v<sub>i</sub>_ to the mandatory (resp. forbidden) set, but the extension problem answers no. In this case, there will be no PMC containing (resp. excluding) _v<sub>i</sub>_, and the branch is given up. This occurs on the right child of the root as there is no PMC excluding _v_<sub>1</sub> in our input graph.

Flashlight Search is very effective when there exists a polynomial time algorithm solving the extension problem. Then, a polynomial-delay polynomial-space algorithm for the enu<tbc>

0
v1
v1
X
No solution without {v1}
v2
v2
v3
v3
v3
No solution with {v1, v2, v3}
v1, v2
v1, v3
with {v1} without {v2, v3}

Figure 4: Example of a Flashlight Search applied to _v_<sub>2</sub>-_v_<sub>1</sub>-_v_<sub>3</sub> to enumerate its two PMCs.

