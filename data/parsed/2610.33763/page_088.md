_with_ \(\nu\neq 0\)_. Then, it holds_

\(\{P_N\}_N\sim_{\mathrm{GLT},\sigma} h_\xi(\theta_1)+\nu a(x)g_\eta(\theta_2),(\theta_1,\theta_2)\in[-\pi,\pi]^2,x\in[0,1],\)

_where_ \(h_\xi\) _and_ \(g_\eta\) _are given in Theorems 6.1-6.2._

**Proof:** Immediate by following the same reasoning as in the proof of Theorem 6.3. \(\square\)

The GLT symbol and singular value distribution of the preconditioned matrix sequence can be derived as a corollary of Theorems 6.3 and 6.4, simply by exploiting the algebra properties in GLT 3. However, it can also be computed more in general avoiding the assumption on the discretization parameters, as we show in the following theorem. Moreover, we can derive the distribution of the eigenvalues.

**Theorem 6.5** _With A<sub>N</sub> as in_ (6.11) _and P<sub>N</sub> as in_ (6.15)_, it holds_<tbc>

\(\{P_N^{-1}A_N\}_N\sim_{\mathrm{GLT},\sigma} 1.\)

<tbc>_Moreover,_<tbc>

\(\{P_N^{-1}A_N\}_N\sim_\lambda 1.\)

<tbc>**Proof:** Setting _R<sub>N</sub>_:=_A<sub>N</sub>-P<sub>N</sub>_, we have<tbc>

\(P_N^{-1}A_N=I_N+P_N^{-1}R_N.\)

<tbc>From the fact that \(\mathrm{rank}R_N\le n\), it follows \(\mathrm{rank}(P_N^{-1}R_N)\le n=o(N)\), therefore<tbc>

\(\{P_N^{-1}R_N\}_N\sim_\mathrm{GLT} 0\)

<tbc>by Lemma 4.1. Hence, by GLT 3 and the fact that {_I<sub>N</sub>}<sub>N</sub>_∼<sub>GLT</sub>1,<tbc>

\(\{P_N^{-1}A_N\}_N\sim_\mathrm{GLT} 1.\)

<tbc>The singular value distribution follows immediately from GLT 1. Concerning the eigenvalue distribution, it is obvious that<tbc>

\(\lambda_j(P_N^{-1}A_N)=1+\lambda_j(P_N^{-1}R_N),j=1,\dots,N,\)

<tbc>therefore

\(\#\left\{j=1,\dots,N:\lambda_j(P_N^{-1}A_N)\neq 1\right\}\le n=o(N).\)

In other words, the eigenvalues of \(\{P_N^{-1}A_N\}_N\) are weakly clustered at 1, in the sense of Definition 2.2. Recalling Remark 2.1, this is equivalent to the fact that the sequence is spectrally distributed as 1.

Recent developments in preconditioning for all-at-once systems and inverse problems for FDEs are closely related to the present work. Li, Lin, Hon, and Wu [78] developed a preconditioned MINRES method for block lower triangular Toeplitz systems, which are ubiquitous in evolutionary PDE discretizations. More recently, Lin, Ke, Hon, and Ng [81] proposed a matching Schur complement preconditioning technique specifically designed for discrete time fractional diffusion ISPs, demonstrating its effectiveness in accelerating the convergence of Krylov methods. These works highlight the growing interest in structure-preserving preconditioners for all-at-once formulations, and the block triangular preconditioner proposed in this chapter builds upon this foundation.

