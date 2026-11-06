<tbc>we define the cumulative norm sequence via<tbc>

\(\rho_j:=\sqrt{\sum_{k=1}^jp_k^2},1\le j\le D.\)

<tbc>Normalization of \(|\phi\rangle\) implies \(\rho_D=1\). For each index _j=D,D_-1_,...,_2, select the rotation angle \(\theta_j\in[0,\pi/2]\) according to<tbc>

\(\mathrm{cos}(\theta_j):=\left\{\begin{array}{ c c }
\frac{\rho_{j-1}}{\rho_j} & \text{if}\rho_j>0, \\
1 & \text{if}\rho_j=0,
\end{array}\right.\mathrm{sin}(\theta_j):=\left\{\begin{array}{ c c }
\frac{p_j}{\rho_j} & \text{if}\rho_j>0, \\
0 & \text{if}\rho_j=0.
\end{array}\right.\)

<tbc>Starting from the state \(|e_1\rangle\), we sequentially apply the _D_-1 single-parameter two-level rotations \(e^{-i\theta_jX_{1j}}\) in descending order _j=D,D_-1_,...,_2. Because \(X_{1j}=|e_1\rangle\langle e_j|+|e_j\rangle\langle e_1|\) acts nontrivially only on span{\(|e_1\rangle,|e_j\rangle\}\), the rotation at step _j_ transforms the amplitude on \(|e_1\rangle\) from \(\rho_j\) to \(\rho_j\mathrm{cos}(\theta_j)=\rho_{j-1}\), while depositing the amplitude \(-i\rho_j\mathrm{sin}(\theta_j)=-ip_j\) onto \(|e_j\rangle\). All previously populated components \(|e_k\rangle\) (_k\>j_) remain unaffected. Consequently, after applying all _D_-1 rotations, the state becomes

\(p_1|e_1\rangle-i\sum_{j=2}^Dp_j|e_j\rangle.\)

A single diagonal unitary transformation adjusts the phases of each basis component simultaneously, mapping this vector directly to \(|\phi\rangle\) (up to a global phase). The total circuit depth is therefore at most (_D_-1)_K<sub>X</sub>+K_diag, establishing (87).

To prove assertion 3, let \(C_\psi\) and \(C_\phi\) be unitary synthesis circuits satisfying<tbc>

\(C_\psi|e_1\rangle=e^{i\alpha}|\psi\rangle,C_\phi|e_1\rangle=e^{i\beta}|\phi\rangle,\)

<tbc>each produced by a parameterized circuit with depth bounded by (_D_-1)_K<sub>X</sub>+K_diag. Since the native pulse operations generate single-parameter sub-groups, the inverse circuit \(C_\psi^{-1}=C_\psi^\dagger\) is obtained by reversing the sequence of pulses and negating their corresponding parameters. Hence, \(\mathrm{depth}(C_\psi^{-1})=\mathrm{depth}(C_\psi)\). Combining these circuits yields<tbc>

\(\left(C_\phi C_\psi^{-1}\right)|\psi\rangle=e^{i(\beta-\alpha)}|\phi\rangle,\)

<tbc>which implies the combined depth bound

\(L_\mathrm{state}\le\mathrm{depth}(C_\psi^{-1})+\mathrm{depth}(C_\phi)\le 2(D-1)K_X+2K_\mathrm{diag},\)

completing the proof of (88).

_Proof of Theorem VIII.4._ Let _s<sub>q</sub>_ and _c<sub>q</sub>_ denote, respectively, the numbers of one-qubit gates and CNOT gates in the unoptimized quantum Shannon decomposition of a _q_-qubit unitary. The recursive decomposition contains four (_q_-1)-qubit unitaries and three uniformly controlled rotations. Each such rotation uses 2<sup>_q_-1</sup> one-qubit rotations and 2<sup>_q_-1</sup> CNOTs. Hence<tbc>

\(s_q\le 4s_{q-1}+3\cdot 2^{q-1},c_q\le 4c_{q-1}+3\cdot 2^{q-1},\)

<tbc>with _s_<sub>1</sub>=1 and _c_<sub>1</sub>=0. Solving these recurrences gives

\(s_q\le 4^q-3\cdot 2^{q-1},c_q\le\frac{3}{4}4^q-\frac{3}{2}2^q.\)

This proves (86).

