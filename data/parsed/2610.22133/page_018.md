## 18 Asteroidal Triples and Friends in (Likely Necessary) Matrix Multiplication Time

Our algorithm.

Our algorithm, rather than listing all dominating pairs, will list all non-dominating pairs, by trying to find for each _u,v_ a _witness_ node \(w\notin N[u]\cup N[v]\) such that _C<sub>w</sub>(u_)=_C<sub>w</sub>(v_). Specifically, the algorithm proceeds as follows:

(**i)** First, we use Main Theorem 1 to find all neighborhood-deleted components. For each \(v\in V\) , let C_<sub>v</sub>_ be the connected components in **G**_<sub>v</sub>_ and set \(\mathcal{C}:=\bigcup_{v\in V}\mathcal{C}_v\). Similarly to Main Theorem 2, we use Lemma 3.2, to compute the count \(|\{v:C\in\mathcal{C}_v\}|\) of the number of times each connected component _C_ appears across the graphs **G**_<sub>v</sub>_.

(**ii)** For each \(v\in V\) , let _M<sub>v</sub>_ denote the largest connected component in C_<sub>v</sub>_, i.e., \(M_v:=argmax_{C\in\mathcal{C}_v}|C|\). If multiple components share the same maximum size, we fix one arbitrarily. We then construct a Boolean \(n\times n\) matrix _A_, indexed by the vertices in _V_ , defined as follows:

\(A[u,w]=\left\{\begin{array}{ c c }
1 & \text{if}u\in M_w \\
0 & \text{otherwise}
\end{array}\right.\)

By computing the BMM product \(AA^\top\), we identify and mark as non-dominating all pairs _u,v_ for which \((AA^\top)[u,v]=1\). That is we mark all pairs that are witnessed by a component in \(\{M_v\}_{v\in V}\).

(**iii)** Next, for each \(C\in\mathcal{C}\), we do the following. We let \(x_C\in V\) be the node with \(C\in\mathcal{C}_{x_C}\) that minimizes the number of nodes in **G**_<sub>x<sub>C</sub></sub>_, i.e.,

\(x_C:=argmin_{w\in V:C\in\mathcal{C}_w}|V(\mathbf{G}_w)|=argmax_{w\in V:C\in\mathcal{C}_w}|N[w]|.\)

If _C_ appears in less than |_V_(**G**_<sub>x<sub>C</sub></sub>_)|/2=(_n_-|_N[x<sub>C</sub>_]|)/2 graphs **G**_<sub>w</sub>_, i.e., if \(|\{w\in V:C\in\mathcal{C}_w\}|<(n-|N[x_C]|)/2\), we do nothing. Otherwise, if \(|\{w\in V:C\in\mathcal{C}_w\}|\ge(n-|N[x_C]|)/2\) we iterate over all pairs of nodes \(u,v\in C\) and mark them as non-dominating pairs.

(**iv)** Return as dominating pairs all pairs _u,v_ that have not been marked as non-dominating in either Step (ii) or Step (iii).

**Correctness.** We show that for each non-dominating pair _u,v_, we identify at least one witness _w_ and mark _u,v_ as non-dominating, either in Step (ii) or in Step (iii).

To this end fix a non-dominating pair _u,v_. For each witness _w_ of _u,v_, let _C<sub>w</sub>(u_)=_C<sub>w</sub>(v_) be the component containing both vertices. Choose _w_<sup>∗</sup> among these witnesses to maximize |_C<sub>w</sub>(u_)|, and set _C_:=_C_<sub>_w_<sup>∗</sup></sub>(_u_)=_C_<sub>_w_<sup>∗</sup></sub>(_v_). We begin by observing that \((AA^\top)[u,v]=1\) if _C=M_<sub>_w_<sup>∗</sup></sub>. Consequently, if _C=M_<sub>_w_<sup>∗</sup></sub>, the pair _u,v_ is marked as non-dominating in Step (ii) and we may henceforth assume that \(C\neq M_{w^*}\).

The following claim establishes that _u,v_ is marked in Step (iii).

\(\square\) Claim 4.10. _The number of_ \(w\in V\) _such that_ \(C\in\mathcal{C}_w\) _is at least_ |_V_(**G**<sub>_w_<sup>∗</sup></sub>)|/2=(_n_-|_N[w_<sup>∗</sup>]|)/2_, i.e.,_ \(|\{w\in V:C\in\mathcal{C}_w\}|\ge(n-|N[w^*]|)/2\)_. In particular, because_ \(n-|N[w^*]|\ge n-|N[x_C]|\) _we have that u,v is marked as a non-dominating pair in Step (iii)._

Proof. Given our assumption that \(C\neq M_{w^*}\), we know that \(|C|\le(n-|N[w^*]|)/2\) (otherwise, _C_ would be _M_<sub>_w_<sup>∗</sup></sub>). Consequently, the number of nodes in **G**_<sub>w<sup>∗</sup></sub>_ that are not contained in _C_ is at least

\(|\{w\in\mathbf{G}_{w^*}:w\notin C\}|=(n-|N[w^*]|)-|C|\ge(n-|N[w^*]|)/2.\)

To conclude, it suffices to show that for each \(w\in V\backslash(N[w^*]\cup C)\) we have \(C\in\mathcal{C}_w\).

To this end, let \(w\in\mathbf{G}_{w^*}\) be an arbitrary node with \(w\notin C\). Since \(w\notin C\), we have that \(N[w]\cap C=\varnothing\). Because of this, each pair of nodes in _C_ remains connected in **G**_<sub>w</sub>_. This implies that _w_ witnesses _u,v_ and \(C':=C_w(u)=C_w(v)\) satisfies \(C\subseteq C'\). However, by our choice of _w_<sup>∗</sup>, we must have that \(|C'|\le|C|\), which means that \(C'=C\). We conclude that \(C\in\mathcal{C}_w\), as desired. \(\square\)

