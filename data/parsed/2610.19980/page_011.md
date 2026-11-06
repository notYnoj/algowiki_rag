<tbc>astronomically unlikely to arise. This is where a human enters the loop, not to hand-build the final construction but to change what the search samples. For unit- square stabbing the vehicle is a _staircase_ construction: squares are never sampled independently but generated as products \(I\times J\) of intervals from a one-dimensional family, which forces exactly the shared-line incidences that make stabbing hard, and the local moves become scans over the interval starts, the common length, the level count and assignments, the support points, and shifted staircase variants, in place of coordinate jitter on squares. A line-stabbing lower bound then follows from a proof template on the one-dimensional part, as we now describe.

**The staircase formulation.** _One-dimensional interval layer._ The construction begins with a finite ordered set of rational support points \(P=\{p_1<p_2<\cdots<p_m\}\subset\mathbb{Q}\) and a rational probability measure \(\mu:P\rightarrow\mathbb{Q}_{\ge 0}\) with \(\sum_{p\in P}\mu(p)=1\). A candidate specifies a common interval length _L_ and a finite family of intervals \(\mathcal{I}=\mathcal{I}_0\sqcup\mathcal{I}_1\sqcup\cdots\sqcup\mathcal{I}_{q-1}\) partitioned into ordered _levels_; every interval has the same length _L_ after<tbc>

<tbc>scaling, and only the starting positions and level labels vary. For each level _r_ the verifier computes a certified lower bound

\(a_r\le min_{I\in\mathcal{I}_r}\mu(I\cap P),\)

the minimum one-dimensional measure captured by every interval in that level. The search variables are the interval starts, the level assignments, the common length, and the support weights that make these inequalities strong.

_Product lift to squares._ The two-dimensional family is formed by products: for \(I\in\mathcal{I}_r\) and \(J\in\mathcal{I}_s\) the square \(Q_{I,J}=I\times J\) is included whenever the level pair is admissible, that is, whenever \(a_r+a_s\ge 1\) for the relevant pairs (_r,s_) below the target threshold. Because _I_ and _J_ share the length _L_, each _Q<sub>I,J</sub>_ is an axis-parallel unit square after a uniform rescaling. A vertical line _x=t_ meets _Q<sub>I,J</sub>_ exactly when \(t\in I\), and a horizontal line _y=t_ exactly when \(t\in J\), so stabbing the squares reduces to hitting the interval family on each axis.

_Lower-bound certificate._ Fix a target integer _T_. For any split into _u_ vertical and _v_ horizontal lines with _u+v\<T_, the staircase levels are arranged so that the vertical lines miss some interval \(I\in\mathcal{I}_r\) and the horizontal lines miss some interval \(J\in\mathcal{I}_s\) with (_r,s_) admissible. The square _Q<sub>I,J</sub>_ is then present and unstabbed, so no set of fewer than _T_ lines can stab the whole family, which proves \(\tau(\mathcal{S})\ge T\). The fractional optimum \(\tau^*(\mathcal{S})\) is computed by the standard LP over the compressed critical-line universe, and the construction is tuned so that \(\tau(\mathcal{S})/\tau^*(\mathcal{S})=14/9\).

**Results.** Two observations follow. The first is negative and instructive: seeding the neutral search<tbc>

\begin{tabular}{ccc}
Configuration & Compact & Scaled \\
Coordinate mutation & 1.5000 & 1.5000 \\
Symmetry hill climb & 1.5000 & 1.4286 \\
Escape search & 1.4400 & 1.4118 \\
\end{tabular}

Unit Square: component-slice convergence around the best final configuration
Vary representation
Vary local search
Vary surrogate
local search-symmetry crossover hilclimb
representation-sqstab exact grid
representation-sqstab exact grid
local search-symmetry crossover hilclimb
surrogate-exact stab gap pressure
surrogate-exact stab gap pressure
1.590
1.590
1.603
1.456
1.456
1.436
Best exact score so far
1.322
1.322
1.269
1.188
1.188
1.102
1.053
1.053
0
1111
2222
3332
4443
0
2030
4059
6088
8118
0.935
0
787
1574
2360
3147
fixed symmetry grid
Cumulative transformer-training epochs
Cumulative transformer-training epochs
cord mutation
exact stab gap pressure
Cumulative transformer-training epochs
line square incidence
sqstab local hilclimb
square partial p bitset
sqstab exact grid
symmetry crossover hilclimb
incidence statistics

Figure 4: Component-slice convergence for unit-square stabbing. Each panel fixes two of the three components at their best-performing choice and varies the third, plotting the best exact integrality gap \(\tau/\tau^*\) found so far against cumulative transformer-training epochs. From left to right the panels vary the representation, the local-search operation, and the surrogate; the surrogate panel shows the strongest single-component separation in the study.

3: Best exact unit-square stabbing gap reached by the compact (244K-parameter) and scaled (1.82M- parameter) transformers on three representative configurations, under the same wall-clock budget.

