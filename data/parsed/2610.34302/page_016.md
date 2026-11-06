## Approximation Analysis.

Let _C<sup>⋆</sup>_ be an optimal set cover solution for the original instance. For each index _i_, let \(C_i^\star\) be a copy of _C<sup>⋆</sup>_ but on the set system (U_<sub>i</sub>,_F_<sub>i</sub>_). We construct a \((2\alpha-\eta)\)-navigable graph _G<sup>⋆</sup>_=(_P,E<sup>⋆</sup>_) as follows.

• **Inter-copy edges:** For every pair of distinct indices \(i,j\in[K]\) and every \(s\in P_i\), add edges from _s_ to _c<sub>j</sub>_ and to every point in \(C_j^\star\).<tbc>

• **Intra-copy edges:** For every \(i\in[K]\) and every pair of distinct points \(s,t\in P_i\), add the directed edge (_s,t_).

We first verify that _G<sup>⋆</sup>_ is \((2\alpha-\eta)\)-navigable. If _s_ and _t_ belong to the same copy, then the direct edge (_s,t_) gives distance 0 to the target. Otherwise, suppose \(s\in P_i\) and \(t\in P_j\) for \(j\neq i\). Then \(\mathsf{d}(s,t)=2\alpha\). If _t=c<sub>j</sub>_ or \(t\in C_j^\star\), the direct edge to _t_ again gives distance 0. If \(t\in\mathcal{F}_j\backslash C_j^\star\), then the edge (_s,c<sub>j</sub>_) satisfies<tbc>

\(\mathsf{d}(c_j,t)=1<\frac{2\alpha}{2\alpha-\eta}=\frac{\mathsf{d}(s,t)}{2\alpha-\eta}.\)

<tbc>Finally, if \(t\in\mathcal{U}_j\), then some set \(S\in C_j^\star\) contains _t_, and the edge (_s,S_) satisfies

\(\mathsf{d}(S,t)=1<\frac{2\alpha}{2\alpha-\eta}=\frac{\mathsf{d}(s,t)}{2\alpha-\eta}.\)

Thus _G<sup>⋆</sup>_ is \((2\alpha-\eta)\)-navigable.

The total number of edges in _G<sup>⋆</sup>_ is

\(|E^\star|=K(K-1)(m+n+1)(|C^\star|+1)+K(m+n+1)(m+n).\)

Suppose _G_=(_P,E_) is an \((\alpha,2\alpha-\eta)\)-bicriteria \(\rho\)-approximation to the sparsest \(\alpha\)-navigable graph, where \(\rho=\frac{1}{10d}lnN\). Since _G<sup>⋆</sup>_ is feasible for the comparison parameter \(2\alpha-\eta\), we have \(|E|\le\rho|E^\star|\). Averaging over the _K(K_-1)(_m+n_+1) pairs (_s,j_) with \(s\in P_i\) and \(i,j\in[K]\), \(i\neq j\), shows that the chosen pair (_s,j_) satisfies

\(|C|\le|V_{s,j}|\le\frac{|E|}{K(K-1)(m+n+1)}\)<br>
\(\le\rho\left(|C^\star|+1+\frac{m+n}{K-1}\right)\)<br>
\(\le\rho\left(|C^\star|+1+\eta\right).\)

Here the last inequality follows from the choice of _K_.

Since \(m\le n^d\) and \(\eta\) is a fixed constant, for all sufficiently large _n_ we have<tbc>

\(N=K(m+n+1)\le\frac{100n^{2d}}{\eta}.\)

<tbc>Therefore<tbc>

\(\rho=\frac{1}{10d}lnN\le\frac{1}{10d}ln\left(\frac{100n^{2d}}{\eta}\right)<0.21lnn\)

<tbc>for all sufficiently large _n_. Also, by our assumption \(|C^\star|\ge 20\) and by \(\eta<1\),<tbc>

\(|C^\star|+1+\eta\le|C^\star|+2\le 1.1|C^\star|.\)

