From _u_, we take the edge (_u,v_<sup>∗</sup>), followed by \((v^*,v)\in E^*\) so that,

\(\hat{\delta}(u,v)\le\hat{\delta}_{\ell(v)}(u,v^*)+1\)<br>
\(\le\delta(u,v)+2(a+1)+2\)<br>
\(\le\delta(u,v)+\beta\)

Thus, to prove Theorem E.1, it only remains to analyze the performance of Algorithm 15.

_Proof._ (Time Complexity)

We separately analyze the complexity of each phase. By Lemma E.4, _E_ occurs with probability \(O\left(\frac{1}{n^2}\right)\). Since in this case Algorithm 15 requires \(\tilde{O}(n^3)\) time, this contributes at most \(\tilde{O}(n)\) to the expected run-time. Thus, in the following assume that _E_ does not occur.

## Phase 0 rdecompose requires _O(m+n_)=_O(n_<sup>2</sup>) time to sample each vertex set randomly and construct the edge sets _E<sub>i</sub>_. Verifying that _D<sub>i</sub>_ is of the appropriate size and dominates \(|N(v)|\ge s_i\) requires time \(\tilde{O}(n^2)\).

## Phase 1 By Lemma E.3, computing the sets _X(u,i),C(u,i_) require time at most \(\tilde{O}\left(n^{2+\frac{1}{k}}\right)\). By Lemma 2.4, augmenting _D<sub>i</sub>_ in Line 210 requires time \(\tilde{O}(n^2)\).

Line 209 requires time,

\(\tilde{O}\left(ns_{k_0+2}s_{k_0}\right)=\tilde{O}\left(n^{3-\frac{2k_0+2}{k}}\right)=\tilde{O}\left(n^{2+\frac{1}{k}}\right)\)

whenever \(\beta\ge 4\) as shown in Lemma E.3.

## Phase 2 First, we bound the complexity of each call to Dijkstra as in the proof of Lemma 3.2 for DenseAPASP.

Fix some _j_. Then, \(|E_j|\le ns_{j-1}=n^{2-\frac{j-1}{k}}\) and \(|D_{j_1}\times D_{j_2}|=\tilde{O}\left(\frac{n}{s_{j_1}}\times\frac{n}{s_{j_2}}\right)=\tilde{O}\left(n^\frac{j_1+j_2}{k}\right)=\tilde{O}\left(n^{2-\frac{j-1}{k}}\right)\) as \(j_1+j_2\le 2k+1-j\). Note for any fixed _w_ that \((w\times V)\cup E^*\) has size \(\tilde{O}(n)\). Summing over \(|D_j|=\tilde{O}\left(\frac{n}{s_j}\right)=\tilde{O}\left(n^\frac{j}{k}\right)\), all invocations of Dijkstra require time \(\tilde{O}\left(n^{2+\frac{1}{k}}\right)\).

Line 215 requires time \(\tilde{O}(n^2)\) as every vertex _u_ is in at most one _q(w,D<sub>j</sub>_) for any fixed _j_.

Finally, Line 219 requires time \(\tilde{O}(n^2)\) over all _u,v,i_. By the bound on \(|C(u,i)|=\tilde{O}(n^{1/k})\), Line 220 requires time \(\tilde{O}\left(n^{2+\frac{1}{k}}\right)\). In particular, this is the overall time bound when _E_ does not occur, giving the desired result by substituting \(k=\frac{3\beta}{2}+1\).

We have the following Corollary.

Recall the following result of Roditty \[Rod23\].

**Lemma E.10** (Theorem 5.1 of Roditty \[Rod23\])**.** _Let_ \(k'\ge 6\) _be an even integer. There is an algorithm that computes an additive_ \(k'-2\) _approximation in_ \(\tilde{O}(n^{2-\frac{2}{k^\prime+2}}m^\frac{2}{k^\prime+2})\) _expected time, for every_ \(u,v\in V\) _for which_ \(\delta(u,v)\le k'\).

