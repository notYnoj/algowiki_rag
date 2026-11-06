<tbc>path tolerance. Each contribution is thus a bounded multiple of a single linear solve, so the total cost to accuracy \(\varepsilon\) is, empirically,

(4.2) \(\mathcal{O}\big(m\mathrm{log}(1/\varepsilon)\big).\)

The constant is the whole-nonlinear-solve-to-one-linear-solve ratio reported below (2- 4), and it stays bounded because the frozen chord-Newton contraction stays bounded away from 1: on the no-fold congestion class directly (§4), and through the fold because the continuation deflates the diverging cut direction and keeps the bordered corrector uniformly conditioned (§3.3); empirically the contraction does not degrade at _F_<sup>∗</sup>. We verify this by sweeping \(\varepsilon\) from 10<sup>-2</sup> to 10<sup>-12</sup> on one graph per class (web, social, road, finite-element): the total inner-solve count grows _linearly_ in \(\mathrm{log}(1/\varepsilon)\), at 0.24-0.60 per decade of accuracy, confirming (4.2).

_The nonlinear/linear cost ratio is_ O(1). Brandt’s yardstick says: solving the nonlinear problem should cost only a small, size-independent multiple of solving one linear problem of the same kind \[35, §8.3\]. We measure exactly this: the full congestion solve (load continuation, all steps, all cycles, lazy refresh) against a single inner setup- and-solve of the linearization at \(\alpha=0\) (the linear resistor network \(B\mathrm{diag}(\rho'(0))B^\top\phi=d\)) on the same graph. Across the classes the ratio is 1.9-4.4--grid 3.1, finite-element 2.5, road 1.9, social 3.8, web (\(1.9\times 10^6\) edges) 4.4--flat in size and class.

\begin{tabular}{ccccccc}
graph & class & _m_ & energy _E_ & LAMG+ (stp) & approxChol (stp) & _t_<sub>L</sub>_/t_<sub>A</sub> \\
`3elt` & 2D mesh & 13,722 & -0.8939 & 0.050 (16) & 0.015 (21) & 3.3 \\
`airfoil1` & 2D FEM & 12,289 & -0.9866 & 0.048 (18) & 0.015 (21) & 3.3 \\
`bodyy5` & aniso. FEM & 55,346 & -0.9045 & 0.56 (18) & 0.070 (21) & 8.0 \\
`bcsstk38` & structural & 173,714 & -0.0432 & 0.14 (15) & 0.22 (21) & 0.6 \\
`G2.circuit` & circuit & 288,286 & -1.9134 & 2.63 (21) & 0.58 (21) & 4.5 \\
`fe.ocean` & FEM mesh & 409,593 & -1.0609 & 3.84 (18) & 0.96 (21) & 4.0 \\
`p2p-Gnutella04` & P2P & 39,994 & -3.1625 & 0.14 (24) & 0.16 (25) & 0.9 \\
`as-caida` & AS/comm & 53,381 & -6.6601 & 0.083 (20) & 0.17 (23) & 0.5 \\
`web-NotreDame` & web & 1,090,108 & -25.957 & 4.51 (27) & 3.69 (29) & 1.2 \\
\end{tabular}

\begin{tabular}{cccccccc}
 & \multicolumn{4}{c}{refresh (\(\eta\)=0.05)} & \multicolumn{3}{c}{forcing \(\eta\) (refresh=0.25)} \\
graph & 0.10 & **0.25** & 0.50 & 0.80 & 0.01 & **0.05** & 0.20 \\
`airfoil1` & 18 & **18** & 18 & 18 & 14 & **18** & 33 \\
`as-caida` & 21 & **20** & 29 & 29 & 17 & **19** & 25 \\
`bodyy5` & 18 & **21** & 18 & 19 & 15 & **18** & 36 \\
`delaunay\_n16` & 18 & **18** & 21 & 18 & 15 & **18** & 33 \\
\end{tabular}

4.4

_Inner-solver ablation inside NLF’s BPR congestion solve, outer method fixed: LAMG+ vs. approximate Cholesky (both_ O(_m)). Wall-clock seconds and outer (chord-Newton) steps, to a_ 10<sup>-7</sup> _residual;_ both return the identical equilibrium _(energy E to the digits shown; flows to_ \(\Delta f\) _relative). t_<sub>L</sub>_/t_<sub>A</sub>_\>_1 _means approximate Cholesky is faster. A representative cross-class subset spanning both speed directions; the corpus-wide summary is in the text and the full per-graph output in the released artifact._

4.5

_Outer-loop parameter sensitivity (approximate-Cholesky inner): outer (chord-Newton) steps to a_ 10<sup>-9</sup> _residual on representative congestion instances._ Refresh--_rebuild the frozen factor when a step’s residual reduction is worse than this threshold (_\(\eta\)=0.05 _fixed): flat in the interior, a few extra steps only when over-frozen (`as-caida`)._ Forcing \(\eta\)--_the inner relative tolerance (refresh_=0.25 _fixed): a looser inner trades directly into more outer steps. The stock_ (\(\text{\textit{refresh}},\eta\))=(0.25,0.05) _(bold) sits in the flat interior and is near time-optimal._

