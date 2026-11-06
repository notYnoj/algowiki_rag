## 6.2 Analysis

At these sizes coverage of the essential set is not a demanding test. With the three six-qubit circuits, the ideal sampler finds all essential modes with probability 0.94 (ellipse, |<tbc>

<tbc><sub>E</sub>|=21) and 0.84 (lens, |<tbc>

<tbc><sub>E</sub>|=15) from 1500 shots, and a uniform sampler needs only about 350 and 78 shots, respectively, for probability 0.9. We therefore base the analysis on the outcome laws and on the noise model of Corollary 6. We then compare the reconstructions at equal subspace size.

### Outcome laws.

10 and Figs. 5 and 3 show that the measured laws differ from the circuit laws by much more than the sampling fluctuation on both platforms. The survival fraction 1-_p_ of the fitted replacement model decreases with circuit size. With _n_<sub>2q</sub> the number of logical two-qubit gates, a fit of the form \(1-p=ce^{-\alpha n_{2q}}\) \[Fig. 3(c)\] gives _c_=0.93 and \(\alpha=0.0061\) for IonQ, and _c_=0.72 and \(\alpha=0.0060\) for IBM, where the IBM fit excludes the saturated circuits with _p\>_0.95. The decay per logical gate is thus the same within the accuracy of the fits. Per native CZ gate the IBM rate is 0.0034, about twice the calibrated gate error, which indicates additional idling and crosstalk errors in the absence of dynamical decoupling. The two platforms differ mainly in the gate-independent loss, about 7.5% for IonQ and about 28% for IBM. The residual after the fit is 1.0 to 2.5 times its sampling value. Thus the noise is not entirely uniform, and the deviation is largest for the strongly concentrated law of the ellipse at _k_=0. For IonQ, a model with independent bit flips on each qubit in addition to uniform replacement reduces the residual to 1.1 to 1.5 times its sampling value, but the fitted flip probabilities vary from circuit to circuit and are not determined reliably by 500 shots. The eight-qubit lens circuits, with 711 to 2975 native two-qubit gates, are fully randomized (_p\>_0.99).

### Parity filter.

For the lens, the measured fraction of shots in the odd-odd sector agrees with the prediction 1-3_p/_4 of the fitted uniform model to within 0.04 for all six-qubit circuits on both platforms. For the fully randomized eight-qubit circuits it approaches the uniform value 1/4, as expected. On IonQ the filter removes about half of all shots and reduces the distance to the circuit law from 0.33 to 0.17 for _k_=0 and from 0.54 to 0.16 for _k_=1. The parity filter therefore acts as a direct and inexpensive noise diagnostic, as anticipated in Sec. 4.4. This use of a measurement-visible constraint is the same mechanism as the particle-number recovery of SQD \[5\] and the code-space recovery of Ref. \[7\]. In the present case the constraint is not engineered; it follows from the isometries of the cross section.

### Dominance.

Corollary 6 predicts \(q_\mathrm{hw}(z)\ge(1-p)q(z)\) for replacement noise. For the pooled six- qubit lens shots, \(\mathrm{min}_{z\in\mathcal{E}_\mathrm{E}}q_\mathrm{hw}(z)/q(z)\) is 0.36 on IonQ and 0.09 on IBM, compared with \(1-\bar{p}=0.35\) and 0.10. For the ellipse the ratio falls below \(1-\bar{p}\) on both platforms: 0.65 versus 0.70 on IonQ, 0.42 versus 0.69 on IBM with six qubits, and 0.14 versus 0.25 on IBM with eight qubits. These violations are consistent with the nonuniform part of the noise, for which the pointwise dominance is not guaranteed. The coverage bounds of Sec. 3 should therefore be applied to hardware data with the measured, not the modeled, outcome law.

\begin{tabular}{cccccccc}
Platform & Case & Admissible & Used & Fraction & Hardware & Residual-greedy & Oracle \\
IonQ & Ellipse 8<sup>2</sup> & 64 & 60 & 0.94 & \(1.5\times 10^{-6}\) & \(1.3\times 10^{-8}\) & \(1.3\times 10^{-8}\) \\
IonQ & Lens 8<sup>2</sup> & 16 & 16 & 1.00 & \(4\times 10^{-16}\) & \(4\times 10^{-16}\) & \(4\times 10^{-16}\) \\
IBM & Ellipse 8<sup>2</sup> & 64 & 61 & 0.95 & \(2.0\times 10^{-5}\) & \(6.9\times 10^{-9}\) & \(6.9\times 10^{-9}\) \\
IBM & Lens 8<sup>2</sup> & 16 & 16 & 1.00 & \(4\times 10^{-16}\) & \(4\times 10^{-16}\) & \(4\times 10^{-16}\) \\
IBM & Ellipse 16<sup>2</sup> & 256 & 227 & 0.89 & \(7.1\times 10^{-7}\) & \(2\times 10^{-15}\) & \(2\times 10^{-15}\) \\
IBM & Lens 16<sup>2</sup> & 64 & 63 & 0.98 & \(2.3\times 10^{-3}\) & \(9.8\times 10^{-6}\) & \(9.8\times 10^{-6}\) \\
\end{tabular}

** 11:** Subspace size and Galerkin error for the full hardware samples (1500 shots per case). Admissible: dimension of the symmetry sector. Used: observed admissible modes. The last three columns give the relative energy error of the hardware set and of classical selections of the same size. Values near 10<sup>-15</sup> are at the level of rounding.

