It is well-known that \(||\cdot||_2^2\) is continuous on the whole space \(\mathbb{C}^{mn\times mn}\). Hence, \(||\cdot||_2^2\) is continuous on \(s(\iota(M([0,1))))\).

To conclude, \(r(\cdot)\) is continuous on \[0,1\). The proof is complete.

**Lemma 10.**

\(c_0:=sup_{\alpha\in(0,1/2]}||\mathcal{C}_\alpha^{-1/2}||_2^2<+\infty.\)

**Proof:** Recall from Lemma 1 that \(\mathcal{C}_\alpha\in\mathcal{Q}(mn)\) for each \(\alpha\in(0,1)\). Then, by Lemma 8, we have \(\mathcal{C}_\alpha^{-1}=\iota(\mathcal{C}_\alpha)\in\mathcal{Q}(mn)\) for each \(\alpha\in(0,1)\). Hence, by Lemma 2, we see that there exists a unique matrix **B** such that \(\mathbf{B}^2=\mathcal{C}_\alpha^{-1}\) and \(\sigma(\mathbf{B})\subset\mathbb{C}_+\).

In fact, both \(\mathcal{C}_\alpha^{-1/2}\) and \(s(\mathcal{C}_\alpha^{-1})\) are valid candidates of **B**. To see this, we firstly note that \((\mathcal{C}_\alpha^{-1/2})^2=\mathcal{C}_\alpha^{-1}\). Moreover, it is well-known that the image \(s(\mathbb{C}\backslash(-\infty,0])\) is a subset of C<sub>+</sub>. Then, by definition of \(\mathcal{C}_\alpha^{1/2}\) and by the fact that \(\sigma(\mathcal{C}_\alpha)\subset\mathbb{C}\backslash(-\infty,0]\), we see that \(\sigma(\mathcal{C}_\alpha^{1/2})\subset\mathbb{C}_+\). That means for each \(\mu\in\sigma(\mathcal{C}_\alpha^{-1/2})\), there exists \(\lambda\in\sigma(\mathcal{C}_\alpha^{1/2})\subset\mathbb{C}_+\) such that \(\mu=\frac{1}{\lambda}\). Rewrite \(\lambda\) as \(\lambda=\lambda_r+\mathbf{i}\lambda_i\) with \(\lambda_r,\lambda_i\in\mathbb{R}\). Then,

\(\mu=\frac{1}{\lambda}=\frac{\lambda_r-\mathbf{i}\lambda_i}{\lambda_r^2+\lambda_i^2}.\)

Since \(\lambda\in\mathbb{C}_+\), \(\lambda_r>0\). Hence, \(\Re(\mu)=\frac{\lambda_r}{\lambda_r^2+\lambda_i^2}>0\). That means \(\mu\in\mathbb{C}_+\). By the generality of \(\mu\) in \(\sigma(\mathcal{C}_\alpha^{-1/2})\), we know that \(\sigma(\mathcal{C}_\alpha^{-1/2})\subset\mathbb{C}_+\). Hence, \(\mathcal{C}_\alpha^{-1/2}\) is a valid candidate of **B**.

On the other hand, by Lemma 2, we know that \(s(\mathcal{C}_\alpha^{-1})\) is also a valid candidate of matrix **B**. Then, the uniqueness of **B** implies that \(s(\mathcal{C}_\alpha^{-1})=\mathcal{C}_\alpha^{-1/2}\) for each \(\alpha\in(0,1)\).

Therefore, \(r(\alpha)=||s(\mathcal{C}_\alpha^{-1})||_2^2=||\mathcal{C}_\alpha^{-1/2}||_2^2\) for each \(\alpha\in(0,1)\). Therefore,<tbc>

\(sup_{\alpha\in(0,1/2]}||\mathcal{C}_\alpha^{-1/2}||_2^2=sup_{\alpha\in(0,1/2]}r(\alpha)\le sup_{\alpha\in[0,1/2]}r(\alpha).\)

<tbc>As shown in Lemma 9, we know that \(r(\cdot)\) is continuous on the compact set \[0,1/2\]. A continuous function on a compact set has a finite upper bound. Therefore,

\(sup_{\alpha\in(0,1/2]}||\mathcal{C}_\alpha^{-1/2}||_2^2\le sup_{\alpha\in[0,1/2]}r(\alpha)<+\infty.\)

The proof is complete.

**Definition 2.** _A function_ \(g:\mathbb{X}\rightarrow\mathbb{Y}\) _between two topological spaces_ X _and_ Y _is said to be continuous if and only if for every open set_ \(\mathbb{V}\subset\mathbb{Y}\)_, the inverse image_

\(g^{-1}(\mathbb{V}):=\{X\in\mathbb{X}|g(X)\in\mathbb{V}\},\)

_is an open subset of_ X.

