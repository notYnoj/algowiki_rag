<tbc>dom 3-regular graphs with 10<sup>6</sup> vertices, we numerically found that VIRAL cuts more edges than the QAOA at every depth \(p\ge 4\) and its expected cut fraction extrapolates to 0.9231(5) for \(p\rightarrow\infty\), very close to the upper bound in Eq. (2) \[15\]. That benchmark, however, compares VIRAL on finite random graphs against the QAOA on the tree, and establishes no bound. Indeed, a random 3-regular graph has short cycles, which at _N_=10<sup>6</sup> enter the radius-_p_ neighborhood of a typical edge already for \(p\unknown 9\), so a cut fraction measured there is not a bound on _M<sub>g</sub>_.

Here we evaluate VIRAL on the tree itself, which makes the comparison with the QAOA well defined and turns its cut fractions into bounds on _M<sub>g</sub>_. We estimate the expected cut fraction on the depth-_p_ tree by sampling the seeds, with 10<sup>7</sup> samples for every even \(p\le 32\). The deepest computation involves \(4\cdot 2^{32}\approx 1.7\times 10^{10}\) vertices per sample. The resulting lower bounds on _M<sub>g</sub>_ are reported in  I and plotted in Fig. 2. They exceed the QAOA bounds and those of Ref. \[8\] at equal depth for every \(p\ge 4\), and they extend the range of girths covered from _g_=36 to _g_=66. At _g_=66 the estimate _c_<sub>VIRAL</sub>(32)=0.913183(89) lies 13 standard errors above the asymptotic record in Eq. (2), and the rigorous bound is \(M_{66}\ge 0.91271\) at 99.9999% confidence level.

_Setup_ - VIRAL assigns to every vertex _i_ a classical spin, i.e., a unit vector \(\mathbf{s}_i=(s_i^x,s_i^y,s_i^z)\in S^2\), and updates<tbc>

<tbc>all spins synchronously for _p_ layers as

\(\mathbf{s}_i(n+1)=R_x(\beta_n)R_z\big(\gamma_nh_i(n)\big)\mathbf{s}_i(n),n=0,\dots,p-1,h_i(n)=\sum_{j\in\partial i}s_j^z(n),\text{(3)}\)

where \(\partial i\) is the set of neighbors of _i_, \(R_z(\theta)\) and \(R_x(\theta)\) are rotations by angle \(\theta\) about the _z_ and _x_ axes, and \(\beta_n,\gamma_n\) are fixed real parameters \[15\]. The initial condition is<tbc>

\(\mathbf{s}_i(0)=\big(\mathrm{cos}\alpha,0,\epsilon_i\mathrm{sin}\alpha\big),\) (4)

<tbc>with a fixed angle \(\alpha\) and independent fair random seeds \(\epsilon_i\in\{-1,+1\}\). After the last layer each spin is thresholded,

\(\sigma_i(p)=\mathrm{sign}(s_i^z(p)),\) (5)

and the cut is the set of edges with \(\sigma_u\neq\sigma_v\). The 2_p_+1 parameters \((\alpha,\beta_0,\dots,\beta_{p-1},\gamma_0,\dots,\gamma_{p-1})\) are trained once, as described below, and then frozen, so that the same parameters are used on every graph. The seeds are essential. On a regular graph, spins that start identical remain identical under Eq. (3), because every vertex sees the same field, _h<sub>i</sub>=h_ for every _i_, and no edge would ever be cut. The seeds break this symmetry and are the only source of randomness in the algorithm. The initial condition in, given by expression (4), has a semiclassical origin. In the truncated Wigner approximation of the QAOA, the unitaries become the classical rotations of Eq. (3) and the initial state \(|+\rangle\) becomes a set of classical spins with (Gaussian) random transverse components, whose width plays the role of \(\hbar\) \[16\]. The seeds \(\epsilon_i\) are the minimal form of this noise: the transverse component has fixed amplitude \(\mathrm{sin}\alpha\) and only its sign is random. In Ref. \[16\] we found that the semiclassical dynamics with a tuned noise level reaches lower energies than the exact QAOA at every depth, and that replacing the Gaussian noise by the seeds and reoptimizing \(\alpha\) together with the angles, which is VIRAL, improves the convergence of the energy to the ground-state value from log(_p)/p_ to 1_/p_. The optimal noise level found there vanishes as \(p\rightarrow\infty\). In accordance, the trained amplitude for MaxCut also decreases with depth, from \(\alpha=0.46\) at _p_=2 to \(\alpha=0.018\) at _p_=32.

Next we show that VIRAL is local, in the sense that whether an edge is cut depends only on a bounded portion of the graph around it. The graph enters Eq. (3) only through the neighbor sets \(\partial i\). Consider the graph of Fig. 1 with _p_=2 and let us trace the computation of \(\sigma_u=\mathrm{sign}(s_u^z(2))\) backwards, as in Fig. 3. By Eq. (3), **s**_<sub>u</sub>_(2) is computed from **s**_<sub>u</sub>_(1) and from the field \(h_u(1)=s_v^z(1)+s_{a_1}^z(1)+s_{a_2}^z(1)\), so it needs the spins at time 1 of _u_ and of its three neighbors, and the only edges involved are the three edges incident to _u_. Each of these four spins at time 1 is in turn computed from the seed of its own vertex and from the seeds of the three neighbors of that vertex. Hence **s**_<sub>u</sub>_(2) is a function of the seeds of the ten vertices within distance 2 of _u_, and the<tbc>

upper bound 0.92386 previous record 0.912
0.90
0.85
0.912
cut fraction
0.910
VIRAL (this work) QAOA
0.80
TPM
L
0.905
20
24
28
32
0.75
0
10
20
30
depth p

FIG. 2. **Cut fraction versus depth on** 3**-regular graphs of girth** \(g\ge 2p+2\). Tree values _c_<sub>VIRAL</sub>(_p_) of  I (circles), QAOA values of Ref. \[4\] (squares) and explicit vector algorithm (TPM) of Ref. \[8\] (triangles). Statistical errors are smaller than the symbols. The dashed line is the upper bound 0.92386 of Eq. (2), the dotted line the previous asymptotic lower bound 0.912. Inset: \(p\ge 20\), with the lower confidence bound _L_ of  I (open circles), which crosses 0.912 at _p_=32. Lines are guides to the eye.

