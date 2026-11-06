## 4.4.1 Tie gadget

Given a man \(m_i\in U\) who ties two women _w<sub>j</sub>_ and _w_<sub>_j_+1</sub>, we construct a tie gadget \(T_i^j\). This gadget models this tie, i.e., it allows _a<sub>i</sub>_ to be matched to _b<sub>j</sub>_ or _b_<sub>_j_+1</sub>. The idea is the following: There are two stable matchings inside the gadget, one leaving _c<sub>i,j</sub>_ unmatched while the other matches _c<sub>i,j</sub>_. The first one allows to match _m<sub>i</sub>_ to _w<sub>j</sub>_ via the 3-set {_a<sub>i</sub>,b<sub>j</sub>,c<sub>i,j</sub>_}, while the second allows to match _m<sub>i</sub>_ to _w_<sub>_j_+1</sub> via {_a<sub>i</sub>,b_<sub>_j_+1</sub>_,c_<sub>_i,j_+1</sub>} (note that in this case _c<sub>i,j</sub>_ prevents the 3-set {_a<sub>i</sub>,b<sub>j</sub>,c<sub>i,j</sub>_} from being blocking). In this case, the 3-set \(\{a_i,b_j,c'_{i,j}\}\) ensures that if {_a<sub>i</sub>,b_<sub>_j_+1</sub>_,c_<sub>_i,j_+1</sub>} is not part of the matching, then the 3-set \(\{a_i,b_j,c'_{i,j}\}\) can be blocking to represent the possibly blocking pair (_m<sub>i</sub>,w<sub>j</sub>_).

We add nine agents \(c'_{i,j}\) and \(d_{i,j}^1,\dots,d_{i,j}^8\), together with the acceptable 3-sets \(\{a_i,c'_{i,j},b_{j+1}\}\), \(\{c_{i,j},d_{i,j}^5,d_{i,j}^8\}\), \(\{d_{i,j}^1,d_{i,j}^2,d_{i,j}^8\}\), \(\{d_{i,j}^1,d_{i,j}^4,d_{i,j}^6\}\), \(\{d_{i,j}^2,d_{i,j}^3,d_{i,j}^7\}\), and \(\{d_{i,j}^3,d_{i,j}^4,d_{i,j}^5\}\). See Figure 3 for an example.

The preferences of any agent arise from the following preferences through the deletion of all 2- sets which are not acceptable for an agent. \(\{d_{i,j}^1,d_{i,j}^2\}\succ\{d_{i,j}^1,d_{i,j}^4\}\succ\{d_{i,j}^2,d_{i,j}^3\}\succ\{d_{i,j}^3,d_{i,j}^4\}\succ\{d_{i,j}^1,d_{i,j}^6\}\succ\{d_{i,j}^3,d_{i,j}^5\}\succ\{d_{i,j}^4,d_{i,j}^5\}\succ\{d_{i,j}^2,d_{i,j}^7\}\succ\{d_{i,j}^3,d_{i,j}^7\}\succ\{d_{i,j}^1,d_{i,j}^8\}\succ\{d_{i,j}^2,d_{i,j}^8\}\succ\{d_{i,j}^4,d_{i,j}^6\}\succ\{d_{i,j}^5,d_{i,j}^8\}\succ\{d_{i,j}^5,c_{i,j}\}\succ\{d_{i,j}^8,c_{i,j}\}\succ\{a_i,c_{i,j}\}\succ\{a_i,c_{i,j+1}\}\succ\{a_i,c'_{i,j}\}\succ\{b_j,c_{i,j}\}\succ\{b_{j+1},c_{i,j+1}\}\succ\{b_j,c'_{i,j}\}\), which can be derived from the following strict order of agents: \(d_{i,j}^1\succ d_{i,j}^2\succ\cdots\succ d_{i,j}^8\succ a_i\succ b_j\succ b_{j+1}\succ c_{i,j}\succ c_{i,j+1}\succ c'_{i,j}\).

The following observation shows that the tie gadget indeed models ties, i.e., it contains a stable matching which matches _a<sub>i</sub>_ to _b<sub>j</sub>_ (corresponding to matching _m<sub>i</sub>_ to _w<sub>j</sub>_) and one which matches _a<sub>i</sub>_ to _b_<sub>_j_+1</sub> (corresponding to matching _m<sub>i</sub>_ to _w_<sub>_j_+1</sub>). Furthermore, given a matching _M_ which matches _a<sub>i</sub>_ or both _w<sub>j</sub>_ and _w_<sub>_j_+1</sub> to 2-sets they prefer to every 2-set of the tie gadget, we can extend _M_ to the tie gadget without introducing a blocking 3-set.

We consider _a<sub>i</sub>_, _b<sub>j</sub>_, and _b_<sub>_j_+1</sub> to be part of the tie gadget \(T_i^j\). Note that _a<sub>i</sub>_, _b<sub>j</sub>_, and _b_<sub>_j_+1</sub> may also be part of other tie gadgets. For a set _X_ of agents, we denote by \(T_i^j-X\) the instance arising from \(T_i^j\) through the deletion of all agents from _X_ as well as every 2-sets containing an agent from _X_ which appears in the preferences of some agent.

**Observation 4.28.** _Let_ \(T_i^j\) _be a tie gadget. The matchings_ \(M_1=\{\{a_i,c_{i,j+1},b_{j+1}\},\{c_{i,j},d_{i,j}^5,d_{i,j}^8\},\{d_{i,j}^2,d_{i,j}^3,d_{i,j}^7\},\{d_{i,j}^1,d_{i,j}^4,d_{i,j}^6\}\}\) _and_ \(M_2=\{\{a_i,c_{i,j},b_j\},\{d_{i,j}^1,d_{i,j}^2,d_{i,j}^8\},\{d_{i,j}^3,d_{i,j}^4,d_{i,j}^5\}\}\) _are sta ble. In_ \(T_i^j-\{a_i\}\) _or_ \(T_i^j-\{b_j,b_{j+1}\}\)_, also the matching_ \(M=\{\{c_{i,j},d_{i,j}^5,d_{i,j}^8\},\{d_{i,j}^2,d_{i,j}^3,d_{i,j}^7\},\{d_{i,j}^1,d_{i,j}^4,d_{i,j}^6\}\}\) _is stable._

bj+1
Ci,j+1
d6 i,j
d7 i,j
d5 i,j
d4 i,j
d3 i,j
ai
d8 i,j
d2 i,j
d1 i,j
Ci,j
bj

Figure 3: The acceptable 3-sets of a tie gadget \(T_i^j\). For example, the line around _a<sub>i</sub>_, _c_<sub>_i,j_+1</sub>, and _b_<sub>_j_+1</sub> indicates that the 3-set {_a<sub>i</sub>,c_<sub>_i,j_+1</sub>_,b_<sub>_j_+1</sub>} is acceptable.

