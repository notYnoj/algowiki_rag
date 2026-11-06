In proving part (i), and determining which of \(v_1,\dots,v_k\in U\backslash\{u\}\) are neighbors of _u_, we begin by computing the disjoint sets \(S_u^-,S_u^+\subseteq U\backslash\{u\}\) with exactly \(\lceil\frac{|\partial(u)|}{2}\rceil-1\) neighbors of _u_; this takes _O_(log_n_) queries and \(\widetilde{O}(n)\) time due to Lemma D.3.

For each _v<sub>i</sub>_ we choose _S_ to be one of \(S_u^-\) or \(S_u^+\) in which _v<sub>i</sub>_ does not appear--say \(S:=S_u^+\). Since \(|\partial(u,S)|<\frac{1}{2}|\partial(u)|\), we know from Observation D.1 that \(\mathrm{sign}(|\partial(S)|-|\partial(S+u)|)=-1\). We then add _v<sub>i</sub>_ to _S_ and ask for \(\mathrm{sign}(|\partial(S+v_i)|-|\partial(S+v_i+u)|)\). Since \(\partial(S,u)\) is just one edge short of reaching half the degree of _u_, this sign increases if and only if \(v_i\in N(u)\). Thus, each test requires one query, and the total query complexity is _k+O_(log_n_). After computing the median sets \(S_u^-\) and \(S_u^+\) in \(\widetilde{O}(n)\) time, we partition the vertices _v_<sub>1</sub>_,...,v<sub>k</sub>_ into two groups based on whether each _v<sub>i</sub>_ lies in \(S_u^-\) or \(S_u^+\); this takes _O(k_) time using bit vector lookups. For each group, we fix the corresponding set \(S:=S_u^+\) or \(S_u^-\) and write its bit vector once in _O(n_) time. Each query (_S+v<sub>i</sub>,S+v<sub>i</sub>+u_) is then constructed in _O_(1) time via bit flipping. The total running time is \(\widetilde{O}(n+k)\).

This proves Theorem 5.1(i).

For part (ii) of the lemma, consider the ordered sequence \(T=(v_1,\dots,v_t)\subseteq U\backslash\{u\}\) and extend it to a total ordering of _U_\\{_u_} by appending the remaining vertices arbitrarily, forming the sequence (_v_<sub>1</sub>_,...,v<sub>t</sub>,v_<sub>_t_+1</sub>_,...,v_<sub>_n_-1</sub>). Define suffixes _R<sub>k</sub>_:={_v<sub>k</sub>,...,v_<sub>_n_-1</sub>} for each _k_; by Lemma D.3, there exists some _k_ such that

\(|\partial(u,R_k)|=\left\lceil\frac{|\partial(u)|}{2}\right\rceil-1,\) (28)

and such a suffix _S_:=_R<sub>k</sub>_ can be found using _O_(log_n_) queries and \(\widetilde{O}(n)\) time via Lemma D.3. To verify that \(|\partial(u,T)|>0\), consider the sequence (_v_<sub>_t_+1</sub>_,...,v_<sub>_n_-1</sub>_,v_<sub>1</sub>_,...,v<sub>t</sub>_) with _T_ placed all the way at the end. The suffix median of this ordering computed using Lemma D.3 is the same as _S_ iff \(|\partial(u,T)|>0\). Otherwise, define the nested sequence

\(S_0:=S,\) (29)

\(S_i:=S\cup\{v_1,\dots,v_i\}\text{for}i=1,\dots,\mathrm{min}(t,k).\) (30)

(Recall that |_T_|=_t_ and |_S_|=_n-k_+1.) We have:

\(|\partial(u,S_0)|=|\partial(u,S)|=\left\lceil\frac{|\partial(u)|}{2}\right\rceil-1,\) (31)

\(|\partial(u,S_{\mathrm{min}(t,k)})|=|\partial(u,S)|+|\partial(u,T\backslash S)|\ge\frac{1}{2}|\partial(u)|.\) (32)

To justify the inequality in (32): if \(|\partial(u,T)|>0\), then \(|\partial(u,T\backslash S)|>0\), because otherwise if \(|\partial(u,T\backslash S)|=0\), then \(N(u)\subseteq S\). But this would imply \(|\partial(u,S)|=|\partial(u)|\), contradicting the fact that less than half the edges incident to _u_ go into _S_ (by the choice of _S_). Hence, _T_\\_S_ must contain a neighbor of _u_.

By Lemma D.2, there exists an index _i_ such that the sign of the query (_S_<sub>_i_-1</sub>_,S_<sub>_i_-1</sub>+_u_) is strictly smaller than that of (_S<sub>i</sub>,S<sub>i</sub>+u_). The corresponding vertex _v<sub>i</sub>_ is the first vertex in _T_ adjacent to _u_, and binary search over \(i\in[\mathrm{min}(t,k)]\) finds it using _O_(log_n_) queries and \(\widetilde{O}(n)\) time.

**Lemma 5.3** (Edge Extraction)**.** _When_ \(n\ge 4\)_, for any vertex u, a subset_ \(T\subseteq U-u\) _of vertices, and any integer k, we can extract_ \(r=\mathrm{min}(k,\partial(u,T))\) _edges from_ \(\partial(u,T)\) _using O(r_log_n_) _queries and_ \(\widetilde{O}(n)\) _time._

_Proof._ We assume that \(|\partial(u,T)|\le\left\lfloor\frac{1}{2}|\partial(u)|\right\rfloor+1\); otherwise, we split _T_ into \(T_+:=T\cap S_u^+\) and \(T_-:=T\cap S_u^-\) using the median sets from Lemma D.3, and recursively extract edges from each.

