at its lowest depth (number of layers) _p_=1 for MaxCut, exact analytic formulas for the expected cost value were obtained in \[4\]. On the other hand, recent work of \[5\] has shown that computing the same quantities for \(p\ge 2\) is itself in general NP-hard (i.e., can be as hard as the underlying problem itself). Our main contribution is to sharpen this dichotomy to show that the \(p\ge 2\) case is in fact #P-hard; i.e., the latter case is as hard as counting the number of optimal solutions of a constraint satisfaction problem, not just finding one, which is generally believed to be a harder task \[6, 7\].

## QAOA for MaxCut

Consider the MaxCut problem on a graph _G_=(_V,E_) on _n_=|_V_| vertices. We identify cuts as spin (bit) assignments \(x\in\{\pm 1\}^n\) with cut value

\(\mathrm{c}_G(x)=\sum_{\{u,v\}\in E}\frac{1-x_ux_v}{2},\mathrm{MC}(G)=\mathrm{max}_x\mathrm{c}_G(x),\#\mathrm{MC}(G)=\{x:\mathrm{c}_G(x)=\mathrm{MC}(G)\}.\) (1)

Finding a maximum cut is a canonical NP-hard optimization problem. Counting maximum cuts exactly, i.e. determining |#MC(_G_)|, is #P-hard \[8, Lemma 13\] (see also \[9, 10\]).

For QAOA applied to MaxCut we define the standard cost and mixer Hamiltonians from the single-qubit Pauli matrices \(X=(\begin{array}{ c c }
0 & 1 \\
1 & 0
\end{array})\) and \(Z=(\begin{array}{ c c }
1 & 0 \\
0 & -1
\end{array})\) as<tbc>

\(C_G=\sum_{\{u,v\}\in E}\frac{I-Z_uZ_v}{2},B=\sum_{v\in V}X_v.\) (2)

<tbc>Here _C<sub>G</sub>_ satisfies \(C_G|x\rangle=c_G(x)|x\rangle\) for every computational basis state \(|x\rangle\). At depth parameter _p_, standard QAOA for MaxCut prepares the quantum state\[11\]<tbc>

\(|\psi_p(\unknown,\unknown)\rangle=(e^{-\mathrm{i}\beta_pB}e^{-\mathrm{i}\gamma_pC_G})\dots(e^{-\mathrm{i}\beta_2B}e^{-\mathrm{i}\gamma_2C_G})(e^{-\mathrm{i}\beta_1B}e^{-\mathrm{i}\gamma_1C_G})|+\rangle^{\otimes n},\) (3)

<tbc>for easy-to-prepare initial product state \(|+\rangle^{\otimes n}=(|0\rangle+|1\rangle)^{\otimes n}/\sqrt{2^n}\), while seeking 2_p_ parameters (angles) \(\gamma_1,\dots,\gamma_p,\beta_1,\dots,\beta_p\) optimizing the cost expectation value

\(F_p(G;\unknown,\unknown)=\langle\psi_p|C_G|\psi_p\rangle.\) (4)

Given \(F_p(G;\unknown,\unknown)\) one can then obtain bounds on the expected approximation ratio obtained by repeatedly preparing and measuring the QAOA state with the same parameters on a quantum computer \[2, 4, 12\]. Evaluations of \(F_p(G;\unknown,\unknown)\) are also important for other algorithm aspects including parameter optimization.

The complexity of evaluating Eq. (4) is distinct from the complexity of sampling from the full QAOA output distribution \[13\]. At _p_=1, the expectation value has an explicit formula on general graphs \[2, 4\] (see Appendix A). By contrast, Wang, Chen, Sun, and Zhang recently showed \[5\] that exact evaluation is NP-hard for every fixed \(p\ge 2\). Their hardness proof writes the cost expectation as a Laurent polynomial in a phase variable and recovers MC(_G_) from its largest nonzero exponent when evaluated for \(C_{G^\prime}\) on a suitably transformed graph \(G'=G'(G)\).

The present work upgrades this mechanism for \(p\ge 2\) from optimization to counting hardness. At _p_=2, we tie the phase angles, \(\gamma_1=\gamma_2=\phi\), and fix the mixer angles to \(\beta_1=\mathrm{arctan}(1/2)\) and \(\beta_2=\pi/4\). This leaves a one-parameter expectation value, which is a Laurent polynomial in \(z=e^{\mathrm{i}\phi}\). We construct reduced problem instances for which the extremal Laurent polynomial coefficient can be evaluated in closed form and is shown to be proportional to the full maximum cut degeneracy |#MC(_G_)| of the input problem graph. The required coefficient property is enforced by complete bipartite subgraph _K<sub>L,L</sub>_ variable gadgets with suitably chosen _L=O(n_), along with densely<tbc>

