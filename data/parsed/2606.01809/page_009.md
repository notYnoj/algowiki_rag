the concept of a right-most shortest path (which we define in the standard way, see for example \[25\]).

**Definition 5.4** (Right-most Shortest Path)**.** _Given a piece P, a vertex v in P, and distinct holes_ \(h,h'\in h(P)\)_, let T_<sub>_v,|h_</sub> _be the shortest path tree from v in P restricted to having the set of leaf vertices consist only of the vertices in h._

_Removing every edge and vertex of P not belonging to h or to T_<sub>_v,|h_</sub> _gives a subgraph with_ |_h_| _faces, excluding h itself. For any such face f, the_ right-most (shortest) path \(\pi_{P,T_{v,|h},f}=\{e_1,e_2,\dots,e_k\}\) _in T_<sub>_v,|h_</sub> _with respect to f is the path that is obtained by the following procedure:_

• _If v is on f, let e_<sub>0</sub> _be an artificial edge_ (_x,v_) _with head v and with tail x being an artificial vertex in the interior of f. For i_=1,2_,...,k, recursively pick the i<sup>th</sup> edge e<sub>i</sub> on_ \(\pi_{P,T_{v,|h},f}\) _as the edge in T_<sub>_v,|h_</sub> _that makes the sharpest right turn at the head of e_<sub>_i_-1</sub> _with respect to e_<sub>_i_-1</sub> _itself. The recursion stops once a leaf vertex in T_<sub>_v,|h_</sub> _is reached (see the fat path in Figure 1(a))._<tbc>

• _If v is not on f, e_<sub>1</sub> _is the unique first edge on the path of T_<sub>_v,|h_</sub> _from v to a vertex of f and the remaining edges e_<sub>2</sub>_,e_<sub>3</sub>_,...,e<sub>k</sub> of_ \(\pi_{H,T_{v,|h},f}\) _are obtained recursively as above._

**Definition 5.5.** _Let f be the face of the subgraph of P in Definition 5.4 such that f contains_ \(h'\)_. Then we define_ \(r_{v,h,h^\prime}\) _to be the last vertex on the path_ \(\pi_{P,T_{v,|h},f}\)_; see Figure 1(a)._

Finally, let us prove the main statement of this section which implies that _S<sub>b,h</sub>_ is the union of _O_(1) intervals. This, together with an additional property below, allows us to apply binary search to find the endpoints of the intervals in \(\tilde{O}(1)\) time, and then we can efficiently update D_<sub>b,h</sub>_.

**Lemma 5.6.** _Given piece P, holes_ \(h,h'\in h(P)\)_, and edge_ \(e^t=(u^t,v^t)\in P\).

_For any vertex b on_ \(h'\)_, and any two distinct vertices_ \(v_i(h),v_j(h)\in S_{b,h}\subseteq Q(h)\) _where_ \(r_{v^t,h^\prime,h}\notin(v_i(h),v_j(h))\)_. Then_ \((v_i(h),v_j(h))\subseteq S_{b,h}\).

h'
h'
f
h
h
rv,h,h'
vj(h)
vk(h) Vi(h)
v
b
u
vt
(a)
(b)

Figure 1: (a): Illustration of Definitions 5.4 and 5.5. In this example, the nine shortest paths from _v_ to _h_ induce nine faces (in addition to _h_) where _f_ is the face containing \(h'\). The indices _i_ of vertices _v<sub>i</sub>(h_) are clockwise around _h_ in this drawing. (b): The contradiction reached in the proof of Lemma 5.6. The bold paths are _T<sub>v</sub>_\[_v<sub>i</sub>(h_)\] and _T<sub>v</sub>_\[_v<sub>j</sub>(h_)\] and the dashed path is a fictitious shortest path from _b_ to _v<sub>k</sub>(h_) that does not benefit from (_u<sup>t</sup>,v<sup>t</sup>_)=_e<sup>t</sup>_.

