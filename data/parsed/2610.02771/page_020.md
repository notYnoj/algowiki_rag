**Lemma 17** (Epoch-wise stitched Bernstein bound)**.** _For each integer_ \(j\ge 0\)_, let_<tbc>

\(N_j:=2^{j+1},x_j(\gamma):=\mathrm{log}\big(\frac{\pi^2(j+1)^2}{3\gamma}\big).\)

<tbc>_Then_

\(\mathrm{Pr}\big(\exists n\in\{2^j,\dots,2^{j+1}-1\}:S_n\ge 2\sqrt{v_Lnx_j(\gamma)}+\frac{b_Lx_j(\gamma)}{3}\big)\le e^{-x_j(\gamma)}.\)

_Proof._ Fix \(j\ge 0\), and write<tbc>

\(N:=N_j=2^{j+1},x:=x_j(\gamma).\)

<tbc>By Ville’s inequality applied to the nonnegative supermartingale \(\{M_n(\lambda)\}_{n\ge 0}\) from Lemma 16, for every \(\lambda\in[0,3/b_L)\),<tbc>

\(\mathrm{Pr}(\exists n\le N:M_n(\lambda)\ge e^x)\le e^{-x}.\)

<tbc>Using the definition of \(M_n(\lambda)\), this is equivalent to<tbc>

\(\mathrm{Pr}(\exists n\le N:\lambda S_n-n\psi_L(\lambda)\ge x)\le e^{-x}.\)

<tbc>Now define the event<tbc>

\(A_\lambda:=\big\{\exists n\le N:S_n\ge\frac{x+N\psi_L(\lambda)}{\lambda}\big\}.\)

<tbc>If \(A_\lambda\) occurs, then for some \(n\le N\),<tbc>

\(\lambda S_n-n\psi_L(\lambda)\ge\lambda\cdot\frac{x+N\psi_L(\lambda)}{\lambda}-N\psi_L(\lambda)=x.\)

<tbc>Hence<tbc>

\(A_\lambda\subseteq\{\exists n\le N:\lambda S_n-n\psi_L(\lambda)\ge x\},\)

<tbc>and therefore<tbc>

\(\mathrm{Pr}(A_\lambda)\le e^{-x}.\)

<tbc>Equivalently,<tbc>

\(\mathrm{Pr}\big(\exists n\le N:S_n\ge\frac{x+N\psi_L(\lambda)}{\lambda}\big)\le e^{-x}\text{for all}\lambda\in[0,3/b_L).\)

<tbc>We now optimize the boundary over \(\lambda\). Set<tbc>

\(c_L:=\frac{b_L}{3}.\)

<tbc>Then<tbc>

\(\frac{x+N\psi_L(\lambda)}{\lambda}=\frac{x}{\lambda}+\frac{Nv_L\lambda}{2(1-c_L\lambda)}=:g(\lambda),0<\lambda<\frac{1}{c_L}.\)

<tbc>Differentiating,<tbc>

\(g'(\lambda)=-\frac{x}{\lambda^2}+\frac{Nv_L}{2(1-c_L\lambda)^2}.\)

<tbc>Setting \(g'(\lambda)=0\) gives<tbc>

\(\frac{x}{\lambda^2}=\frac{Nv_L}{2(1-c_L\lambda)^2}.\)

<tbc>Taking square roots and rearranging,<tbc>

\(\frac{\sqrt{x}}{\lambda}=\frac{\sqrt{Nv_L/2}}{1-c_L\lambda}\Longleftrightarrow\frac{1}{\lambda}=\sqrt{\frac{Nv_L}{2x}}+c_L.\)

<tbc>Thus the optimizer is<tbc>

\(\lambda_*=\frac{1}{\sqrt{Nv_L/(2x)}+c_L}.\)

