<tbc>Ren et al. \[24\] study ISL allocation as a multi-objective optimization problem under dynamic topology and resource limits. At the physical-layer/network interface, Gioulis et al. \[25\] present a constellation-aware optical ISL model that evaluates power requirements across an orbital period, supporting more realistic feasibility constraints for temporal adjacency. Finally, learning-based routing in dynamic LEO settings has also gained traction; Riyad et al. \[26\] report Q-learning based routing over snapshot- derived topologies, reflecting a trend toward adaptive routing under time-varying connectivity.

Taken together, recent literature shows (i) renewed algorithmic attention to temporal shortest/fastest path computation and its acceleration, and (ii) rapidly growing interest in time-dependent routing/planning for LEO mega- constellations with laser ISLs. Our work targets the intersection of these themes by focusing on all-pairs shortest _communication-time_ paths under discrete-time feasibility constraints, with an implementation structure intentionally aligned with parallelizable primitives.

## 3 NETWORK MODEL AND ASSUMPTIONS

This section introduces the basic preliminaries of the network model and the assumptions.

### 3.1 Preliminaries

We introduce a model of the temporal graph to be used for our later discussions, which is formulated around the concepts of time-varying connectivity in a temporal graph as given in \[27\], but with some modifications. The following components describe our model:

#### 3.1.1 Temporal graph representation

We denote a temporal graph as _G_=(_V,E<sub>t</sub>_), where \(V=\{1,2,\cdots,n\}\) is the set of _n_ vertices in the graph and _E<sub>t</sub>_ is the set of time-varying edges considered over a time window of size _T_ starting from time _t_=0 to _t=T_. This time window of observation will be represented as _W_=\[0_,T_\].

#### 3.1.2 Time Window

In general, a temporal edge \(e_{pq}\in E_t\) connecting two vertices _p_ and _q_ during this time window _W_ will be represented by a tuple \((p,q,[t_1,\Delta t_1],[t_2,\Delta t_2],\cdots,[t_k,\Delta t_k])\), where the vertices _p_ and _q_ are connected only during the non-overlapping time durations \([t_i,t_i+\Delta t_i],i=1,2,\cdots,k\) with the time ordering of \(0\le t_1<t_1+\Delta t_1<t_2<t_2+\Delta t_2<\cdots<t_k<t_k+\Delta t_k\le T\). An example of such time-varying connections is shown by the horizontal line segments in Fig. 1 for _k_=3. We refer to these time durations \([t_i,t_i+\Delta t_i],i=1,2,\cdots,k\) as the _connectivity durations_ for the vertices _p_ and _q_ during the observation window \[0_,T_\], and denote these by _CD<sub>pq</sub>_\[0_,T_\] or simply _CD<sub>pq</sub>_ when the time window \[0_,T_\] is implied from the context.

#### 3.1.3 Time slots for each snapshot

We divide the time window \[0_,T_\] in equal intervals of time duration \(\tau\) (refer to Fig. 1 for a diagrammatic representation), where a snapshot of the connectivity is taken during each such interval. Each interval’s length \(\tau\) may be set to the<tbc>

<tbc>most petite possible duration used to observe the graph’s time-varying nature with maximum temporal resolution. The exact value of \(\tau\) may be chosen depending on the requirements of typical real-life applications, e.g., phone calls, email communications, etc., for which the temporal graph model will be used.

**Example 1.** _For example, the message transmission delay can be computed as_ \(\mathcal{D}=\frac{\mathcal{Q}_\sharp}{\mathcal{B}}\) _, where Q is the size of the message m and B is the bit rate of a channel in a particular band \[28\]. Therefore, consider a node v<sub>i</sub> starts the transmission of message m of size_ 10_MB at a time slot t over GSM band_ 20_MHz. Then, the communication latency can be computed as:_ \(\mathcal{D}=\frac{10}{20}=0.5\) _seconds. But in case the same message will be sent through GSM Band_ 10_MHz, then_ D _will be_ \(\mathcal{D}=\frac{10}{20}=1\) _seconds. Hence, we consider the value of_ \(\tau\) _depending on the current availability of the channel bandwidth and the size of the message to be sent. In this example,_ \(\tau\) _will be set to one second, and for each second, we take the snapshot accordingly._

We assume that \(T=M\tau\), so that there will be a total of _M_ snapshots, numbered as \(0,1,2,\cdots,M-1\) taken during these _M_ intervals \([0,\tau],[\tau,2\tau],\cdots,\dots[(M-1)\tau,T]\), respectively to provide the total connectivity information of every edge of the temporal graph during the time window \[0_,T_\] under consideration. An interval _I=j_ will refer to the time duration from \(j\tau\) to \((j+1)\tau\).

Two vertices _p_ and _q_ will be connected by an edge _e<sub>pq</sub>_ during the _j<sup>th</sup>_ snapshot, \(j\in\{0,1,2,\cdots,M-1\}\), if there is a continuous connectivity of duration at least \(\lambda\tau\) (\(0<\lambda<1\)) during the interval \([j\tau,(j+1)\tau]\) which also has a non-null intersection with at least one of the _k_ connectivity durations \([t_i,t_i+\Delta t_i],i=1,2,\cdots,k\) of the vertices _p_ and _q_. Note that, \(\lambda\) can be a priori fixed depending on the specific application requirements.

#### 3.1.4 Connectivity String

The connectivity information during the time window \[0_,T_\] from the vertex _p_ to the vertex _q_ of the temporal graph will then be represented by a binary string of length _M_, termed as the _connectivity string_, in which each bit corresponds to a<tbc>

t1
t2
t3
epq
t1+At1
t2+At2
t3+At3
connectivity
0
T
2T
3T
4T
5T
6T
7T
8T
9T
10T = T
time

Fig. 1. Connectivity durations of edge _e<sub>pq</sub>_

