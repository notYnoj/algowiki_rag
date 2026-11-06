_Proof._ (Time Complexity) Throughout, we use the fact that \(\gamma,\beta\) are constants. Then, we chose a constant _k_ to satisfy \(T'(k)=O(T(\gamma))\) where \(T'(k)\) is the running time of **AdditiveAPASP** when required to produce additive error _k_. Since _C_ is a function of constants, _C_ is a constant as well. In particular, **BoundedAdditiveAPASP** requires \(O(T(\gamma))\) time, **(2,1)-APASP** requires \(\tilde{O}(n^2)=O(T(\gamma))\) time, and **AdditiveAPASP** requires \(O(T(\gamma))\) time, proving the desired time complexity.

We give some examples for \(\gamma=6\).

**Corollary 7.3.** _In time T_(6)=_n_<sup>2.06382</sup> _(Corollary 5.14), we can obtain any of the following approximations._

\(\left(\frac{9}{5},2\right),\left(\frac{8}{5},3\right),\left(\frac{7}{5},4\right),\left(\frac{6}{5},5\right)\)

## 7.2 Extension to Weighted Graphs

In this section, we give the simple observation that a good additive approximation can imply a multiplicative approximation even for weighted graphs, if given sufficient additional additive error.

**Theorem 7.4.** _Let_ \(1\le\alpha<3\) _and_ \(\beta\ge 1\) _be an integer. Let_ \(T(\gamma)\) _be the running time of Theorem 6.3 when asked to produce a_ \((1+\varepsilon,2w_{u,v}(\gamma))\) _approximation. Let_ \(\gamma=\left\lceil\frac{\alpha(\beta+1)+(\beta-1)}{2}\right\rceil-1\)_. Then, Algorithm 9 produces an_ \((\alpha,2w_{u,v}(\beta))\)_-approximation in time_ \(T(\gamma)\).

Suppose for some integer \(\gamma\ge 1\) we have a \((1+\varepsilon,2w_{u,v}(\gamma))\) approximation from Theorem 6.3. Given an integer value \(\beta<\gamma\), suppose we want a \((\alpha,2w_{u,v}(\beta))\) approximation for APSP on weighted graphs. Consider the edges that are the \(\beta+1,\beta+2,\dots,\gamma\)-th heaviest edges in a given shortest path _P_. Then,<tbc>

\(\sum_{i=\beta+1}^\gamma h(P,i)\le(\gamma-\beta)h(P,\beta+1)\le\frac{\gamma-\beta}{\beta+1}\mathsf{wt}(P)\)

<tbc>as the weight of the \(\beta+1\)-heaviest edge is at most a \(\frac{1}{\beta+1}\) fraction of the path’s total weight. In particular, if \(\hat{\delta}\) is the distance estimate given by Theorem 6.3,

\(\hat{\delta}(u,v)\le(1+\varepsilon)\mathsf{wt}(P)+2\overline{h}(P,\gamma)\)<br>
\(\le(1+\varepsilon)\mathsf{wt}(P)+2\frac{\gamma-\beta}{\beta+1}\mathsf{wt}(P)+2\overline{h}(P,\beta)\)<br>
\(\le\left(\frac{2\gamma-\beta+1}{\beta+1}+\varepsilon\right)\delta(u,v)+2\overline{h}(P,\beta)\)

Then, let us express \(\gamma\) in terms of \(\alpha,\beta\). In particular, we require \(\gamma\) such that,

\(\alpha\ge\frac{2\gamma-\beta+1}{\beta+1}+\varepsilon\)<br>
\(\gamma\le\frac{(\alpha-\varepsilon)(\beta+1)+(\beta-1)}{2}\)

