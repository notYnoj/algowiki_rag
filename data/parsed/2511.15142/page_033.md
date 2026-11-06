_Proof._ Let _L<sub>j</sub>_={_v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>j</sub>_} and _R<sub>j</sub>_={_v<sub>j</sub>,v_<sub>_j_+1</sub>_,...,v_<sub>_n_-1</sub>} for \(j\in[n-1]\). First, check if \(\partial(v_1)>\partial(v_1+u)\) in which case, we can conclude \(S_u^-=\emptyset,S_u^+=\{v_2,v_3,\dots,v_{n-1}\}\) because {_u,v_<sub>1</sub>} has to be the only edge using Observation D.1. Similarly for _v_<sub>_n_-1</sub>. So from now on, assume that \(\partial(v_1)\le\partial(v_1+u)\) and \(\partial(v_{n-1})\le\partial(v_{n-1}+u)\). Equivalently, this can also be written as \(\partial(R_2)\ge\partial(R_2+u),\partial(L_{n-2})\ge\partial(L_{n-2}+u)\).

In what follows, we will first describe how to compute \(S_u^-\) and then use a similar argument to compute \(S_u^+\). If \(\partial(v_1)=\partial(v_1+u)\), then again we can simply conclude \(S_u^-=\emptyset\) because this implies that \(|\partial(u)|=2\) and {_u,v_<sub>1</sub>} is an edge. Otherwise, if \(\partial(v_1)<\partial(v_1+u)\), we can search for \(S_u^-\) as a tipping point for the chain defined by the sequence _v_<sub>1</sub>_,v_<sub>2</sub>_,...,v_<sub>_n_-2</sub> using Lemma D.2 because \(\partial(v_1)<\partial(v_1+u)\) and \(\partial(v_1,\dots,v_{n-2})\ge\partial(v_1,\dots,v_{n-2}+u)\). By the arguments in Lemma D.2, there exists \(i\in[n-2]\) such that \(v_i\in N(u)\) and

\(|\partial(u,L_{i-1})|<\frac{1}{2}|\partial(u)|,|\partial(u,L_i)|\ge\frac{1}{2}|\partial(u)|.\) (25)

This implies that \(S_u^-:=L_{i-1}\) satisfies \(|\partial(u,S_u^-)|=\cap\frac{|\partial(u)|}{2}\big|-1\). We can use the same argument to get \(S_u^+\). Moreover, since \(S_u^-\) and \(S_u^+\) are prefix and suffix of the same ordering, and contain no more than half the neighbors of _u_, they must be disjoint. The proof makes two calls to Lemma D.2, one for each ordering, with _O(n_) preprocessing. Each call takes \(\widetilde{O}(n)\) time, so the total running time is \(\widetilde{O}(n)\).

## D.1 Proof of Structural Primitives Lemma

We can now prove the main structural result Theorem 5.1, which we restate for convenience:

**Theorem 5.1** (Structural Primitives)**.** _When_ \(n\ge 4\)_, for any vertex_ \(u\in U\):

(_i)_ _Given a set of k vertices_ \(A=\{v_1,\dots,v_k\}\subseteq U\backslash\{u\}\)_, the neighbors of u in A can be determined using k+O_(log_n_) _queries and_ \(\widetilde{O}(n+k)\) _time._<tbc>

_(ii)_ _Given an ordered subset_ \(T=(v_1,\dots,v_t)\subseteq U\backslash\{u\}\)_, either the neighbor_ \(v_i\in N(u)\) _of u with the smallest index_ \(i\in[t]\) _(or a certificate that_ \(N(u)\cap T=\emptyset\)_) can be found using O_(log_n_) _queries and_ \(\widetilde{O}(n)\) _time._

Before we prove the theorem, we first prove a primitive that shows how to identify if a vetrex is isolated using constant queries when \(n\ge 4\):

**Lemma D.4** (Home Alone)**.** _For any three vertices_ \(u,v,w\in U\)_, vertex u is isolated iff_

\(|\partial(v)|=|\partial(u+v)|,|\partial(w)|=|\partial(u+w)|,|\partial(v+w)|=|\partial(u+v+w)|.\) (26)

_Proof._ The three equalities are trivial when _u_ is isolated. Given the equalities, we observe that they can be written equivalently as

\(|\partial(u,v)|=\frac{1}{2}|\partial(u)|,|\partial(u,w)|=\frac{1}{2}|\partial(u)|,|\partial(u,v+w)|=\frac{1}{2}|\partial(u)|.\) (27)

Using the fact that \(|\partial(u,v+w)|=|\partial(u,v)|+|\partial(u,w)|\) gives \(|\partial(u)|=0\).

_Proof of Theorem 5.1._ We first check if \(\partial(u)=\emptyset\) using Lemma D.4. If \(\partial(u)=\emptyset\), there are no neighbors of _u_ in _A_ in part (i) and we can certify that \(N\cap T=\emptyset\) in part (ii). Assume \(\partial(u)\neq\emptyset\) from here on.

