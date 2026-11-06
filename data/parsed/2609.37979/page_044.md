The analogous implication can be shown for approximating Max-_k_-Coverage with a small data structure.

**Theorem 9.6.** _Assume that there is an_ \(\varepsilon>0\) _such that_ Gap-Max-3-\(\mathsf{SAT}_{1,1-\varepsilon}\) _cannot be solved in the Isomorphic-Priors model with k prior instances each of size at most n and query time polynomial in n, even when k_=1 _prior instance is given._

_Then there is an_ \(\varepsilon'>0\) _such that_ Max-_k_-Coverage _cannot be approximated within_ \((1-1/e+\varepsilon')\) _in the Isomorphic-Priors model with data structure of size polynomial in n and query time polynomial in n, even when k_=1 _prior instance is given. Also, there is an_ \(\varepsilon''\) _such that k_-Median _cannot be approximated better than_ \((1+2/e-\varepsilon'')\) _in the Isomorphic-Priors model with data structure of size polynomial in n and query time polynomial in n, even when k_=1 _prior instance is given._

## 9.1 Hardness Results for Gl

We show that GI cannot be solved in our setting with a small data structure, unless \(\mathsf{GI}\in\mathsf{coMA}\). The following Lemma is inspired by \[LT92, Corollary 4.4\].

**Lemma 9.7.** _Unless_ \(\mathsf{GI}\in\mathsf{coMA}\), GI _cannot be solved in the Isomorphic-Priors model with k prior instances each having at most n many vertices with a data structure of polynomial size in n and query time polynomial in n, even when k_=1 _prior instance is given._

_This statement is even true for a randomized data structure such that the query is correct with probability_ 5/6.

_Proof._ Assume that there is an algorithm consisting of the preprocessing phase Pre and query phase Query in the Isomorphic-Priors model that solves GI with a data structure of size poly_<sub>k</sub>(n_)<sup>35</sup> and query time poly_<sub>k</sub>(n_), and in particular works for _k_=1.

We show that this implies \(\overline{\mathsf{GI}}\in\mathsf{MA}\), and hence \(\mathsf{GI}\in\mathsf{coMA}\).

### An MA protocol for <o>GI</o>.

On a tuple of input graphs (_G_<sub>0</sub>_,G_<sub>1</sub>), Merlin sends Arthur a string _D_ of length poly(_n_), claimed to be a valid data structure for the single prior instance

\(I^\star:=(G_0,G_0).\)

Arthur repeats the following test twice

1. choose a uniform random bit \(b\in\{0,1\}\) and a uniform random permutation \(\pi\) of \[_n_\],<tbc>

2. form the query instance<tbc>

<tbc>\(J:=(G_0,\pi(G_b)),\)<tbc>

3. compute _z_:=Query(_D,J_) and define \(\widehat{b}:=0\) iff _z_=1 (otherwise \(\widehat{b}:=1\)),<tbc>

4. accept this round iff \(\widehat{b}=b\).

Arthur accepts iff the majority of the _t_ rounds accept.

### Completeness.

Assume \(G_0\unknown\cong G_1\). Let Merlin send the actual data structure _D_=Pre({_I<sup>⋆</sup>_}). If _b_=0, then there exists an isomorphism \(\varphi:G_0\rightarrow\pi(G_0)\), hence \(J=(G_0,\pi(G_0))\) is isomorphic to _I<sup>⋆</sup>_ via \((\mathrm{id},\varphi)\) and GI(_J_)=1. Thus correctness forces Query(_D,J_)=1, so \(\widehat{b}=0=b\) with probability at least 5/6. If _b_=1, then \(G_0\unknown\cong\pi(G_1)\), so GI(_J_)=0 and moreover _J_ is not isomorphic to _I<sup>⋆</sup>_. By correctness on non-matching queries, Query(_D,J_) is either 0 or \(\perp\) with probability at least 5/6, hence \(z\neq 1\) and therefore \(\widehat{b}=1=b\) with probability at least 5/6. Thus, each round accepts with probability at least 5/6. Therefore, Arthur accepts with probability at least 25/36_\>_2/3.

<sup>35</sup>This means that the size is polynomial in _n_ if _k_ is fixed.

