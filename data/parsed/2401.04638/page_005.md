<tbc>that our deterministic rounding-up method can achieve a 2- approximation ratio within \(O\left(n^2\right)\). The exact runtime of the algorithm depends on the specific LP formulation and LP solver, but is polynomial.

We will now extend the above method to obtain an approximation result for the MCRN problem of \(\tau=\text{US}\).

**Theorem 2.** _If the min-congestion multi-commodity unsplittable flow problem has a_ \(\rho\)_-approximation algorithm based on rounding techniques on its LP solution, e.g.,_ \(\rho=O\left(logm/loglogm\right)\) _\[32\], then the MCRN problem with_ \(\tau=\text{\textit{US can be approximated by}}2\rho\).

_Proof:_ First, we note that the ILP formulation in §III-A1 also works for \(\tau=\text{US}\). Let \(\lambda_\text{opt}\) be the optimal value of the above relaxed LP for \(\tau=\text{SS}\), which is obviously a lower bound for the MRCP problem with \(\tau=\text{US}\).

For the MCRN problem of \(\tau=\text{US}\), we first solve it by assuming \(\tau=\text{SS}\) as Theorem 1 to obtain a matching _M_. For each \(\left\{i,j\right\}\in M\), we set _d<sub>i,j</sub>_=0 and _d<sub>j,i</sub>_=0 in _D_ to obtain a new set of demands \(D'\). By replacing _D_ by \(D'\) into the ILP formulation in §III-A1, we can obtain a new relaxed LP formulation \(LP\left(D'\right)\), which has an optimal congestion \(\lambda\). Clearly, it has \(\lambda\le 2\cdot\lambda_\text{opt}\) by Theorem 1. Given \(D'\), we can solve the min-congestion multi-commodity unsplittable flow problem on a static network (_V,E_) to obtain a \(\rho\)-approximation congestion \(\lambda'\) by applying rounding techniques on the splittable (optimal) flow of \(LP\left(D'\right)\), which further implies \(\lambda'\le\rho\cdot\lambda\le 2\rho\cdot\lambda_\text{opt}\). Thus, \(\lambda'\) is a \(2\rho\)-approximation result for \(\tau=\text{US}\).

## B. Polynomial-Time Solvable Cases

After obtaining approximation results for general cases of segregated model, we will show a restricted case, where demands contain a single source (resp., dest.), is efficiently solvable in Theorem 3. The proof of Theorem 3 is easy as only one reconfigurable link can be used here under segregated model, which is deferred due to limited space.

**Theorem 3.** _When_ \(\tau=\text{\textit{SS}}\)_, if the demands D have a single source (resp., dest.), the MCRN problem is polynomial-time solvable._

## C. Approximation Lower Bounds for Segregated Routing Model

In the following, we show that the problem under the splittable and segregated routing is APX-complete, implying that our 2-approximation algorithm achieves a tight bound.

**Theorem 4.** _For_ \(\tau=\text{\textit{SS}}\)_, the min-congestion reconfigurable network problem (MCRN) is APX-complete, even if the demands D are uniform in size and the graph G<sub>D</sub> induced by D is acyclic and bipartite, e.g., a 3D matching._

_Proof:_ Let \(\Pi^\text{con}\) denote the min-congestion reconfigurable network problem (MCRN) of \(\tau=\text{SS}\), where the induced graph _G<sub>D</sub>_ by demands _D_ is acyclic and bipartite, and \(\forall d_{i,j}\in D:d_{i,j}\in\left\{3,0\right\}^2\). We note that the minimum vertex cover<tbc>

<tbc>problem on 3-regular graph \(\Pi\) is APX-complete, which cannot be approximated better than a ratio \(\rho\in\left(1,2\right)\) \[33\]. To show APX-hardness of \(\Pi^\text{con}\), we give a gap-preserving reduction from the minimum vertex cover problem on 3-regular graph to reveal that \(\Pi^\text{con}\) cannot be approximated better than a factor \(min\{\rho,1.2\}\). The construction is illustrated in Fig. 1.

Given an instance _I_=(_G<sub>U</sub>_=(_U,E<sub>U</sub>_)) of the minimum vertex cover problem \(\Pi\), where _G<sub>U</sub>_ is a 3-regular graph with |_U_|=_n_, we construct an instance \(I'\) of \(\Pi^\text{con}\), as shown in Figure 1. Let the constructed instance be \(I'=(G,\mathcal{E},c,D)\), where a static network _G_=(_V,E_), a set of reconfigurable links E, the capacity function \(c:\vec{E}\cup\vec{\mathcal{E}}\mapsto\left\{1,3\right\}\) (each bi- directed link has the same capacities on both directions), and demands _D_. We construct nodes _V_ as follows:

\(\bullet\) For each vertex \(u_i\in U\) of _I_, where \(i\in\left\{1,\dots,n\right\}\), we construct three nodes: \(v_i\in V_1\), \(a_i\in A\) and \(b_i\in B\);<tbc>

\(\bullet\) For each edge \(\left\{u_i,u_j\right\}\in E_U\), we construct 2 nodes: \(v_{ij}\in V_2\) and \(v'_{ij}\in V_2\);<tbc>

\(\bullet\) Moreover, we have additional two nodes {_a,o_}.<tbc>

\(\bullet\) Finally, let constructed nodes be

\(V=A\cup B\cup V_1\cup V_2\cup\left\{a,o\right\}.\)

All static links (edges) _E_ will be constructed as follows, where their capacities are defined by \(c:\vec{E}\mapsto\left\{1,3\right\}\):

\(\bullet\) For each edge \(\left\{u_i,u_j\right\}\in E_U\) of _I_, where \(i,j\in\left\{1,\dots,n\right\}\) and \(i\neq j\), we construct the following static (bi-directed) links: \(\left\{v_i,v_{ij}\right\}\in E_1\), \(\left\{v_{ij},v_j\right\}\in E_1\), \(\left\{v_{ji},v'_{ij}\right\}\in E_2\), \(\left\{v'_{ij},b_j\right\}\in E_3\) and \(\left\{v'_{ij}b_i\right\}\in E_3\)<tbc>

\(\bullet\) For each \(u_i\in U\) of _I_, there are two static bi-directed links: \(\left\{a_i,a\right\}\in E_A\) and \(\left\{v_i,o\right\}\in E_o\).

<sup>2</sup> To have integer capacities, in this proof, we use a matrix of entries in {0,3}, which can be transferred to a 0/1 matrix by scaling down each capacity by a factor 3.

a1
v1
b1
5
1
a1
v1i
v1i
3
3
3
a
0
b1
a2
1
vi
3
v' ni
v2i
1
1
v2i
bn
vni
b2
an
vn
v2
3

Fig. 1. Illustration of our gap-preserving reduction from the minimum vertex cover problem to the MCRN problem with \(\tau=\text{SS}\). Each green node _v_<sub>1</sub>_,v_<sub>2</sub>_,v<sub>i</sub>,...,v<sub>n</sub>_ corresponds to one vertex in the given minimum vertex cover instance. The dashed lines show a subset of reconfigurable links E, whose two endpoints have non-zero demands in _D_, and solid lines indicate static links _E_, where there are _k_ parallel paths between _a_ and _o_ in the static network. Each bi-directed link in \(\mathcal{E}\cup E\) has the same capacity in both directions, and we define capacities: \(c:\vec{\mathcal{E}}\mapsto\left\{3\right\}\) and \(c:\vec{E}\mapsto\left\{1,3\right\}\). The capacity value is marked on each bi-directed (static) link in the figure.

