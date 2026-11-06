where **a**=(_a_<sub>1</sub>_,...,a_<sub>_n_-1</sub>), _S<sub>n</sub>_ is the set of permutations of the _n_ legs, and \(\pi\mathcal{C}_n\) denotes the tensor with its legs permuted by \(\pi\). Definition 4.5 gives the full construction. We prove that \(t_\phi>0\). The normalization yields \(P_\phi(1,\dots,1,b)=b\) for every positive integer _b_, while interpolation gives \(P_\phi(\mathbf{a})\le D^{1/t_\phi}\).

**Concavity and shifted tripling.** The two polynomial inequalities from \[Ope26a\] extend to this profile. First, \(P_\phi\) is discretely concave in each input length. We take the Kronecker product with a two-dimensional identity tensor on one input and the output, and consider the kernel and quotient of a diagonal substitution on homogeneous binary forms. Multiplication by each fixed tuple of the other inputs preserves this kernel. Consequently, a single choice of bases works for all tuples, and a local degeneration produces two blocks with neighboring input lengths. The entropy inequality turns these matched blocks into concavity.

Second, for positive integers _a_<sub>1</sub>_,...,a_<sub>_n_-2</sub>_,h_ and \(S=\sum_{j=1}^{n-2}(a_j-1)\), a three-sector decomposition gives

\(P_\phi(a_1,\dots,a_{n-2},3h+S)\ge 3P_\phi(a_1,\dots,a_{n-2},h).\)

The outer sectors are translated copies of the shorter polynomial tensor. The middle sector becomes the same tensor after reversing each shared input index and exchanging the last input with the output. The product over all leg permutations makes this exchange harmless. In both constructions, the first _n_-2 inputs remain separate legs.

**Growth along the diagonal.** We extend OpenAI’s growth argument \[Ope26a, Section 5\] to _n_-1 input lengths. Increase the coordinates of (_a,...,a_) one at a time until reaching (_a_+1_,...,a_+1). At each step, tripling and concavity imply a multiplicative increase of at least 1+2/(_na_). There are _n_-1 steps, and an elementary product estimate gives \(P_\phi(a,\dots,a)\ge a^{2(n-1)/n}\) for every positive integer _a_. Comparing this with \(P_\phi(a,\dots,a)\le((n-1)(a-1)+1)^{1/t_\phi}\) forces \(t_\phi\le n/(2(n-1))\). Since a complete graph tensor is the Kronecker product of its edge tensors,

\(\phi(\mathsf{GT}_2(K_n))=2\sum_{1\le i<j\le n}p_{i,j}^{(\phi)}\le 2^{n^2/4}.\)

Strassen’s spectral duality then gives the upper bound in Theorem 1.1.

## 1.4 A barrier for the polynomial constructions

The preceding argument gives the upper bound _n_<sup>2</sup>/4. For odd _n_, it leaves open whether a different combination of the same ingredients can reach the maximum cut. Amanov, van den Berg, and Zuiddam \[ABZ26, Theorem 5.4\] answer the corresponding three-leg question by defining a formal reduction system and a numerical certificate that is monotone under its rules. We extend their symmetric certificate to _n_ legs. Our system includes interpolation, concavity, shifted tripling, and a separation construction that retains an auxiliary polynomial tensor, together with specified rules for combining them. The next theorem shows that these rules cannot improve the threshold _n_<sup>2</sup>/4.

As in Theorem 1.1, we state the conclusion for edge dimension 2. The formal complete-graph expression **G**<sub>_n,_2</sub> and diagonal expression **I**_<sub>n</sub>(R_) from Definition 5.3 evaluate to GT<sub>2</sub>(_K<sub>n</sub>_) and the diagonal tensor of size _R_, respectively. The relation \(\unknown_{\mathrm{poly},n}\) from Definition 5.5 records derivations from the listed rules.

**Theorem 1.2** (barrier for the polynomial constructions)**.** _For every integer_ \(n\ge 3\) _and every positive integer R,_

\(\mathbf{G}_{n,2}\unknown_{\mathrm{poly},n}\mathbf{I}_n(R)\Longrightarrow\mathrm{log}_2R\ge\frac{n^2}{4}.\)

