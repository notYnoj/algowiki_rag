**Lemma 6.** _The matrix_ \(\mathcal{Q}_\alpha=\mathcal{P}_\alpha^{-1/2}\mathcal{Y}\mathcal{C}_\alpha\mathcal{P}_\alpha^{-1/2}\) _is both real symmetric and orthogonal, i.e.,_ \(\sigma(\mathcal{Q}_\alpha)\subset\{-1,1\}\).

**Proof:** First, we show that \(\mathcal{Q}_\alpha\) is real-valued. Since both \(\mathcal{C}_\alpha^{-1/2}\) and \((\mathcal{C}_\alpha^{-1/2})^T\) are real-valued matrices by Lemma 4 (a), \(\mathcal{P}_\alpha^{-1}=\mathcal{C}_\alpha^{-1/2}(\mathcal{C}_\alpha^{-1/2})^T\) is also real-valued. Furthermore, \(\mathcal{P}_\alpha^{-1}\) itself is a normal equation matrix, so it is HPD. By Lemma 1, we know that \(\mathcal{P}_\alpha^{-1}\) is nonsingular. As a result, \(\mathcal{P}_\alpha^{-1/2}\) being a matrix square root of a real-valued HPD matrix is also real-valued HPD. Hence, \(\mathcal{Q}_\alpha=\mathcal{P}_\alpha^{-1/2}\mathcal{Y}\mathcal{C}_\alpha\mathcal{P}_\alpha^{-1/2}\), which is a product of real-valued matrices, is real-valued.

By Lemma 4 (a) that \((\mathcal{C}_\alpha^{1/2})^T\mathcal{Y}=\mathcal{Y}\mathcal{C}_\alpha^{1/2}\) and \((\mathcal{C}_\alpha^{-1/2})^T\mathcal{Y}=\mathcal{Y}\mathcal{C}_\alpha^{-1/2}\), we have

\(\mathcal{Q}_\alpha^T\mathcal{Q}_\alpha=\mathcal{Q}_\alpha^2=\mathcal{P}_\alpha^{-1/2}\mathcal{Y}\mathcal{C}_\alpha\mathcal{P}_\alpha^{-1}\mathcal{Y}\mathcal{C}_\alpha\mathcal{P}_\alpha^{-1/2}\)<br>
\(=\mathcal{P}_\alpha^{-1/2}\mathcal{Y}\mathcal{C}_\alpha\mathcal{C}_\alpha^{-1/2}(\mathcal{C}_\alpha^{-1/2})^T\mathcal{Y}\mathcal{C}_\alpha\mathcal{P}_\alpha^{-1/2}\)<br>
\(=\mathcal{P}_\alpha^{-1/2}\mathcal{Y}\mathcal{C}_\alpha^{1/2}\mathcal{Y}\mathcal{C}_\alpha^{1/2}\mathcal{P}_\alpha^{-1/2}\)<br>
\(=\mathcal{P}_\alpha^{-1/2}(\mathcal{C}_\alpha^{1/2})^T\underbrace{\mathcal{Y}^2}_{=I_{mn}}\mathcal{C}_\alpha^{1/2}\mathcal{P}_\alpha^{-1/2}\)<br>
\(=\mathcal{P}_\alpha^{-1/2}\mathcal{P}_\alpha\mathcal{P}_\alpha^{-1/2}\)<br>
\(=I_{mn}.\)

Thus, \(\mathcal{Q}_\alpha\) is orthogonal.

Since \(\mathcal{Q}_\alpha\) is real symmetric and orthogonal, we know that \(\sigma(\mathcal{Q}_\alpha)\subset\mathbb{R}\cap\{z:|z|=1\}=\{-1,1\}\). The proof is complete.

In what follows, we will estimate \(||\mathcal{E}_\alpha||_2\).

From the proof of Lemma 6, we know that \(\mathcal{P}_\alpha^{-\frac{1}{2}}\) is real symmetric. Moreover, since \(\mathcal{R}_\alpha\) is a real block Toeplitz matrix with symmetric blocks, \(\mathcal{Y}\mathcal{R}_\alpha\) is real symmetric. Hence, \(\mathcal{E}_\alpha=\mathcal{P}_\alpha^{-1/2}\mathcal{Y}\mathcal{R}_\alpha\mathcal{P}_\alpha^{-1/2}\) is real symmetric. Let \(\rho(\cdot)\) denote the spectral radius of a matrix. We have

\(||\mathcal{E}_\alpha||_2=||\mathcal{P}_\alpha^{-1/2}\mathcal{Y}\mathcal{R}_\alpha\mathcal{P}_\alpha^{-1/2}||_2=\rho(\mathcal{P}_\alpha^{-1/2}\mathcal{Y}\mathcal{R}_\alpha\mathcal{P}_\alpha^{-1/2})\)<br>
\(=\rho(\mathcal{P}_\alpha^{-1}\mathcal{Y}\mathcal{R}_\alpha)\)<br>
\(\le||\mathcal{P}_\alpha^{-1}\mathcal{Y}\mathcal{R}_\alpha||_2\)<br>
\(=||\mathcal{C}_\alpha^{-1/2}(\mathcal{C}_\alpha^{-1/2})^T\mathcal{Y}\mathcal{R}_\alpha||_2\)<br>
\(\le||\mathcal{C}_\alpha^{-1/2}(\mathcal{C}_\alpha^{-1/2})^T||_2||\mathcal{Y}\mathcal{R}_\alpha||_2=||\mathcal{C}_\alpha^{-1/2}||_2^2||\mathcal{R}_\alpha||_2.\) (2.2)

**Lemma 7.** _The principal square root_ \(s(\cdot)\)_, as a matrix function, is continuous on_ Q(_K_) _for any positive integer K._

**Proof:** By Proposition 1, \(s(\cdot)\) is holomorphic on \(\mathbb{C}\backslash(-\infty,0]\) and thus infinitely differentiable on \(\mathbb{C}\backslash(-\infty,0]\). Then, Lemma 7 is a direct consequence of \[21, Theorem 1.19\]. The proof is<tbc>

