_Proof of Proposition 2(iii)_ Fix an item _i_ and a round _t_. By conjugacy, the posterior density of \(\eta_i\) given H_<sub>t</sub>_ is proportional to \(exp\{a\eta-bA_i(\eta)\}\), where

\(a=a_i+\sum_{n=1}^{N_i(t)}Y_{i,n},b=b_i+N_i(t).\)

The standard moment identity for this natural exponential family conjugate posterior gives \(\mu_i(t)=\frac{a}{b}\) (Diaconis and Ylvisaker 1979). Additionally,

\(0=\int_{\EuScript{E}_i}\frac{d}{d\eta}\left[\left(A'_i(\eta)-\frac{a}{b}\right)exp\{a\eta-bA_i(\eta)\}\right]d\eta,\)

which, after expanding the derivative and normalizing, gives

\(\mathbb{E}_t\left[A''_i(\eta_i)\right]=b\mathbb{E}_t\left[\left(A'_i(\eta_i)-\frac{a}{b}\right)^2\right]=bv_i(t).\)

Fix \(d\ge 1\), and let \(S_d=\sum_{n=1}^dY_{i,N_i(t)+n}\) denote the sum of the _d_ additional observations. Conditional on \(\eta_i\), \(\mathbb{E}_t\left[S_d|\eta_i\right]=dA'_i(\eta_i)=d\theta_i\) and \(\mathbb{V}_t\left(S_d|\eta_i\right)=dA''_i(\eta_i)\). Therefore, by the law of total variance,

\(\mathbb{V}_t(S_d)=\mathbb{E}_t\left[\mathbb{V}_t(S_d|\eta_i)\right]+\mathbb{V}_t\left(\mathbb{E}_t\left[S_d|\eta_i\right]\right)=dbv_i(t)+d^2v_i(t)=d(b+d)v_i(t).\)

After observing these additional samples, the posterior density of \(\eta_i\) is proportional to \(exp\left\{(a+S_d)\eta-(b+d)A_i(\eta)\right\}\) . Applying the same conjugate-posterior mean identity gives

\(\mathbb{E}\left[\theta_i|\mathcal{H}_t,S_d\right]=\frac{a+S_d}{b+d}.\)

Hence,

\(\mathbb{V}_t\left(\mathbb{E}\left[\theta_i|\mathcal{H}_t,S_d\right]\right)=\frac{\mathbb{V}_t(S_d)}{(b+d)^2}=\frac{d}{b+d}v_i(t).\)

Finally, the law of total variance gives

\(v_i(t)=\bar{v}_i(t,d)+\mathbb{V}_t\left(\mathbb{E}\left[\theta_i|\mathcal{H}_t,S_d\right]\right).\)

Therefore

\(c_i(t,d)^2=\frac{\bar{v}_i(t,d)}{v_i(t)}=\frac{b}{b+d}=\frac{1}{1+\frac{1}{b}d}.\)

Since _b=b<sub>i</sub>+N<sub>i</sub>(t)\>_0, (10) holds with \(\lambda_i(t)=\frac{1}{b_i+N_i(t)}\). □

## Appendix B: Closed forms for the conjugate families of Proposition 3

In each subsection, we first define the round-_t_ posterior parameters and then suppress their argument _t_ in the remaining formulas.

