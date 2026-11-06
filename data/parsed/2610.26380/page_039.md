<tbc>**Algorithm A.1** Approximate Knowledge Gradient with order-_w_ truncation (AKGw)

**Input:** \(\unknown_{t-1}\), \(\Sigma_{t-1}\), round budget _B<sub>t</sub>_, remaining total budget _R_<sub>rem</sub> (initially _R_), excess from the previous round (initially zero), and _w_

1: \(B_\mathrm{rem}\leftarrow B_t\) - excess

2: \(n\leftarrow 0\), \(U\leftarrow 0\), \(\Sigma'_t(0)\leftarrow\Sigma_{t-1}\)

3: Compute (_q<sub>t</sub>,b<sub>t</sub>_) via Corollary 1

4: **while** _B_<sub>rem</sub>_\>_0 **and** \(R_\mathrm{rem}\ge\mathrm{min}(r_0,r_1)\)

5: \((i,j)\leftarrow\mathrm{argmax}_{(i,j)\in\mathcal{I}:r_j\le R_\mathrm{rem}}\frac{\Delta_n^{(w)}((i,j))}{r_j}\triangleright\) (A.5)

6: **if** \(\Delta_n^{(w)}((i,j))=0\)

7: \((i,j)\leftarrow\mathrm{argmax}_{(i,j)\in\mathcal{I}:r_j\le R_\mathrm{rem}}\psi_{t,ij}(n)\)

8: Update the covariance from \(\Sigma'_t(n)\) to \(\Sigma'_t(n+F^{ij})\) by (12)

9: \((i_{U+1},j_{U+1})\leftarrow(i,j)\), \(U\leftarrow U+1\), \(n\leftarrow n+F^{ij}\)

10: \(B_\mathrm{rem}\leftarrow B_\mathrm{rem}-r_j\), \(R_\mathrm{rem}\leftarrow R_\mathrm{rem}-r_j\)

11: \(\mathrm{excess}\leftarrow\mathrm{max}\{0,-B_\mathrm{rem}\}\)

12: **return** _n(t)=n,R_<sub>rem</sub>, and excess

when the round budget is spent or no evaluation is affordable, and the output is the batch’s count matrix _n_. The endgame batch-building procedure, which we call AKGw, is summarized in Algorithm A.1.

The choice of _w_ depends on how large the problem is, and on the time and computational resources available. With a current batch of size \(U\ge w-1\), the computation of (A.5) for all candidate evaluations is dominated by computing \(|\mathcal{I}|\genfrac(){pt}{2}{U}{w-1}2^ww\)-dimensional multivariate normal CDFs. The method is therefore tractable either when the batch size _U_ is small (for example, with a small _B<sub>t</sub>_) or when _w_ is sufficiently small (in our simulations, we use _w=_3).

## A.2.4. Proof of Proposition A.1

_Proof._ Fix a round _t_, a candidate batch (_i_<sub>1</sub>_,j_<sub>1</sub>)_,...,(i<sub>U</sub>,j<sub>U</sub>_), with count matrix _n_, and an outcome vector \(x=(x_1,\dots,x_U)^\top\in\{-1,1\}^U\). Recall that _j<sub>u</sub>_:=min(1_,j<sub>u</sub>),e_<sub>0</sub>:=**0**. For each _u=_1_,...,U_, introduce the latent Gaussian variable<tbc>

\(Z_u=\beta_{j_u}\left[(e_{i_u}-e_{j_u})^\top\theta-\theta_0\unknown\{j_u=0\}\right]+\varepsilon_u,\)

<tbc>where \(\varepsilon=(\varepsilon_1,\dots,\varepsilon_U)^\top\sim N(\mathbf{0},I_U)\) is independent of \(\theta\). Then<tbc>

\(X_u=1\Longleftrightarrow Z_u\ge 0,X_u=-1\Longleftrightarrow Z_u<0.\)

<tbc>Under the prior \(p_{t-1}(\cdot)=N(\unknown_{t-1},\Sigma_{t-1})\), the vector \(Z=(Z_1,\dots,Z_U)^\top\) is multivariate normal. Its mean vector is \(m=(m_1,\dots,m_U)^\top\), with<tbc>

\(m_u=\mathbb{E}[Z_u]=\beta_{j_u}(\mu_{t-1,i_u}-\mu_{t-1,j_u}).\)

<tbc>Its covariance matrix is \(C\in\mathbb{R}^{U\times U}\) with<tbc>

\(C_{uu^\prime}=\mathrm{Cov}(Z_u,Z_{u^\prime})=\beta_{j_u}\beta_{j_{u^\prime}}(e_{i_u}-e_{j_u})^\top\Sigma_{t-1}(e_{i_{u^\prime}}-e_{j_{u^\prime}})+\unknown\{u=u'\}.\)

<tbc>Define

\(D=\mathrm{diag}\left(\sqrt{C_{11}},\dots,\sqrt{C_{UU}}\right),D_x=\mathrm{diag}(x_1,\dots,x_U),\widetilde{C}_x=D_xD^{-1}CD^{-1}D_x.\)

