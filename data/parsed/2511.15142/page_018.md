## 4.2.1 Efficient Separation via Dynamic Programming

As a quick warm-up, we show an efficient algorithm for the separation problem using dynamic programming, when the feasible set F is 2_<sup>U</sup>_. (Note that even these cases were not efficiently implementable using the Sieving algorithm of Section 2).

Define

\(\mathcal{V}_i=\{w(S):S\subseteq[i]\},0\le i\le n,\)

as the set of vector values obtained by adding a subset of the first _i_ columns of _W_. We can compute \(\mathcal{V}_i=\mathcal{V}_{i-1}\cup\{w_i+v:v\in\mathcal{V}_{i-1}\}\) starting from \(\mathcal{V}_0=\emptyset\) and increasing _i_ stopping when \(|\mathcal{V}_i|>\ell\). This implies that there exists a value \(v\in\mathcal{V}_i\) that is not in _Z_ as \(|Z|=\ell\).

The set _S_ such that _w(S_)=_v_ can be constructed by tracking the computation of V_<sub>i</sub>_.

## 4.2.2 Efficient Separation for Linear Matroids via Algebraic Techniques

In this section, we show how to solve the separation problem for F being the bases of a linear matroid M=(_U,_I). Recall that a linear matroid of rank _k_ is represented by vectors \(V=\{v_1,\dots,v_n\}\subset\mathbb{R}^k\), where each _v<sub>i</sub>_ corresponds to an element in _U_. The independent sets I are those subsets of _U_ whose corresponding vectors are linearly independent, and the bases F are the independent sets of size _k_.

In order to solve the separation problem for vector costs _w<sub>i</sub>_, we proceed in two steps:

1. First, we solve the problem when the dimension of the vectors in the separation problem is _s_=1, i.e., we are given a collection of scalars _c_<sub>1</sub>_,...,c<sub>n</sub>_, and a collection _Z_ of scalars, and want to find a feasible set \(S\in\mathcal{F}\) such that \(\sum_{i\in S}c_i\notin Z\).<tbc>

2. Secondly, we encode each vector _w<sub>i</sub>_ into a unique non-negative scalar \(\widehat{w}_i\) (and each vector in _Z_ also to a scalar), and apply the result from the first step.

The scalar encoding in the second step is easy to describe. For a vector \(v\in[-M,M]^s\), define its encoding

\(g(v):=(3nM)^s+\sum_{j=1}^s(3nM)^{j-1}v_j.\)

**Lemma 4.6** (Scalar Encoding)**.** _For any vector_ \(v\in[-M,M]\)_, its encoding g(v_) _takes on values in_ \[0,(3_nM_)<sup>_s_+1</sup>\]_. Moreover, for any two subsets_ \(S,S'\subseteq U\)_, the sums of the encoded values are equal if and only if the sums of the original vectors are equal: i.e.,_ \(\sum_{i\in S}g(w_i)=\sum_{i\in S^\prime} g(w_i)\Longleftrightarrow\sum_{i\in S}w_i=\sum_{i\in S^\prime} w_i\).

Given this, we turn to the first step, and give an algorithm for the separation problem when the columns _w<sub>i</sub>_ of _W_ are scalars:

**Lemma 4.7** (Separation for Linear Matroids)**.** _Given a linear matroid_ M=(_U,_I)_, non-negative integers c_<sub>1</sub>_,c_<sub>2</sub>_,...,c<sub>n</sub> for elements in U, and a set of non-negative values_ \(Z=\{z_1,\dots,z_\ell\}\)_, we can identify a basis_ \(S\in\mathcal{F}\) _of_ M _such that_ \(c(S)\notin Z\) _(or decide that no such basis exists) in_ \(\mathrm{poly}(n,\ell,\mathrm{log}M)\) _time, where_ \(M=\mathrm{max}_{i\in[n],j\in[\ell]}\{c_i,z_j\}\).

To give the main idea behind the lemma, let us first give a proof that yields a running time of poly(_n,M_). The full proof showing a poly(_n,_log_M_) runtime is deferred to the appendix.

