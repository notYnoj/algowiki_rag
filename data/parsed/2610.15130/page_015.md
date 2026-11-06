# Supplementary Material for "Recall-Bounded Staleness for Filtered Multi-Tenant ANN Graph Indexes under Concurrent Updates"

This document supplements the main manuscript. It contains the full proofs (Appendix I), three supporting tables, external comparisons, and three supporting figures. Numbering of results, sections, and tables referenced below (e.g. Theorem 3, Lemma 7, § V-C) is that of the main paper.

### I. PROOFS

#### A. Proof of the toy bound (Theorem 3)

The load-bearing object is the per-merge degradation _g(c,N_) (Assumption 2); the horizon bound then assembles _M_ merges and concentrates. We couple the merged graph \(G_\mathrm{merge}^{(c)}\) against the from-scratch \(\alpha\)-RNG-optimal graph on the same final point set.

#### _(S1-S3) Topology divergence._

By Definition 1 the _c_ batch points are mutually invisible, so every intra-batch shortcut a from-scratch build would create is missing. The count of such missing edges is

\(E_\mathrm{miss}=\Theta\big(\mathrm{min}(c^2/N,Rc)\big),\) (1)

the _R_-cap on out-degree squeezing the naive _c_<sup>2</sup>_/N_ below the linear ceiling _Rc_ (measured _R_-cap fill \(15\%\rightarrow 50\%\) over the _c_-sweep; fixed-_N_ exponent \(\theta=1.46\), 95% CI \[1.33,1.59\] over _n_=5 values of _c_). The fill measurement fixes the form, placing the exponent strictly between the unconstrained _c_<sup>2</sup> and the saturated _Rc_ and making the fitted slope range-dependent (1.34 over \(c\in[5,20]\)K, 1.46 over \(c\in[5,80]\)K) rather than a universal constant. The hub re-prune (M2) contributes a subdominant, budget-soft _V_<sub>0</sub> floor _g_<sub>0</sub>(_L_).

#### _(S4) Divergence_ \(\rightarrow\) _recall._

The topology divergence lifts to recall@_k_ loss near-linearly (\(\psi\approx 1\)) below the batch- fraction ceiling _c/(N+c_). Three independent measurements agree on the exponent. Edge counting gives \(\theta\)=1.46; a three-replicate streaming recall sweep gives \(\gamma=1.46\pm 0.14\); a \(\mu\)-matched three-base recall fit gives \(a_\mathrm{recall}=1.45\) with _b_<sub>recall</sub>=0.64 against the topology \(b=0.50\pm 0.04\). The \(\pm 10-15\%\) spread across methods fixes \(\psi\approx 1\) as near-linear lift with no amplifying power. Matching \(\mu=kc/N\) across bases aligns the transfer, leaving a mild 0.50 vs. 0.64 residual between the topology and recall exponents.

#### _(S5) Horizon assembly._

Summing _g(c,N<sub>m</sub>_) over the \(M=\lceil\lambda_\mathrm{ins}T/c\rceil\) merges with growing _N<sub>m</sub>_ gives

\(L^*(c,T)=\Theta\big(\lambda_\mathrm{ins}Tc^{a-1}N_0^{-b}\big),\) (2)

which increases in _c_ because _a_-1_\>_0, the anti-amortization direction. A direct partition-counting argument, with total missing intra-batch edges \(\Theta(\lambda_\mathrm{ins}Tkc/N)\propto c\), re-derives this direction independently of the coupling. The merges are combined by a union bound over miss events, giving

\(L^*\le\sum_mg(c,N_m),\) (3)

the upper bound Theorem 8 uses. Reconcile only unions buffered reverse edges and re-prunes, so it leaves earlier missing intra-batch edges in place and the per-merge terms accumulate. Loss components share capacity across merges, which makes the additive sum (3) conservative. Over twelve merges (§ V-B) the realized cumulative loss is 0.37-0.44 of the additive prediction, and the _c_-independent _V_<sub>0</sub> floor decays with merge index. This saturation of the _c_-independent floor removes the \(Mg_0\propto 1/c\) term, so it eliminates rather than creates an amortization regime.

#### _(S6) Concentration._

The degree cap gives bounded per- insert influence _O(R_<sup>2</sup>). McDiarmid on the divergence and Bernstein on the sparse, bounded (\(X_q\in[0,1]\)) query-recall average, union-bounded over the _M_ merge checkpoints, yield

\(L^*\le\mathbb{E}[L^*]+O\big(R^2\sqrt{\lambda_\mathrm{ins}T\mathrm{ln}(M/\delta)}\big)=\mathbb{E}[L^*](1+o(1))\) (4)

with probability \(\ge 1-\delta\). The exponents \(\theta\) and _b_ are calibrated on this substrate (Remark 9), and the direction and functional form follow from the argument above and its measurements.

#### B. Proof of the frontier-mass lemma (Lemma 7)

#### _(S0) The recall identity._

By Assumption 4 the post-filter receives a distance-ordered list of \(\beta L\) candidates with in- predicate count _X<sub>q</sub>_. Suppose first the list is the _true_ metric top- \(\beta L\). Its in-predicate members are then exactly the _X<sub>q</sub>_ nearest in-predicate points of the whole dataset, since any nearer in- predicate point would itself lie in the top-\(\beta L\). The per-label ground truth is the _k_ nearest in-predicate points, so the retained top-min(_X<sub>q</sub>,k_) of the filtered list is a prefix of the ground- truth list, giving recall=min(_X<sub>q</sub>,k)/k_ as an exact equality rather than a bound. This is the quantity the measurement of § V-C computes, taking the post-filter top-_k_ and scoring against per-label brute-force ground truth. For an approximate search the list is not the true top-\(\beta L\); write \(\delta_\mathrm{ann}(L)\) for the expected fraction of a query’s in-predicate ground-truth points

Namrata Das, Kailas Devadkar, Anand Godbole<br> Sardar Patel Institute of Technology, Mumbai, India

