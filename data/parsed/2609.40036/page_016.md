**Definition 4** (Linial-Simkin ensemble)**.** _Fix_ \(D\ge 3\), \(c\in(0,1)\)_, and even n. Set_<tbc>

\(g(n):=max\{3,\lfloor clog_{D-1}n\rfloor\}.\) (63)

<tbc>_Begin with a fixed Hamilton cycle H on_ \[_n_\]_. When the current minimum degree is k_-1_\<D, choose uniformly an unordered pair of degree-(k_-1) _vertices at current graph distance at least g(n_)-1_, and add the edge between them. Abort if no such pair exists; otherwise continue until the graph is D-regular. A completed degree-increment round adds a perfect matching, so a successful run has the form_

\(G=H\cup M_1\cup\cdots\cup M_{D-2}.\) (64)

_Let_ L_<sub>n,D,c</sub> be the output probability distribution conditioned on successful completion._

Every successful output of the Linial-Simkin process is simple, connected, and has girth at least _g(n_). The completion probability tends to one by \[LS20, Theorem 1.1 and Proposition 2.1\], while the uniform choice of admissible pairs is part of the definition.

We now turn to the ML decoding properties of the Linial-Simkin graphs. The key point is that the syndrome determines the error only modulo the cycle space:

\(B^T\mathbf{e}=B^T\mathbf{e}'\Longleftrightarrow\mathbf{e}-\mathbf{e}'\in kerB^T.\) (65)

Thus every nonzero circulation \(\mathbf{f}\in kerB^T\) gives a possible competitor **E**-**f** to the true error **E**. ML decoding succeeds precisely when the true error is the most likely element of its syndrome coset. Consequently, the basic obstruction to ML decoding is a circulation \(\mathbf{f}\neq 0\) for which **E**-**f** is at least as likely as **E**. For a fixed circulation **f**, this pairwise confusion probability is controlled by the Bhattacharyya overlap between the probability distribution over noise vectors and its coordinatewise translate. Indeed, writing

\(L(\mathbf{e}):=\prod_{j=1}^m\nu_p(e_j),\) (66)

the elementary inequality<tbc>

\(\mathbf{1}_{\{L(\mathbf{e}-\mathbf{f})\ge L(\mathbf{e})\}}L(\mathbf{e})\le\sqrt{L(\mathbf{e})L(\mathbf{e}-\mathbf{f})}\) (67)

<tbc>gives

\(Pr\{L(\mathbf{E}-\mathbf{f})\ge L(\mathbf{E})\}\le\sum_{\mathbf{e}\in\mathbb{F}_q^E}\sqrt{L(\mathbf{e})L(\mathbf{e}-\mathbf{f})}=\prod_{j:f_j\neq 0}\sum_{z\in\mathbb{F}_q}\sqrt{\nu_p(z)\nu_p(z-f_j)}.\) (68)

Thus the worst single-coordinate overlap controls the pairwise ML error probability for every competing circulation, with a cost exponential in the support size of that circulation. This is the same channel parameter that appears in standard pairwise ML bounds for group codes on symmetric channels \[Com08, §2.5\].

The competing objects here are cycles and, more generally, circulations. A _D_-regular graph has approximately \((D-1)^\ell\) possible non-backtracking closed walks of length \(\ell\), while each nonzero coordinate of a competing circulation contributes a factor at most \(Z_\theta(p)\) to the pairwise overlap, where<tbc>

\(Z_\theta(p):=max_{a\neq 0}\sum_{z\in\mathbb{F}_q}\sqrt{\nu_p(z)\nu_p(z-a)},\) (69)

