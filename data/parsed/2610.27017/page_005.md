Dividing both sides of (2.2) by \(\eta_1\), we have<tbc>

\(\left(\frac{1}{\eta_1}D^{(m)}+I_N\otimes T_N^{\gamma_1}+\frac{\eta_2}{\eta_1}T_N^{\gamma_2}\otimes I_N\right)\mathbf{u}^{(m)}=\frac{1}{\eta_1}\Delta t\mathbf{f}^{(m)}+\frac{1}{\eta_1}D^{(m)}\mathbf{u}^{(m-1)}.\)

<tbc>Define

\(A_N^{(m)}=\frac{1}{\eta_1}D^{(m)}+I_N\otimes T_N^{\gamma_1}+\frac{\eta_2}{\eta_1}T_N^{\gamma_2}\otimes I_N,\)<br>
\(\mathbf{b}^{(m)}=\frac{1}{\eta_1}\Delta t\mathbf{f}^{(m)}+\frac{1}{\eta_1}D^{(m)}\mathbf{u}^{(m-1)}.\) (2.3)

Then (2.2) is equivalent to

\(A_N^{(m)}\mathbf{u}^{(m)}=\mathbf{b}^{(m)},1\le m\le M.\) (2.4)

After fixing the partition number _N_, discretizing (1.1) yields a set of matrices \(\{A_N^{(m)}\}\). When the coefficient _d(x,y,t_)=0, _D_<sup>(_m_)</sup> degenerates to the zero matrix, and in this case, \(A_N^{(m)}\) is independent of the time level _m_ and is denoted by _A<sub>N</sub>_. The matrix _A<sub>N</sub>_ is symmetric positive definite and strictly diagonally dominant, and it is a Block-Toeplitz-Toeplitz-Block (BTTB) matrix.

BTTB matrices belong to the class of multilevel Toeplitz matrices, and their spectral information is closely related to the generating function of the corresponding BTTB matrix sequence. Let us now recall the definitions of Toeplitz matrix sequences and BTTB matrix sequences.

**Definition 2.1.** \[20\] Let \(f(\theta)\in L^1([-\pi,\pi])\) and let {_f<sub>k</sub>_} be the Fourier coefficients defined as<tbc>

\(f_k:=\frac{1}{2\pi}\int_{[-\pi,\pi]}f(\theta)e^{-\mathbf{i}k\theta}\mathrm{d}\theta,\)

<tbc>where **i**<sup>2</sup>=-1. Then the Toeplitz matrix of order _n_ associated with \(f(\theta)\) is

\(T_n(f)=[f_{i-j}]_{i,j=1}^n.\)

The function \(f(\theta)\) is called the generating function of the matrix sequence \(\{T_n(f)\}_{n\in\mathbb{N}}\).

**Definition 2.2.** \[20\] Let \(f(\theta_1,\theta_2)\in L^1([-\pi,\pi]^2)\) and let {_f_<sub>\[_k_<sub>1</sub>_,k_<sub>2</sub>\]</sub>} be the Fourier coefficients defined as<tbc>

\(f_{[k_1,k_2]}=\frac{1}{4\pi^2}\int_{-\pi}^\pi\int_{-\pi}^\pi f(\theta_1,\theta_2)e^{-\mathbf{i}(k_1\theta_1+k_2\theta_2)}\mathrm{d}\theta_1\mathrm{d}\theta_2.\)

<tbc>Then the Block-Toeplitz-Toeplitz-Blocks matrix of order _n=n_<sub>1</sub>_n_<sub>2</sub> associated with \(f(\theta_1,\theta_2)\) is<tbc>

\(T_n^{(2)}(f)=\left[\left[f_{[i_1-j_1,i_2-j_2]}\right]_{i_2,j_2=1}^{n_2}\right]_{i_1,j_1=1}^{n_1}.\)

<tbc>Accordingly, \(f(\theta_1,\theta_2)\) is called the generating function of matrix sequence \(\{T_n^{(2)}(f)\}_{n\in\mathbb{N}}\). Moreover, \(T_n^{(2)}(f)\) also admits the following representation:

\(T_n^{(2)}(f)=\sum_{|k_1|<n_1}\sum_{|k_2|<n_2}f_{[k_1,k_2]}J_{n_1}^{[k_1]}\otimes J_{n_2}^{[k_2]},\) (2.5)

where \(J_n^{[k]}\) is the matrix of order _n_ whose (_i,j_) entry equals 1 if _i-j=k_ and zero otherwise.

In order to obtain the generating function of \(\{A_N\}_{N\in\mathbb{N}}\), we first give the following lemma.

