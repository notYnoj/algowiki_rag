Then,

\(||\mathcal{E}_\alpha||_2\le c_0||\mathcal{R}_\alpha||_2=\alpha c_0\left(\sqrt{||L||_2^2+1}+1\right)=c_1\alpha.\)

The proof is complete.

**Theorem 13.** _For any constant_ \(\nu\in(0,1)\)_, choose_ \(\alpha\in(0,\eta]\) _with_<tbc>

\(\eta:=\mathrm{min}\left\{\frac{\nu^2}{c_1},\frac{1}{2}\right\},\)

<tbc>_where c_<sub>1</sub> _is defined in Lemma 12. Then, the MINRES solver for the preconditioned system (1.10) has a convergence rate independent of both_ \(\tau\) _and h, i.e.,_

\(||\tilde{\mathbf{r}}_k||_2\le 2\nu^{k-1}||\tilde{\mathbf{r}}_0||_2,k\ge 1,\)

_where_ \(\tilde{\mathbf{r}}_k=\mathcal{P}_\alpha^{-1}\mathcal{YT}\mathbf{u}_k-\mathcal{P}_\alpha^{-1}\mathcal{Y}\mathbf{f}\) _denotes the residual vector at kth MINRES iteration with_ **u**_<sub>k</sub> denoting the kth iterative solution by MINRES;_ \(\tilde{\mathbf{r}}_0\) _denotes the initial residual vector computed by an arbitrary real-valued initial guess_ **u**<sub>0</sub>.

**Proof:** By \(\alpha\in(0,\eta]\subset(0,1/2]\) and Lemma 12, we know that

\(\sigma(\mathcal{P}_\alpha^{-1}\mathcal{YT})\subset[-1-\alpha c_1,-1+\alpha c_1]\cup\left[1-\alpha c_1,1+\alpha c_1\right]\)<br>
\(\subset\left[-1-\frac{c_1\nu^2}{c_1},-1+\frac{c_1\nu^2}{c_1}\right]\cup\left[1-\frac{c_1\nu^2}{c_1},1+\frac{c_1\nu^2}{c_1}\right]\)<br>
\(=\left[-1-\nu^2,-1+\nu^2\right]\cup\left[1-\nu^2,1+\nu^2\right],\)

which together with Lemma 5 implies that

\(||\tilde{\mathbf{r}}_k||_2\le 2\left(\frac{\sqrt{(1+\nu^2)^2}-\sqrt{(1-\nu^2)^2}}{\sqrt{(1+\nu^2)^2}+\sqrt{(1-\nu^2)^2}}\right)^{[k/2]}||\tilde{\mathbf{r}}_0||_2\)<br>
\(=2\left(\nu^2\right)^{[k/2]}||\tilde{\mathbf{r}}_0||_2\)<br>
\(\le 2\left(\nu^2\right)^{\frac{k}{2}-\frac{1}{2}}||\tilde{\mathbf{r}}_0||_2=2\nu^{k-1}||\tilde{\mathbf{r}}_0||_2.\)

The proof is complete.

**Remark 3.** _As indicated in Theorem 13, the convergence rate bound (i.e.,_ \(\nu\)_) of the MINRES solver can be taken as a constant independent of matrix size. For such a fixed_ \(\nu\)_, the corresponding_ \(\eta\) _needs to be of_ \(\mathcal{O}(\frac{1}{c_1})\)_, where c_<sub>1</sub> _defined in Lemma 12 depends on both c_<sub>0</sub> _and_ ||_L_||<sub>2</sub>_. Clearly,_ ||_L_||<sub>2</sub> _depends on m (the number of spatial grid points). Meanwhile, c_<sub>0</sub> _defined in Lemma 10 depends on n (the number of time steps). To summarize, setting_ \(\eta=\mathrm{min}\left\{\nu^2/c_1,1/2\right\}\) _for some constant_ \(\nu\in(0,1)\) _and taking_ \(\alpha\in(0,\eta]\) _leads to a matrix-size independent convergence rate bound of the MINRES solver._

