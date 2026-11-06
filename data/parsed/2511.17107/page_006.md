_The matrix_ \(\mathbf{F}=(F_{ij})_{1\le i,j\le N}\) _is defined by_ \(F_{ij}=\frac{1}{\sqrt{N}}\omega^{(i-1)(j-1)}\) _and_ \(\omega=\mathrm{exp}\left(\mathrm{i}\frac{2\pi}{N}\right)\)_. As a corollary, the product of any two circulant matrices is commutative:_ **C**<sub>1</sub>**C**<sub>2</sub>=**C**<sub>2</sub>**C**<sub>1</sub> _whenever_ **C**<sub>1</sub> _and_ **C**<sub>2</sub> _are circulant matrices._

_Proof._ The proof is provided in \[1\].

**Proposition 2.2.** _The matrices_ A _and_ B _defined in_ (2.6), (2.7) _and_ (2.11) _satisfy:_ BA=**0**.

_Proof._ It suffices to verify that \(\hat{\mathcal{D}}_i\hat{\mathcal{D}}_j=\hat{\mathcal{D}}_j\hat{\mathcal{D}}_i\), which is equivalent to the commutativity of the product of D_<sub>s,i</sub>_ and D_<sub>t,j</sub>_ for any \(s,t\in\{0,1\}\) and \(i,j\in\{1,2,3\}\). When \(i\neq j\) the result is proved by the mixed product property

\((A_1\otimes B_1)(A_2\otimes B_2)=(A_1A_2)\otimes(B_1B_2)\) (2.15)

for any _A<sub>i</sub>_, _B<sub>i</sub>_ with compatible shapes. Thus multiplications of D_<sub>s,i</sub>_ and D_<sub>t,i</sub>_ are commutative. When _i=j_ the result holds due to Lemma 2.1 and the mixed product property (2.15).

**Proposition 2.3** (Main Result of Kernel Compensation)**.** _Let_ \(\mathcal{A},\mathcal{M}\in\mathbb{C}^{N^\mathcal{A}\times N^\mathcal{A}}\) _and_ \(\mathcal{B}\in\mathbb{C}^{N^\mathcal{B}\times N^\mathcal{A}}\) _be matrices such that:_ BA=**0**_, and_ M _is HPD. We assume that_

\(\overbrace{\text{\textit{\textbf{eigenvalues of}}}\mathcal{A}\mathcal{M}\mathcal{A}^\dagger}^\text{\textit{\textbf{.}}}:\overbrace{0,0,\cdots,0}^{N_0^\mathcal{A}\text{\textit{\textbf{zeros}}}}<\overbrace{\lambda_1^\mathcal{A}\le\lambda_2^\mathcal{A}\le\cdots\le\lambda_{N_1^\mathcal{A}}^\mathcal{A}}^{N_1^\mathcal{A}\text{\textit{\textbf{nonzeros}}}}\) (2.16)

\(\overbrace{\text{\textit{\textbf{eigenvalues of}}}\mathcal{B}^\dagger\mathcal{B}}^\text{\textit{\textbf{.}}}:\overbrace{0,0,\cdots,0}^{N_0^\mathcal{B}\text{\textit{\textbf{zeros}}}}<\overbrace{\lambda_1^\mathcal{B}\le\lambda_2^\mathcal{B}\le\cdots\le\lambda_{N_1^\mathcal{B}}^\mathcal{B}}^{N_1^\mathcal{B}\text{\textit{\textbf{nonzeros}}}}\) (2.17)

_Then the eigenvalue distributions of_ \(\mathcal{A}\mathcal{M}\mathcal{A}^\dagger+\gamma\mathcal{B}^\dagger\mathcal{B}\) _are_

\(\overbrace{0,\cdots,0}^{\mathrm{dim}H\text{\textit{\textbf{zeros}}}}<\lambda_1\le\lambda_2\le\cdots\le\lambda_m\le\cdots,\) (2.18)

_where_ \(\gamma\) _is an arbitrary positive number,_ \(\mathcal{H}:=\mathrm{ker}\mathcal{A}^\dagger\cap\mathrm{ker}\mathcal{B}\)_. There holds_

\(\left\{\lambda_1,\cdots,\lambda_m,\cdots\right\}=\left\{\lambda_1^\mathcal{A},\cdots,\lambda_{N_1^\mathcal{A}}^\mathcal{A}\right\}\cup\left\{\gamma\lambda_1^\mathcal{B},\cdots,\gamma\lambda_{N_1^\mathcal{B}}^\mathcal{B}\right\}.\) (2.19)

_Proof._ We refer the reader to \[8\] for the proof.

The kernel compensation formulation (2.13) allows us to recover the nonzero eigenvalues of \(\mathcal{A}\mathcal{M}_\varepsilon\mathcal{A}^\dagger\) by computing the spectrum of the penalized system \(\mathcal{A}\mathcal{M}_\varepsilon\mathcal{A}^\dagger+\gamma\mathcal{B}^\dagger\mathcal{B}\). Proposition 2.3 shows the first _m_ smallest positive eigenvalues of the two systems are identical, provided that \(\gamma\) satisfies \(\gamma\lambda_1^\mathcal{B}\ge\lambda_m^\mathcal{A}\). To characterize the resulting null space H and determine an appropriate value for the penalty coefficient \(\gamma\), we present the following analysis.

**Lemma 2.4.** _When the coordinate change_ (2.8) **A**=**_I_**<sub>3</sub>**_, we have_

_(1). The block matrices_ A _and_ B _satisfy_ AA<sup>†</sup>+B<sup>†</sup>B=diag(L,L,L) _with_

\(\mathcal{L}=\mathcal{B}\mathcal{B}^\dagger=\mathcal{D}_1^\dagger\mathcal{D}_1+\mathcal{D}_2^\dagger\mathcal{D}_2+\mathcal{D}_3^\dagger\mathcal{D}_3\in\mathbb{C}^{N^3\times N^3},\) (2.19)

_(2). If there holds conditions_

\(\mathbf{k}\neq\mathbf{0},\mathrm{max}_{i=1,2,3}|\mathbf{k}_i|\le\pi,\text{\textit{grid size}}h=\frac{1}{N}<\frac{1}{\pi},\) (2.20)

_then the smallest nonzero eigenvalue of_ B<sup>†</sup>B_, as is denoted by_ \(\lambda_1^\mathcal{B}\) _in Proposition 2.3, satisfies_ \(\lambda_1^\mathcal{B}=\lambda_\mathrm{min}(\mathcal{L})=\left\|\mathbf{k}\right\|_2^2\).

