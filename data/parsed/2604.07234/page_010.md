<tbc>property for the distribution of \((\sigma,\tau)\sim\Sigma^2\) : if we select indices \(i\in[N]\) and \(j\in[M]\) and condition on the event that \(\sigma(j)=\tau(j)=i\), then the pairs<tbc>

\((\sigma|_{[j-1]},\tau|_{[j-1]}),(\sigma|_{[M]\backslash[j]},\tau|_{[M]\backslash[j]})\)

<tbc>become conditionally independent and, after a trivial relabeling, uniform in \(\Sigma_{i-1,j-1}^2,\Sigma_{N-i,M-j}^2\), respectively. This leads to a recursive structure for the moment generating function which underlies the proof of Lemma 4.1. This lemma proves the formula<tbc>

(1.11) \(\sum_{\sigma,\tau\in\Sigma} 2^{\langle\sigma,\tau\rangle}=\sum_{\ell=0}^M\sum_{1\le j_1<\cdots<j_\ell\le M}\sum_{1\le i_1<\cdots<i_\ell\le N}\prod_{k=1}^{\ell+1}\genfrac(){pt}{2}{i_k-i_{k-1}-1}{j_k-j_{k-1}-1}^2\)

<tbc>where we define _i_<sub>0</sub>=_j_<sub>0</sub>=0 and \(i_{\ell+1}=N+1,j_{\ell+1}=M+1\). The benefit of this formula is that the expression inside the summand depends on the tuples \((j_1,\dots,j_\ell)\) and \((i_1,\dots,i_\ell)\) only through the empirical measure<tbc>

\(\mu=\frac{1}{\ell+1}\sum_{k=1}^{\ell+1}\delta_{(i_k-i_{k-1},j_k-j_{k-1})}\)

<tbc>supported on \(\mathbb{N}_{>0}^2\). This is finite-dimensional, so as \(N,M\rightarrow\infty\), (1.11) turns into a constrained variational problem in the space of probability measures in \(\mathbb{N}_{>0}^2\). Indeed, the limit of the log of (1.11) normalized by _N_ is shown to be<tbc>

\(\mathsf{R}(\alpha)=sup_{\rho\in(0,1)}\alpha\rho\Phi(\rho),\)

<tbc>where for each fixed \(\rho\), the inner quantity \(\Phi(\rho)\) is the supremum of<tbc>

\(H(\nu)+\mathbb{E}_\nu[logw(a,b)],\)

<tbc>where _H_ is the Shannon entropy and \(w(a,b)=\genfrac(){pt}{2}{a-1}{b-1}^2\), over probability measures \(\nu\) supported in \(\mathbb{N}_{>0}^2\) satisfying the mean constraints

\(\mathbb{E}_{(a,b)\sim\nu}[a]=\frac{1}{\alpha\rho},\mathbb{E}_{(a,b)\sim\nu}[b]=\frac{1}{\rho}.\)

Conceptually, this is the heart of the proof: all of the combinatorics has now been absorbed into a finite- dimensional order parameter, namely the law solving the variational problem \(\Phi(\rho)\).

The second half of the argument is to solve this variational problem explicitly. For fixed \(\rho\), one introduces Lagrange multipliers for the normalization and moment constraints. This shows that the maximizing measure must lie in an exponential family:<tbc>

\(\nu^*(a,b)\propto w(a,b)x^ay^b\)

<tbc>for suitable parameters _x,y\>_0. Thus the optimization is encoded by a two-variable partition function

\(Z(x,y)=\sum_{a\ge 1}\sum_{1\le b\le a}w(a,b)x^ay^b.\)

The value of the variational problem can then be expressed in terms of log_Z(x,y_) together with the moment constraints. The next step is therefore analytic rather than probabilistic: one computes _Z(x,y_) in closed form. This is done by rewriting the sum using Vandermonde’s identity and then evaluating the resulting generating function explicitly.

Once the inner variational problem over \(\nu\) has been solved, one returns to the outer optimization in \(\rho\). Here the key observation is that at an interior optimizer, the envelope theorem implies that the derivative of the outer objective is proportional to log_Z(x,y_). Hence optimality forces the normalization condition

\(Z(x,y)=1.\)

This is what collapses the remaining optimisation to a purely algebraic system. Combining the equation _Z(x,y_)=1 with the stationarity relation coming from the moment constraints yields two equations in the

