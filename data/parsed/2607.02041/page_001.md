# NLF: A RESISTOR-NETWORK FRAMEWORK AND LINEAR-TIME SOLVER FOR CONVEX NETWORK-FLOW EQUILIBRIA<sup>∗</sup>

**Abstract.** We present **NLF** (Nonlinear Laplacian Flow), a unified framework and linear-time solver for convex network-flow equilibria. Congestion (traffic) routing, minimum-delay communication routing, and maximum flow--each the stationarity of a convex, edge-separable energy--share one form: the _nonlinear graph Laplacian_ \(B\rho(B^\top\phi)=\alpha d\), where a monotone edge law \(\rho_e\) encodes the physics (undirected graphs; directed variants are future work). NLF solves it by an inexact damped chord-Newton iteration whose frozen global linearization--a weighted graph Laplacian--is inverted by a lazily refreshed near-linear Laplacian solver (engine-agnostic; default: approximate Cholesky, LAMG+ interchangeable). The whole nonlinear solve costs 2-4 linear Laplacian solves, so a near- linear inner solve makes the wall-clock empirically O(_m_) in the edge count _m_ (not a proved bound). On single-commodity congestion over real road-network topologies (BPR cost), NLF converges for all 2,003 SuiteSparse corpus graphs up to \(1.8\times 10^7\) edges and on three larger graphs up to \(5.6\times 10^7\) edges. Against a state-of-the-art interior-point method (IPM), NLF was a median \(2.6\times\) faster where both converge and \(>45\times\) on the poorly-separable graphs where the IPM’s direct KKT core is super- linear; against matrix-free L-BFGS, a median \(4.2\times\) faster and the only solver to finish--within a \(5\times\) wall-clock budget--on the 90 hardest instances. A multicommodity extension routes _K_ commodities through one shared hierarchy at O(_Km_) per step; on real capacity data, congestion inflates shared- corridor costs (up to \(8.8\times\)) without rerouting. The same machinery recovers the exact combinatorial max-flow as a short sequence of Laplacian solves, with the cut potential as a by-product.  and benchmarks: https://github.com/orenlivne/nlf.

**Key words.** network equilibrium, traffic assignment, maximum flow, algebraic multigrid, nonlinear multigrid, inexact Newton methods, continuation, graph Laplacian

**AMS subject classifications.** 90B20, 90C35, 65F10, 65N55, 90B10, 05C21

**1. Introduction.** Flows on networks at equilibrium are everywhere: drivers distributing over a road map until no route is faster (traffic assignment [9, 10, 11]), packets routed to minimize delay in a communication network [15, 16], current in a resistor network [26], and--at the combinatorial extreme--the maximum flow through a capacitated graph [17, 18, 20]. These look like different problems with different algorithms: traffic assignment is solved by Frank-Wolfe or general convex optimization, max-flow by augmenting-path or push-relabel combinatorics. We make a unifying observation and build a single fast solver on it.

_The observation._ Each of these is the stationary point of a convex, edge-separable energy in the node potentials, and its Euler equation is one and the same _nonlinear graph Laplacian_,

(1.1) \(B\rho(B^\top\phi)=\alpha d,\)

where _B_ is the node-edge incidence matrix, \(\phi\) the node potentials, _d_ a source/sink demand, \(\alpha\) a load, and \(\rho_e\) a monotone edge law that alone encodes the physics: a saturating \(\rho_e\) gives a hard capacity (max flow); a gently rising \(\rho_e\) gives a congestion cost (traffic)<sup>1</sup>. The flow is \(f_e=\rho_e\big((B^\top\phi)_e\big)\), and every Newton linearization of (1.1) is an ordinary weighted graph Laplacian \(J=B\mathrm{diag}(\rho')B^\top\). For congestion and routing problems \(\alpha\) is a given input; for maximum flow, \(\alpha\) is an unknown to be maximized.

<sup>∗</sup>Submitted to the editors July 3, 2026. <sup>†</sup>Pine Birch Analytics, 35 Kelinger Rd, Churchville, PA 18966-1033 (`oren.livne@gmail.com`, tel. 312-533-9130, `pinebirchanalytics.com`; ORCID: 0000-0001-6700-483X). <sup>1</sup>Notation: \(\rho\) acts componentwise and \(\rho_e\) denotes the law on an individual edge _e_.

arXiv:2607.02041v1 [math.NA] 2 Jul 2026

OREN E. LIVNE<sup>†</sup>

