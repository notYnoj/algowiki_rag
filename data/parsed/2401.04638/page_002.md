<tbc>general settings (outlined in  I), and also a fine-grained algorithmic analysis for restricted cases.

#### a) Segregated Routing:

We provide a mixed-integer programming formulation for segregated and un-/splittable flow models whose LP relaxation can be solved efficiently. For splittable flows, we present a 2-approximation algorithm by a novel deterministic rounding approach, and also prove the APX-hardness even if its demands are _uniform_ and the _graph induced by demands_ is bipartite. However, we also show that the problem becomes tractable for demands with a single source (resp., destination). For unsplittable flows, we show that the min-congestion reconfigurable network problem cannot be approximated better than the min-congestion multi- commodity unsplittable flow problem (MCMF) \[22\], but any \(\rho\)-approximation algorithm based on rounding techniques for the MCMF problem can be utilized to give a \(2\rho\)-approximation for the reconfigurable network problem. This implies an approximability of \(\Theta\left(logm/loglogm\right)\) for segregated and unsplittable routing, where _m_ is the number of static links.

#### b) Non-Segregated Routing:

Under the splittable (resp., unsplittable) flow model, even for demands of a single source (resp., destination), the problem cannot be approximated better than \(\Omega\left(c_\mathrm{max}/c_\mathrm{min}\right)\) unless P=NP, where _c_<sub>max</sub> (resp., _c_<sub>min</sub>) denotes the maximum (resp., minimum) capacity on all links, and it still remains NP-hard for _uniform capacities_, i.e., \(c:\vec{E}\cup\vec{\mathcal{E}}\mapsto\{a\}\) for \(a\in\mathbb{R}_{>0}\). However, the problem with uniform capacities becomes efficiently solvable for demands of a single commodity under un-/splittable flow.

Our trace-driven simulations show that our algorithms significantly improve on state of the art methods.

### B. Organization

We introduce our formal model and preliminaries in §II. Our algorithmic and hardness results for the segregated model are presented in §III, followed by a study of non-segregated routing in §IV. We then investigate the performance of our algorithms with trace-driven simulations in \(\mathsection\)V. Lastly, we discuss related work in §VI and conclude in §VII.

## II. MODEL AND PRELIMINARIES

We first introduce our network model, demands and routing policies, and then formalize the min-congestion demand<tbc>

<tbc>aware network design problem in §II-A. We then provide preliminaries for proving hardness or approximation in §II-B.

**Network Model.** Let _N_=(_V,E,E,c_) be a _reconfigurable (hybrid)_ network \[23\], \[24\] connecting _n_ nodes _V_={_v_<sub>1</sub>_,...,v<sub>n</sub>_} (e.g., top-of-the-rack switches), using static links _E_ (usually electrically packet-switched), where (_V,E_) is called the _static network_ of _N_. The network _N_ also contains a set of reconfigurable (usually optical) links E, s.t., (_V,_E) constitutes a _complete graph_ on _V_ . The graph \((V,E\cup\mathcal{E})\) is a _bidirected_<sup>1</sup> _(multi)-graph_ such that two directions of each bidirected link \(\{v_i,v_j\}\in E\) (resp. \(\{v_i,v_j\}\in\mathcal{E}\)), where \(v_i,v_j\in V\) , work as two _(anti-parallel) directed links_ (_v<sub>i</sub>,v<sub>j</sub>_) and (_v<sub>j</sub>,v<sub>i</sub>_) respectively. We use the symbol \(\vec{E}\) (resp. \(\vec{\mathcal{E}}\)) to denote the set of corresponding directed links of _E_ (resp. E). Moreover, a function \(c:\vec{E}\cup\vec{\mathcal{E}}\mapsto\mathbb{R}_{\ge 0}\) defines _capacities_ for both directions of each bidirected link in \(E\cup\mathcal{E}\), where the _maximum_ (resp., _minimum) capacity_ is denoted by _c_<sub>max</sub> (resp., _c_<sub>min</sub>). We denote _uniform capacities_ if \(c:\vec{E}\cup\vec{\mathcal{E}}\mapsto\{a\}\), where \(a\in\mathbb{R}_{\ge 0}\), e.g., _a_=1. The reconfigurable network _N_ can only implement a subset of reconfigurable links E, which must be a matching \(M\subseteq\mathcal{E}\), to provisionally enhance the static network (_V,E_). The enhanced graph \(N\left(M\right)=(V,E\cup M,c)\) determines the actual topology of the communicating network, where _N(M_) is called a _reconfigured network_ and the matching _M_ is called a _reconfiguration_ of _N_.

**Traffic Demands.** The reconfigured network should serve a certain communication pattern, represented as a \(|V|\times|V|\) communication matrix \(D:=\left(d_{i,j}\right)_{|V|\times|V|}\) (_demands_) with non- negative real-valued entries. An entry \(d_{i,j}\in\mathbb{R}_{\ge 0}\) represents the traffic load (frequency) or a demand from the node _v<sub>i</sub>_ to the node _v<sub>j</sub>_. With a slight abuse of notation, let _D(v<sub>i</sub>,v<sub>j</sub>_) also denote a demand from _v<sub>i</sub>_ to _v<sub>j</sub>_ hereafter. For each demand _D(v<sub>i</sub>,v<sub>j</sub>)\>_0, the pair (_v<sub>i</sub>,v<sub>j</sub>_) is called a commodity with the source _v<sub>i</sub>_ and the destination _v<sub>j</sub>_. The matrix of demands _D_ is called _single commodity_ if it contains only one commodity, otherwise multi-commodity. A multi-commodity matrix _D_ is called single source (resp., destination) if all commodities share the same source (resp., destination). Demands _D_ are called _uni_

<sup>1</sup> Symmetrical connectivity is the standard industry assumption for static cabling, however for reconfigurable links as well. Outside highly experimental hardware, e.g. \[5\], off-the-shelf products use full-duplex connections \[25\], \[26\] and this model assumption is hence prevalent, even in Free-Space Optics \[27\] proposals.

\begin{tabular}{cccccc}
**Approximation Bounds \&** & **Splittable** & **Segregated** & **Restrictions** & **Restrictions** & **Results** \\
**Time Complexity** & **Flow** & **Routing** & **On Demands** & **On Capacities** & **References** \\
2-approximation & yes & yes & & & Thm. 1 \\
APX-complete & yes & yes & uniform and bipartite demands & & Thm. 4 \\
Tractable & yes & yes & single source (resp., dest.) & & Thm. 3 \\
_O_(log_m/_loglog_m_)-approximation & no & yes & & & Thm. 2 \\
Lower Bound: \(\Omega\left(logm/loglogm\right)\) & no & both & & & Thm. 5 \\
Lower Bound: \(\Omega\left(c_\mathrm{max}/c_\mathrm{min}\right)\) & both & no & single source (resp., dest.) & & Thm. 6 \\
NP-hard & both & no & single source (resp., dest.) & uniform & Thm. 7 \\
Tractable & both & no & single commodity & uniform & Thm. 8 \\
\end{tabular}

TABLE I

SUMMARY OF OUR APPROXIMATION UPPER AND LOWER BOUNDS ON THE MCRN PROBLEM (DEFINITION 1).

