## 6.2 Fine-mesh finite element solution

1 reports the relative errors of the finite element solution \(\Phi_h\) of (41) with _U_<sup>∗</sup>=_I<sub>h</sub>U_ computed by Newton’s method on the fine mesh alone. The energy norm error is _O(h_) and the _L_<sup>2</sup> error is _O(h_<sup>2</sup>), in agreement with Corollary 4.9 for _s_=2 and _t_=1. At _h_=1/32 the relative errors are about 8.7% in the energy norm and 0.36% in _L_<sup>2</sup>; the energy error is the larger one because \(|||\cdot|||\) contains the factor \(\epsilon_s=80\) in _D<sub>s</sub>_ and the exact solution has frequency \(2\pi\). The _L_<sup>4</sup> error also converges as _O(h_<sup>2</sup>), which is faster than the rate _h_<sup>_s_-1+_t/_4</sup>=_h_<sup>5/4</sup> guaranteed by (55); the latter is obtained from the Gagliardo-Nirenberg inequality (11) and is not sharp for smooth solutions. Since the nonlinearity is weak compared with the diffusion term, Newton’s method converges in three or four iterations from the zero initial guess.

## 6.3 Two-grid solution with _H∼h_<sup>2/5</sup>

2 and Figure 1(a) compare the two-grid solution \(\Phi_h^\text{tg}\) of Algorithm 1 with the fine-mesh solution \(\Phi_h\) for coarse meshes chosen by the rule _H≈h_<sup>2/5</sup> (which Corollary 5.3 covers only when \(\sigma\ge s\)): since the available coarse meshes have \(H\in\{1/2,1/4,\dots\}\), we take for _H_ the dyadic mesh size nearest to _h_<sup>2/5</sup>; the value of _h_<sup>2/5</sup> is listed for comparison. For \(h\le 1/16\) the energy norm errors of the two-grid and the fine-mesh solutions agree to three significant digits, and both converge as _O(h_). The additional error \(e_E(\Phi_h-\Phi_h^\text{tg})\) caused by replacing the fine Newton iteration by one correction is between two and three orders of magnitude below the discretization error for \(h\le 1/16\). The last column gives the total time of the two-grid solve (coarse Newton iteration plus one fine linear solve, excluding mesh and load assembly in both cases); for _h_=1/32 it is 2.6 s against 8.2 s for the full fine-mesh Newton iteration. The gain is moderate because the full Newton iteration needs only three steps in this test; for problems that require more (damped) Newton steps, the saving should be larger.

\begin{tabular}{ccccccccc}
_h_ & DOFs & \(e_E(\Phi-\Phi_h)\) & rate & \(e_2(\Phi-\Phi_h)\) & rate & \(e_4(\Phi-\Phi_h)\) & rate & Newton its. \\
1/4 & 343 & 6.835e-01 & - & 2.259e-01 & - & 1.926e-01 & - & 4 \\
1/8 & 3375 & 3.448e-01 & 0.99 & 5.655e-02 & 2.00 & 4.791e-02 & 2.01 & 3 \\
1/16 & 29791 & 1.729e-01 & 1.00 & 1.420e-02 & 1.99 & 1.208e-02 & 1.99 & 3 \\
1/32 & 250047 & 8.655e-02 & 1.00 & 3.557e-03 & 2.00 & 3.030e-03 & 2.00 & 3 \\
\end{tabular}

\begin{tabular}{ccccccccc}
_h_ & _H_ & _h_<sup>2/5</sup> & \(e_E(\Phi-\Phi_h)\) & \(e_E(\Phi-\Phi_h^\text{tg})\) & \(e_2(\Phi-\Phi_h^\text{tg})\) & \(e_E(\Phi_h-\Phi_h^\text{tg})\) & coarse its. & time (s) \\
1/4 & 1/2 & 0.574 & 6.8353e-01 & 7.1349e-01 & 2.792e-01 & 7.98e-02 & 6 & 0.01 \\
1/8 & 1/2 & 0.435 & 3.4480e-01 & 3.5485e-01 & 9.734e-02 & 4.65e-02 & 6 & 0.06 \\
1/16 & 1/4 & 0.330 & 1.7294e-01 & 1.7296e-01 & 1.438e-02 & 3.15e-04 & 4 & 0.28 \\
1/32 & 1/4 & 0.250 & 8.6551e-02 & 8.6560e-02 & 3.732e-03 & 2.82e-04 & 4 & 2.64 \\
\end{tabular}

1: Relative errors of the fine-mesh finite element solution \(\Phi_h\) (full Newton iteration).

2: Two-grid solution with _H≈h_<sup>2/5</sup>: relative energy-norm error of the fine-mesh solution \(\Phi_h\) and of the two-grid solution \(\Phi_h^\text{tg}\), relative _L_<sup>2</sup> error of \(\Phi_h^\text{tg}\), relative distance between the two, coarse Newton iterations, and wall time of the two-grid solve.

