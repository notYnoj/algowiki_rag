<tbc>_G_ assigns value \(F(P)\ge 0\) for each directed path _P_ in _G_. We say that _P_ is a flow path of _F_ if _F(P)\>_0. The _congestion_ on edge _e_ of _F_ is \(\cong_F(e)=\frac{\sum_{e\in PF(P)}}{c(e)}\) and the congestion of _F_ is \(\cong_F=\mathrm{max}_{e\in E}\cong_F(e)\). The _length_ of _F_ is the maximum total length overall flow paths of _F_, i.e., \(\mathrm{max}_{P:F(P)>0}\ell(P)\). The _hopbound_ of _F_ is the maximum number of edges overall flow paths of _F_, i.e., max<sub>_P:F(P)\>_0</sub>|_E(P_)|. For any vertex set _U_, a _demand D on U_ assigns a value \(D(u,v)\ge 0\) for each vertex pair \((u,v)\in U\). The demand _D<sub>F</sub>_ routed by _F_ is defined as \(D_F(u,v):=\sum_{(u,v)\text{-path}_PF}F(P)\). We say that _D_ is routable with length \(\ell\), congestion \(\kappa\), and hopbound _h_ if there exists a flow _F_ with length \(\ell\), congestion \(\kappa\), and hopbound _h_ that routes _D_. When _D_ is routable in _G_ with congestion 1, we sometimes just say that _D_ is routable in _G_. With this, we are ready to define LC-flow shortcuts.

**Definition 4.1** (Length-Constrained Flow Shortcuts)**.** A shortcut \(G'=(V\cup V',E\cup E')\) is a _length-constrained flow shortcut of G_ with hopbound _h_,<sup>7</sup> congestion slack \(\kappa\), and length slack _s_ if:

1. Every demand on _V_ routable in _G_ with length \(\lambda\) and congestion 1 is routable in \(G'\) with length \(\lambda s\), congestion 1, and hopbound _h_, and<tbc>

2. Every demand on _V_ routable in \(G'\) with length \(\lambda\) and congestion 1 is routable in _G_ with length \(\lambda\) and congestion \(\kappa\).

The concept of LC-flow shortcut above was recently defined in undirected graphs \[HHL<sup>+</sup>24\]. They show that, for any _n_-vertex undirected graph _G_ with capacity and length at most poly(_n_) and a parameter _k_, there exists a flow shortcut \(G'\) with hopbound _h=O(k_), length slack _s=O(k_), congestion slack \(\mathrm{poly}(k\mathrm{log}n)n^{O(1/\sqrt{k})}\), and size \(|E'|\le n^{1+O(1/\sqrt{k})}\mathrm{poly}(\mathrm{log}n)\). It is an interesting open problem if an LC-flow shortcut with non-trivial guarantee exists.

## Reachability Shortcuts, Distance Shortcuts, and Congestion Shortcuts.

Observe that a reachability shortcut is precisely an LC-flow shortcut when the constraints related to length and congestion in Definition 4.1 are removed.

We will use the terms _distance shortcut_ and _congestion shortcut_ to refer to an LC-flow shortcut when the respective constraint related to congestion and length in the definition of Definition 4.1 is removed.

More specifically, when focusing only on length, Definition 4.1 simplifies to distance shortcuts as follows. Let dist_<sub>G</sub>(s,t_) denote the distance from _s_ to _t_ in _G_. Let \(\mathrm{dist}_G^h(s,t)\) denote the minimum length of paths with hopbound _h_ from _s_ to _t_ in _G_.

**Definition 4.2** (Distance Shortcuts)**.** A shortcut \(G'=(V\cup V',E\cup E')\) is a _distance shortcut of G_ with hopbound _h_ and length slack _s_ if, for every vertex pair \((s,t)\in V\times V\) ,

1. If \(\mathrm{dist}_G(s,t)\le\lambda\), then \(\mathrm{dist}_{G^\prime}^h(s,t)\le\lambda s\) and<tbc>

2. If \(\mathrm{dist}_{G^\prime}(s,t)\le\lambda\), then \(\mathrm{dist}_G(s,t)\le\lambda\).

When focusing only on congestion, Definition 4.1 simplifies to congestion shortcuts as follows:

**Definition 4.3** (Congestion Shortcuts)**.** A shortcut \(G=(V\cup V',E\cup E')\) is a _congestion shortcut of G_ with hop bound _h_ and congestion slack \(\kappa\) if

1. Every demand on _V_ routable in _G_ is routable in \(G'\) with hopbound _h_, and<tbc>

2. Every demand on _V_ routable in \(G'\) is routable in _G_ with congestion \(\kappa\).<tbc>

<sup>7</sup>The hopbound in this section has the same purpose as the diameter in previous sections. We change to our terminology to hopbound to avoid confusion, because the graph here has edge lengths.

