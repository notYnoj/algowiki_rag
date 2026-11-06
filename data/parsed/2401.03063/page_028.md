Moreover,

\(\sum_{i\in(S(\overrightarrow{r})\cap I_{p_1,p_2}(\overrightarrow{r}))^c}\frac{N_i}{2}=\sum_{i\in(S(\overrightarrow{r}))^c\cap I_{p_1,p_2}(\overrightarrow{r})}\frac{N_i}{2}+\sum_{i\in(I_{p_1,p_2}(\overrightarrow{r}))^c}\frac{N_i}{2}\)<br>
\(\le\upsilon\frac{1+p_2}{2}\varepsilon m+\frac{\varepsilon n}{2}\)<br>
\(\le 2\varepsilon n,\)

and therefore,

\(LC_n\ge(1-2\varepsilon)(\gamma_2+\eta)n.\)

Given the choice of \(\varepsilon\), \((1-2\varepsilon)(\gamma_2+\eta)>\gamma_2\), so by concentration, this has probability exponentially small to happen. Therefore, \(\mathbb{P}\left((C_\varepsilon^n)^c\right)\le\mathbb{P}\left((C_\varepsilon^n)^c\cap B_{\varepsilon,p_1,p_2}^n\right)+\mathbb{P}\left((B_{\varepsilon,p_1,p_2}^n)^c\right)\) goes to zero (exponentially fast) as _n_ goes to infinity.

Now for \(i\in\{1,\dots,m\}\), let

\(V_i=max_{x\in\{0,1\}^v}\left|LCS(X_1\cdots X_{\upsilon(i-1)}x_1\cdots x_\upsilon X_{\upsilon i+1}\cdots X_n;Y_1\cdots Y_n)-LCS(X_1\cdots X_n;Y_1\dots Y_n)\right|.\)

But, for any \(i\in(S(\overrightarrow{r}))^c\), it follows that \(V_i\ge 1\), and so

\(\mathbb{E}\left(\frac{1}{m}\sum_{i=1}^mV_i^2\right)>\varepsilon\mathbb{P}(C_\varepsilon^n).\)

Now, for \(x\in\{0,1\}^v\) and \(j\in\{\upsilon(i-1)+1,\dots,\upsilon i\}\), let

\(\delta_j(x)=LCS(X_1\cdots X_{\upsilon(i-1)}x_1\cdots x_{j-\upsilon(i-1)}X_{j+1}\cdots X_n;Y_1\cdots Y_n)\)<br>
\(-LCS(X_1\cdots X_{\upsilon(i-1)}x_1\cdots x_{j-\upsilon(i-1)-1}X_j\cdots X_n;Y_1\cdots Y_n),\)

so that,

\(V_i^2=max_{x\in\{0,1\}^v}\left|\sum_{j=\upsilon(i-1)+1}^{\upsilon i}\delta_j(x)\right|^2\le max_{x\in\{0,1\}^v}\upsilon\sum_{j=\upsilon(i-1)+1}^{\upsilon i}\delta_j(x)^2\le\upsilon\sum_{j=\upsilon(i-1)+1}^{\upsilon i}max_{x\in\{0,1\}^v}\delta_j(x)^2.\)

Note that \(\mathbb{E}\Delta_j^2=\mathbb{E}\delta_j(X'_1,\dots,X'_\upsilon)^2\) (where \(\Delta_j\) is the difference in length between the original LCS and the LCS modified, via an independent copy of the variable at spot _j_, (see the next section for the precise definition of \(\Delta_j\))), and

\(\mathbb{E}_{X_1^\prime,\dots,X_\upsilon^\prime}\Delta_j^2\ge\frac{1}{2^\upsilon}max_{x\in\{0,1\}^v}\delta_j(x)^2.\)

Hence, \(\mathbb{E}\Delta_j^2\ge\mathbb{E}max_{x\in\{0,1\}^v}\delta_j(x)^2/2^\upsilon\), and so \(V_i^2\le\upsilon 2^\upsilon\sum_{j=\upsilon(i-1)+1}^{\upsilon i}\mathbb{E}\Delta_j^2\). Therefore,

\(\mathbb{E}\left(\frac{1}{m}\sum_{i=1}^mV_i^2\right)\le\frac{\upsilon 2^\upsilon}{m}\sum_{j=1}^n\mathbb{E}\Delta_j^2,\)

Finally,

\(\varepsilon\mathbb{P}(C_\varepsilon^n)<\upsilon^22^\upsilon B_1(2n),\)

and thus, for _n_ large enough, \(B_1(2n)>\varepsilon/2\upsilon^22^\upsilon\).

**Remark 4.6.** _The above result is a necessary condition (certainly not sufficient, though) to have VarLC<sub>n</sub> asymptotically linear. This implies that there exists_ \(C'>0\)_, such that for all n,_ \(B_1(2n)\ge C'\)_, as for all n, B_<sub>1</sub>(2_n)\>_0.

