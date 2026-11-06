<tbc>is strictly concave on the convex set of probability measures satisfying the moment constraints since _H_ is strictly concave and \(\mathbb{E}_\nu[\mathrm{log}w]\) is linear in \(\nu\). Furthermore, for any probability measure \(\nu\) satisfying these constraints, it follows from \(w(a,b)\le 4^a\) that<tbc>

\(\mathbb{E}_\nu[\mathrm{log}w]\le(\mathrm{log}4)\mathbb{E}_\nu[a]=(\mathrm{log}4)/(\alpha\rho)<\infty\)

<tbc>and, letting (_A,B_) be a random vector with law \(\nu\),<tbc>

\(H(\nu)=H(A,B)=H(A)+H(B|A)\le H(A)+\mathbb{E}\left[\mathrm{log}A\right]<\infty,\)

<tbc>so the evaluation of the functional at any such \(\nu\) is finite. Introducing Lagrange multipliers \(\lambda_0\) for the normalization constraint \(\sum_{a,b}\nu(a,b)=1\), \(\lambda_1\) for \(\mathbb{E}_\nu[a]=1/(\alpha\rho)\), and \(\lambda_2\) for \(\mathbb{E}_\nu[b]=1/\rho\), the first-order condition<tbc>

\(\frac{\partial}{\partial\nu(a,b)}\big[H(\nu)+\mathbb{E}_\nu[\mathrm{log}w]-\lambda_0\big(\sum\nu-1\big)-\lambda_1\big(\mathbb{E}_\nu[a]-1/(\alpha\rho)\big)-\lambda_2\big(\mathbb{E}_\nu[b]-1/\rho\big)\big]=0\)

<tbc>gives \(-\mathrm{log}\nu(a,b)-1+\mathrm{log}w(a,b)-\lambda_0-\lambda_1a-\lambda_2b=0\), hence

\(\nu^*(a,b)=\frac{w(a,b)e^{-\lambda_1a}e^{-\lambda_2b}}{Z'},\)

where \(Z'=e^{1+\lambda_0}\) ensures normalization. It can be shown that

(1) the Lagrange multiplier equations admit a solution, i.e., corresponding values \(\lambda_0^*\), \(\lambda_1^*\), and \(\lambda_2^*\) for which the normalization and coordinate mean constraints are satisfied;<tbc>

(2) the corresponding measure \(\nu^*\) is the unique global maximizer of the objective functional.<tbc>

<tbc>We do this in Appendix E. Letting \(\big(\lambda_1^*,\lambda_2^*\big)\) denote corresponding such values, setting the values \(x:=e^{-\lambda_1^*}\) and \(y:=e^{-\lambda_2^*}\) yields the form (4.26) with \(Z'=Z(x,y)\).

To evaluate the optimal value, we substitute this optimizer into the objective and then approximate it by admissible measures. Since<tbc>

\(\mathrm{log}\nu^*(a,b)=\mathrm{log}w(a,b)+a\mathrm{log}x+b\mathrm{log}y-\mathrm{log}Z,\)

<tbc>substituting \(\nu^*\) into the functional to get \(H(\nu^*)+\mathbb{E}_{\nu^*}[\mathrm{log}w]\) yields that<tbc>

\(H(\nu^*)+\mathbb{E}_{\nu^*}[\mathrm{log}w]=-\mathbb{E}_{\nu^*}[\mathrm{log}\nu^*]+\mathbb{E}_{\nu^*}[\mathrm{log}w]=\mathrm{log}Z-(\mathrm{log}x)\mathbb{E}_{\nu^*}[a]-(\mathrm{log}y)\mathbb{E}_{\nu^*}[b],\)

<tbc>which is (4.27). Though \(\nu^*\) itself does not have finite support, we may approximate it via a sequence of finitely supported probability measures satisfying the moment constraints. Specifically, we define<tbc>

\(\mu_n(\cdot):=\nu^*\big(\cdot|E_n\big);E_n:=\left\{(a,b)\in\mathbb{N}_{>0}^2:b\le a\le n\right\}.\)

<tbc>It directly follows from this construction that<tbc>

\(\mathbb{E}_{\mu_n}[a]\rightarrow\mathbb{E}_{\nu^*}[a]=1/(\alpha\rho);\mathbb{E}_{\mu_n}[b]\rightarrow\mathbb{E}_{\nu^*}[b]=1/\rho.\)

<tbc>Therefore, we may construct a sequence of probability measures \(\nu_n\) supported on the three tuples<tbc>

\((1,1),(2/\lfloor\alpha\rho\rfloor,1),(2/\lfloor\alpha\rho\rfloor,2/\lfloor\alpha\rho\rfloor)\)

<tbc>such that there exist values \(\epsilon_n\rightarrow 0\) for which the mixture probability measure<tbc>

\(\nu_n^*:=(1-\epsilon_n)\mu_n+\epsilon_n\nu_n\)

<tbc>satisfies the mean constraints \(\mathbb{E}_{\nu_n}[a]=1/(\alpha\rho)\) and \(\mathbb{E}_{\nu_n}[b]=1/\rho\). Then, we have that

\(\big(H(\nu^*)+\mathbb{E}_{\nu^*}[\mathrm{log}w]\big)-\big(H(\nu_n)+\mathbb{E}_{\nu_n}[\mathrm{log}w]\big)=^\text{(E.3)}D_\text{KL}\big(\nu_n\big\|\nu^*\big)\)<br>
\(\le(1-\epsilon_n)D_\text{KL}\big(\mu_n\big\|\nu^*\big)+\epsilon_nD_\text{KL}\big(\nu_n\big\|\nu^*\big)=-(1-\epsilon_n)\mathrm{log}\nu^*(E_n)+\epsilon_nD_\text{KL}\big(\nu_n\big\|\nu^*\big)\checkmark 1.\)

This yields (4.27). □

