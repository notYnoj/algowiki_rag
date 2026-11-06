candidate list _L<sub>j</sub>_ into a query group _G<sub>j</sub>_, screening their half- precision lifted rows on tensor cores and filtering out candidates whose certified lower bound \(\beta(\mathbf{q},\mathbf{x})\) exceeds _U_(**q**) (Figure 2, panel 2). In Stage 3, the survivors of all probed lists are aggregated per query and verified at full precision in increasing order of their certified bounds, terminating verification as soon as the lower bound reaches the current _k_-th exact distance _h<sub>k</sub>_ (Figure 2, panel 3).

## 3.3 List-Local Certified Threshold

The screening threshold of LyCHEE is established from exact distances to a small set of representative vectors chosen from the probed lists, termed _anchors_ (Figure 2, panel 1).

**Definition 3.1** (List Anchors and Probed Anchor Set)**.** Consider an inverted list \(L_j=(\mathbf{x}_{j,1},\dots,\mathbf{x}_{j,|L_j|})\subset\mathbb{R}^D\). For a fixed stride \(s\in\mathbb{N}^+\), the _anchors_ of _L<sub>j</sub>_ are the designated subset of stored vectors at regular index intervals:

\(\Omega(L_j)=\big\{\mathbf{x}_{j,i\cdot s}\big|1\le i\le\lfloor|L_j|/s\rfloor\big\}\subset L_j,\) (3)

whose full-precision representations are preserved in device memory. For a query **q** probing lists \(S(\mathbf{q})=\bigcup_{j\in J(\mathbf{q})}L_j\), where _J_(**q**)=(_j_<sub>1</sub>_,...,j<sub>n<sub>p</sub></sub>_) ranks cluster centers by distance \(\|\mathbf{q}-\mathbf{c}_{j_1}\|\le\cdots\le\|\mathbf{q}-\mathbf{c}_{j_{n_p}}\|\), the _probed anchor set_ \(\mathcal{A}(\mathbf{q})\subseteq S(\mathbf{q})\) is the sequence of the first _b_ anchors gathered from \(\Omega(L_{j_1})\), \(\Omega(L_{j_2})\),_..._ in center order, where \(b\ge k\) denotes the anchor budget.

Given A(**q**), LyCHEE computes the exact squared distance \(\|\mathbf{q}-\mathbf{x}\|^2\) for each anchor \(\mathbf{x}\in\mathcal{A}(\mathbf{q})\). The list-local certified threshold is then

\(U(\mathbf{q})=(1+\tau)d_{(k)}\big(\mathbf{q},\mathcal{A}(\mathbf{q})\big),\) (4)

where _d_<sub>(_k_)</sub> is the _k_-th smallest exact squared distance among the anchors A(**q**), and \(\tau\) is a small relative slack that covers the rounding of the screening threshold. If the probed lists hold fewer than _k_ anchors, _U_(**q**) falls back to a bound that every stored vector satisfies, computed from the norm of the query and the largest norm of the stored vectors. The query then scans its fewer than (_k+n<sub>p</sub>)s_ probed vectors exactly.

**Proposition 3.2.** _Under Definition 3.1, if_ \(|\mathcal{A}(\mathbf{q})|\ge k\)_, then_ \(U(\mathbf{q})\ge r_k(\mathbf{q})\).

_Proof._ By Definition 3.1, the anchors are \(|\mathcal{A}(\mathbf{q})|\ge k\) distinct vectors of _S_(**q**). The _k_ nearest of them form a subset of _S_(**q**) of size _k_ whose largest squared distance is _d_<sub>(_k_)</sub>. The _k_-th smallest squared distance over the superset _S_(**q**) cannot exceed the largest distance of any of its subsets of size _k_, so that \(r_k(\mathbf{q})\le d_{(k)}\le U(\mathbf{q})\). □

The threshold of Proposition 3.2 is local to the probed lists. A threshold from anchors of the whole dataset bounds the _k_-th distance in the dataset, which is smaller than _r<sub>k</sub>_(**q**) when the probed lists miss some true neighbors. A screening under such a threshold could therefore return fewer than _k_ vectors of _S_(**q**). The list-local threshold instead keeps every member of _A<sub>k</sub>_(**q**) under the screening at every _n<sub>p</sub>_. Moreover, the anchors of the nearest lists come first, so that the budget _b_ spends exact distances on the anchors that are most likely to lie near **q** and keeps _U_(**q**) close to _r<sub>k</sub>_(**q**).

## 3.4 Routed Tensor Screening

Given the list-local threshold _U_(**q**) of each query from Stage 1, Stage 2 screens candidate vectors within probed lists on GPU tensor cores. A naive per-query scan cannot map onto tensor cores efficiently: each query probes a different subset of _n<sub>p</sub>_ lists, while an individual inverted list of a few thousand vectors offers too little work for a single query to fill a tensor-core tile. LyCHEE therefore batches _B_ queries and groups the queries that probe list _L<sub>j</sub>_ into a query group _G<sub>j</sub>_. The queries in _G<sub>j</sub>_ and the candidate vectors in _L<sub>j</sub>_ then form dense matrix tiles of 128\(\times\)128 rows on tensor cores (Figure 2, panel 2). Every list therefore streams through cache and tensor cores once per batch, however many queries probe it. All lists share the global basis _V_ of CertEx, so that one lifted row of a query screens all its probed lists; Section 4.6 shows that this basis excludes all but a few hundred probed vectors.

For each query row and candidate row in a tile, tensor cores compute their half-precision inner product, incorporating the certificate coordinates of Eq. (1) to establish<tbc>

(1) Probing & threshold ($3.3)
(2) Routed tensor screening ($3.4)
(3) Ordered bound verification ($3.5)
Query groups Gj x Candidate lists Lj
hk: k-th exact dist
L1
L2
L3
L2
Candidates sorted by B
Pruned (B > hk):
G1
Full vectors unread
U(q)
Early exit stops loop
q
L1
G2
Verified (B < hk):
Exact dist ||q - x||2
L3
Anchor a E A:
G3
Survivor (q, x):
Top-k found (k = 3)
Exact dist ||q - a||2
B(q, x) < U(q)
0.0
0.2
0.4
0.6
Lower bound B / exact dist

Figure 2: The search pipeline of LyCHEE for a batch of queries across its three execution stages.

