guarantees. Because the complete proof is relatively long, we only present the main steps in this document: all intermediate computations can be found in the Appendix B.

**Proposition 5.1.** _Given a scalar_ \(x_0\in]0,1-\zeta]\) _and_ \(\lambda_{\epsilon,x_0}=\frac{4x_0(1-\epsilon)}{(1-\epsilon+x_0)^2}\)_, we have_ \(f(\lambda x,\lambda y)\le\lambda\breve{f}_{\mathcal{X}_{\epsilon,\theta,\zeta,\eta}}(x,y)\) _for any_ \((x,y)\in\mathcal{X}_{\epsilon,\theta,\zeta,\eta}\) _such that_ \(x\ge x_0\) _and_ \(\lambda\in[0,\lambda_{\epsilon,x_0}]\).

The full proof of Proposition 5.1 can be found in Appendix B.1. The scalar \(\lambda_{\epsilon,x_0}\) can be seen as a shrinking factor transforming a feasible solution of the DCMF<sub>env</sub> into a feasible solution of the DCMCF problem that satisfies the delay Constraints (11) : \(\sum_{a\in p}f(\frac{b^kx_p^k}{c_a},\frac{y_a}{c_a})\le b^kx_p^k\times d^k\forall k\in K,p\in P^k\).

Let us introduce additional notation that will be used throughout the remainder of this section: \(|P|=\mathrm{max}_{k\in K}|P^k|>1\), \(u=\mathrm{max}_{a\in A}u_a\), and \(b=\mathrm{min}_{k\in K}b^k\).

**Lemma 5.3.** _Given scalars_ \(\gamma>0\) _and S\>_1_, for any_ \(k\in K\), \(p\in P^k\) _and_ \(a\in p\) _such that_ \(u_a\ge\frac{b^k\gamma}{S|P^k|}\)_, we have:_

\(\lambda_{\gamma,S}^{post}=\frac{4ub\gamma S|P|}{(uS|P|+b\gamma)^2}\le\lambda_{1-\frac{u_a}{c_a},\frac{b^k\gamma}{c_aS|P^k|}}.\)

Lemma 5.3 translates this generic shrinking factor into the specific parameters of the DCMCF problem to provide a uniform scaling factor \(\lambda_{\gamma,S}^{post}\) for all paths exceeding a given threshold. The proof, found in Appendix B.2, relies on the monotonicity of the shrinking factor with respect to the demand sizes, path counts, and arc load bounds.

**Proposition 5.2.** _Given a solution of the DCMF<sub>env</sub> problem with objective value_ \(\tilde{\gamma}\)_, there exists a feasible solution of DCMCF with objective value_ \(\frac{b\tilde{\gamma}}{u(|P|-1)+b\tilde{\gamma}}\tilde{\gamma}\).

Proposition 5.2 establishes an ex-post performance guarantee by constructing a feasible DCMCF solution from the relaxation. As detailed in Appendix B.3, the proof filters the relaxed solution by setting path usages below a threshold _S_<sup>∗</sup> to zero, and scales the flow on the remaining paths<tbc>

