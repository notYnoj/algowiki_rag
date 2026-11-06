<tbc>**Algorithm 3.2** NLF arclength continuation (max-flow fold).

**Require:** demand _d_; maximize \(\alpha\) to find \(F^*\triangleright\) congestion needs no continuation: Algorithm 3.1 at the target load

1: \(\phi\leftarrow 0\), \(H\leftarrow\emptyset\triangleright\) trivial solution at \(\alpha=0\)

2: _Seed a feasible load:_ \(\alpha_\mathrm{hi}\leftarrow\sum_{e\sim s}c_e\) (\(\ge F^*\), source-cut bound); set \(\alpha\leftarrow 0.1\alpha_\mathrm{hi}\) and halve until Algorithm 3.1 converges (so \(\alpha<F^*\))

3: _Bracket F_<sup>∗</sup>: try load \(g\alpha\) (_g_=1.7) with Algorithm 3.1; accept (\(\alpha\leftarrow g\alpha\)) while it converges, stop at the first failure (\(g\alpha\ge F^*\))

4: refresh _H_; tangent (\(\dot{\phi},\dot{\alpha}\)) by (3.1); initialize arc-step \(\Delta s\)

5: **while** \(|\dot{\alpha}|>\mathrm{tol}\) **do** \(\triangleright\dot{\alpha}\rightarrow 0\) marks the fold, \(\alpha\rightarrow F^*\)

6: _predictor:_ \((\phi,\alpha)+=\Delta s(\dot{\phi},\dot{\alpha})\); _corrector:_ iterate (3.3) with line search, _H_ lazily refreshed (Algorithm 3.1)

7: on success grow \(\Delta s\) and reorient the tangent (3.1); on a fresh-_H_ failure set \(\Delta s\leftarrow\Delta s/2\) and re-predict

8: **end while**

9: **return** \(\phi,F^*=\alpha\)

Fig. 3.1. _**(a)** The_ \(\alpha\)_-V fold (max-flow). As the load_ \(\alpha\) _is driven up, the source-sink gap_ \(V=|\phi_s-\phi_t|\) _grows;_ \(\alpha\) _rises, then folds onto the min-cut value F_<sup>∗</sup> _as the cut saturates_ (\(\rho'\rightarrow 0\)_, J singular) with_ \(V\sim-\mathrm{log}(F^*-\alpha)\)_. Stepping_ \(\alpha\) _crowds the fold; continuing in_ \(V\approx\psi\) _keeps steps uniform. Congestion laws have no such fold. **(b)** Pseudo-arclength predictor-corrector, drawn where_ \(\phi,\alpha\) _are both scalars so the equilibria form a plane curve_ \(\rho(\phi)=\alpha d\)_. From the previous solution the_ predictor _advances_ \(\Delta s\) _along the unit tangent_ (\(\dot{\phi},\dot{\alpha}\)) _to an off-curve point P_<sup>∗</sup>_; the_ corrector _drives the equilibrium residual r and the arclength residual N to zero through the bordered system_ (3.3)_. Its Newton step splits as_ \(\delta\phi=\delta\alpha u+w\) _(block elimination_ (3.4)_) with u=J_<sup>+</sup>_d along the tangent and w=J_<sup>+</sup>_r cancelling r; near the fold_ \(u\propto\chi/\lambda_\mathrm{min}\) _is large but is pinned by the scalar arclength row, so the inner solves stay well-conditioned._

_Scope: an undirected, single-commodity._ Throughout this section the congestion problem is the undirected, single-commodity Beckmann relaxation: flows are signed, the cost depends on |_f<sub>e</sub>_|, and Wardrop’s path-nonnegativity is dropped (App. A). Our experiments establish two claims: (i) this undirected congestion equilibrium is exactly (1.1) for the inverse-BPR law, and (ii) a robust O(_m_) linear graph Laplacian inner solve makes it linear-time. The real road networks supply real topologies, capacities, and BPR data exercised with a single source-sink demand; we cross-check NLF against an independent high-accuracy solver on the identical convex program.

## 4.1. The BPR congestion law.

On a congested road the travel time rises with the flow it carries. The field-standard model is the Bureau of Public Roads (BPR)

The a-V cusp: continuing in a folds at F* (why we continue in V=w)
F* (max flow)
6
F* = 5 RS (max flow = min-cut)
P*
5
w = J+r
(8Φ, 8a)
r
4
rises linearly (network un-saturated)
throughput a
fold / cusp: a-F*, da/dV=0 cut saturates (p=0), J singular,
3
V = log(F*-a)
0.7
As (Φ) corrected
0.6
bordered corrector
/8Φ = =
0.5
ΦΦ = -N
1
0.4
prev. solution
a-driven branch (the max-flow solution)
0
0
10
20
30
40
50
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
2.25
source-sink potential gap V= |Φ2 Φ1
potential Φ (cut amplitude μ = x
(a)

