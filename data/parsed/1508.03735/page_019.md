**Claim 4.** _For all_ \(t\in[T]\)_, the approximate count C(t_) _satisfies_ \(|C(t)-\sum_{i=1}^t\tau(i)|\le r\)_. The summary statistic U can be written with_ \(O\left(\frac{\|\tau\|_0logT}{r}\right)\) _bits._

The second one takes the compressed message from ApproxCount as input, and extracts the approximate counts. See Algorithm 4.

**Algorithm 4** ExtractCount(_U,r,T_)

**Input:** a list of update steps _U_, refinement parameter _r_, and time horizon _T_

**Initialize:** a counter \(C:[T]\rightarrow\mathbb{N}\) such that \(\tau(t)=0\) for all \(t\in[T]\)

**for:** each \((t,\bullet)\in U\)

Let \(c'=C(t-1)\)

**if** \(\bullet=+\): \(c=c'+r\); **else**: \(c=c'-r\)

**for:** each \(t'\in\{t,\dots,T\}\):

Let \(C(t')=c\)

**Output:** the approximate counts _C_

Looking ahead, we will use ApproxCount in the coordinator’s encoding function to compress the information in the simulated dynamics, and use ExtractCount in each player’s decoding function to extract the information about the dynamics.

## 6.1 Atomic Routing Games and Best-Response Dynamics

An _atomic routing game_ instance is defined by a directed graph _G_=(_V,E_), _n_ players with their sources- sink pairs (_s_<sub>1</sub>_,d_<sub>1</sub>)_,...,(s<sub>n</sub>,d<sub>n</sub>_), and a continuous, nondecreasing and \(\lambda\)-Lipschitz cost function \(c_e:[0,n]\rightarrow[0,1]\) for each edge \(e\in E\). Each player _i_ needs to route 1 unit of flow from _s<sub>i</sub>_ to _d<sub>i</sub>_, so her strategy set A_<sub>i</sub>_ is the set of _s<sub>i</sub>-d<sub>i</sub>_ paths. We think of a flow of a single player alternately as a vector indexed by paths _P_, and as a vector indexed by edges _e_. The aggregate flow is the sum over all player flows. A flow _f_ (viewed as a vector indexed by paths) is _feasible_ if for each player _i_, \(f_P^{(i)}\) equals 1 for exactly one _s<sub>i</sub>-d<sub>i</sub>_ path and equals 0 for all other paths. We can translate such a flow into a flow indexed by edges by defining \(f_e^{(i)}=\sum_{e\in P}f_P^{(i)}\). The cost _c<sub>P</sub>(f_) of path _P_ in a flow _f_ is

\(c_P(f)=\sum_{e\in P}c_e(f_e)\)

where \(f_e=\sum_{i=1}^nf_e^{(i)}\). We will denote the number of edges by _m_, the set of feasible flow by F, and sometimes abuse notation to use _f_<sup>(_i_)</sup> to denote the path of player _i_. Now we formalize the notion of approximate equilibrium flow in a routing game.

**Definition 7** (Approximate Equilibrium Flow)**.** _Let f be a feasible flow for the atomic instance_ (_G,c). The flow f is an_ \(\varepsilon\)-equilibrium flow _if each player_ \(i\in[n]\) _is playing_ \(\varepsilon\)-best-response_, that is for every pair every pair of s<sub>i</sub>-d<sub>i</sub> paths_ \(P,P'\) _with_ \(f_P^{(i)}>0\),

\(c_P(f)\le c_{P^\prime}(f')+\varepsilon\)

_where_ \(f'\) _is the flow identical to f except for its i-th component:_ \(f_P^{^\prime(i)}=0\) _and_ \(f_{P^\prime}^{^\prime(i)}=1\)_. When f is a_ 0_-equilibrium flow, we simply say that f is a equilibrium flow._

