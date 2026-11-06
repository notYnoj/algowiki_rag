Taking the power \(1/\eta\) of the two values in the concavity rule gives, respectively,

\(H_d(\mathbf{a},b+1)+H_d(\mathbf{a},b-1),2H_d(\mathbf{a},b).\)

Their comparison follows from concavity. The analogous comparison for tripling is \(3H_d(\mathbf{a},h)\le H_d(\mathbf{a},3h+S)\). Exchanging the last two legs does not change the certificate. Appending a common partial summand of value _w_ adds \(w^{1/\eta}\) to both sides of either comparison after taking the power \(1/\eta\). This verifies both contextual polynomial rules.

It remains to verify separation, where the sizes of the polynomial resource and retained edge may be chosen independently. Let _w<sub>h</sub>_=V_<sub>n</sub>(X<sub>h</sub>_) for \(0\le h<m\). Hölder’s inequality with exponents \(1/\eta\) and \(1/(1-\eta)\) gives<tbc>

\(\sum_{h=0}^{m-1}w_h\le m^{1-\eta}\left(\sum_{h=0}^{m-1}w_h^{1/\eta}\right)^\eta.\)

<tbc>The last inequality of Lemma 5.8 gives<tbc>

\(\mathcal{V}_n(\mathsf{C}_n(m,\dots,m,t))\ge t^\eta m^{1-\eta},\)

<tbc>because \(\eta(d-1)/(d+1)=1-\eta\) when _d=n_-1. Consequently,

\(t^\eta\sum_{h=0}^{m-1}w_h\le\mathcal{V}_n(\mathsf{C}_n(m,\dots,m,t))\left(\sum_{h=0}^{m-1}w_h^{1/\eta}\right)^\eta.\)

These are precisely the values of the target and source of the separation rule. Every generator preserves the required inequality. Reflexivity and transitivity also preserve it, so induction on a finite derivation completes the proof.

Lemma 5.10 reduces the barrier to evaluating two families of expressions. The formal diagonal has value equal to its size, whereas the complete-graph expression has one fixed contribution from each edge. Positivity then allows the same argument to cancel any formal catalyst.

**Theorem 5.11** (operational barrier)**.** _Let_ \(n\ge 3\) _and_ \(R\ge 1\) _be integers. For the formal resources and relation in Definitions 5.3 and 5.5,_<tbc>

\(\mathbf{G}_{n,2}\unknown_{\mathrm{poly},n}\mathbf{I}_n(R)\Longrightarrow\mathrm{log}_2R\ge\frac{n^2}{4}.\)

<tbc>_More generally, suppose that R<sub>N</sub>,h<sub>N</sub> are positive integers and_ \(Z_N\in\mathcal{F}_n\) _for every positive integer N, that_ log<sub>2</sub>_h<sub>N</sub>=o(N), and that_<tbc>

\(\mathbf{G}_{n,2}^{\otimes_K^N}\otimes_KZ_N\unknown_{\mathrm{poly},n}\mathbf{I}_n(R_N)\otimes_K\mathbf{I}_n(h_N)\otimes_KZ_N\)

<tbc>_for every sufficiently large N. Then_<tbc>

\(\mathrm{liminf}_{N\rightarrow\infty}\frac{\mathrm{log}_2R_N}{N}\ge\frac{n^2}{4}.\)

<tbc>_Proof._ There are \(\genfrac(){pt}{2}{n}{2}\) edges, and every edge expression of dimension 2 has value \(2^{\eta_n}\). Multiplicativity therefore gives<tbc>

\(\mathcal{V}_n(\mathbf{G}_{n,2})=2^{\genfrac(){pt}{2}{n}{2}\eta_n}=2^{n^2/4}.\)

