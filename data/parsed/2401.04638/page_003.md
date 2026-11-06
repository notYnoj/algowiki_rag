<tbc>_form_ if all non-zero entries _d<sub>i,j</sub>\>_0 have the same value. The graph _G<sub>D</sub> induced by_ demands _D_ is defined as a simple graph _G<sub>D</sub>_=(_V,E<sub>D</sub>_), where _E<sub>D</sub>_={{_v<sub>i</sub>,v<sub>j</sub>_}:_d<sub>i,j</sub>+d<sub>j,i</sub>\>_0}.

**Routing Models.** For networking, _unsplittable_ routing requires that all flows of a demand \(d_{i,j}\in D\) must be sent along a single (directed) path, while _splittable_ routing does not restrict the number of paths used for the traffic of each demand; For a reconfigured network, segregated routing requires flows of each demand \(d_{i,j}\in D\) being transmitted on either the static network or the reconfigurable link between two endpoints of this demand, but non-segregated routing admits reconfigurable links used as shortcuts for flows along static links \[2\], \[3\].

Hence, there are _four different routing models: Unsplittable_ & _Segregated (US), Unsplittable_ & _Non-segregated (UN), Splittable_ & _Segregated (SS),_ and _Splittable_ & _Non-segregated (SN)._

### A. Min-Congestion Reconfigurable Network Problem

_"As minimizing the maximum congestion level in all links is a desirable feature of DCNs_ \[28\], \[29\]_, the objective of our work is to minimize the maximum link load"_

Yang et al. \[30\] (ACM SIGMETRICS 2020)

**Congestion.** Given a reconfigured network _N(M_) and demands _D_, let \(f:\vec{E}\cup\vec{M}\mapsto\mathbb{R}_{\ge 0}\) be _a flow_ serving _all_ demands _D_ in _N(M_), s.t. the size of the net flow from \(v_i\in V\) to \(v_j\in V\) equals to _d<sub>i,j</sub>_ for each demand entry \(d_{i,j}\in D\), under a routing model \(\tau\in\{\text{US},\text{UN},\text{SS},\text{SN}\}\). For each \(d_{i,j}\in D\), let \(f_{i,j}:\vec{E}\cup\vec{M}\mapsto\mathbb{R}_{\ge 0}\) denote the sub-flow of _f_ caused by the demand _d<sub>ij</sub>_. Thus, the flow _f_ can be further defined as \(f=\{f_{i,j}:d_{i,j}\in D\}\), where \(\forall e\in\vec{E}\cup\vec{M}:f(e)=\sum_{d_{i,j}\in D}f_{i,j}\left(e\right)\) and _f(e_) can exceed _c(e_). We consider _loads of a flow f_ on both static and reconfigurable links, i.e., \(\ell:\vec{E}\cup\vec{M}\mapsto\mathbb{R}_{\ge 0}\). _The load of each directed link_ \(e\in\vec{E}\cup\vec{M}\) induced by a flow _f_ is defined as \(\ell\left(e\right):=\frac{f(e)}{c(e)}\), and the _maximum load_ of _f_ is defined as \(\ell_\text{max}(f):=\text{max}\left\{\ell\left(e\right):e\in\vec{E}\cup\vec{M}\right\}\). Given a routing model \(\tau\in\{\text{US},\text{UN},\text{SS},\text{SN}\}\), the _congestion_ in a reconfigured network _N(M_) to serve _D_ is defined as

\(\lambda:=\text{min}\left\{\ell_\text{max}\left(f\right):\text{a flow}f\text{serving}D\text{in}N\left(M\right)\text{under}\tau.\right\}\)

**Definition 1** (Min-Congestion Reconfigurable Network Problem (MCRN))**.** _Given a reconfigurable network N_=(_V,E,_E_,c), a routing model_ \(\tau\in\{\text{\textit{US}},\text{\textit{UN}},\text{\textit{SS}},\text{\textit{SN}}\}\)_, and a demand matrix D, find a matching (reconfiguration)_ \(M\subseteq\mathcal{E}\)_, s.t., the congestion_ \(\lambda\) _to serve D in the network N(M_) _under the routing model_ \(\tau\) _is minimized._

### B. Preliminaries of Approximation Upper and Lower Bounds

A problem has an _approximation upper bound_ \(\alpha\) if there exists a polynomial-time \(\alpha\)-approximation algorithm to solve it, while a problem has an _approximation lower bound_ \(\alpha'\) if no polynomial-time algorithm can approximate it better than \(\alpha'\) unless P=NP. An approximation factor preserving reduction \[22\] can be constructed to reveal the approximability between two problems.

We next introduce the classic min-congestion multi- commodity flow problem, which will be used later.

**Definition 2** (Min-Congestion Multi-Commodity Flow Problem)**.** _We are given a demand matrix D, a static (directed) network N_=(_V,E_) _with the capacity function_ \(c:\vec{E}\mapsto\mathbb{R}_{\ge 0}\)_, and a routing model (splittable/unsplittable). Our goal is to find a flow:_

\(f=\left\{f_{ij}:\vec{E}\mapsto\mathbb{R}_{\ge 0}|d_{ij}\in D\right\},\)

_serving D under the given (splittable/unsplittable) routing model, s.t., the maximum load_ \(\text{max}_{e\in\vec{E}}\frac{f(e)}{c(e)}\) _can be minimized, where_ \(f(e)=\sum_{d_{ij}\in D}f_{ij}\left(e\right)\).

## III. SEGREGATED ROUTING MODEL

In this section, we start to study the MCRN problem under segregated routing. We first introduce LP-based approximation algorithms for both splittable and unsplittable flow models in §III-A, and then show that the MCRN problem of splittable flow is tractable for demands of a single source (resp., destination) in §III-B. Finally, we discuss approximation lower bounds for the problem under both splittable and unsplittable flow models in §III-C.

### A. Approximation Algorithms

Our approximation algorithms are based on solving a linear programming relaxation of the MCRN problem under segregated routing and obtaining a feasible solution by deterministic rounding. Thus, we will first present the ILP formulation of the problem under segregated routing, which is same for both splittable and unsplittable flow.

#### 1) ILP tion:

To simplify the ILP formulation, we denote each node \(v_i\in V\) simply by \(i\in V\) , e.g., a demand \(d_{i,j}\in D\) has source \(i\in V\) and sink \(j\in V\) . For the segregated routing model, we note that each reconfigurable link \(\left\{i,j\right\}\in M\) indicates that its demands _d<sub>i,j</sub>_ and _d<sub>j,i</sub>_ must be solely sent on \(\left\{i,j\right\}\in\mathcal{E}\), and other demands, whose two endpoints are not connected by a reconfigurable link included in _M_, will only transfer on the static network (_V,E_). We can write the min- congestion reconfigurable network problem with \(\tau\in\{\text{SS},\text{US}\}\) as the following mixed-integer linear program (MILP).

\(\text{min}\lambda\) (1)

\(\text{s.t.}\)<br>
\(\sum_{P\in\mathcal{P}_{i,j}}f_P\ge\left(1-z_{i,j}\right)\cdot d_{i,j}\forall i,j\in V\) (2)

\(\sum_{P\in\mathcal{P}:e\in P}f_P\le\lambda\cdot c\left(e\right)\forall e\in\vec{E}\) (3)

\(z_{i,j}\cdot d_{i,j}\le\lambda\cdot c\left(\left(i,j\right)\right)\forall\left(i,j\right)\in\vec{E}\) (4)

\(0\le\sum_{j\in V}z_{i,j}\le 1\forall i\in V\) (5)

\(f_P\ge 0\forall P\in\mathcal{P}\) (6)

\(z_{i,j}=z_{j,i}\forall i,j\in V\) (7)

\(z_{i,j}\in\left\{0,1\right\}\forall i,j\in V\) (8)

