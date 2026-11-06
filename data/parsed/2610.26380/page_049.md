<tbc>Note that \(\mathbf{1}^\top\mathbf{b}_t=1\), which gives the following

\(\mathbf{g}_{t,i}\in\mathbf{1}^\perp,\mathbf{g}_{t,i}-\mathbf{g}_{t,j}=\mathbf{e}_i-\mathbf{e}_j,\mathrm{span}\{\mathbf{g}_{t,1},\dots,\mathbf{g}_{t,I}\}=\mathbf{1}^\perp\text{for every}t,\)

used repeatedly below.

For \(L\in\mathcal{D}\), let \(\alpha_t(L)\) and \(\delta_t(L)\) denote the quantities \(\alpha_{t,ij}\) and \(\delta_{t,ij}\) in Lemma 2 for the corresponding evaluation. The marginal score of SA can be written in unified form as

\(G_t(L):=\frac{1}{r_L}\sum_{i:\sigma_{t-1,i}>0}\int_0^\frac{\delta_{t\left(L\right)}\left(\mathbf{g}_{t,i}^\top\Sigma_{t-1}L\right)^2}{\sigma_{t-1,i}^2L^\top\Sigma_{t-1}L}\frac{\sigma_{t-1,i}}{2\sqrt{1-s}}\phi\left(\frac{z_{t-1,i}}{\sqrt{1-s}}\right)ds.\) (D.1)

This is (11) for the corresponding evaluation, with any zero-variance summand omitted because its contribution is zero.

Define the realized opportunity cost after _T_ rounds by

\(\mathrm{OC}_T:=\sum_{i\in S_k^*(\theta)}\theta_i-\sum_{i\in S_k^*(\mu_T)}\theta_i.\)

Thus, the conclusion of Theorem 2 is \(\mathbb{E}[\mathrm{OC}_T]\rightarrow 0\) as \(R\rightarrow\infty\).

## D.2. Proof roadmap

There are two main components to the proof. The first, and far more technical, is to argue that the set of directions the algorithm samples infinitely many times contains the decision-relevant subspace \(\mathbf{1}^\perp\) in its span. The second component then argues that, if this is the case, the full history identifies \(P\theta\), and thus the expected opportunity cost decays to 0 as well.

To prove the first claim, we will argue by contradiction. Let \(E_\infty\) be the set of directions sampled infinitely often, and let \(M:=\mathrm{span}(E_\infty)\). We assume by contradiction that \(\mathbf{1}^\perp\unknown\in M\), and condition on an event \(\Omega_\mathcal{E}:=\{E_\infty=\mathcal{E}\}\), where the set of recurrent directions is fixed. On this event, after some finite random time, every subsequently sampled direction lies in E. This reduces the proof to showing two things: for the directions \(L\in\mathcal{E}\), their marginal score \(G_t(L)\rightarrow 0\), while the total score over D stays bounded away from 0. Thus, for all sufficiently large _t_, at least one direction outside E has a larger score than every direction in E, contradicting the assumption that every subsequently sampled direction lies in E.

The proof of Theorem 2 relies on eight lemmas, organized as follows. Lemma D.1 establishes that posterior variance goes to 0 and the posterior mean converges along every direction in the span of recurrently sampled directions. Lemma D.2 proves that posterior variance remains uniformly positive outside that span. Lemmas D.3 and D.4 transfer these conclusions to the approximate posterior covariance and provide the bounds needed for the marginal scores. Lemma D.5 bounds the affine threshold and the weights _w_<sub>_t_-1_,i_</sub>. Lemma D.6 shows that the scores of recurrent directions decay, while Lemma D.7 shows that the total score stays bounded away from 0 whenever \(\mathbf{1}^\perp\) is not contained in the recurrent span. Finally, Lemma D.8 shows that "projected" mean convergence suffices for expected opportunity cost.

