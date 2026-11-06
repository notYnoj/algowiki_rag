<tbc>Since \(\psi''_\beta(t)=\beta(\beta-1)t^{-1-\beta}\) and \(t_k=k\Delta t\), we get

\(\ell_k=(\Delta t)^{\beta+1}\beta(\beta-1)\frac{1}{(k\Delta t)^{1+\beta}}+(\Delta t)^{\beta+1}O((\Delta t)^2)\)<br>
\(=(\Delta t)^{\beta+1}\beta(\beta-1)\frac{1}{k^{1+\beta}(\Delta t)^{1+\beta}}+O((\Delta t)^{\beta+3})\)<br>
\(=\kappa\beta(\beta-1)\frac{1}{k^{1+\beta}}+O((\Delta t)^{\beta+3}).\)

Thus \(\ell_k=\frac{\beta(\beta-1)}{k^{1+\beta}}+O((\Delta t)^{\beta+3})\), so \(\ell_k\sim\frac{C}{k^{1+\beta}}\) as \(k\rightarrow\infty\) with \(C=\beta(\beta-1)\). Since \(\beta\in(0,1)\), we have \(1+\beta>1\), and therefore the series

\(\sum_{k=0}^\infty|\ell_k|\)

is convergent. Consequently, \(g_\beta\) belongs to the Wiener class. Hence \(g_\beta\) is continuous and \(2\pi\)-periodic, and \(B_M=T_M(g_\beta)\) by definition.

By **GLT1**, we conclude<tbc>

\(\{B_M\}_M\sim_{\mathrm{GLT},\sigma} g_\beta(\theta).\)

<tbc>Finally, all the eigenvalues of _B<sub>M</sub>_ are trivially equal to \(\ell_0=b_0\) because of the triangular structure, we have

\(\{B_M\}_M\sim_\lambda b_0.\)

This follows immediately from the definition of distribution.

**Remark 4.4.** _As it is evident from the final part of the proofs of Theorem_ (4.1) _and Theorem 4.3, the fact that the involved generating functions belong to the Wiener class is not a goal, but it is instrumental in applying the GLT axioms for deducing in a fast way the distribution in the sense of the singular values_

We are now ready to compute the GLT symbol of the sequence associated with the full coefficient matrix, shown in (7). To provide meaningful results, we introduce a mild assumption regarding the rate at which the discretization parameters tend to zero with respect to one another.

**Theorem 4.5.** _Let_ \(a:[0,1]\rightarrow\mathbb{R}\) _be continuous almost everywhere and let_ \(\gamma=\frac{\Gamma(2-\beta)(\Delta t)^\beta}{(\Delta x)^\alpha}\) , \(\gamma^*\) _as in Remark 4.2. Then_

(_c1)_ \(\{\mathcal{A}_{N,M}\}_{N,M}\sim_\mathrm{GLT}\gamma^*a(x)f_\alpha(\theta_1)+g_\beta(\theta_2)\),<tbc>

_(c2)_ \(\{\mathcal{A}_{N,M}\}_{N,M}\sim_\sigma\gamma^*a(x)f_\alpha(\theta_1)+g_\beta(\theta_2)\),

_with_ \(\mathcal{A}_{N,M}=B_M\otimes I_N+I_M\otimes\gamma\mathcal{D}_N(a)\overline{G_{\alpha,N}}\)_, where_ \(f_\alpha(\theta)=e^{-i\theta}(1-e^{i\theta})^\alpha\) _and_ \(g_\beta\) _is the symbol of B<sub>N</sub> from Theorem 4.3._

_Proof._ It is enough to prove (_c_1), since (_c_2) can be directly inferred from (_c_1) and **GLT1**. From The orem (4.1), we already know that the sequence of matrices {_G<sub>N</sub>}<sub>N</sub>_ is distributed in the GLT sense as \(\gamma^*a(x)f_\alpha(\theta_1)\). Moreover, by Theorem (4.3), the sequence {_B<sub>M</sub>}<sub>M</sub>_ admits the GLT symbol \(g_\beta(\theta_2)\). There fore, by combining these two GLT symbols through the Kronecker sum structure of A_<sub>N,M</sub>_ (see Axiom **GLT4**) and invoking the ∗-algebra property of the GLT class Axiom **GLT3**, part 2, we deduce that

\(\{\mathcal{A}_{N,M}\}_{N,M}\sim_\mathrm{GLT}\gamma^*a(x)f_\alpha(\theta_1)+g_\beta(\theta_2),\)

which establishes (_c_1). The statement (_c_2) then follows directly from (_c_1) and Axiom **GLT1**.

