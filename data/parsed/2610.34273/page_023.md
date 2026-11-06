_where_ \(H(\theta)=-\sum_{i=1}^s\theta_iln\theta_i\) _and_ 0ln0=0.

_Proof._ Put \(p=p_{k-1,k}^{(\phi)}\). Lemma 4.4, proved in Subsection 4.1, gives \(\phi(E_{k-1,k}^{(q)})=q^p\) for every positive integer _q_. We use only this single-edge property here.

First suppose that all entries of \(\theta\) are rational, and let _N_ range through positive multiples of their common denominator. Define the set of sector words<tbc>

\(\mathcal{W}_N=\{w\in\{1,\dots,s\}^N:|\{r:1\le r\le N,w_r=i\}|=N\theta_i\text{for every}1\le i\le s\}.\)

<tbc>On each of the last two legs of \(A^{\otimes_KN}\), project onto the coordinate sectors whose words belong to W_<sub>N</sub>_. Supported terms have the same word on these two legs, because each factor of _A_ has matched sectors. Thus the resulting restriction \(B_N\unknown A^{\otimes_KN}\) has

\(M_N=|\mathcal{W}_N|=\frac{N!}{\prod_{i=1}^s(N\theta_i)!}\)

matched sectors and still shares its first _k_-2 legs. The counting formula follows by choosing the \(N\theta_1\) positions of label 1, then the \(N\theta_2\) positions of label 2, and continuing through label _s_.

The block corresponding to \(w\in\mathcal{W}_N\) is \(\otimes_{Kr=1}^NA_{w_r}\). It contains exactly \(N\theta_i\) copies of _A<sub>i</sub>_ for every \(1\le i\le s\). Reordering these factors induces coordinate permutations within each leg, so every block has the same spectral value \(C_N=\prod_{i=1}^s\phi(A_i)^{N\theta_i}\). Apply Theorem 3.1 to _B<sub>N</sub>_. Spectral monotonicity under restriction and degeneration, followed by additivity and multiplicativity, gives

\((2k-1)M_N\phi(A)^N\ge(2k-1)M_N\phi(B_N)\)<br>
\(\ge M_NC_N\phi(E_{k-1,k}^{(M_N)})\)<br>
\(=M_N^{1+p}C_N.\)

Canceling _M<sub>N</sub>_ and taking _N_-th roots yields

\(\phi(A)\ge(2k-1)^{-1/N}M_N^{p/N}\prod_{i=1}^s\phi(A_i)^{\theta_i}.\)

To evaluate the limit, Stirling’s formula gives ln(_m_!)=_m_ln_m-m+O_(ln(_m_+1)) for nonnegative integers _m_, with 0ln0=0. Since _s_ and \(\theta\) are fixed and \(\sum_{i=1}^s\theta_i=1\), we obtain

\(lnM_N=NlnN-N-\sum_{i=1}^s\big(N\theta_iln(N\theta_i)-N\theta_i\big)+O(sln(N+1))\)<br>
\(=-N\sum_{i=1}^s\theta_iln\theta_i+O(sln(N+1)).\)

Consequently, \(N^{-1}lnM_N\rightarrow H(\theta)\). Letting _N_ tend to infinity through the permitted multiples proves the desired inequality for rational probability vectors. Spectral monotonicity is applied to each fixed degeneration before taking this limit; Lemma 2.17 allows its degree to depend on _N_.

Finally, every _A<sub>i</sub>_ is nonzero, so \(\phi(A_i)\ge 1\). The function \(\theta\mapsto H(\theta)\) is continuous on the probability simplex, since \(xlnx\rightarrow 0\) as \(x\rightarrow 0^+\). The function \(\theta\mapsto\prod_{i=1}^s\phi(A_i)^{\theta_i}\) is also continuous there. Every probability vector is a limit of rational probability vectors, so the inequality extends to all \(\theta\) by continuity.

