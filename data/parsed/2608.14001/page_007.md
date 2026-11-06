<tbc>possible choices, meaning that generically aliasing should not be a significant issue. And, like the the case of \(\mathbf{T}_{2,\ell}\), when extending to general \(\mathbf{T}_{3,\ell}\), increasing the lags can provide more diverse information that addresses the aliasing problem.

For _m\>_3, the determinant of (14) only becomes more complicated since the non-uniform sampling adds more conditions involving rational functions in combinatorial fashion.

Although the above conjecture may be difficult to prove for larger _m_ and \(\ell\) values, we will show that it is possible to derive explicit analytical results for an upper bound-but unfortunately not for the more important lower bound-on the scaled determinant of **T** (14) for all \(\ell\), which will at least ensure we avoid **T** being non-singular from having unbounded singular values. In addition, we can establish positive results in the asymptotic regime as \(\ell\rightarrow\infty\) for the scaled determinant of **T**, its condition number and its rank. Finally, we perform numerical simulations to generate empirical results as another means of supporting the conjecture.

_Definition 4:_ Let \(\mathbf{T}\in\mathbb{C}^{\ell\times m}\) be a generalized Vandermonde matrix as in (14). We say the _pseudo-transfinite diameter_ is:

\(\tilde{d}_m(\mathbf{T})=\left(det\left(\left(\sqrt{\frac{m}{\ell}}\mathbf{T}^H\right)\left(\sqrt{\frac{m}{\ell}}\right)\mathbf{T}\right)^{1/2}\right)^{1/\genfrac(){pt}{2}{m}{2}}\) (19)

If we define \(\mathbf{S}=\left(\sqrt{\frac{m}{\ell}}\mathbf{T}^H\right)\left(\sqrt{\frac{m}{\ell}}\mathbf{T}\right)\), then \(\tilde{d}_m(\mathbf{T})=\left(det(\mathbf{S})^{1/2}\right)^{1/\genfrac(){pt}{2}{m}{2}}\).

The intuition of why \(\sqrt{m/\ell}\) is an appropriate scaling factor for **T** in the above definition relates to the total "energy" of the matrix, which is connected to the Frobenius norm. The Frobenius norm of a matrix \(\mathbf{T}\in\mathbb{C}^{\ell\times m}\) with entries _T<sub>pk</sub>_ is related to the sum of its squared entries and the trace of **T**_<sup>H</sup>_**T**:<tbc>

\(\|\mathbf{T}\|_F^2=\sum_{p=1}^m\sum_{k=1}^\ell T_{pk}^2=tr(\mathbf{T}^H\mathbf{T})\) (20)

<tbc>The Frobenius norm of \(\sqrt{m/\ell}\mathbf{T}\) is then:

\(\left\|\sqrt{\frac{m}{\ell}}\mathbf{T}\right\|_F^2=\sum_{p=1}^m\sum_{k=1}^\ell\frac{m}{\ell}T_{pk}^2=\sum_{p=1}^m\left(\frac{1}{\ell}\sum_{k=1}^\ell T_{pk}^2\right)\) (21)

In effect, the scaling factor \(\sqrt{m/\ell}\) averages the total energy contribution of the \(T_{pk}^2\) terms over the number of lags \(\ell\) used and rescales that average by _m_ to be comparable to the behavior of the case when \(\ell=m\).

To analyze **T**, we have the following lemma about the entries of **S**.

_Lemma 1:_ Let \(\mathbf{S}=(m/\ell)\mathbf{T}^H\mathbf{T}\) with **T** as in (14) and entries _s<sub>pq</sub>_ with \(p,q\in\{1,\dots,m\}\). Then the entries of **S** are:<tbc>

\(s_{pp}=ms_{pq}=\frac{m}{\ell}\sum_{k=1}^\ell e^{-i(\theta_p-\theta_q)\tau_k}\) (22)

<tbc>and the radii of the Gerschgorin discs of **S** are:<tbc>

\(R_p:=\sum_{q=1,p\neq q}^m|s_{pq}|=\sum_{q=1,p\neq q}^m\left|\frac{m}{\ell}\sum_{k=1}^\ell e^{-i(\theta_p-\theta_q)\tau_k}\right|\) (23)

<tbc>_Proof:_ For \(\mathbf{S}=(m/\ell)\mathbf{T}^H\mathbf{T}\) with **T** as in (14), the diagonal entries of **S**, denoted by _s<sub>pp</sub>_, are:

\(s_{pp}=\frac{m}{\ell}\sum_{k=1}^\ell\bar{z}_p^{\tau_k}z_p^{\tau_k}=\frac{m}{\ell}\sum_{k=1}^\ell\left(\bar{z}_pz_p\right)^{\tau_k}\) (24)

When \(z_p=e^{i\theta_p}\), then \(\bar{z}_p=e^{-i\theta_p}\), \(\bar{z}_pz_p=1\), in which case \(s_{pp}=(m/\ell)\cdot\ell=m\). The off-diagonal entries of **S** are:

\(s_{pq}=\frac{m}{\ell}\sum_{k=1}^\ell\bar{z}_p^{\tau_k}z_q^{\tau_k}=\frac{m}{\ell}\sum_{k=1}^\ell e^{-i(\theta_p-\theta_q)\tau_k}\) (25)

Summing over the _qs_ in each row excluding the diagonal terms yields the expression for _R<sub>p</sub>_.

We prove in the next theorem that the pseudo-transfinite diameter as in Definition 4 is bounded above and that the bound converges to 1 at a sub-linear rate based on the number of points _m_. This ensures the generalized determinant of **T** is bounded and that **T** cannot be non-singular due to unbounded singular values. The result applies for any choice of lag \(\ell\).

_Theorem 4:_ Let \(\mathbf{T}\in\mathbb{C}^{\ell\times m}\) be as in (14). Consider points \(z_p=e^{i\theta_p}\) for \(p\in\{1,\dots,m\}\) where the \(\{\theta_p\}_{p=1}^m\in\mathbb{R}\) are distinct. Let \(\{\tau_k\}_{k=1}^\ell>0\) be a set of distinct powers. Then,

\(\tilde{d}_m(\mathbf{T})\le m^{1/(m-1)}\) (26)

and \(\tilde{\tau}(\mathbf{T}):=lim_{m\rightarrow\infty}\tilde{d}_m(\mathbf{T})=1\).

_Proof:_ For a given \(\mathbf{T}\in\mathbb{C}^{\ell\times m}\), let \(\mathbf{S}=\left(\sqrt{\frac{m}{\ell}}\mathbf{T}^H\right)\left(\sqrt{\frac{m}{\ell}}\mathbf{T}\right)\). By Lemma 1, _s<sub>pp</sub>=m_. Then:<tbc>

\(tr(\mathbf{S})=\sum_{p=1}^ms_{pp}=\sum_{p=1}^mm=m^2\)

<tbc>Since \(\mathbf{S}=(m/\ell)\mathbf{T}^H\mathbf{T}\), \(tr(\mathbf{S})=(m/\ell)tr(\mathbf{T}^H\mathbf{T})\), which, when combined with the above expression, yields:

\(tr(\mathbf{T}^H\mathbf{T})=m\ell\) (27)

Next, we consider \(\tilde{d}_m(\mathbf{T})\), beginning with det(**S**)<sup>1/2</sup>. (Note that when \(m=\ell\), det(**S**)<sup>1/2</sup>=det(**T**), as expected, and, when **T** is as in (10), (19) is equivalent to (12) as desired.) For the generalized case where \(m\neq\ell\) and **T** is as in (14):

\(det(\mathbf{S})^{1/2}=det\left(\left(\frac{m}{\ell}\right)\mathbf{T}^H\mathbf{T}\right)^{1/2}=\left(\frac{m}{\ell}\right)^{m/2}\left(\prod_{p=1}^m\lambda_p(\mathbf{T}^H\mathbf{T})\right)^{1/2}=\left(\frac{m}{\ell}\right)^{m/2}\prod_{p=1}^m\sigma_p(\mathbf{T})\text{(28)}\)

By the Geometric Mean - Quadratic Mean inequality, applicable to a set of real numbers greater than 0, which is certainly true for the set of singular values \(\{\sigma_p(\mathbf{T})\}_{p=1}^m\):

\(\prod_{p=1}^m\sigma_p(\mathbf{T})\le\left(\frac{1}{m}\sum_{p=1}^m\sigma_p(\mathbf{T})^2\right)^{m/2}\) (29)

