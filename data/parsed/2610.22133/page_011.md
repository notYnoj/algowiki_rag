### Matrix Multiplication and Witnesses.

For our algorithms we need to be able to list _witnesses_ for a Boolean matrix product. For that purpose, we use the following result.

**Theorem 3.1** (Deterministic Witness Reporting \[AN96\])**.** _There is a deterministic_ \(\tilde{\mathcal{O}}(\mathrm{MM}(p,q,r))\)_-time algorithm that, given a Boolean_ \(p\times q\) _matrix A and a_ \(q\times r\) _matrix B, reports one witness for each nonzero entry of the Boolean matrix product AB. That is, for every pair_ (_i,j_) _such that AB_\[_i,j_\]=1_, the algorithm reports an index_ \(k\in[1..q]\) _satisfying A_\[_i,k_\]=1 _and B_\[_k,j_\]=1.

### Deterministic Fingerprints for Partitions.

Suppose we are given a graph **G**=(_V,E_) and a family of vertex sets \(\mathcal{S}\subseteq 2^V\). Further, let _C<sub>S</sub>(v_) be the connected component of \(v\in V\) in **G**\[_S_\]. To quickly check whether \(C_S(v)=C_{S^\prime}(v')\) for distinct \(v,v'\in V\) and \(S,S'\in\mathcal{S}\), we introduce the following fingerprints for the connected components.

**Lemma 3.2.** _Consider a set V_=\[1_..n_\] _together with k partitions_ P<sub>1</sub>_,...,_P_<sub>k</sub> of V, and for_ \(v\in V\) _let P<sub>i</sub>(v_) _denote the set of the i-th partition containing v. Then, in deterministic time_ O(_nk_log(_nk_))_, we can construct functions_ \(h_1,\dots,h_k:V\rightarrow[1..M]\) _with M=_O(_nk_) _that assigns a_ fingerprint _to each set of each partition, such that h<sub>i</sub>(v_)=_h<sub>j</sub>(u_) _if and only if P<sub>i</sub>(v_)=_P<sub>j</sub>(u)._

**Proof.** Let \(\mathcal{P}=\sqcup_{i=1}^k\mathcal{P}_i\) be the multiset containing all sets. We proceed as follows.

**Our algorithm.** First, we sort the elements of each set \(P\in\mathcal{P}\), looking at them as lists. Equal lists have equal size, so we partition P into buckets by length; lists in different buckets get different fingerprints. Within a bucket \(\mathcal{P}^\ell\subseteq\mathcal{P}\) all lists have length \(\ell\), and we sort them lexicographically, making equal lists adjacent. A single scan then assigns fingerprints by incrementing a global counter whenever the current list differs from its predecessor, and we store _h<sub>i</sub>(v_) as the fingerprint of _P<sub>i</sub>(v_) in a table indexed by \([1..k]\times V\) . It is not difficult to see that this construction satisfies the claimed property.

**Runtime.** Sorting sets initially, bucketing by lengths, and the final scan cost at most O(_nk_log_n_).

For the lexicographic sort on \(\mathcal{P}^\ell\) we use \(\mathcal{O}(|\mathcal{P}^\ell|\mathrm{log}|\mathcal{P}^\ell|)\) comparisons, where each comparison costs \(\mathcal{O}(\ell)\) time. Overall this costs \(\mathcal{O}(\sum_{\ell=1}^n\ell\cdot|\mathcal{P}^\ell|\mathrm{log}|\mathcal{P}^\ell|)=\mathcal{O}(nk\mathrm{log}(nk))\), because the sizes of the lists sum up to _nk_ and \(|\mathcal{P}^\ell|=\mathcal{O}(nk)\); empty buckets contribute zero.

## 4 Proofs

### 4.1 Induced Subgraph Connected Components in Matrix Multiplication Time

In this subsection, we present the proof for Main Theorem 1 and Lemma 4.2, which proves the upper and lower bounds for the induced subgraph connected component problem.

**Main Theorem 1.** _There is a deterministic algorithm that solves the induced subgraph connected component problem in time_ \(\tilde{\mathcal{O}}(\mathrm{MM}(|\mathcal{S}|,n,n))\) _for an n-node input graph and a non-empty input set_ S.

**Proof.** Let **G**=(_V,E_) be an undirected _n_-node graph, and let \(\mathcal{S}\subseteq 2^V\) be non-empty. To compute the connected components of **G**\[_S_\] for each \(S\in\mathcal{S}\), we rely on the following subroutine.

Claim 4.1. _For each_ \(S\in\mathcal{S}\)_, let_ \(f_S:V\rightarrow[1..M]\cup\{\perp\}\) _be a function, where M=_poly(_n). Then, in time_ \(\tilde{\mathcal{O}}(\mathrm{MM}(|\mathcal{S}|,n,n))\)_, for each_ \(S\in\mathcal{S}\) _and w such that_ \(f_S(w)\neq\perp\)_, we can find a node_ \(u\in V\) _that satisfies_ \(\{u,w\}\in E\), \(f_S(u)\neq f_S(w)\) _and_ \(f_S(u)\neq\perp\)_, or verify that no such node exists._

Proof. Let _B=_O(log_n_) be the number of bits required to represent any value in \[1_..M_\]. The algorithm proceeds as follows:

