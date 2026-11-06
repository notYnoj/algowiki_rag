_O(B(n+B_)), respectively, while still maintaining a running time of poly(_n,B_). See Section 1.1.3 for a summary comparing the results.

## 5 Minimum Cut using Cut Comparisons

We now turn to specific combinatorial problems, and give efficient algorithms using their structural properties. We begin with the min-cut problem on graphs and prove Theorems 1.6 and 1.7, which we restate for convenience.

**Theorem 1.6** (Minimum cut)**.** _There is a randomized algorithm that computes the exact minimum cut of a simple graph G with high probability using_ \(\widetilde{O}(|V|)\) _cut comparison queries and_ \(\widetilde{O}(|V|^2)\) _time._

**Theorem 1.7** (Graph recovery)**.** _A simple unweighted graph_ \(G\notin\{K_2,\bar{K}_2,K_3,\bar{K}_3\}\) _can be recovered using_ \(O(min\{(|E|+|V|)log|V|,|V|^2\})\) _cut comparison queries and in_ \(\widetilde{O}(|V|^2)\) _time._

In order to prove the two results, we draw on the following useful primitives that can be obtained using the cut comparison queries:

**Theorem 5.1** (Structural Primitives)**.** _When_ \(n\ge 4\)_, for any vertex_ \(u\in U\):

(_i)_ _Given a set of k vertices_ \(A=\{v_1,\dots,v_k\}\subseteq U\backslash\{u\}\)_, the neighbors of u in A can be determined using k+O_(log_n_) _queries and_ \(\widetilde{O}(n+k)\) _time._<tbc>

(_ii)_ _Given an ordered subset_ \(T=(v_1,\dots,v_t)\subseteq U\backslash\{u\}\)_, either the neighbor_ \(v_i\in N(u)\) _of u with the smallest index_ \(i\in[t]\) _(or a certificate that_ \(N(u)\cap T=\emptyset\)_) can be found using O_(log_n_) _queries and_ \(\widetilde{O}(n)\) _time._

**Remark 5.2** (A Note on Runtimes)**.** We assume that the query input (_S,T_) to the comparison oracle is given as two bit vectors encoding the sets _S_ and _T_ respectively. The running time bounds are the total computation done to process the query information, where oracle calls are assumed to take unit time. The dominant cost is writing down the input bit vectors for queries, which takes _O(n_) time per query. In addition, we separately account for standard algorithmic overhead, such as binary search or other data structure updates.

### 5.1 Graph Reconstruction

With the power of Theorem 5.1 behind us, the graph recovery problem is easily solved. Indeed, using Theorem 5.1(i), we can discover the neighborhood of node \(u\in V\) using _n_-1+_O_(log_n_) queries and \(\widetilde{O}(n)\) time; summing over all nodes gives us the graph _G_ in at most _O(n_<sup>2</sup>) queries and \(\widetilde{O}(n^2)\) time.

To get the better bound of _O(m_log_n_) for sparse graphs, we use Theorem 5.1(ii) to prove:

**Lemma 5.3** (Edge Extraction)**.** _When_ \(n\ge 4\)_, for any vertex u, a subset_ \(T\subseteq U-u\) _of vertices, and any integer k, we can extract_ \(r=min(k,\partial(u,T))\) _edges from_ \(\partial(u,T)\) _using O(r_log_n_) _queries and_ \(\widetilde{O}(n)\) _time._

_Proof._ Start with _T_<sub>0</sub>:=_T_ and extract a neighbor \(v_i\in N(u)\cap T_i\) (if any) from \(\partial(u,T_i)\) using Theorem 5.1(ii); set _T_<sub>_i_+1</sub>:=_T<sub>i</sub>-v<sub>i</sub>_, and repeat. Each step requires _O_(log_n_) queries and \(\widetilde{O}(n)\) time. Repeating this for \(r=min(k,\partial(u,T))\) neighbors gives a total of _O(r_log_n_) queries and \(\widetilde{O}(nr)\) time. A more efficient implementation, which amortizes the search and is detailed in Section D, achieves the claimed \(\widetilde{O}(n)\) time.

