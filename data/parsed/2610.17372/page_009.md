<tbc>is _O(Mn_<sup>2</sup>). The loop in lines 11-19 in the procedure _update\_all\_possible\_contacts_ ensures that there cannot be more than one 3-tuple in _P(p,r_) with a given value of \(I_f^{pq}\). Thus, the total number of 3-tuples in any entry _P(p,q_) or _P(q,r_) of the path matrix is always less than or equal to _M_. Also, while entering any new entry (3-tuple \((I_s^{pq},I_f^{pq},pred^{pq})\)) in the path matrix (line 26), we need to search the existing 3-tuples (which are arranged in a sorted increasing order of \(I_f^{pq}\)), for inserting the new element in its correct position in this sorted list as in binary insertion sort. This step would need _O(M_) time. Hence, each call to the procedure _update\_all\_possible\_contacts_ in the forward as well as backward steps requires _O(M_<sup>2</sup>) time. Thus each of forward and backward steps needs _O(M_<sup>2</sup>_n_<sup>3</sup>) time. The procedure find _minimum\_time\_path_ needs _O(Mn_<sup>2</sup>) time. Hence, we get the following result.

**Theorem 2.** _Algorithm 1 requires O(M_<sup>2</sup>_n_<sup>3</sup>) _time complexity to compute the all-pairs shortest time paths in a temporal graph._

## 6 EXPERIMENTAL SETUP

This section describes the experimental design in a way that directly validates the modeling choices and algorithmic primitives introduced in Sections 3 and 4. In particular, we validate: (i) snapshot-based temporal discretization and the construction of connectivity strings _CS<sub>pq</sub>_; (ii) the run-length feasibility constraint of length _t<sub>pq</sub>_ used by Procedure 1; (iii) correctness of the path-matrix updates (Procedure 3) relative to trusted baselines; (iv) the necessity of the forward and backward passes in Algorithm 1; and (v) the computational scaling behavior implied by Theorem 2. We also quantify the network-level implications of optical range constraints and waiting-vs-traversal behavior that are unique to temporal routing.

### 6.1 Experimental Goals and What We Validate

The experiments are organized around four validation questions that map one-to-one to the methodology:

1) **Temporal-graph validity:** Does the snapshot construction produce meaningful time-varying adjacency consistent with LEO geometry, and does the resulting _CS<sub>pq</sub>_ capture periodic contact patterns over one orbit?<tbc>

2) **Run-length feasibility validity:** Do run-length requirements (Procedure 1) correctly enforce the model assumption that a hop (_p,q_) is traversable only when _CS<sub>pq</sub>_ contains a contiguous run of ones of length \(\ge t_{pq}\) after packet arrival?<tbc>

3) **Algorithmic correctness validity:** Does Algorithm 1 compute the same shortest communication-time outcomes as baselines that are known-correct (time- expanded graph shortest paths, and temporal Dijkstra-like methods) on problem sizes where those baselines are feasible?<tbc>

4) **Computational scaling validity:** Do runtime and memory scale with (_n,M_) in a way consistent with Theorem 2, and does the matrix-style update structure admit practical acceleration via data-parallel kernels (bit operations and batched run detection)?<tbc>

<tbc>We report both _algorithmic_ metrics (run- time/memory/scaling and baseline agreement) and _network_ metrics (reachability, shortest communication time, hop count, and waiting fraction).

### 6.2 Observation Window and Snapshot Discretization \((T,M,\tau)\)

As described in the methodology, we represent the network as a temporal graph over an observation window _W_=[0_,T_] divided into _M_ snapshots of duration \(\tau\) such that \(T=M\tau\). For LEO constellations, the topology is strongly periodic due to deterministic orbital dynamics. Therefore, we choose _T_ to span approximately one orbital period, so that the temporal graph contains a full recurrence of link formation and dissolution.

In the main experiments we use a nominal orbital period of _P_<sub>orb</sub>=96 minutes (LEO-like), and perform sensitivity checks for \(P_\mathrm{orb}\in[90,128]\) minutes. For each \(\tau\) we set<tbc>

\(M=\left\lceil\frac{P_\mathrm{orb}}{\tau}\right\rceil,\) (1)

<tbc>and sweep temporal resolution using

\(\tau\in\{5,10,20\}\text{s.}\) (2)

For _P_<sub>orb</sub>=96 minutes this yields _M_={1152,576,288} snapshots.

**Discretization validity check.** To validate that the snapshot durations are fine-grained enough for contact modeling, we measure (i) snapshot-wise average degree over time (Fig. 7), and (ii) link-run statistics derived from _CS<sub>pq</sub>_ ( 6). The goal is to ensure that observed connectivity is not an artifact of overly coarse sampling (missing short contacts) or overly fine sampling (inflating _M_ without changing routing outcomes).

### 6.3 Constellation Mobility and Link Feasibility Model

Satellite positions are computed using deterministic Keplerian orbit propagation. This guarantees that the induced temporal graph is structured and periodic, which is central to our motivation for precomputation over one orbit. At each snapshot index \(j\in\{1,\dots,M\}\), an optical ISL between satellites (_p,q_) is declared feasible if

\(d_{pq}(j)\le R,\) (3)

where _d<sub>pq</sub>(j_) is the inter-satellite distance at snapshot _j_, and _R_ is the optical range threshold. We evaluate

\(R\in\{659,1319,1500,1700\}\text{km.}\) (4)

For each (_p,q_) we construct the connectivity string

\(CS_{pq}^{(R)}[j]=\unknown\{d_{pq}(j)\le R\},\) (5)

which matches the connectivity-string definition in Section 3. This binary string is the primitive consumed by Procedure 1 for finding the next contiguous run of ones.

Because temporal routing depends on _when_ neighbors appear and disappear, we validate the time-varying adjacency behavior using a node-centric storyboard across consecutive snapshots. Figures 4 and 5 show a focus satellite<tbc>

