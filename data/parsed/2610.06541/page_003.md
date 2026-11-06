**"Theorem" C.** _For integer_ \(T\ge 1\)_, let H be a twice continuously differentiable Hermitian family on_ \[0,1\] _with_ \(\|H'\|\le L\) _and_ \(\|H''\|\le 2\nu\)_, U its evolution under H(t/T_) _starting at the identity, and_ \(W_T=e^{-iH((T-1)/T)}\cdots e^{-iH(1/T)}e^{-iH(0)}\)_. Suppose each interior sample H(j/T),_ 0_\<j\<T, has spectrum in an interval of length at most_ \(\bar{w}\)_, and its nonzero eigenvalue differences lie at distance at least_ \(\gamma>0\) _from every nonzero multiple of_ \(2\pi\)_, with L,_ \(\nu\), \(\gamma\)_, and_ \(\bar{w}\) _independent of T. Then_

\(\big\|e^{-iH(1)/2}W_Te^{iH(0)/2}-U(T)\big\|=O_{\gamma,\bar{w}}\big((L+L^2+\nu)/T\big).\)

Thus, operator-norm bounds comparing _U(T_) with a target also hold for the phase-corrected product, adding _O_(1_/T_) error (Theorem 6.4). Since the half-step phases preserve the endpoint spectral subspaces, any continuous adiabatic bound on endpoint leakage then transfers to _W<sub>T</sub>_ under these comparison hypotheses, retaining the continuous theorem’s hypotheses (Theorem 6.5). A continuous _C/T_ bound therefore gives \(O(1/\delta)\) unit steps for target leakage \(\delta\) (Corollary 6.7).

For quantum linear systems, which ask for the state \(A^{-1}b/\|A^{-1}b\|\), take _A_ positive definite of condition number \(\kappa\), with \(\|A\|=\|b\|=1\). An and Lin’s path \[2\] (Definition 6.8), with speed proportional to the 3/2 power of its gap lower bound, satisfies the comparison hypotheses with error \(O(\kappa/T)\). Their gap bound and the continuous Jansen–Ruskai–Seiler theorem \[16\] give leakage \(O(\kappa/T)\), so \(O(\kappa/\delta)\) factors suffice (Corollary 6.9).

A walk is an ordered sequence of unitaries (Definition 6.10). For samples of a _C_<sup>2</sup> unitary family whose spectra avoid a common open arc, a Hermitian logarithm cut inside that arc gives an _O_(1_/T_) evolution comparison, up to half-step phases (Theorem 6.11), and adiabatic transfer retains the continuous theorem’s hypotheses on this logarithm path. Appendix A constructs a rescaled qubitized walk, a product of two reflections encoding the Hamiltonian \[21\], for quantum linear systems with such an arc. Given preparation of _b_, it recovers Costa et al.’s \(O(\kappa/\delta)\) query count \[8\], with constant success probability signaled by a measurement and state-vector error at most \(\delta\), up to global phase.

### 1.2. Prior work and outline.

Earlier discrete adiabatic theorems take unit steps as given and impose conditions on their variation and eigenphase (eigenvalue-argument) gaps \[27, 8\]. Yi and Crossson apply continuous adiabatic theory to logarithms of Trotter steps assuming negligible discretization error \[31\], while Theorem 6.11 bounds the product’s operator-norm distance from the logarithm’s evolution by _O_(1_/T_), up to the half-step phases, under the stated regularity and free-arc hypotheses. For the sampled exponentials _e_<sup>-_iH(j/T_)</sup>, _O_(1_/T_) leakage is known for nondegenerate spectra \[30\], under multistep-gap hypotheses \[1\], and asymptotically for a ground state \[23\], whereas Theorem 6.4 compares evolutions in operator norm without requiring gaps between spectral bands, allowing levels to cross.

Section 2 prepares the comparison tools, and Section 3 develops bit truncation, fine-step comparison, and adiabatic transfer. Section 4 counts truncation-level crossings and compares with time sampling, while Section 5 extends truncation to other levels and proves the bound assembling piecewise comparisons for unit steps. Section 6 applies the construction to time, proves unit-step transfer, and treats quantum linear systems and walks. Section 7 discusses applications, open questions, and implementation, and Appendix A gives the walk circuit and query count.

## 2. Preliminaries

In this section, we define the evolutions and induced products used throughout the paper. Duhamel and Davis–Kahan prepare the fine-step comparison and its adiabatic transfer, while the frame operator prepares the unit-step comparison. Throughout, \(d\ge 1\), _T\>_0, and every Hamiltonian family takes Hermitian values. For \(H,G:[0,T]\rightarrow\mathbb{C}^{d\times d}\), the unitary evolutions _U,V_ solve

(2.1) \(\left\{\begin{array}{ c }
i\dot{U}(t)=H(t)U(t), \\
U(0)=1,
\end{array}\right.\left\{\begin{array}{ c }
i\dot{V}(t)=G(t)V(t), \\
V(0)=1.
\end{array}\right.\)

**Definition 2.1.** A family _G_ is _piecewise constant_ if there are times \(0=t_0<t_1<\cdots<t_n=T\) and matrices _G_<sub>0</sub>_,...,G_<sub>_n_-1</sub> with _G(t_)=_G<sub>j</sub>_ on each _piece_ (_t<sub>j</sub>,t_<sub>_j_+1</sub>). The _t<sub>j</sub>_ are its _piece endpoints_. Its _induced product_ is

(2.2) \(W=e^{-i(t_n-t_{n-1})G_{n-1}}\cdots e^{-i(t_2-t_1)G_1}e^{-i(t_1-t_0)G_0},\)

with one unitary per piece, applied in the order of time.

