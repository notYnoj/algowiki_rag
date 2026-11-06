Now fix _t\>T_<sub>0</sub> and let _f<sub>t</sub>_ denote the posterior density given H_<sub>t</sub>_. Every observation collected after round _T_<sub>0</sub> is taken along some direction \(L\in\mathcal{E}\subseteq M\). The corresponding likelihood factor depends on \(\theta\) only through \(L^\top\theta\). If \(\theta=u+v\) with \(u\in M\) and \(v\in M^\perp\), then

\(L^\top\theta=L^\top(u+v)=L^\top u,\)

because \(L\in M\) and \(v\perp M\). It follows that

\(f_t(u,v)=\frac{f_0(u,v)\Psi_t(u)}{Z_t}\)

for some nonnegative function \(\Psi_t\) on _M_ and some normalizing constant _Z<sub>t</sub>\>_0. Therefore, for fixed **_u_**, the conditional distribution of the \(M^\perp\) component does not change after round _T_<sub>0</sub>.

Define

\(c(u):=\int_{M^\perp} f_0(u,v)dv,\)

and let _C_(**_u_**) denote the covariance matrix under the conditional density \(f_0(u,\cdot)/c(u)\) on \(M^\perp\). Choose a bounded closed neighborhood \(O\subseteq M\) of \(R_M\theta\). Since _f_<sub>0</sub> is continuous and is bounded above by a constant multiple of the Gaussian prior density, dominated convergence implies that _C_(**_u_**) is continuous on _O_.

For every \(u\in O\), the conditional distribution of **_v_** has a strictly positive density on all of \(M^\perp\). Hence, its covariance matrix _C_(**_u_**) is positive definite on \(M^\perp\). Since _O_ is compact and _C_(**_u_**) is continuous, there exists \(\eta_0>0\) such that

\(C(u)\unknown\eta_0Id_{M^\perp}(u\in O).\)

It remains to show that, under the round-_t_ posterior, the **_u_**-coordinate belongs to _O_ with probability that approaches 1. Choose \(\epsilon>0\) such that the closed ball of radius \(2\epsilon\) around \(R_M\theta\) is contained in _O_. By condition (ii), for all sufficiently large _t_,

\(\|R_M\mu_{t-1}^*-R_M\theta\|_2<\epsilon.\)

For such _t_, if \(u\notin O\), then

\(\|u-R_M\mu_{t-1}^*\|_2\ge\epsilon.\)

Thus, by Markov’s inequality,

\(\mathbb{P}(u\notin O|\mathcal{H}_t)\le\frac{tr(R_M\Sigma_{t-1}^*R_M)}{\epsilon^2}\rightarrow 0.\)

Finally, the law of total covariance gives

\(Q\Sigma_{t-1}^*Q\unknown\mathbb{E}[C(u)|\mathcal{H}_t]\unknown\eta_0\mathbb{P}(u\in O|\mathcal{H}_t)Q.\)

The probability on the right converges to 1, so the claim holds eventually with \(\eta=\eta_0/2\). Next we get a uniform upper bound on the posterior covariance.

