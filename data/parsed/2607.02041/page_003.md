<tbc>no-fold instance and the setting of our sharpest result (§4). The incumbent solvers are Frank-Wolfe and bush-based methods (§4.2).

_Communication and data-center routing._ Routing packets to minimize end-to- end delay under the Kleinrock _M/M/_1 model \[15, 16\] is the same equilibrium with a capacity-saturating delay law--a fold instance handled by the continuation of §3.3.

_Maximum flow (logistics, scheduling, vision)._ The capacitated maximum-flow problem \[17, 18\] is the saturating-law extreme of the same energy (§5). NLF recovers the exact value together with the min cut and the full flow-vs-load curve. Combinatorial solvers are faster to obtain the maximum flow value, but do not return the smooth interior flow or the parametric curve that an outer optimizer manipulates when max flow is an inner step.

_Nonlinear resistor and analog-circuit networks._ The most literal instance: monotone two-terminal devices (diodes, varistors, memristors) in DC steady state give (1.1) with \(\rho_e\) the device _I-V_ law--the form of DC circuit analysis and in-memory- computing crossbars. As with OPF (§7.5) these topologies are typically structured, where direct solvers are efficient; NLF would have an edge only for large, irregular analog networks.

Across all applications, in addition to a scalar optimum (e.g., the maximum flow value) the equilibrium (flow), its binding-constraint structure (min cut), and its sensitivity to load are also required for design optimization, which is the gap NLF targets.

**1.3. Prior work, and how NLF differs.** Three lines of work meet at (1.1); NLF sits in the gap none of them fills.

_The Laplacian paradigm for flow._ Electrical-flow algorithms \[23\] and IPM for generalized flow \[24\] solve a sequence of linear weighted-Laplacian systems inside an outer multiplicative-weights or barrier loop, reaching an \((1+\epsilon)\)-approximate optimum; the flow is a linear function of the potential and all nonlinearity lives in the outer schedule. NLF instead places the nonlinearity in the constitutive law \(f=\rho(B^\top\phi)\), so a single energy encodes the capacity and the equilibrium reached is exact (§2).

_Fast linear Laplacian solvers._ Nearly-linear solvers for _Lx=b_ such as combinatorial multigrid \[6\], support-tree/Spielman-Teng theory \[5\], approximate Cholesky \[25, 36\], and algebraic multigrid including LAMG \[1\] address the linear, unconstrained problem only. They are the engine, not the method: NLF calls a robust O(_m_) Laplacian solver as its inner kernel but adds the nonlinear, capacity-constrained equilibrium layer on top. AMG has also been applied to the complex-valued non-separable AC power-flow equations \[7\]--a nonlinear system with no objective and a non-Laplacian Jacobian, solved by nonlinear FAS multigrid with a multiplicative coarse correction (no Newton, no fold); a different problem class from the real, edge-separable, SPD- Laplacian constrained flow program here.

_Multilevel optimization._ NLF is not multilevel optimization in the MG/OPT sense \[29, 30, 31\]: it does not build coarse optimization models or recurse the objective. While the equilibrium is nonlinear equation (1.1), NLF employs a near-linear inner solve only as the linear inner solve inside a frozen-linearization chord-Newton continuation; the nonlinearity is carried by the edge law and the outer continuation, not by a coarse-grid objective. However, Sec. 7.5 outlines how NLF might be extended to a multilevel optimization paradigm when a cost functional is added.

_Combinatorial and transport-specific solvers._ Augmenting-path and push-relabel max-flow \[18, 21\] and the almost-linear-time exact algorithm \[20\]--a theoretical breakthrough with galactic constants, not a practical implementation--target directed max/min-cost flow; Frank-Wolfe \[13\] and bush-based assignment (Algorithm B \[38\],<tbc>

