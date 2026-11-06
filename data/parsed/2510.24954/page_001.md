Reviving Thorup’s Shortcut Conjecture

**Abstract**

We aim to revive Thorup’s conjecture [Tho92] on the existence of _reachability shortcuts_ with ideal size-diameter tradeoffs. Thorup originally asked whether, given any graph _G_=(_V,E_) with _m_ edges, we can add _m_<sup>1+_o_(1)</sup> “shortcut” edges _E_<sub>+</sub> from the transitive closure _E_<sup>∗</sup> of _G_ so that \(dist_{G_+}(u,v)\le m^{o(1)}\) for all \((u,v)\in E^*\), where \(G_+=(V,E\cup E_+)\). The conjecture was refuted by Hesse [Hes03], followed by significant efforts in the last few years to optimize the lower bounds [HP21, LVWX22, BH23a, VXX24, HXX25].

In this paper, we observe that although Hesse refuted the _letter_ of Thorup’s conjecture, his work [Hes03]--and all followup work [HP21, LVWX22, BH23a, VXX24, HXX25]--does not refute the _spirit_ of the conjecture, which should allow _G_<sub>+</sub> to contain both new shortcut edges and _new Steiner vertices_. Our results are as follows.

\(\bullet\) On the positive side, we present explicit attacks that break all known shortcut lower bounds [Hes03, HP21, LVWX22, BH23a, VXX24, HXX25] when Steiner vertices are allowed.

\(\bullet\) On the negative side, we rule out ideal _m_<sup>1+_o_(1)</sup>-size, _m_<sup>_o_(1)</sup>-diameter shortcuts whose “thickness” is _t=o_(log_n/_loglog_n_), meaning no path can contain _t_ consecutive Steiner vertices.

\(\bullet\) We propose a candidate hard instance as the next step toward resolving the revised version of Thorup’s conjecture.

Finally, we show promising implications. Almost-optimal parallel algorithms for computing a generalization of the shortcut that _approximately_ preserves distances or flows imply almost- optimal parallel algorithms with _m_<sup>_o_(1)</sup> depth for _exact_ shortcut paths and _exact_ maximum flow. The state-of-the-art algorithms have much worse depth of _n_<sup>1/2+_o_(1)</sup> [RHM<sup>+</sup>23a] and _m_<sup>1+_o_(1)</sup> [CKL<sup>+</sup>22], respectively.

<sup>∗</sup>New York University <sup>†</sup>Carnegie Mellon University <sup>‡</sup>ETH Zürich \(^\mathsection\)INSAIT, Sofia University "St. Kliment Ohridski" and ETH Zürich \(^\unknown\)University of Michigan \(^\unknown\)MPI-INF and Saarland University \(^\unknown\)**Hasso Plattner Institute, University of Potsdam**

Aaron Bernstein<sup>∗</sup> Henry Fleischmann<sup>†</sup> Maximilian Probst Gutenberg<sup>‡</sup> Bernhard Haeupler<sup>§</sup> Gary Hoppenworth\(^\unknown\) Yonggang Jiang\(^\unknown\) George Z. Li<sup>†</sup> Seth Pettie\(^\unknown\) Thatchaphol Saranurak\(^\unknown\) Leon Schiller**

