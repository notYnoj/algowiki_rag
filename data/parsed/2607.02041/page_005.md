<tbc>**2.2. The fold dichotomy.** The single feature that governs difficulty is whether the edge law _saturates_.  2.1 lists three standard instances.

\(\bullet\) _Soft congestion (rising_ \(\rho\)_, no saturation)._ The load \(\alpha\) is a given input. The cost rises with flow but imposes no hard cap, so \(\rho_e\) is unbounded and the law never _saturates_: \(\rho'_e>0\) at every finite flow (for BPR \(\rho'_e\) is large near free flow and decays as _f_ grows, but never reaches 0). Hence _J_ is nonsingular at every equilibrium--no feasibility limit and no fold. Traffic assignment with BPR cost is of this type; on its bounded-flow equilibria _J_ is well-conditioned, so (1.1) is solved directly at the target load, with no continuation (§4).<tbc>

\(\bullet\) _Hard capacity (saturating_ \(\rho\)_, conductance_ \(\rightarrow 0\)_)._ \(\alpha\) is an unknown to be maximized. The flow cannot exceed a capacity _c<sub>e</sub>_, so \(\rho_e\) is bounded and \(\rho'_e\rightarrow 0\) as the edge saturates. As \(\alpha\) rises to a feasibility limit, the saturating edges form a cut and _J folds_--a continuation limit point where \(\alpha\) caps at the min cut _F_<sup>∗</sup> and _J_ becomes singular. Maximum flow and minimum-delay communication routing (Kleinrock delay) are of this type; they require arclength continuation through the fold (§3.3).

**2.3. The max-flow law in detail.** For the saturating instance used in §5, take

(2.5) \(\rho_e(g)=\left\{\begin{array}{ c c }
c_e^+tanh(g/c_e^+), & g\ge 0, \\
-c_e^-tanh(g/c_e^-), & g<0,
\end{array}\right.\Psi_e(g)=c_e^2logcosh(g/c_e),\)

a soft-capacity barrier: \(\Psi_e(g)=\frac{1}{2}g^2\) for \(|g|\checkmark c_e\) (a unit resistor) and grows only linearly, \(\Psi_e\rightarrow c_e|g|\), for \(|g|\gg c_e\) (a saturated edge), so \(\rho_e=\Psi'_e\) clamps the flow smoothly to \(-c_e^-\le f_e\le c_e^+\). Here \(w_e=1-(f_e/c_e)^2\in[0,1]\) represents "edge openness," 1 for a slack edge and 0 for a saturated one, and **the forming min-cut is exactly the zero-conductance set**, which is why AMG aggregation driven by a relaxation-based strong-connection measure refuses to coarsen across it (§5). The congestion (BPR) law is given where it is used, in §4.

**2.4. Relation to prior Laplacian-paradigm formulations.** Solving flow through graph-Laplacian systems is the core of a productive line of work, but NLF’s mechanism is fundamentally different. Electrical-flow methods \[23\] and their _p_- Laplacian descendants compute a sequence of _linear_ electrical flows \(f=diag(w)B^\top\phi\) --each a fixed weighted-Laplacian solve--and steer an _outer_ multiplicative-weights loop to a \((1+\epsilon)\)-approximate max-flow; IPM for (generalized) flow \[24\] likewise wrap a Laplacian solve in a barrier path-following loop. NLF instead places the nonlinearity in a _constitutive law_: \(f=\rho(B^\top\phi)\) is a saturating function of the gradient, so the single energy of (1.1) encodes the capacity exactly and its feasibility limit is the exact min cut. The outer loop is then a short continuation through one scalar fold, not a reweighting or barrier schedule. The Beckmann congestion instance (2.3) is already known \[9\]; the novelty is the saturating-resistor reformulation of

\begin{tabular}{ccccc}
Problem & Marginal cost _t<sub>e</sub>(f_) & Conductance \(\rho'_e\) & Fold? & Application \\
maximum flow \[17, 19\] & box \(|f|\le c_e\) (soft barrier) & \(\rightarrow 0\) at cut & yes & vision, matching \\
min-delay routing \[15, 16\] & 1/(_c<sub>e</sub>-f_) (Kleinrock) & \(\rightarrow 0\) at \(f\rightarrow c_e\) & yes & communication \\
congestion \[9, 10, 11\] & \(t_e^0\big(1+b(f/c_e)^p\big)\) & _\>_0 (no satn.) & no & road traffic \\
\end{tabular}

2.1

_Three instances of the resistor-network framework_ (1.1)_. The edge law_ \(\rho_e\) _(flow vs. potential gradient) is the inverse of the marginal cost_ \(t_e=\Phi'_e\)_. "Fold" marks a feasibility limit where the conductance_ \(\rho'_e\rightarrow 0\) _and J becomes singular._

