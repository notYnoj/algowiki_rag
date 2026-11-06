Both subsets satisfy the same degree bound, and the total query and runtime complexity remains the same.

Let _S_ be a median set disjoint from _T_, which exists by construction and can be found using _O_(log_n_) queries and \(\widetilde{O}(n)\) time. Let _T_={_v_<sub>1</sub>_,...,v<sub>t</sub>_}, and define the nested sets \(S_j:=S\cup\{v_1,\dots,v_j\}\). We maintain two bit vectors: one for the fixed set _S_, and one for the growing prefix of _T_.

In each iteration, we find the smallest index _j_ such that the sign of the query (_S_<sub>_j_-1</sub>_,S_<sub>_j_-1</sub>+_u_) is strictly smaller than that of (_S<sub>j</sub>,S<sub>j</sub>+u_), indicating that \(v_j\in N(u)\). We locate this index using the doubling version of binary search. Once _v<sub>j</sub>_ is found, we report the edge {_u,v<sub>j</sub>_}, remove _v_<sub>1</sub>_,...,v<sub>j</sub>_ from _T_, and repeat. Since we extract at most _r_ edges, we perform at most _r_ such searches, each requiring _O_(log_n_) queries, for a total of _O(r_log_n_) queries overall.

### Running time.

Constructing the median set _S_ takes \(\widetilde{O}(n)\) time. To construct the query sets, we reuse the bit vector for _S_ and build each query by appending a prefix \(\{v_1,\dots,v_i\}\subseteq T\). In each iteration, the doubling search explores prefixes of geometrically increasing size until it finds a neighbor at index _j_. The total size of all prefixes queried in that iteration is _O(j_log_t_), so the time spent constructing queries is _O(j_log_t_). Deleting _v_<sub>1</sub>_,...,v<sub>j</sub>_ from _T_ also takes \(\widetilde{O}(j)\) time. The values _j_<sub>1</sub>_,...,j<sub>r</sub>_ across all _r_ iterations sum to at most _n_ as these are gaps between the edge indices, so the overall total time taken is \(O\left(\sum_{i=1}^rj_ilogn\right)=\widetilde{O}(n)\).

## D.2 Cut sparsifiers using \(\widetilde{O}(n)\) queries

Using Lemma 5.4, we show that we can implement the sparsifier construction from \[RSW18, Algorithm 3.4\] and the min-cut computation from \[RSW18, Algorithm 4.1\] using \(\widetilde{O}(n/\varepsilon^2)\) cut comparison queries. The mentioned algorithms and relevant theorems from \[RSW18\] are mentioned verbatim below:

5.1 **Input:** An accuracy parameter \(\varepsilon\), and a cut-query oracle for graph _G_.

1. Initialize an empty graph _H_ on _n_ vertices and \(G_0\leftarrow G\).<tbc>

2. For _j_=0_,...,_log_n_, set \(\kappa_j=n2^{-j}\) and:<tbc>

(a) Subsample \(G'_j\) from _G<sub>j</sub>_ by taking each edge of _G<sub>j</sub>_ with probability<tbc>

<tbc>\(q_j=min\left(\frac{100\cdot 40\cdot lnn}{\kappa_j},1\right).\)<tbc>

(b) In each connected component of \(G'_j\):<tbc>

i. While there exists a cut of size \(\le q_j\cdot\frac{4}{5}\kappa_j\), remove the edges from the cut. Let the connected components induced by removing the cut edges be _C_<sub>1</sub>_,...,C<sub>r</sub>_.<tbc>

ii. For every \(i\in[r]\) and every edge (known or unknown) with both endpoints in _C<sub>i</sub>_,<br>
set the approximate edge strength \(k'_e:=\frac{1}{2\kappa_j}\) (alternatively, subsample every edge in<br>
\(C_i\times C_i\) with probability \(2q_j/\varepsilon^2\) and add it to _H_ with weight \(\varepsilon^2/2q_j\)).<tbc>

iii. Set _G_<sub>_j_+1</sub> as the graph obtained by contracting _C<sub>i</sub>_ for each \(i\in[r]\) in _G<sub>j</sub>_.

**Theorem D.5** (Theorem 3.5 from \[RSW18\])**.** _For each edge_ \(e\in G\)_, the approximate edge strength_<tbc>

**Algorithm 5:** (Approximating Edge Strengths and Sampling a Sparsifier _H_)

**Output:** The edge strength approximators \(\{k'_e\}\) (or the sparsifier _H_).

