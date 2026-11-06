## 20 Asteroidal Triples and Friends in (Likely Necessary) Matrix Multiplication Time

**Main Theorem 4.** _There is a deterministic_ \(\tilde{\mathcal{O}}(n^\omega)\)_-time algorithm for listing all two-pairs._

**Proof.** Let **G**=(_V,E_) be an undirected graph.

**Our algorithm.** We proceed as follows:

(**i)** We first precompute several quantities. Using Main Theorem 1, we find all neighborhood-deleted components. Furthermore, via matrix multiplication, we compute for each pair of vertices _u,v_ the number of common neighbors \(|N(u)\cap N(v)|\) and the size of their set difference |_N(u_)\\_N(v_)|. We also set up the fingerprints of Lemma 3.2.<tbc>

(**ii)** Next, for each node \(v\in V\) , we consider **G**_<sub>v</sub>_ and the set of connected components C_<sub>v</sub>_ within it. For each \(C\in\mathcal{C}_v\), we iterate over all nodes \(w\in C\) to compute the set \(M_v(C):=\{w:|N(v)\cap N(w)|=max_{x\in C}|N(v)\cap N(x)|\}\), which consists of all nodes in _C_ that maximize the number of common neighbors with _v_ in **G**. From each set _M<sub>v</sub>(C_), we also select an arbitrary _representative_ node _r<sub>v</sub>(C_).<br>
Among all nodes \(w\in C\), we restrict our testing to whether _v_ and the representative _r<sub>v</sub>(C_) form a two-pair. By Proposition 4.11, any node in _C_ that does not maximize the number of common neighbors with _v_ in **G** cannot form a two-pair with _v_. Furthermore, it is easy to observe that either all nodes in _M<sub>v</sub>(C_) form a two-pair with _v_, or none of them do.<tbc>

(**iii)** For each node \(v\in V\) and each \(C\in\mathcal{C}_v\), we iterate over all nodes \(w\in C\backslash N[r_v(C)]\) in O(|_C_|) time. If there exists a node _w_ satisfying _C<sub>r<sub>v</sub>(C_)</sub>(_w_)=_C<sub>r<sub>v</sub>(C_)</sub>(_v_), we mark _v_ and _r<sub>v</sub>(C_) as not a two-pair.<tbc>

(**iv)** For each node \(v\in V\) and each \(C\in\mathcal{C}_v\), we again iterate over all nodes \(w\in C\) to compute the following quantity:

\(\Delta_v(C):=\sum_{w\in C\backslash N[r_v(C)]}|N(w)\cap N(v)|-\sum_{w\in C\backslash N[r_v(C)]}|N(w)\cap N(r_v(C))|+\sum_{w\in C\cap N(r_v(C))}|N(w)\backslash N[r_v(C)]|.\) (8)

If \(\Delta_v(C)>0\), we mark _v_ and _r<sub>v</sub>(C_) as not a two-pair.

(**v)** Finally, for each node \(v\in V\) , we list all nodes _u_ that form a two-pair with _v_. Specifically, for each \(C\in\mathcal{C}_v\), if _v_ and _r<sub>v</sub>(C_) have not been marked as not a two-pair, we report all nodes \(u\in M_v(C)\) as forming a two-pair with _v_.

**Correctness.** Let \(v\in V\) and \(C\in\mathcal{C}_v\) be arbitrary. Moreover, abbreviate _u_:=_r<sub>v</sub>(C_). As elaborated earlier, it suffices to show that _v_ and _u_ are not marked if and only if _v_ and _u_ are a two-pair.

We first observe that _u_ and _v_ are not a two-pair if and only if there is \(w\in C\backslash\{u\}\) that satisfies \((N(w)\cap N(v))\backslash N(u)\neq\varnothing\). We first prove that _u_ and _v_ are marked in Step (iii) if and only if there is \(w\in C\backslash N[u]\) with \((N(w)\cap N(v))\backslash N(u)\neq\varnothing\).

Claim 4.12. _There is a node_ \(w'\in C\backslash N[u]\) _with_ \(C_u(w')=C_u(v)\) _if and only if there is a node_ \(w\in C\backslash N[u]\) _with_ \((N(w)\cap N(v))\backslash N(u)\neq\varnothing\).

Proof. First, suppose there exists a node \(w'\in C\backslash N[u]\) such that \(C_u(w')=C_u(v)\). Consider an arbitrary path \(\pi\) from \(w'\) to _v_ in **G**_<sub>u</sub>_. Let _x_ be the first node on \(\pi\) that is not in _C_, and let \(w\in C\) be its immediate predecessor on the path. Note that any neighbor of _w_ that is not in _C_ must belong to _N(v_); therefore, \(x\in N(v)\). Therefore, \(w\in C\backslash N[u]\) and \((N(w)\cap N(v))\backslash N(u)\neq\varnothing\).

Conversely, observe that \(v\notin N(u)\), \(w\notin N(u)\), and \((N(w)\cap N(v))\backslash N(u)\neq\varnothing\) immediately imply that _v_ and _w_ are connected by a path of length two in **G**_<sub>u</sub>_. Thus, _C<sub>u</sub>(w_)=_C<sub>u</sub>(v_). \(\triangleleft\)

It remains to prove that if there is no \(w\in C\backslash N[u]\) with \((N(w)\cap N(v))\backslash N(u)\neq\varnothing\), then \(\Delta_v(C)>0\) if and only if _u_ and _v_ are not a two-pair.

Claim 4.13. _If there is no_ \(w\in C\backslash N[u]\) _with_ \((N(w)\cap N(v))\backslash N(u)\neq\varnothing\)_, then_ \(\Delta_v(C)=\sum_{w\in C\cap N(u)}|(N(w)\cap N(v))\backslash N(u)|\)_. In particular,_ \(\Delta_v(C)>0\) _if and only if there is_ \(w\in C\backslash\{u\}\) _with_ \((N(w)\cap N(v))\backslash N(u)\neq\varnothing\).

\(\blacktriangleleft\)

