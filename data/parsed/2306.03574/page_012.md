complete.

Define the inverse operation \(\iota\) as \(\iota:\mathbf{A}\in GL(K)\rightarrow\iota(\mathbf{A})=\mathbf{A}^{-1}\in GL(K)\) for any positive integer _K_.

**Lemma 8.** \(\iota(\cdot)\) _is a continuous on_ Q(_K_) _and_ \(\iota(\mathcal{Q}(K))\subset\mathcal{Q}(K)\) _for any positive integer K ._

**Proof:** It is well-known that the inverse operation \(\iota(\cdot)\) is continuous on _GL(K_). Hence, for \(\iota(\cdot)\) is continuous on Q(_K_), a subset of _GL(K_).

It remains to show that the image of Q(_K_), under the mapping \(\iota(\cdot)\), is a subset of Q(_K_). For any \(\mathbf{A}\in\mathcal{Q}(K)\), it holds<tbc>

\(\sigma(\iota(\mathbf{A}))=\sigma(\mathbf{A}^{-1})=\left\{\frac{1}{\lambda}\big|\lambda\in\sigma(\mathbf{A})\right\}.\)

<tbc>That means, for any \(\mu\in\sigma(\iota(\mathbf{A}))\), there exists \(z\in\sigma(\mathbf{A})\) such that \(\mu=\frac{1}{z}\). Rewrite _z_ as _z=z<sub>r</sub>_+**i**_z<sub>i</sub>_ with \(z_r,z_i\in\mathbb{R}\). Then,

\(\mu=\frac{1}{z}=\frac{1}{z_r+\mathbf{i}z_i}=\frac{z_r-\mathbf{i}z_i}{z_r^2+z_i^2}.\)

As \(\mathbf{A}\in\mathcal{Q}(K)\), \(z\in\mathbb{C}\backslash(-\infty,0]\) by definition of Q(_K_).

If _z<sub>i</sub>_=0, then \(z_r+\mathbf{i}z_i\in\mathbb{C}\backslash(-\infty,0]\) implies that _z<sub>r</sub>\>_0. In such case \(\Re(\mu)=\frac{z_r}{z_r^2+z_i^2}>0\), which means \(\mu\in\mathbb{C}\backslash(-\infty,0]\).

If \(z_i\neq 0\), then \(\unknown(\mu)=-\frac{z_i}{z_r^2+z_i^2}\neq 0\), which means \(\mu\in\mathbb{C}\backslash(-\infty,0]\).

To conclude, \(\mu\in\mathbb{C}\backslash(-\infty,0]\). By the generality of \(\mu\) in \(\sigma(\iota(\mathbf{A}))\), we know that \(\sigma(\iota(\mathbf{A}))\subset\mathbb{C}\backslash(-\infty,0]\) and thus \(\iota(\mathbf{A})\in\mathcal{Q}(K)\). That means for any \(\mathbf{A}\in\mathcal{Q}(K)\), it holds \(\iota(\mathbf{A})\in\mathcal{Q}(K)\). In other words, \(\iota(\mathcal{Q}(K))\subset\mathcal{Q}(K)\). The proof is complete.

**Lemma 9.** _Denote_ \(r(\alpha):=||s(\mathcal{C}_\alpha^{-1})||_2^2\) _for_ \(\alpha\in[0,1)\)_. Then,_ \(r(\cdot)\) _is a continuous function on_ \[0,1).

**Proof:** Clearly, \(r(\alpha)\) can be written in a composite form: \(r(\alpha)=||s\circ\iota\circ M(\alpha)||_2^2\), where \(M(\cdot):\alpha\in[0,1)\rightarrow M(\alpha)=\mathcal{C}_\alpha\in\mathcal{Q}(mn)\). To show the continuity of \(r(\cdot)\), it suffices to show the continuity of \(M(\cdot)\) on \[0,1), the continuity of \(\iota(\cdot)\) on the image _M_(\[0,1)\), the continuity of \(s(\cdot)\) on the image \(\iota(M([0,1)))\).

\(M(\alpha)\) is an affine operator with respect to \(\alpha\) and it is clearly continuous on \[0,1).

By Lemma 1, \(M([0,1))\subset\mathcal{Q}(mn)\). Lemma 8 shows that \(\iota\) is continuous on Q(_mn_) and thus is continuous on the subset _M_(\[0,1)\).

By Lemma 8, \(\iota(M([0,1)))\subset\iota(\mathcal{Q}(mn))\subset\mathcal{Q}(mn)\). Lemma 7 shows that \(s(\cdot)\) is continuous on Q(_mn_) and thus is continuous on the subset \(\iota(M([0,1)))\).

