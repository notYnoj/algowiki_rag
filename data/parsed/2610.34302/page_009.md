<tbc>_Proof._ By triangle inequality,<tbc>

\(\mathsf{d}(u,v)\ge\mathsf{d}(c,u)-\mathsf{d}(c,v).\)

<tbc>Thus it suffices to prove

\(\mathsf{d}(c,v)<\frac{\mathsf{d}(c,u)-\mathsf{d}(c,v)}{\alpha},\)

which is equivalent to \((\alpha+1)\mathsf{d}(c,v)<\mathsf{d}(c,u)\). This is exactly the assumption.

**Lemma 2.2.** _Both algorithms_ (_Algorithms 2.3 and 2.4_) _compute_ \(\alpha\)_-navigable graphs for_ (_P,_d).

_Proof._ The proof only uses the following common property of the level-_i_ cover: its clusters form a partition of _P_, and each cluster _C_ with center _p_ satisfies \(C\subseteq B(p,r_i/(\alpha+2))\).

Fix one of the two algorithms, a source point \(s\in P\), and a target point \(t\in P\) with \(s\neq t\). Let _i_ be an index such that \(r_i<\mathsf{d}(s,t)\le r_{i+1}\); such an index exists by the scaling assumption. Since the level-_i_ clusters cover _P_, the point _t_ lies in some cluster _C_ with center _p_, and hence<tbc>

\(\mathsf{d}(t,p)\le\frac{r_i}{\alpha+2}.\)

<tbc>By triangle inequality,<tbc>

\(\mathsf{d}(s,p)\le\mathsf{d}(s,t)+\mathsf{d}(t,p)\le r_{i+1}+\frac{r_i}{\alpha+2},\)

<tbc>and

\(\mathsf{d}(s,p)\ge\mathsf{d}(s,t)-\mathsf{d}(t,p)>r_i-\frac{r_i}{\alpha+2}.\)

Thus \(p\in A_i(s)\), so the algorithm adds the edge (_s,p_).

Finally,

\(\frac{\mathsf{d}(p,s)}{\alpha+1}>\frac{1}{\alpha+1}\left(r_i-\frac{r_i}{\alpha+2}\right)=\frac{r_i}{\alpha+2}\ge\mathsf{d}(p,t).\)

Thus \(\mathsf{d}(p,t)<\mathsf{d}(p,s)/(\alpha+1)\). By Lemma 2.1, the edge (_s,p_) is an \(\alpha\)-navigation from _s_ to _t_. Since this holds for every distinct pair \(s,t\in P\), the output graph is \(\alpha\)-navigable.

## 2.4 Constant Bicriteria Approximation.

**Lemma 2.3.** _Let_ (_P,_d) _be a metric space of n points and let_ \(\alpha\ge 1\)_. Let G_=(_P,E_) _be the graph returned by Algorithm 2.3. Then G is an_ \((\alpha,\beta)\)_-bicriteria_ 5_-approximation, where_

\(\beta=2(1+\delta)(\alpha+2)+2=2\alpha+8+\frac{4}{\alpha}.\)

_Proof._ Let _G<sup>⋆</sup>_=(_P,E<sup>⋆</sup>_) be a sparsest \(\beta\)-navigable graph, and fix a source vertex \(s\in P\). Write \(E_s^\star=\{(s,x)\in E^\star\}\) for the out-edges of _s_ in _G<sup>⋆</sup>_.

Since \(E_s=\bigcup_{i=0}^LE_s^i\), we have \(|E_s|\le\sum_{i=0}^L|E_s^i|\). To bound this sum, we consider all pairs (_i,p_) such that \((s,p)\in E_s^i\); the same center _p_ is counted separately at different levels. For each such pair, the \(\beta\)-navigability of _G<sup>⋆</sup>_ guarantees an edge \((s,x)\in E_s^\star\) such that

\(\mathsf{d}(x,p)<\frac{\mathsf{d}(s,p)}{\beta}.\)

Choose one such edge and define \(\phi_s(i,p)=(s,x)\).

**Claim 2.4.** _For each fixed level i, the map_ \(p\mapsto\phi_s(i,p)\) _is injective on_ \(\{p\in P|(s,p)\in E_s^i\}\).

