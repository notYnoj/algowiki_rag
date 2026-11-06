_Proof._ Fix \(u\in V\) and \(k_0+1\le qi\le k_0+\frac{\beta}{2}-1\), Consider the event _E(u,i_).<tbc>

\(\mathrm{Pr}(E(u,i))=\mathrm{Pr}(\neg A(u,i)\wedge B(u,i)\le\mathrm{Pr}(B(u,i)|\neg A(u,i))\)

<tbc>Conditioned on \(\neg A(u,i)\), define the random variable \(X=|N(u,r_i)\cap D_{i+1}|\). Since _D_<sub>_i_+1</sub> is constructed by sampling each vertex probability \(p=\frac{3\mathrm{log}n}{s_{i+1}}\), _X_ is the sum of at most _s<sub>i</sub>_ Bernoulli random variables. Let _Y_ be the sum of _s<sub>i</sub>_ Bernoulli random variables with the same probability _p_ so that _Y_ stochastically dominates _X_. Note that \(\mathbb{E}[X]\le\frac{3\mathrm{log}ns_i}{s_{i+1}}=3s_{k-1}\mathrm{log}n\). By a standard Chernoff bound,

\(\mathrm{Pr}(X>12s_{k-1}\mathrm{log}n)\le\mathrm{Pr}(Y>12s_{k-1}\mathrm{log}n)<\mathrm{exp}(-3s_{k-1}\mathrm{log}n)\)

Thus, we can easily union bound over _O(n_) events _E(u,i_) as each occurs with inverse exponential probability. Note that _C(u,i_) is defined from the randomly chosen _D<sub>i</sub>_, and these sets are constructed before _D<sub>i</sub>_ is augmented by a deterministic hitting set of _X(u,i_) in Line 210.

From Lemma 2.6, `rDominate` with high probability satifies the necessary requirements. To see this, consider some threshold _s<sub>i</sub>_ and vertex \(\mathrm{deg}(v)\ge s_i\). The probability _D<sub>i</sub>_ fails to dominate _s<sub>i</sub>_ with _P_ chosen above is at most,

\((1-p)^{s_i}\le\mathrm{exp}(-3\mathrm{log}n)\le n^3\)

We union bound over all _u,i_ to obtain the probability \(\tilde{O}(1/n^2)\).

Second, the probability that \(|D_i|\ge\frac{12n\mathrm{log}n}{s_i}\) is small by an identical argument to the error bound for _E<sub>i</sub>_. Since we bound over _O_(1) events, these also occur with negligible probability. We conclude the proof by union bounding over all the error events.

**Lemma E.5.** _Suppose that the error event E does not occur. Then, Algorithm 15 outputs_ \(\hat{\delta}\) _such that,_

\(\delta(u,v)\le\hat{\delta}(u,v)\le\delta(u,v)+\beta\)

_for all_ \(\delta(u,v)\le\beta+1\).

We delay the proof of Lemma E.5, instead beginning with a few useful lemmas that will be crucial to our proof. In the following lemma, we prove that a reasonable additive approximation is obtained whenever _A(u,i_) is true. That is, we assume \(|N(u,r_i)|\ge s_i\) is large.

**Lemma E.6.** _Let_ \(k_0+1\le i\le k_0+\frac{\beta}{2}-1\)_. Let u,v be a pair of vertices and_ \(P\subset E_{k_0+1}\) _be a shortest path. Suppose_ \(|N(u,r_i)|\ge s_i\) _where_ \(r_i=\frac{\beta}{2}-(i-(k_0+1))\)_. Then, after Line 219 we have,_<tbc>

\(\hat{\delta}(u,v)\le\delta(u,v)+\beta\)

<tbc>_Proof._ Suppose \(|N(u,r_i)|\ge s_i\), then there is some vertex \(w\in X(u,i)\cap D_i\subset N(u,r_i)\cap D_i\) so that \(\delta(u,p(u,D_i))\le r_i\). In particular,

\(\hat{\delta}(u,v)\le r_i+\hat{\delta}(p(u,D_i),v)\)

Let us examine the quantity \(\hat{\delta}(p(u,D_i),v)\). Since after Line 210 the shortest path in _G_ between _u,p(u,D<sub>i</sub>_) is at most _r<sub>i</sub>_, we begin by showing that the path between _u,p(u,D<sub>i</sub>_) exists in the graph _G<sub>i,u</sub>_. If there is an edge missing from _E<sub>i</sub>_, let _w_ be the vertex closest to _u_ such that deg(_w)\>s_<sub>_i_-1</sub>. Therefore, \(N(w)\cap D_{i-1}\neq\emptyset\) and \(N(w)\cap D_i\neq\emptyset\). If _w_ is not the vertex immediately preceding _p(u,D<sub>i</sub>_), then this violates the property that _p(u,D<sub>i</sub>_) is the nearest vertex in _D<sub>i</sub>_ to _u_. Otherwise, if _w_ is the vertex immediately preceding _p(u,D<sub>i</sub>_), then the edge (_w,p(u,D<sub>i</sub>_)) is accessible in the<tbc>

