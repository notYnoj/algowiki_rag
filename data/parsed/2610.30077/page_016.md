### Ablations.

Two parameters entering the scheme are, by construction, not supposed to affect the computed solution, which we check here directly. First, Theorem 4.1 only requires \(\varepsilon_q\ge 0\), so the extra stress-smoothing term \(\varepsilon_q\Delta q\) is not needed for stability. Sweeping \(\varepsilon_q\) from 10<sup>-3</sup> down to 0 confirms that (12) continues to hold and E remains monotone at every value, including \(\varepsilon_q=0\), with the computed solution itself moving by only \(4\times 10^{-6}\). Second, the SAV constant _C_<sub>0</sub> (Section 2) is a free modelling choice introduced purely to keep the square root well defined, and should not change the physical solution: varying _C_<sub>0</sub> over five orders of magnitude changes \(\phi,q\) by at most \(8\times 10^{-11}\), confirming that it does not.

### 7.3 Coupled-vs-uncoupled demonstration

Using the configuration above (_N_=128, \(\Delta t=10^{-3}\), dealiased, identical seeded IC), we run the coupled model and its \(A\equiv 0\) control (which decouples _q_ and reduces (1a) to plain Cahn-Hilliard with the same \(b(\phi)\)) to _T_=10.

Mass is conserved to \(\sim 5\times 10^{-12}\) in both runs and E decreases strictly every step. The two models behave very differently (Figure 6 and Figure 7): from the identical _E_(0)=0.1729, the \(A\equiv 0\) control has released 83% of its initial energy by _t_=10 and reached a coarsening plateau, while the coupled model has released only 59% and is still on a visibly downward slope, not yet at equilibrium. The GMRES cost mirrors the morphology: the coupled model needs a median 333 iterations/step (the steep \(A(\phi)\) term is genuinely expensive to precondition, Section 7.2), while the \(A\equiv 0\) control, with no coupling term to resolve, needs only 16.

_Robustness_: the scheme remains stable over 10<sup>4</sup> steps on the reference configuration of the  1, and the viscoelastic coupling measurably slows and delays phase separation relative to an uncoupled control from the identical initial perturbation, consistent with Tanaka’s viscoelastic suppression of phase separation \[5\]. The results above use a single realisation per case, at \(\Delta t=10^{-3}\) specifically, given the cost of finer \(\Delta t\) documented in Section 7.1. A systematic study of these dependencies is follow-on work that this method was built to make affordable.

## 8 Conclusion

We have derived and verified a linear, second-order, unconditionally energy-stable SAV-BDF2 scheme for the CHQ viscoelastic phase-separation model. Stability rests on an exact discrete energy-dissipation identity requiring only the model’s own coercivity assumption, frozen at the<tbc>

Agreement with independent Newton-BDF2 solver (generic coefficients, N= 19, T= 0.12)
-
-
slope 2
10-7
10-8
10-3
At

Figure 5: Agreement with the independent nonlinear Newton-BDF2 solver, generic coefficient set, \(19\times 19\) grid, _T_=0.12: \(\|\phi_\text{SAV}-\phi_\text{NL}\|_\infty\) against a slope-2 reference, all five \(\Delta t\).

