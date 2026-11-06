<tbc>Objects in the same fiber _F(z_) have \(\Delta=0\) and differ only in vector space X, while the _M_ fibers {_z_<sub>1</sub>_,...,z<sub>M</sub>_} form distinct spatial sites on S.

Lemma 3.4 (Coordinate-Fiber Closure). _For every disk c_=(_g,r_) _and coordinate z,_ \(F(z)\cap\mathcal{A}(c)\neq\emptyset\Longleftrightarrow F(z)\subseteq\mathcal{A}(c)\)_. Because all_ \(v\in F(z)\) _have the same distance_ \(\Delta(z,g)\) _to g, a disk never splits a fiber (Figure 2(a)), and the induced fiber subgraph G_\[_F(z_)\] _is identical under every disk that admits z._

Theorem 3.5 (Two-Scale Route Decomposition). _For any directed graph G_=(_V,E_) _and disk c, G_\[A(_c_)\] _is strongly connected if: (i) **(Intra-fiber connectivity)** G_\[_F(z_)\] _is strongly connected for every active fiber_ \(F(z)\subseteq\mathcal{A}(c)\)_; and (ii) **(Coordinate-quotient connectivity)** the quotient graph formed by contracting each active fiber_ \(F(z)\subseteq\mathcal{A}(c)\) _into a single site vertex z is strongly connected._

_Example 3.6._ In Figure 2(b), the quotient path \(z_0\rightarrow z_1\rightarrow z_2\) across active sites is supported by inter-coordinate bridge edges \(a_0\rightarrow b_1\) and \(a_1\rightarrow b_2\) (Condition (ii)). Condition (i) connects these bridges through intra-fiber paths \(s\rightarrow a_0\) in _F(z_<sub>0</sub>), \(b_1\rightarrow a_1\) in _F(z_<sub>1</sub>), and \(b_2\rightarrow t\) in _F(z_<sub>2</sub>), forming an end-to-end path in _G_\[A(_c_)\]. Neither condition scales with the number of possible query disks: Condition (i) involves only _M_ static fiber subgraphs fixed at index construction time, and Condition (ii) depends only on the spatial sites inside \(\Omega_c\).

## 3.3 Polylogarithmic Guarantees

**Coordinate Tie-Breaking and Two-Scale Selection.** To maintain connectivity on small disks, each vertex _u_ allocates a quota of _B<sub>g</sub>_ edges to geographically nearby candidates. If _u_ simply linked to its _B<sub>g</sub>_ geographically closest objects, a nearby landmark _z_ with thousands of co-located photos would fill all _B<sub>g</sub>_ slots with ties at _z_ and leave no edges to surrounding sites, violating Condition (ii) of<tbc>

<tbc>Theorem 3.5; conversely, keeping only one arbitrary object per site would disconnect multi-object fibers and violate Condition (i).

To satisfy both conditions, we model D by a regular marked point process \[9, 31\] (Appendix A.4): _M_ distinct sites _Z_<sub>1</sub>_,...,Z<sub>M</sub>_ are drawn on a compact, connected region \(\mathcal{S}\subseteq\mathbb{S}^2\) with bounded density \(0<p_{s,-}\le p_s(z)\le p_{s,+}\), and each site _Z<sub>i</sub>_ hosts a fiber _F(Z<sub>i</sub>_) of size \(f_i\ge 1\) (\(\sum_{i=1}^Mf_i=n\)) whose vectors \(X_v\sim v_{Z_i,\Theta_i}\) come from a geodesic support of intrinsic dimension _d_<sub>X</sub>_\>_0, diameter _D<sub>x</sub>_, and doubling constant _C<sub>D</sub>_. Each vertex _u_ selects geographic edges using two rules: (1) _Intra-fiber_ \(\alpha\)_-witness rule_: within _F(z_), _u_ scans up to _K<sub>f</sub>_ candidates \(v\in F(z)\backslash\{u\}\) in ascending _d(x<sub>u</sub>,x<sub>v</sub>_) and retains _v_ unless an earlier retained \(w\in F(z)\) satisfies \(d(x_v,x_w)\le d(x_u,x_v)/\alpha\) (\(\alpha>1\)). (2) _Nearest-first coordinate stream: u_ visits sites \(z\neq s_u\) in nondecreasing \(\Delta(s_u,z)\) and applies Rule (1) inside each _F(z_) until _B<sub>g</sub>_ new edges are selected, with cumulative charge \(L_u(\rho)=\sum_{z:\Delta(s_u,z)\le\rho}\chi_u(z)\) within radius \(\rho\).

**Bounding Per-Site Quota Consumption.** Partition X\\{_x<sub>u</sub>_} into dyadic shells \[2<sup>-_k_</sup>_D_<sub>x</sub>,2<sup>-(_k_-1)</sup>_D_<sub>x</sub>\] from minimum separation \(\varepsilon_\alpha=\Theta((\delta/n^2)^{1/d_\mathcal{X}})\) to _D<sub>x</sub>_. Because any two \(\alpha\)-pruned survivors in the same shell are separated by \(>1/(2\alpha)\) of the shell radius, doubling packing limits each shell to \(\le P_\alpha=C_D^{\lceil log_2(4\alpha)\rceil}=O(1)\) survivors; across all shells, with probability \(\ge 1-\delta/3\)_, any site z of arbitrary size f<sub>z</sub> consumes at most_

\(a_\alpha=min\big\{K_f,P_\alpha\big(1+\big\lceil log_2(D_x/\varepsilon_\alpha)\big\rceil\big)\big\}=O\big(log(nM/\delta)\big)\) (2)

slots of _B<sub>g</sub>_. Meanwhile, RGG theory \[30, 31\] shows that linking active sites within radius \(\rho_c=C_s\sqrt{\lambda_2(\Omega_c)log(3M/\delta)/(M\pi_c)}\) (\(\pi_c=\int_{\Omega_c}p_sd\lambda_2\)) connects the coordinate quotient across \(\Omega_c\), with at most \(h_c=\lceil C_hlog(3M/\delta)\rceil\) sites per \(\rho_c\)-ball (Appendix A.5).

Theorem 3.7 (Two-Scale and End-to-End Strong Connectivity). _Under the regular marked-site model (Appendix A.4), for_<tbc>

(a) Two sources, same IDs
(b) Reuse w to prune v
(c) Keep once, sort by d
VECTOR SPACE
d(xu,
VECTOR SPACE
d(xu,
VECTOR SPACE
d(xu,
p
P = [w, p]
p
a = 2
p
w reused no extra slot
y
Bv = 2
y
pool misses y
y: one new slot
=4.47
Bv = 2, Bg = 1
one object w two source roles
3 distinct IDs
1
x
u
w
v
u
w
v
u
w
v
d =
2
3
4
5
d =
2
3
4
5
d =
2
3
4
5
GEOGRAPHY
A(su, z)
Gap ≤ half the distance from u?
Read surviving radii near far
1
gap
d/2
row(u)
p
f far
V
X
prune
Z
F(z)
1.5
w
y
p
near
w
v
y
keep
d = 2
d = 4
d = 5
Su
one coordinate
2
one w y before p because 4 < 5
vector source
fiber F(z)
both
X pruned
not stored
radius = d(xu,

**Figure 3: Dual-source row assembly in REACH (Algorithm 1) on vector-distance shells** \(d=d(x_u,\cdot)\in\{2,3,4,5\}\)**. (_a) Two sources, same IDs_: Stage 1 selects** _P_=\[_w,p_\] (_B<sub>v</sub>_=2; **pool misses** _y_**), while Stage 2 reaches nearest fiber** _F(z_)={_w,v,y_}**. _(b) Reuse w to prune v_**: Inside** _F(z_) (**\(\alpha=2\)**), w **prunes** _v_ (**gap** \(=1\le 1.5=d/2\)**) while** _y_ **survives (gap** ≈4.47_\>_2=_d/2)**. _(c) Keep once, sort by d_**: Reusing** \(w\in P\) **takes no extra slot while** _y_ **takes** _B<sub>g</sub>_=1; **reading surviving radii near-to-far yields** row(_u_)=\[_w,y,p_\]**.

