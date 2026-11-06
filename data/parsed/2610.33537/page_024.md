## Appendix B. The hydrodynamic boundary conditions

Assume the solid wall has temperature \(\theta^W\) and velocity **_u_**_<sup>W</sup>_. For the case where the outward unit normal vector is **_n_**=_e_<sub>1</sub>=(1,0,0)<sup>T</sup>, let \([\rho^+,u^+,\theta^+]\) and \(\tilde{f}^+\) denote the updated interior macroscopic quantities and the moment solution, respectively. The ghost-cell macroscopic quantities \([\rho^g,u^g,\theta^g,\sigma^g,q^g]\) are obtained from the formulae in \[18\] as

\(\rho^g=\rho^+,u^g=u^++2(u_1^W-u_1^+)e_1,\theta^g=\theta^+,\sigma_{kk}^g=\tilde{\sigma}_{kk}^+(k=1,2,3),\sigma_{23}^g=\tilde{\sigma}_{23}^+,\)<br>
\(\sigma_{12}^g=\frac{4\chi}{2-\chi}\left(\sum_{k=0}^{\lfloor(M-1)/2\rfloor} S(1,2k)\left(\theta^+\right)^{\frac{1}{2}-k}\tilde{f}_{(2k,1,0)}^++\left(u_2^+-u_2^W\right)\sum_{k=0}^{\lfloor M/2\rfloor} S(1,2k)\left(\theta^+\right)^{\frac{1}{2}-k}\tilde{f}_{(2k,0,0)}^+\right)-\tilde{\sigma}_{12}^+,\)<br>
\(\sigma_{13}^g=\frac{4\chi}{2-\chi}\left(\sum_{k=0}^{\lfloor(M-1)/2\rfloor} S(1,2k)\left(\theta^+\right)^{\frac{1}{2}-k}\tilde{f}_{(2k,0,1)}^++\left(u_3^+-u_3^W\right)\sum_{k=0}^{\lfloor M/2\rfloor} S(1,2k)\left(\theta^+\right)^{\frac{1}{2}-k}\tilde{f}_{(2k,0,0)}^+\right)-\tilde{\sigma}_{13}^+,\)<br>
\(q_1^g=\frac{12\chi}{2-\chi}\left(\sum_{k=0}^{\lfloor M/2\rfloor} S(3,2k)\left(\theta^+\right)^{\frac{3}{2}-k}\tilde{f}_{(2k,0,0)}^++\left(\frac{\theta^+}{2}-\frac{\theta^W}{3}\right)\sum_{k=0}^{\lfloor M/2\rfloor} S(1,2k)\left(\theta^+\right)^{\frac{1}{2}-k}\tilde{f}_{(2k,0,0)}^+\right)-3\tilde{f}_{(3,0,0)}^+\)<br>
\(+\frac{4\chi}{2-\chi}\left(\sum_{k=0}^{\lfloor(M-2)/2\rfloor} S(1,2k)\left(\theta^+\right)^{\frac{1}{2}-k}\tilde{f}_{(2k,2,0)}^+-\frac{1}{2}\left((\theta^W-\theta^+)+(u_2^W-u_2^+)^2\right)\sum_{k=0}^{\lfloor M/2\rfloor} S(1,2k)\left(\theta^+\right)^{\frac{1}{2}-k}\tilde{f}_{(2k,0,0)}^+\right)-\tilde{f}_{(1,2,0)}^+\)<br>
\(+\frac{4\chi}{2-\chi}\left(\sum_{k=0}^{\lfloor(M-2)/2\rfloor} S(1,2k)\left(\theta^+\right)^{\frac{1}{2}-k}\tilde{f}_{(2k,0,2)}^+-\frac{1}{2}\left((\theta^W-\theta^+)+(u_3^W-u_3^+)^2\right)\sum_{k=0}^{\lfloor M/2\rfloor} S(1,2k)\left(\theta^+\right)^{\frac{1}{2}-k}\tilde{f}_{(2k,0,0)}^+\right)-\tilde{f}_{(1,0,2)}^+,\)<br>
\(q_2^g=\tilde{q}_2^+,q_3^g=\tilde{q}_3^+,\) (B.1)

where \(\chi=1\) is the accommodation coefficient. The stress tensor \(\tilde{\sigma}^+\) and heat flux \(\tilde{q}^+\) are computed from the expansion coefficients \(\tilde{f}_\alpha^+\) of \(\tilde{f}^+\). The function \(S(\cdot,\cdot)\) is defined recursively as

\(S(r,s)=\left\{\begin{array}{ c c }
1/2, & r=s=0, \\
K(1,s-1), & r=0,s\neq 0, \\
K(r,0), & r\neq 0,s=0, \\
K(r,s)+S(r-1,s-1)s/r, & \text{otherwise,}
\end{array}\right.\) (B.2)

where the auxiliary function \(K(\cdot,\cdot)\) is defined as

\(K(r,s)=\left\{\begin{array}{ c c }
\frac{(-1)^{(r+s-1)/2}(s-1)!!}{\sqrt{2\pi}r2^{(r-1)/2}((r-1)/2)!}, & r\text{is odd and}s\text{is even,} \\
0, & \text{otherwise.}
\end{array}\right.\) (B.3)

## Appendix C. Derivation of the Fourier convergence estimates

This appendix gives the details behind the Fourier-analysis results stated in section 3. We use the moment system (26)-(27), the hydrodynamic variables in (29), and the SGS iterations (31)-(34). Throughout the derivation, the parameters satisfy

\(0<\nu<1,C_{M+1}\ge\sqrt{3}.\) (C.1)

The first condition is the CFL restriction for the model, while the second holds automatically for \(M\ge 2\).

### Appendix C.1. Error evolution and the error-propagation matrix

We first clarify the relationship between \(\delta u_j^{(n+1)}\) and \(\delta u_j^{(n)}\), defined in (36). Recall that **_u_**_<sub>j</sub>_ is the exact discrete solution in (30). For one moment SGS iteration, define the errors before the forward sweep, after the forward sweep, and after the backward sweep by

\(e_j^{n,s}=u_j^{(n,s)}-u_j,e_j^{n,s+1/2}=u_j^{(n,s+1/2)}-u_j,e_j^{n,s+1}=u_j^{(n,s+1)}-u_j.\) (C.2)

