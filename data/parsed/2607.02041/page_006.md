<tbc>max-flow, and placing max-flow, congestion, and minimum-delay routing under one nonlinear Laplacian solved via existing linear Laplacian algorithms.

**3. The NLF algorithm.** The two problem classes need different outer loops. For congestion (no fold), \(\alpha\) is a given input, so (1.1) is solved _directly_ at that load by a handful of inexact chord-Newton steps (Algorithm 3.1), warm-started from \(\phi=0\); no load ramp is needed--a single fixed-load solve converges across the corpus (§4.5). For max-flow (fold), \(\alpha\) is the unknown maximizer, and continuation from \(\alpha=0\) in pseudo- arclength parametrization tracks the solution curve through the fold to _F_<sup>∗</sup>, each fixed-\((\phi,\alpha)\) subproblem again a handful of chord-Newton steps. The inner solver’s setup--its factor or hierarchy--is built once, frozen across steps and re-formed only when an observed-convergence monitor signals it has drifted too far. The numbers of

(A1) max-flow: saturating law, p' - 0 at the cut
(B1) max-flow: the cut is the saturated edge set
min cut = active set
1.5
saturated: p'-0, f+Ce
1.0
+
0.5
S
t
0.0
-0.5
f= Po(g) (flow)
-1.0
p'e (conductance)
saturated edges carry full flow fe = Ca (p'-0); all s-t flow crosses the cut
-4
-3
-2
-1
0
1
2
3
4
g = (B T Φ)e
(A2) min-delay (Kleinrock 1/(ce-f): saturates at capacity
(B2) min-delay: Abilene backbone, computed NLF equilibrium
1.4
SEAS
1.2
CHI
1.0
DEN
KC
ND
NYCT
0.8
SWK
NAS
0.6
LA
0.4
ATL
0.2
f= Po(g) (flow)
HOU
p'e (conductance)
0.0
(g) (scaled)
2
4
6
8
10
12
0.0
0.2
0.4
0.6
0.8
1.0
g = (B T Φ)e
link utilization f/Ce (delay = 1/(ce-f))
(A3) congestion (BPR): no cap, conductance bounded > no fold
(B3) congestion: Sioux Falls, computed NLF equilibrium
f= Po(g) (unbounded)
2.0
p'e E (0, p'max)
W(g) (scaled)
1.5
1.0
S
0.5
0.0
0
1
2
3
4
5
0.00
0.25
0.50
0.75
1.00
1.25
g = (B T Φ)e
equilibrium utilization
fel/ce

Fig. 2.1. _The three instances of the framework (one row per line of  2.1); column (A) the edge law_ \(\rho_e\) _(flow), its derivative_ \(\rho'_e\) _(the solution-dependent conductance) and the energy_ \(\Psi_e\)_; column (B) the behavior it induces._ Row 1, max-flow (tanh): _the law saturates at_ \(\pm c_e\) _and_ \(\rho'_e\rightarrow 0\)_; (B1) the saturated edges are the min cut = the active set, and_ \(\phi\) _steps across them._ Row 2, minimum-delay routing (Kleinrock 1/(_c<sub>e</sub>-f_)): _the law saturates at capacity--the fold class, handled by the continuation of §3.3; (B2) the real application: the Abilene/Internet2 backbone colored by the_ computed _NLF min-delay equilibrium for a Seattle_\(\rightarrow\)_New York demand._ Row 3, congestion (BPR): _the law is unbounded and_ \(\rho'_e\) _is bounded away from zero--no fold, pure cycling; (B3) the real application: the Sioux Falls road network colored by the_ computed _NLF equilibrium utilization_ |_f<sub>e</sub>|/c<sub>e</sub> for a single source-sink demand (§4)._

