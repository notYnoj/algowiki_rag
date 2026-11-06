**Definition 1.** (Matrix function via Jordan canonical form \[21, Definition 1.2\]) _Let_ **A**=**Z**_J_**Z**<sup>-1</sup> _be a Jordan canonical form of a matrix_ \(\mathbf{A}\in\mathbb{C}^{N\times N}\) _with_<tbc>

\(J=\mathrm{blockdiag}(J_{n_i}(\lambda_i))_{i=1}^k,\{\lambda_i\}_{i=1}^k\in\sigma(\mathbf{A}),\sum_{i=1}^kn_i=N.\)

<tbc>_For a function g of one complex variable that is sufficiently smooth on each point of_ \(\sigma(\mathbf{A})\)_, a matrix function is defined by_<tbc>

\(g(\mathbf{A}):=\mathbf{Z}\mathrm{blockdiag}(g(J_{n_i}(\lambda_i)))_{i=1}^k\mathbf{Z}^{-1},\)

<tbc>_where_ \(g(J_{n_i}(\lambda_i))\) _is an upper triangular Toeplitz matrix given as_

\(g(J_{n_i}(\lambda_i))=\mathrm{UTT}\left(\left(\frac{g(\lambda_i)}{0!},\frac{g'(\lambda_i)}{1!},\dots,\frac{g^{(j)}(\lambda_i)}{j!},\dots,\frac{g^{(n_i-1)}(\lambda_i)}{(n_i-1)!}\right)\right)\in\mathbb{C}^{n_i\times n_i}.\)

For \(z\in\mathbb{C}\), define _s(z_) as the principal branch of complex square root of _z_.

**Proposition 1.** (\[39, Example 1.16\]) _The principal square root function_ \(s(\cdot)\) _is holomorphic on_ \(\mathbb{C}\backslash(-\infty,0]\).

By Definition 1 and Proposition 1, \(s(\cdot)\) as a matrix function is well-defined on Q(_K_) for any positive integer _K_.

Denote \(\mathbb{C}_+:=\{z\in\mathbb{C}|\Re(z)>0\}\).

**Lemma 2.** (\[21, Theorem 1.29\]) _For_ \(\mathbf{A}\in\mathcal{Q}(K)\) _with any positive integer K,_

**(a)** _there exists a unique matrix_ **B** _such that_ **B**<sup>2</sup>=**A** _and_ \(\sigma(\mathbf{B})\subset\mathbb{C}_+\);

**(b)** _the matrix_ **B** _is exactly s_(**A**);

**(c)** _if, additionally,_ **A** _is real, then s_(**A**) _is real._

**Proof:** The results of Lemma 2 come from \[21, Theorem 1.24\] and \[21, Theorem 1.29\]. \(\square\)

Since \(\sigma(\mathcal{T})=\sigma(L)\subset(1,+\infty)\subset\mathbb{C}\backslash(-\infty,0]\), \(\mathcal{T}\in\mathcal{Q}(mn)\). That means _s_(T) is well defined. In the rest of this paper, we use the notation \(\mathcal{T}^\frac{1}{2}\) to represent _s_(T).

**Lemma 3.** _Let_ \(\mathcal{T}\in\mathbb{R}^{mn\times mn}\) _be defined by (1.2). Then,_

**(a)** T<sup>1/2</sup> _is invertible;_

**(b)** T<sup>1/2</sup> _is a real-valued matrix;_

**(c)** YT<sup>1/2</sup> _is symmetric._

**Proof:** As discussed above, \(\sigma(\mathcal{T})\subset(1,+\infty)\). Therefore, \(\sigma(\mathcal{T}^{1/2})\subset(1,+\infty)\), which proves part (a).

