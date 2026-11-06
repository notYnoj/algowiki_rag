This statement is folklore and follows from the previous works. As we did not find the statement with a bound on \(\lambda_n\), we include it for completeness. We start by showing that a \(\gamma(n)\) approximate SVP algorithm can be used to build a \(\sqrt{n}\gamma(n)\) approximate SIVP algorithm.

**Theorem B.1.** _Let_ \(\gamma:\mathbb{N}\rightarrow\mathbb{R}_{\ge 1}\) _be non-decreasing. Suppose there is an oracle that, on input any rank-m lattice_ M_, returns a nonzero vector_ \(\mathbf{x}\in\mathcal{M}\) _such that_<tbc>

\(\|\mathbf{x}\|_2\le\gamma(m)\lambda_1(\mathcal{M}).\)

<tbc>_Then there is a polynomial-time algorithm that, given an n-dimensional lattice_ L_, makes n oracle calls and outputs n linearly independent vectors_ \(\mathbf{b}_1,\dots,\mathbf{b}_n\in\mathcal{L}\) _such that_

\(\|\mathbf{b}_i\|_2\le\sqrt{n}\gamma(n)\lambda_n(\mathcal{L})\text{\textit{for all}}i\in[n].\)

_In particular, this gives a polynomial-time reduction from_ \(\gamma(n)\)_-SVP to_ \(\sqrt{n}\gamma(n)\)_-SIVP._

_Proof._ We construct the vectors **b**<sub>1</sub>_,...,_**b**_<sub>n</sub>_ iteratively. Assume that \(\mathbf{b}_1,\dots,\mathbf{b}_{i-1}\in\mathcal{L}\) have already been constructed and are linearly independent. Let _W_<sub>_i_-1</sub>:=span(**b**<sub>1</sub>_,...,_**b**<sub>_i_-1</sub>), and let \(\pi_i:\mathbb{R}^n\rightarrow W_{i-1}^\perp\) be the orthogonal projection onto the orthogonal complement of _W_<sub>_i_-1</sub>. Consider the projected lattice<tbc>

\(\mathcal{L}_i:=\pi_i(\mathcal{L})\subseteq W_{i-1}^\perp.\)

<tbc>Since \(dim(W_{i-1}^\perp)=n-i+1\), the lattice L_<sub>i</sub>_ has rank _n-i_+1. We call the \(\gamma\)-SVP oracle on L_<sub>i</sub>_, obtaining a nonzero vector \(\mathbf{y}_i\in\mathcal{L}_i\) such that

\(\|\mathbf{y}_i\|_2\le\gamma(n-i+1)\lambda_1(\mathcal{L}_i).\)

Choose any lift \(\mathbf{x}_i\in\mathcal{L}\) such that \(\pi_i(\mathbf{x}_i)=\mathbf{y}_i\). Now size-reduce **x**_<sub>i</sub>_ with respect to **b**<sub>1</sub>_,...,_**b**<sub>_i_-1</sub>, i.e., write \(\mathbf{x}_i=\sum_{j=1}^{i-1}\alpha_j\mathbf{b}_j+\mathbf{r}_i\), where \(\mathbf{r}_i\in\mathbb{R}^n\), and let \(\mathbf{b}_i:=\mathbf{x}_i-\sum_{j=1}^{i-1}\lfloor\alpha_j\rfloor\mathbf{b}_j\). Then \(\mathbf{b}_i\in\mathcal{L}\), and since subtracting vectors in _W_<sub>_i_-1</sub> does not change the projection onto \(W_{i-1}^\perp\), we still have \(\pi_i(\mathbf{b}_i)=\mathbf{y}_i\). In particular, \(\mathbf{y}_i\neq 0\) implies \(\mathbf{b}_i\notin W_{i-1}\), so **b**<sub>1</sub>_,...,_**b**_<sub>i</sub>_ are linearly independent.

Let \(\mathbf{b}_1^*,\dots,\mathbf{b}_i^*\) denote the Gram-Schmidt orthogonalization of **b**<sub>1</sub>_,...,_**b**_<sub>i</sub>_. By construction, \(\mathbf{b}_i^*=\pi_i(\mathbf{b}_i)=\mathbf{y}_i\), and the size-reduction step ensures that the Gram-Schmidt coefficients satisfy<tbc>

\(|\mu_{i,j}|\le\frac{1}{2}\text{for all}j<i.\)

<tbc>We now bound \(\|\mathbf{b}_i^*\|_2\). By definition of \(\lambda_i(\mathcal{L})\), there exist _i_ linearly independent vectors \(\mathbf{v}_1,\dots,\mathbf{v}_i\in\mathcal{L}\) such that \(\|\mathbf{v}_t\|_2\le\lambda_i(\mathcal{L})\) for all \(t\in[i]\). Since _W_<sub>_i_-1</sub> has dimension _i_-1, not all of these _i_ vectors can lie in _W_<sub>_i_-1</sub>. Hence there exists \(t\in[i]\) such that \(\pi_i(\mathbf{v}_t)\neq 0\). Therefore, \(\pi_i(\mathbf{v}_t)\) is a nonzero vector of L_<sub>i</sub>_, and so<tbc>

\(\lambda_1(\mathcal{L}_i)\le\|\pi_i(\mathbf{v}_t)\|_2\le\|\mathbf{v}_t\|_2\le\lambda_i(\mathcal{L}).\)

<tbc>Using the oracle guarantee and the monotonicity of \(\gamma\), we obtain

\(\|\mathbf{b}_i^*\|_2=\|\mathbf{y}_i\|_2\le\gamma(n-i+1)\lambda_1(\mathcal{L}_i),\)<br>
\(\le\gamma(n)\lambda_i(\mathcal{L}),\)<br>
\(\le\gamma(n)\lambda_n(\mathcal{L}).\)

Finally, since \(\mathbf{b}_i=\mathbf{b}_i^*+\sum_{j=1}^{i-1}\mu_{i,j}\mathbf{b}_j^*\), the orthogonality of the Gram-Schmidt vectors gives

\(\|\mathbf{b}_i\|_2^2=\|\mathbf{b}_i^*\|_2^2+\sum_{j=1}^{i-1}\mu_{i,j}^2\|\mathbf{b}_j^*\|_2^2.\)

