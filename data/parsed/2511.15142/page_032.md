## D Omitted proofs from Section 5

We begin with a simple observation allowing us to test, for a vertex _u_ and any non-empty set _S_ that is a proper subset of _U-u_, whether a majority of _u_’s neighbors lie inside _S_.

**Observation D.1.** Suppose we perform a cut comparison query on the pair _S_ and _S+u_. Then the result of the query is:<tbc>

\(\mathrm{sign}(|\partial(S)|-|\partial(S+u)|)=\mathrm{sign}\left(|\partial(u,S)|-\frac{1}{2}|\partial(u)|\right).\) (21)

<tbc>_Proof._ Indeed,

\(|\partial(S)|-|\partial(S+u)|=|\partial(u,S)|-|\partial(u,U\backslash(S+u))|\)<br>
\(=2|\partial(u,S)|-|\partial(u)|.\)

Therefore, the sign of the query (_S,S+u_) indicates whether a majority of _u_’s edges go into _S_.

The above observation allows us to reason about neighborhood structure. We now formalize how to use this to isolate individual neighbors.

**Lemma D.2** (tipping point)**.** _For_ \(u\in U\)_, consider a set_ \(\emptyset\neq S\subseteq U\backslash\{u\}\)_, and a sequence v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>t</sub> of vertices in_ \(U\backslash(S\cup\{u\})\)_. Define_ \(S_i=S\cup\{v_1,\dots,v_i\}\)_. Suppose_ \(S_t\neq U-u\) _and the comparisons of the queries_ (_S_<sub>0</sub>_,S_<sub>0</sub>+_u_) _and_ (_S<sub>t</sub>,S<sub>t</sub>+u_) _differ. Then there exists an index_ \(i\in[t]\) _such that_

\(\mathrm{sign}(|\partial(S_{i-1})|-|\partial(S_{i-1}+u)|)<\mathrm{sign}(|\partial(S_i)|-|\partial(S_i+u)|).\) (22)

_The corresponding vertex v<sub>i</sub> must be a neighbor of u, and can be identified using O_(log_t_) _queries and_ \(\widetilde{O}(n)\) _time via binary search._

_Proof._ By Observation D.1, the \(\mathrm{sign}(|\partial(S)|-|\partial(S+u)|)\) is monotonic in _S_, since the quantity \(|\partial(u,S)|\) increases as _S_ grows. Therefore, if the sign changes between _S_<sub>0</sub> and _S<sub>t</sub>_, then by monotonicity, it must strictly increase at some index _i_, which proves (22). Moreover, using the equality in (21) again, (22) can be rewritten as

\(|\partial(u,S_{i-1})|<|\partial(u,S_i)|,\) (23)

and hence _u_ is adjacent to the vertex _v<sub>i</sub>_. Finally, a binary search over the chain finds such an _i_ using _O_(log_t_) queries. The binary search performs _O_(log_t_) queries, each requiring _O(n_) time to write bit vectors, for a total of \(O(n\mathrm{log}t)=\widetilde{O}(n)\). The additional binary search logic takes _O_(log_t_) time.

We now apply these ideas to construct balanced sets around each vertex.

**Lemma D.3** (median sets)**.** _For any vertex u with_ \(\partial(u)\neq\emptyset\)_, and an ordering v_<sub>1</sub>_,...,v_<sub>_n_-1</sub> _of the vertices in U-u, there exist disjoint sets_ \(S_u^-,S_u^+\subseteq U\backslash\{u\}\) _that are a prefix and a suffix of the sequence such that_

\(|\partial(u,S_u^-)|=|\partial(u,S_u^+)|=\left\lceil\frac{|\partial(u)|}{2}\right\rceil-1.\) (24)

_These sets can be found using O_(log_n_) _queries and_ \(\widetilde{O}(n)\) _time._

