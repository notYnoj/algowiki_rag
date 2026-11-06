separate correction attempts to reduce the six role-equality residuals using only six scalar controls. Two controls add to the root logits the features<tbc>

\(\left(\frac{s_X-s_Y}{16},\frac{s_Y-s_Z}{16}\right).\)

<tbc>At each level \(\ell\in\{4,3\}\), two controls add to the region logits at shape _s_ and permutation _p<sub>r</sub>_ the features

\(\left(\frac{s_{p_r(Y)}-s_{p_r(X)}}{2^\ell},\frac{s_{p_r(Z)}-s_{p_r(X)}}{2^\ell}\right).\)

A \(6\times 6\) Jacobian is estimated by central differences with step 10<sup>-4</sup>. Up to four Newton corrections are computed by least squares with relative singular-value cutoff 10<sup>-12</sup>, scaling a correction down if its infinity norm exceeds 1. The balancing attempt terminates early when \(\|h\|_\infty<10^{-11}\).

Both unbalanced iterates and balanced candidates are evaluated using the minimum-based objective (14), and the best candidate is retained. Balancing is a candidate-generation step: the augmented-Lagrangian continuation proceeds from its own iterate. In floating-point monitoring, a minimum of three entries is evaluated with the conservative approximation

\(\mathrm{sin}\mathrm{n}_\varepsilon(a)=-\varepsilon\mathrm{ln}\sum_{k=1}^3e^{-a_k/\varepsilon},\varepsilon=10^{-14},\)

which lies between \(\mathrm{min}_ka_k-\varepsilon\mathrm{ln}3\) and min_<sub>k</sub>a<sub>k</sub>_. The final rational evaluation uses the actual minima.

The selected point comes from the balancing step following the last outer pass. Its floating-point minimum-based objective is approximately 2.3711592385931133. The search is local and supplies no certificate of global optimality. The reported settings describe the continuation that produced the witness; reproduction of the mathematical bound requires the final witness and its checker, independently of repeating the optimization trajectory.

## 3.4 Positive rational export and independent reconstruction

The selected probabilities are converted to integer numerators with denominator 2<sup>80</sup>, preserving normalization and the paired symmetry of local split probabilities. Orbit masses are then expanded into equal probabilities for their ordinary strings. Increasing the common denominator to 2<sup>96</sup> makes this expansion exact, since the relevant orbit sizes are powers of two. Consequently the delivered witness contains rational distributions on explicitly ordered strings rather than an orbit-compressed numerical model.

The logarithmic dual parameters are converted separately. In each factor row, subtract the smallest active logarithmic value before exponentiation and rational approximation. The resulting active factors are at least 1, and their integer numerators are not restricted to machine-word size. This choice preserves large ratios without forcing small factors onto a fixed positive floor. In particular, normalizing by the largest factor and clipping small rounded values could substantially weaken the entropy bound despite preserving positivity. The chosen row normalization avoids that loss. Such row rescalings leave (4) unchanged. More generally, the validity of the bound requires only strict positivity of the exported factors; neither a small approximation error nor a stationarity check is an assumption of the verification.

The checker validates support, nonnegativity, exact normalization, child shapes, complementary references, and the recursively reconstructed complete split distributions. It evaluates the six global copies in physical coordinates before taking the published minima. Binary logarithms and subsequent expressions are enclosed by rational outward intervals. The numerical result is reported in Section 4.

