The polynomial-time LP decoder attains cut fractions approaching \(b_q\big(p_\mathrm{LP}^\mathrm{cert}(D,c)\big)\) by Corollary 2 and Theorem 1. For _q\>_2, the sharper lower bound above uses minimum-weight decoding, which is NP-hard in general.

We first compare DQI performance to the classical vector algorithm of Thompson, Parekh, and Marwaha (TPM) \[TPM22\], followed by Gaussian rounding \[FJ97\]. We observe that TPM gives a larger improvement at large degree on the same ensemble. As the girth grows, the inner product of adjacent unit vectors tends to \(\sigma_D=-2\sqrt{D-1}/D\). Assigning each vertex the label with largest inner product among _q_ independent standard Gaussian vectors gives the limiting expected cut fraction

\(T_q(D)=1-q\int_{\mathbb{R}^2}\phi_{\sigma_D}(x,y)\Phi_{\sigma_D}(x,y)^{q-1}dxdy,\sigma_D=-\frac{2\sqrt{D-1}}{D},\) (94)

where \(\phi_\sigma\) and \(\Phi_\sigma\) are the standard bivariate Gaussian density and distribution function with correlation \(\sigma\). The integral is the probability that one specified label wins at both endpoints. For _q_=2, \(T_2(D)=\mathrm{arccos}(\sigma_D)/\pi\). Expanding at zero correlation gives, with independent _Z<sub>a</sub>_∼N(0,1),

\(T_q(D)=\frac{q-1}{q}+\frac{\kappa_q}{\sqrt{D}}+O_q(D^{-1}),\kappa_q=\frac{2}{q-1}\left(\unknown\mathrm{max}_{1\le a\le q}Z_a\right)^2>0.\) (95)

This exceeds the _O<sub>q</sub>(D_<sup>-1</sup>) improvement of reliably decoded DQI at large _D_. The TPM limit also exceeds _U<sub>q</sub>(D_) at every parameter pair in  3.

Second, we compare DQI with simulated annealing (SA). We start each run from a uniformly random assignment and return the best assignment visited. A sweep visits every vertex, proposing a uniformly chosen different label and accepting it by the Metropolis rule, with energy equal to the number of unsatisfied constraints. The inverse temperature increases linearly between sweeps, with endpoints chosen on separate tuning instances. For Max-_k_-Cut, the same evaluation graphs are used for every field at a given degree; their sizes, girth, and sampling errors are given in  3.

