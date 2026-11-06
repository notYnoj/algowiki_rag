In particular, this gives at least \(\lfloor n/8\rfloor\) pairs satisfying the claimed bound.

**Case** |**_U_**|**_\>n/_2:** Consider the set system of neighborhoods<tbc>

\(\mathcal{F}_1:=\{N_G(u)|u\in U\}\)

<tbc>over the domain _V(G_). Its members are distinct and |F<sub>1</sub>|=|_U_|_\>n/_2. Every subsystem \(\mathcal{F}'\subseteq\mathcal{F}_1\) satisfies<tbc>

\(\pi_{\mathcal{F}^\prime}(m)\le\pi_G(m)\le c\cdot m^\rho\)

<tbc>for every positive integer _m_. By Theorem 32, there is a constant \(k:=k(c,\rho)\) such that every subsystem \(\mathcal{F}'\) with at least two members contains distinct \(F,F'\) with

\(|F\triangle F'|\le k\cdot\frac{n}{|\mathcal{F}'|^{1/\rho}}.\)

The neighborhood _N<sub>G</sub>(u_) will be referred to as _F<sup>u</sup>_ when considered as a member of the set system. Starting with F<sub>1</sub>, repeat \(\lfloor n/8\rfloor\) times: choose such a pair _F<sup>u<sub>i</sub></sup>,F<sup>v<sub>i</sub></sup>_ and remove both sets to obtain F<sub>_i_+1</sub>. Before every choice, fewer than _n/_4 sets have been removed, so the current subsystem has more than _n/_4 members and the preceding application of Theorem 32 applies. The corresponding vertex pairs {_u<sub>i</sub>,v<sub>i</sub>_} are disjoint, and every chosen pair satisfies

\(|N_G(u_i)\triangle N_G(v_i)|\le k\cdot\frac{n}{|\mathcal{F}_i|^{1/\rho}}<k\cdot 4^{1/\rho} n^{1-1/\rho}.\)

Taking \(K:=k\cdot 4^{1/\rho}\) proves the first assertion. For the consequence, if C has VC density \(\rho\), choose a constant _c_ witnessing this fact and apply the first assertion to every graph in C. With \(d:=max(8,\lceil K\rceil)\), each _n_-vertex graph in C has at least \(\lfloor n/d\rfloor\) disjoint pairs with symmetric difference at most \(dn^{1-1/\rho}\). Thus, C has versatile symmetric difference of exponent \(1-1/\rho\).

