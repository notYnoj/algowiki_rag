**Proof:** To prove _a_1), we first recall that the argument relies on the fundamental properties of the GLT class, in particular the second part in GLT 2 and the third part stated in GLT 3. More precisely, we have<tbc>

\(\mathcal{D}_N(a)=D_N(a)=\mathrm{diag}_{i=1,2,\dots,N}a(x_i)\)

<tbc>and hence<tbc>

\(\{\mathcal{D}_N(a)=D_N(a)\}_N\sim_\mathrm{GLT}a(x)\)

<tbc>by using GLT 2. Furthermore, by Proposition 8.2 via axiom GLT 2, we find<tbc>

\(\{\overline{G_{\alpha,N}}\}_N\sim_\mathrm{GLT}f_\alpha(\xi_1).\)

<tbc>In conclusion by equation (8.8) and GLT 3, we obtain _a_1) i.e.

\(\{\mathcal{D}_N(a)\overline{G_{\alpha,N}}\}_N\sim_\mathrm{GLT}a(x)f_\alpha(\xi_1),\)

so that, by invoking GLT 1, we infer _a_2).

And what about

_a3_) \(\{\mathcal{D}_N(a)\overline{G_{\alpha,N}}\}_N\sim_\lambda a(x)f_\alpha(\xi_1)?\)

Since \(G_{\alpha,N}\) is not Hermitian, its eigenvalue distribution cannot be immediately deduced from GLT 1, even if other tools are available \[21\].<br>
To illustrate the relationship between the eigenvalue distributions and the associated symbols, we present two representative examples for which Figures 8.1-8.2 indicate that the question in _a_3) has a positive answer, which is clear in the constant coefficient case. Indeed, although the convergence is slow, we believe that the answer is positive even in the variable coefficient case.<br>
In the one-dimensional case, we first consider the constant-coefficient matrix \(\overline{G_{\alpha,N}}\) and compare its eigenvalues with sampled values of the symbol \(f_\alpha(\xi_1)\) (Figure 8.1). The two graphs almost superpose and hence we observe a positive answer to the question in _a_3) when _a(x_) is a constant function. The fact holds also formally because of the results in \[21\], where the authors study the canonical distribution of Toeplitz matrix sequences for a rich class of parametric generating functions which includes \(f_\alpha\) for every \(\alpha\in(1,2)\). Hence<tbc>

\(\{\overline{G_{\alpha,N}}\}_N\sim_\lambda f_\alpha(\xi_1).\)

<tbc>We then examine the variable-coefficient case \(D_N(a)\overline{G_{\alpha,N}}\) with _a(x_)=_x_<sup>2</sup>+1, comparing the eigenvalues with sampled values of the symbol \(a(x)f_\alpha(\xi_1)\) (Figure 8.2). Also in this more complicate setting, the numerics suggest that the answer to the question in _a_3) is positive as reported Figure 8.2. We also tried the more degenerate case of _a(x_)=_x_<sup>2</sup> and also in this case the agreement is remarkable. In fact, since _a(x_) is continuous with range \[0,1\], the range of \(a(x)f_\alpha(\xi_1)\) for fixed \(\xi_1\) is exactly the segment connecting the complex zero with the value \(f_\alpha(\xi_1)\): as a consequence the total range of the GLT symbol \(a(x)f_\alpha(\xi_1)\) is exactly the convex hull of the range of \(f_\alpha(\xi_1)\). On the other hand, since 1+_x_<sup>2</sup> is continuous with range \[1,2\], the eigenvalues fill the disconnected (highly nonconvex) region<tbc>

\(\bigcup_{y\in[1,2]}y\mathrm{range}(f_\alpha)=\big\{yz:y\in[1,2],z\in\mathrm{range}(f_\alpha)\big\},\)

