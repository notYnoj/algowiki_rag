<tbc>_Proof._ We denote by _P<sub>i</sub>_ and _Q<sub>i</sub>_ the paths _s<sub>i</sub>x<sub>i</sub>y<sub>i</sub>t<sub>i</sub>_ and _s<sub>i</sub>w<sub>i</sub>z<sub>i</sub>t<sub>i</sub>_ respectively. We denote by _f<sub>i</sub>(e_) the flow value on edge _e_ induced by the flow paths for _s<sub>i</sub>t<sub>i</sub>_.

From Theorem C.2, for each of the demands \(\{s_i,t_i\}(i\in\{1,2,3\})\), either _f<sub>i</sub>(s<sub>i</sub>x<sub>i</sub>_)=1 (_s<sub>i</sub>_ is routed up) or _f<sub>i</sub>(s<sub>i</sub>w<sub>i</sub>_)=1 (_s<sub>i</sub>_ is routed down). Similarly each _t<sub>i</sub>_ is routed down or up. We say that _s<sub>i</sub>t<sub>i</sub>_ is _coherent_ if _s<sub>i</sub>_ and _t<sub>i</sub>_ are routed in the same direction. Observe that if a support path for an external demand enters the gadget, it cannot use any edges incident with _s<sub>i</sub>_ or _t<sub>i</sub>_ for _i_=1,2,3. Hence our goal is to that at least one of _P<sub>xy</sub>_ or _Q<sub>xy</sub>_ is not part of any support path for any external demand.

For any \(r\in\{1,2,3\}\), if _s<sub>r</sub>t<sub>r</sub>_ is coherent (routing up, say), then any support _s<sub>r</sub>t<sub>r</sub>_-path is either exactly _P<sub>r</sub>_ or it starts with _s<sub>r</sub>x<sub>r</sub>y_<sub>_r_-1</sub>_...y_<sub>0</sub> and ends with _x_<sub>4</sub>_y_<sub>3</sub>_...y<sub>r</sub>t<sub>r</sub>_. In the latter case we say the path _escapes_. If any coherent _s<sub>r</sub>t<sub>r</sub>_ does not have any escaping support paths (i.e., it routes entirely on _P<sub>r</sub>_), then it is impossible for any external demand to route using _P<sub>xy</sub>_ if _s<sub>r</sub>t<sub>r</sub>_ routes up, and impossible to use _P<sub>wz</sub>_ if _s<sub>r</sub>t<sub>r</sub>_ routes down. In these cases, the lemma holds with _Q=P<sub>wz</sub>_ in the former case and _Q=P<sub>xy</sub>_ in the latter. So we may assume each coherent _s<sub>r</sub>t<sub>r</sub>_ has an escaping support path.

For any incoherent pair, all the support paths leave and re-enter the gadget, and therefore use up 2 units of capacity on the cut {_y_<sub>0</sub>_x_<sub>1</sub>_,z_<sub>0</sub>_w_<sub>1</sub>_,y_<sub>3</sub>_x_<sub>4</sub>_,z_<sub>3</sub>_w_<sub>4</sub>}. Hence if there are 2 incoherent pairs, then no external demand may cross through the gadget, in which case the lemma holds. We may thus assume that there are _i\<j_ such that _s<sub>i</sub>t<sub>i</sub>_ and _s<sub>j</sub>t<sub>j</sub>_ are coherent. Let \(k\in\{1,2,3\}\backslash\{i,j\}\).

**Case 1:** Suppose both _s<sub>i</sub>t<sub>i</sub>_ and _s<sub>j</sub>t<sub>j</sub>_ are routed in the same direction, say up. Since both _s<sub>i</sub>t<sub>i</sub>_ and _s<sub>j</sub>t<sub>j</sub>_ have a support path that escapes, these paths cross, a contradiction.

**Case 2:** The remaining case is when both _s<sub>i</sub>t<sub>i</sub>_ and _s<sub>j</sub>t<sub>j</sub>_ are routed in distinct directions, and _s<sub>k</sub>t<sub>k</sub>_ is not coherent (otherwise it would be in the same direction as _s<sub>i</sub>t<sub>i</sub>_ or _s<sub>j</sub>t<sub>j</sub>_ and the previous case applies). Without loss of generality, we may assume that _s<sub>i</sub>t<sub>i</sub>_ is routed up and _i\<k_. To avoid crossing the escaping path for _s<sub>i</sub>t<sub>i</sub>_ at _y<sub>i</sub>_, every support path for _s<sub>k</sub>t<sub>k</sub>_ must use _y_<sub>3</sub>_x_<sub>4</sub>. However, this does not leave enough capacity for the escaping path for _s<sub>i</sub>t<sub>i</sub>_ that also uses this edge, a contradiction.

By routing each demand up, or each demand down, one of the two paths _P<sub>xy</sub>_, _P<sub>wz</sub>_ is free to be used by support paths from external demands.

Thus, the gadget from Figure 12 can be used to replace two edges \(e'\) and \(e''\), with the effect of forbidding the use of both edges in the fractional uncrossed flow: it adds the constraint that either \(x(e')=0\) or \(x(e'')=0\).

**Lemma C.4** (Clause Gadget, Figure 13)**.** _The clause gadget (Figure 13) has a solution even if we remove two of the three edges_ \(e',e'',e'''\)_. It has no solution if we remove all three edges_ \(e',e'',e'''\).

_Proof._ It easily follows from Theorem C.3 by a simple case analysis, as only one of the two edges crossed by the double blue line can be used in routing the demand edge.

## C.3 Hardness of Finding Uncrossed Fractional Flows

**Theorem C.5.** _The problem Fractional Uncrossed Flow is NP-complete._

X1
y1
X2
y2
X3
y3
yo
X4
yo
X4
S1
S2
S3
t1
t2
t3
zo
W1
Z1
W2
Z2
W3
Z3
W4
ZO
W4

Figure 12: Coupled Arcs Gadget. A gadget that forbids the use of one arc among two, for any flow path from terminal outside the gadget. Recall that the circle refers to the schematic of the Terminal Gadget from Figure 11. On the right, a schematic representation of the Coupled Arcs Gadget.

