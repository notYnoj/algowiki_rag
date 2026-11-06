Similarly, the maximum delay limit for commodity _k<sub>L</sub>_ is \(d_L=2+\frac{1}{2W}\). Any arc (_u<sub>i</sub>,v<sub>j</sub>_) traversed by _k<sub>L</sub>_ must satisfy:

\(d_{(s,u_i)}+d_{(u_i,v_j)}+d_{(v_j,t)}\le d_L\Longrightarrow 1+d_{(u_i,v_j)}+1\le 2+\frac{1}{2W}\Longrightarrow d_{(u_i,v_j)}\le\frac{1}{2W}.\)

This stricter delay constraint imposes the tighter upper bound \(y_{(u_i,v_j)}\le w_i\) for any arc (_u<sub>i</sub>,v<sub>j</sub>_) traversed by _k<sub>L</sub>_.

By flow conservation, the total flow exiting node _u<sub>i</sub>_ equals the total flow entering that node for any \(i\in I\). Lemma 2.5 shows that the load entering _u<sub>i</sub>_ is _y_<sub>(_s,u<sub>i</sub>_)</sub>=_mw<sub>i</sub>_+(_m_-1)_W_+1, and the load exiting on arc (_u<sub>i</sub>,t_) is _y_<sub>(_u<sub>i</sub>,t_)</sub>=1. Therefore, the total load distributed across the _m_ outgoing arcs \(\{(u_i,v_j)\}_{j\in I}\) is:

\(\sum_{j\in I}y_{(u_i,v_j)}=y_{(s,u_i)}-1=mw_i+(m-1)W\)

We deduce that at least _m_-1 arcs must carry a load strictly greater than _w<sub>i</sub>_. If this were not the case, at least two arcs would carry a load of at most _w<sub>i</sub>_, and the remaining _m_-2 arcs would carry a maximum of _w<sub>i</sub>+W_. The total flow would then be bounded by 2_w<sub>i</sub>_+(_m_-2)(_w<sub>i</sub>+W_)=_mw<sub>i</sub>_+(_m_-2)_W_, which is strictly less than the flow _mw<sub>i</sub>_+(_m_-1)_W_ exiting node _u<sub>i</sub>_.

Because commodity _k<sub>L</sub>_ requires \(y_{(u_i,v_j)}\le w_i\), it can cross at most one arc (_u<sub>i</sub>,v<sub>j</sub>_) for any given \(i\in I\), meaning it can route a maximum volume of _w<sub>i</sub>_ from that object node. Given that the total demand for commodity _k<sub>L</sub>_ is \(b_L=W=\sum_{i\in I}w_i\), it must maximize its allowed flow across all object nodes \(\{u_i\}_{i\in I}\). Thus, _k<sub>L</sub>_ must use exactly one arc (_u<sub>i</sub>,v<sub>j</sub>_) per object \(i\in I\) and route exactly _w<sub>i</sub>_ units of flow across it. Consequently, the remaining _m_-1 arcs exiting each _u<sub>i</sub>_ must carry exactly _w<sub>i</sub>+W_ of commodity _k<sub>H</sub>_ and exhibit a delay of exactly \(\frac{1}{W}\).

