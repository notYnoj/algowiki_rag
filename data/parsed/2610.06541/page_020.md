**Appendix A: Quantum linear systemsby a rescaled quobitized walk**

Michael Jarret

Abstract. (This appendix is written as a companion note, with its own title, abstract, and local notation.) We use a continuous adiabatic theorem to obtain \(O(\kappa/\delta)\) queries for quantum linear systems, giving a rescaled quobitized walk, its circuit, and endpoint operations. Rescaling keeps a fixed spectral arc free, so the unit-step comparison constants are absolute.

### A.1. Introduction.

For the rescaled quobitized walk \[21\], transferring a continuous adiabatic bound through its logarithm (Theorems 6.5 and 6.11) recovers Costa et al.’s \(O(\kappa/\delta)\) query count \[8\]. We use the Bernoulli- majorant bounds (Lemma 2.9) and An and Lin’s AQC(3/2) path (Corollary 6.9 and Definition 6.8) \[2\], then examine how the walk construction affects the constant.

### A.2. Setting and result.

The task is to prepare _A_<sup>-1</sup>_b/_∥_A_<sup>-1</sup>_b_∥, with ∥_b_∥=1, from a Hermitian block encoding (_O,V_) of positive definite _A=V_<sup>†</sup>_OV_ , where _O_ is a Hermitian involution and _V_ an isometry. For an exact normalized block encoding \(A=\iota^\dagger U_A\iota\) with isometry \(\iota\), take \(O=|0\rangle\langle 1|\otimes U_A+|1\rangle\langle 0|\otimes U_A^\dagger\), with \(V=|+\rangle\otimes\iota\) \[8\], which uses a constant number of controlled calls to _U<sub>A</sub>_ and \(U_A^\dagger\). An and Lin’s path is _H(f_)=(1-_f)H_<sub>0</sub>+_fH_<sub>1</sub>, where, with \(Q_b=I-|b\rangle\langle b|\),<tbc>

\(H_0=\left(\begin{array}{ c c }
0 & Q_b \\
Q_b & 0
\end{array}\right),H_1=\left(\begin{array}{ c c }
0 & AQ_b \\
Q_bA & 0
\end{array}\right).\)

<tbc>The walk encodes this path through the isometry

\(L=|0\rangle\otimes I_2\otimes|0\rangle^{\otimes 2}\otimes V,\)

and reversing _L_’s implementation decodes the output.

**Definition A.1.** Put \(\alpha(f)=\sqrt{(1-f)^2+f^2}\). Use four qubits, ordered as in _L_, followed by the space codom_V_ of _O_. Put _Q_<sub>0</sub>=diag(_VQ<sub>b</sub>V_<sup>†</sup>,0),<tbc>

\(R_{1,0}=\left(\begin{array}{ c c }
I & 0 \\
0 & -I
\end{array}\right),R_{0,1}=\left(\begin{array}{ c c }
0 & I \\
I & 0
\end{array}\right),R=\frac{(1-f)R_{1,0}+fR_{0,1}}{\alpha},\)<br>
\(\Pi=\frac{1}{\sqrt{2}}\left(\begin{array}{ c c }
I & I \\
I & -I
\end{array}\right),\Pi_Q=\left(\begin{array}{ c c }
Q_0 & I-Q_0 \\
I-Q_0 & Q_0
\end{array}\right),\Pi_1=\left(\begin{array}{ c c }
1/2 & \sqrt{3}/2 \\
\sqrt{3}/2 & -1/2
\end{array}\right),\)

<tbc>and \(G=\mathrm{diag}(\mathrm{diag}(R,R),\Pi_Q\mathrm{diag}(\Pi,\Pi))\). The outer block indices of _G_, of \(\Pi_Q\), and of _R_ and \(\Pi\) correspond to qubits 2, 3, and 4, respectively. The operator diag(_I,O,I,O_) applies _O_ when qubit 4 is \(|1\rangle\). Define

\(E=\Pi_1\otimes\left[G\left(\left(\begin{array}{ c c }
0 & 1 \\
1 & 0
\end{array}\right)\otimes\mathrm{diag}(I,O,I,O)\right)G^\dagger\right].\)

Put \(Z=I_2\otimes\mathrm{diag}(I,0,Q_0,I-Q_0)\) to isolate the solution line. Fix \(\kappa>1\) with AQC(3/2) schedule _f_ (Definition 6.8). Define _W(s_)=(2_LL_<sup>†</sup>-_I)E(f(s_)) and \(F_s=(I+iE(f(s)))/\sqrt{2}\).

Only diag(_I,O,I,O_) in _E_ queries _O_, giving one controlled query per walk step or endpoint operation. By Lemma A.3, _E(f_) is a Hermitian involution with<tbc>

\(L^\dagger E(f)L=H(f)/(2\sqrt{2}\alpha(f)).\)

<tbc>Since _E_<sup>2</sup>=_I_, _F<sub>s</sub>_ is unitary. If _H(f(s_))_v_=0, the compression gives _L_<sup>†</sup>_ELv_=0 and hence, using _E_<sup>2</sup>=_I_,

\(WLv=-ELv,WELv=Lv,WF_sLv=iF_sLv.\)

The entry \(\langle 0|\Pi_1|0\rangle=1/2\) rescales the encoded block to norm at most 1/2, leaving a \(\kappa\)-independent arc free of eigenvalues of _W_. When ∥_A_∥=1, the gap parameter \(\kappa\) below can be taken to be the condition number \[2, Appendix A\].

