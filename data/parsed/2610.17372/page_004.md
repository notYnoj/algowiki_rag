<tbc>snapshot interval so that a bit will be set to 1 if the connectivity between _p_ and _q_ was there during the corresponding time interval, and set to 0, otherwise.

Note that in each snapshot interval, if \(\tau\) is greater or equal to a certain value, then only we consider the connection set the value 1. For example, considering the Example 1, if \(\tau\ge 1\), then we set the bit value 1 other 0.

This connectivity string from _p_ to _q_ during the time window \[0_,T_\] will be denoted by _CS<sub>pq</sub>_\[0_,T_\] or simply _CS<sub>pq</sub>_ when the time window \[0_,T_\] is implied from the context. We assume that every edge of the temporal graph is symmetric (undirected) and hence, _CS<sub>pq</sub>_\[0_,T_\]=_CS<sub>qp</sub>_\[0_,T_\].

**Example 2.** _Referring to the timing diagram for connection as given in Fig. 1 with M_=10_, the connectivity between the vertices p and q is expressed by the 10-bit binary string 1110110110 (the most significant bit corresponds to the snapshot interval_ \([0,\tau]\)_)._

### 3.2 Assumptions

\(\bullet\) We assume that a finite amount of time is needed to traverse every edge in the path, and the snapshot interval \(\tau\) is so small that this time to traverse an edge is always more than \(\tau\). Without loss of generality, we assume for simplicity that this time to traverse an edge can be expressed as some non-zero integral multiple of \(\tau\).

\(\bullet\) During the whole time window \[0_,T_\], the distance _d<sub>pq</sub>_ from _p_ to _q_, as well as the time _t<sub>pq</sub>_ to traverse the edge _e<sub>pq</sub>_ from _p_ to _q_ (when it exists throughout the period _t<sub>pq</sub>_) will be assumed to be constant. Given these information, it may be noted that when we start traversing the edge _e<sub>pq</sub>_ at any time during the interval _I=j_, i.e., during \([j\tau,(j+1)\tau]\), this connecting edge _e<sub>pq</sub>_ must exist continuously during the interval \([j\tau,(j+t_{pq})\tau]\) for the completion of the traversal.

\(\bullet\) A temporal graph will be represented by an \(n\times n\) adjacency matrix _A_ whose (_p,q)<sup>th</sup>_ entry will be a 3- tuple given as _A(p,q_)=(_CS<sub>pq</sub>,d<sub>pq</sub>,t<sub>pq</sub>_).

## 4 METHODOLOGY

Consider a temporal path \(p_1p_2\cdots p_m\) from a vertex _p_<sub>1</sub> to another vertex _p<sub>m</sub>_ that exists in the temporal graph _G_=(_V,E<sub>t</sub>_) during the time window _W_=\[0_,T_\] under consideration. After reaching a vertex \(p_j,j=2,3,\cdots,m-1\) along the path from the vertex _p_<sub>_j_-1</sub>, a connection from _p<sub>j</sub>_ to _p_<sub>_j_+1</sub> following the trail should be continuously available (without any break) in any subsequent _t_<sub>_p<sub>j</sub>p_<sub>_j_+1</sub></sub> snapshot intervals. To satisfy this requirement, one may have to wait at the vertex _p<sub>j</sub>_ for some time until the required connectivity to the vertex _p_<sub>_j_+1</sub> is guaranteed. We illustrate this situation by the following example.

**Example 3.** _Consider a temporal graph with five vertices for which the vertex set is V_={1,2,3,4,5}_. The connecting edges are time-varying in nature with the aggregated static graph as shown in Fig. 2 during an observation window_ \([0,10\tau]\)_. The time varying nature of the connecting edges_ \(e_{12},e_{23},e_{14},e_{43},e_{25},e_{35}\) _and e_<sub>45</sub> _are given by the following connectivity strings, each of length 10:_

_Let two time units (each unit is equal to the length of an interval) be needed to traverse any of these four edges, and we need to reach the vertex 3 from vertex 1. One possibility is that we start at interval I_=0 _to reach vertex 4 traversing the edge e_<sub>14</sub> _during the intervals 0 and 1, wait there for two time intervals and then traverse the edge e_<sub>43</sub> _during the intervals 4 and 5. Thus, we reach vertex 3 at interval I_=5 _and the total time of travel is 6 units._

_Another possibility is that we start from vertex 1 at interval I_=3_, reach vertex 2 at interval I_=4_, and then reach vertex 3 at I_=6_. In this case, the total time of travel is only 4 units although the arrival time is at interval I_=6.

_Yet another possibility exists as follows : start from vertex 1 at interval I_=4 _to reach vertex 4 at interval I_=5_, wait at vertex 4 for one interval and then reach vertex 3 at I_=8_, with a total travel time of 5 units._

_The first of these three schemes is an example for reaching vertex 3 from vertex 1 by following the earliest arrival time path, the second one is by following the fastest path or shortest time path, and the third one is by following the latest departure time path._

_If the distances between the vertices are given as d_<sub>12</sub>=8_,d_<sub>23</sub>=4_,d_<sub>14</sub>=5_, and d_<sub>43</sub>=6 _(shown in Fig. 2 as the labels of the corresponding edges), then the path 1-4-3 is the shortest distance path from vertex 1 to vertex 3._

While traversing a path from _p_ to _q_, we refer to the time of start from the initial vertex _p_ of this path by the starting interval \(I_s^{pq}\) and the time of arrival at the final vertex _q_ of the path by the finishing interval \(I_f^{pq}\). We represent this path by a 3-tuple \((I_s^{pq},I_f^{pq},pred^{pq})\), where _pred<sup>pq</sup>_ is the predecessor vertex of _q_ in the path. _pred<sup>pq</sup>_ will enable us to trace this path from _p_ to _q_ backward, starting from _q_. It may be noted that we would like to<tbc>

\(Timeintervals(I):0123456789CS_{12}=00011011CS_{23}=0110100CS_{14}=11011010CS_{43}=00001101CS_{25}=000111100CS_{35}=110000110CS_{45}=0000000111\)

(8)
(4)
1
2
3
(6)
(10)
(4)
(5)
4
5
(15)

Fig. 2. Aggregated static graph for the example situation

