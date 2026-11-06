## 2 Preliminaries

We index the word positions from 1. In particular, \(w=w[1]w[2]\cdots w[s]\) for every word _w_ of length _s_. We let log_x_ denote the base-2 logarithm of _x_. For integers \(\ell\unknown r\), let \([\ell,r]\) be the integer interval spanning all values from \(\ell\) to _r_, inclusively, and for integer _n_, let \[_n_\]=\[1_,n_\]. Graphs are simple (without loops or parallel edges), undirected, and finite. For a graph _G_, we denote its vertex- and edge-set as _V(G_) and _E(G_), respectively.

### 2.1 Neighborhood complexity

For a graph _G_, let \(\pi_G(m)\) be the maximum number of distinct neighborhoods of vertices in _G_ restricted to a set of at most _m_ vertices, i.e.,

\(\pi_G(m):=max_{X\subseteq V(G),|X|\unknown m}|\{N_G(v)\cap X:v\in V(G)\}|.\)

We say that _G_ has _c-linear neighborhood complexity_ (or _c_-LNC) if \(\pi_G(m)\unknown c\cdot m\) for all positive \(m\in\mathbb{N}\). Class C has _linear neighborhood complexity_ if there exists a constant _c_ such that all graphs \(G\in\mathcal{C}\) have _c_-LNC. We say that C has _VC density_ \(\rho\) if there exists a constant _c_ such that for all \(G\in\mathcal{C}\), \(\pi_G(m)\unknown cm^\rho\) for all positive _m_. Finally, we say that _G_ has \((c,\rho)\)_-polynomial neighborhood complexity_ (or \((c,\rho)\)-PNC) if \(\pi_G(m)\unknown c\cdot m^\rho\) for all positive \(m\in\mathbb{N}\).

### 2.2 Symmetric difference and sd-degeneracy

In this paper, we define the _symmetric difference_ of two vertices _u,v_ in a graph _G_ as

\(\mathrm{sd}_G(u,v):=|N_G(u)\triangle N_G(v)|,\)

where \(\triangle\) denotes the symmetric difference of two sets: \(X\triangle Y:=(X\backslash Y)\cup(Y\backslash X)\). There are slight variations in defining the symmetric difference of _u,v_ (depending on whether or not _u,v_ themselves count), but they only differ by a constant additive term. We say that two distinct vertices _u,v_ are _d-near-twins_ in _G_ if \(\mathrm{sd}_G(u,v)\unknown d\), and are _twins_ if sd_<sub>G</sub>(u,v_)=0.

The _symmetric difference_ sd(_G_) of a graph _G_ is the least nonnegative integer _d_ such that for every induced subgraph _H_ of _G_ with at least two vertices, there are two _d_-near-twins in _H_.

An _sd-degeneracy sequence_ of an _n_-vertex graph _G_ is a list (_u_<sub>1</sub>_,v_<sub>1</sub>)_,...,(u_<sub>_n_-1</sub>_,v_<sub>_n_-1</sub>) of pairs of vertices of _G_ such that

• \(u_i\neq v_i\) for every \(i\in[n-1]\),<tbc>

• _V(G_)={_u_<sub>1</sub>_,u_<sub>2</sub>_,...,u_<sub>_n_-2</sub>_,u_<sub>_n_-1</sub>_,v_<sub>_n_-1</sub>}, and<tbc>

• there is no _i\<j_ such that \(u_i\in\{u_j,v_j\}\).<tbc>

<tbc>Informally, it is an elimination sequence where only the first element of the pair is removed at each step. The _width_ of the sd-degeneracy sequence (_u_<sub>1</sub>_,v_<sub>1</sub>)_,...,(u_<sub>_n_-1</sub>_,v_<sub>_n_-1</sub>) is defined as

\(\mathrm{max}_{i\in[n-1]}\mathrm{sd}_{G-\{u_1,u_2,\dots,u_{i-1}\}}(u_i,v_i).\)

The _sd-degeneracy_ of _G_ (where ’sd’ stands for symmetric difference) is the least integer _d_ such that _G_ admits an sd-degeneracy sequence of width _d_.

Equivalently, the class of graphs of sd-degeneracy at most _d_ can be defined by induction on the number of vertices: a graph _G_ has sd-degeneracy at most _d_ if either \(|V(G)|\unknown 1\), or there is a pair of distinct vertices \(u,v\in V(G)\) such that \(\mathrm{sd}_G(u,v)\unknown d\) and the graph _G-u_ has sd-degeneracy at most _d_.

