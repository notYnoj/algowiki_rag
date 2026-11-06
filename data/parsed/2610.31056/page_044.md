## 7.3 Distribution of the sum of Integer random Variables

In the integer setting, we repeatedly encounter the distribution of a sum of a large number of i.i.d. integer-valued random variables. Local Central Limit Theorem (LCLT) gives a good approximation of this distribution. This theorem has been studied extensively in probability theory and statistics (see, e.g. \[IL65\], \[MU17\], \[LL10\], \[Fel91\]). In our analysis, we make use of the following corollary of the LCLT.

**Theorem 7.1.** \[_MU17_\] \[**_Sharper version of LCLT._**\] _Let X_<sub>1</sub>_,X_<sub>2</sub>_,...,X<sub>n</sub> be a sequence of I.I.D, distributed over the set_ \[_M_\] _for some integer_ \(M\ge 1\) _with_ \(\mathbb{E}(X_i)=\mu\) _and_ \(\mathsf{Var}(X_i)=\sigma^2<\infty\)_. Then there exists c_<sub>1</sub>_,c_<sub>2</sub>_,n_<sub>0</sub>_,C\>_0 _such that for all_ \(n\ge n_0\) _and for all integers k satisfying_<tbc>

\(|k-n\mu|\le C\sigma\sqrt{n}(\text{\textit{Central Window of Gaussian}}),\)

<tbc>_we have_<tbc>

\(\frac{c_1}{\sigma\sqrt{n}}\le\mathbb{P}\left(\bar{X}=k\right)\le\frac{c_2}{\sigma\sqrt{n}},\)

<tbc>_and hence_

\(\mathbb{P}\left(\bar{X}=k\right)=\Theta\left(\frac{1}{\sigma\sqrt{n}}\right).\)

**Remark 4.** _The assumptions of the local central limit theorem remain valid when M=M(n), since the variables remain uniformly bounded and their variance is strictly positive for all n._

Recall that, in the integer case, \(a_i^{(pq)}\in[0,pq)\) and \(a_i^{(r)}\in[0,r)\). These are integers and not field elements. Let \(\mu_{pq}\) and \(\sigma_{pq}^2\) denote the mean and the variance of the random variables \(a_i^{(pq)}\forall 1\le i\le n\), then we have

\(\mu_{pq}:=\mathbb{E}\left(a_i^{(pq)}\right)=\frac{pq-1}{2}=\Theta(pq),\)<br>
\(\sigma_{pq}^2:=\mathsf{Var}\left(a_i^{(pq)}\right)=\Theta((pq)^2)<\infty.\)

Since the random variable \(\{a_i^{(pq)}\}_{i=1}^n\) are I.I.D. and their variance is bounded, we can use Theorem 7.1 to compute the distribution of their sum as follows

**Corollary 1.** _For a fixed vector_ \(\mathbf{u}_i\in\mathsf{A}\) _with Hamming weight_ \(w_i=\Theta(n)\)_, for any_ \(s_{pq}=w_i\mu_{pq}+\mathcal{O}(\sigma_{pq}\sqrt{w_i})\) _we have the following_

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{TS},pq,i}=\mathbf{a}^{(pq)}\cdot\mathbf{u}_i=s_{pq}\right)=\Theta\left(\frac{1}{\sigma_{pq}\sqrt{w_i}}\right)\)<br>
\(=\Theta\left(\frac{1}{pq\sqrt{n}}\right).\)

Similarly, we can compute the distribution of the sum of the random variables \(\{a_i^{(r)}\}_{i=1}^n\). In analyzing the expectation of the random variable C<sup>(int)</sup>, the bottleneck problem is to understand the interdependency of the following events depending on the vector **a**<sup>(_pq_)</sup>,

• \(S_{\mathsf{LS},i}^{(p)}=\mathbf{a}^{(p)(L)}\cdot\mathbf{u}_i^{(L)}modp=k\),<tbc>

• \(S_{\mathsf{TS},i}^{(pq)}=\mathbf{a}^{(pq)}\cdot\mathbf{u}_i=l\),<tbc>

