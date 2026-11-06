**Algorithm 3** ObliviousSINGLEQuery: HNSW single query

**Input:** Query \(\vec{q}\); top-layer entry \(i_\mathrm{top}^\mathcal{D}\); tables \(\{\mathcal{G}_\ell,\mathcal{D}_\ell\}_{\ell=0}^{L-1}\) and D<sub>-1</sub>; params \((ef,\overline{\Delta},M)\); result count _k_.

**Output:** Top-_k_ nearest neighbor vectors of \(\vec{q}\).

1: \(i_\mathrm{ep}^\mathcal{D}\leftarrow i_\mathrm{top}^\mathcal{D}\)

2: **for** \(\ell=L-1\) **to** 1 **do**

3: \(W_\ell\leftarrow\) ObliviousSearchLayer(\(\vec{q}\), \(i_\mathrm{ep}^\mathcal{D}\), _ef_=1, \(\overline{\Delta^{(\ell)}}\), _M_, \(\ell\))

4: \((\omega^\mathcal{D},b^\mathcal{D},\delta)\leftarrow W_\ell[0]\)

5: \(i_\mathrm{ep}^\mathcal{D}\leftarrow b^\mathcal{D}\)

6: \(W_0\leftarrow\) ObliviousSearchLayer(\(\vec{q}\), \(i_\mathrm{ep}^\mathcal{D}\), _ef_, \(\overline{\Delta^{(0)}}\), _M_, \(\ell=0\))

7: Reveal \(\{b_i^\mathcal{D}\}_{i=0}^{k-1}\) in \(W_0\triangleright\) top-_k_ vector addresses in additional table

8: Fetch final top-_k_ vectors \(\{\vec{v}_i\}_{i=0}^{k-1}=\{\mathcal{D}_{-1}[b_i^\mathcal{D}]\}_{i=0}^{k-1}\)

9: Reconstruct \(\{\vec{v}_i\}_{i=0}^{k-1}\) to Querier

10: **return** \(\{\vec{v}_i\}_{i=0}^{k-1}\)

<tbc>_U_ queries using a single shuffled HNSW index with no further online reshuffling. To achieve this, we propose using two global cross-query visited structures, one for graph nodes and the other for vectors, so later queries can safely reuse previously accessed information without re-accessing the underlying tables.

## 5.1 Double Visitor Arrays

The challenge in the multiple-query setting is that later queries may need to access nodes and vectors that earlier queries already accessed. As noted above, the single-query protocol prevents repeated data access with an array _V_ tracking previously accessed nodes. Moving to the multiple-query setting, one straightforward idea is to simply make _V_ global, so that each node can be accessed by only one query. However, queries may have overlapping search<tbc>

<tbc>paths, so simply globalizing _V_ would make multi-query HNSW search incorrect.

To address this issue, we propose two global cross-query caches recording all nodes and vectors accessed so far. Specifically, we maintain a graph-side visited set \(V_\ell^\mathcal{G}\) and a vector-side visited set \(V_\ell^\mathcal{D}\), which store the neighbor information of visited nodes and the contents of visited vectors, respectively. When exploring a node _v_ in graph \(\mathcal{G}_\ell\), we first check whether \(v\in V_\ell^\mathcal{G}\). If so, the neighbor information of _v_ is retrieved from \(V_\ell^\mathcal{G}\), followed by a dummy graph access. Otherwise, _v_ and all its neighbor information are read from \(\mathcal{G}_\ell\) and stored in \(V_\ell^\mathcal{G}\) for future use. After obtaining the neighbor information, we access each neighbor’s vector to compute its query distance. Similarly, for each vector access, we first check \(V_\ell^\mathcal{D}\). If the vector is already present, it is retrieved from \(V_\ell^\mathcal{D}\), followed by a dummy vector access. Otherwise, it is loaded from \(\mathcal{D}_\ell\) and appended to \(V_\ell^\mathcal{D}\). Moreover, before processing multiple queries, we pre-shuffle both the graphs and the vector databases so that all nodes and vectors, including dummy ones, remain anonymous. More precisely, for each graph access, we first perform a linear scan of \(V_\ell^\mathcal{G}\). Then, depending on whether the target node is already in the cache, we access either the real node or a dummy node in the graph. Finally, we access \(V_\ell^\mathcal{G}\) again to store the newly retrieved real node or a dummy entry. Notably, we generate \(U\times T\) dummy nodes so that each graph access can use a different dummy node. Similarly, for each vector access, we first scan \(V_\ell^\mathcal{D}\), then access either a real or dummy vector, and finally store it in \(V_\ell^\mathcal{D}\).

### 5.1.1 Security Sketch.

The multi-query protocol extends the single- query protocol with cross-query caches for repeated graph and<tbc>

Measure 2: Duplicate Layer s
The Global
Original HNSW Access Pattern
Oblivious HNSW Access Pattern
2
ID
Vector
Access
Measure 1: ID Shuffle
ID
Vector
A
[1,1,1,1]
C
D
Layer 2
A
F
Access
A
[3,3,3,3]
Entry Node
B
[2,2,2,2]
B
[1,1,1,1]
C
[3,3,3,3]
Access
A
D
ID Shuffle
C
F
A
Access
[2,2,2,2]
Nearest Candidate
Valid Steps
Pad to ef + 5 Steps
D
[4,4,4,4]
C
B
F
Layer 1
B
F
D
1
Search Result
H
E
[5,5,5,5]
Access
A
D
ID Shuffle
B
G
A
A
[5,5,5,5]
Query Node
Step 1
Step 2
Step 3
Step 4
G
[7,7,7,7]
C
B
F
Layer 0
Access
Access
Padded Path
Step 5
K
Access Pattern
Access Pattern:
0
Node Edge
Layer 2 Access Global : A, C
Layer 2 Access 2: A, B
ID Vector
Layer 1 Access Global : B, D, E
Layer 1 Access 1: A, E, F
A
[7,7,7,7]
Padded Node Edge
Layer 0 Access Global : B, D, F, G
Layer 0 Access 0: A, D, F, G
B
[1,1,1,1]
A, B, D, F are accessed again
Repeat access exists
No Repeat for each table
(a) Oblivious logical flow: upper-bounded termination
(b) Oblivious Access Pattern
Initial with entry node
Step 1
Step 2
Step 3
Step 4
Replace visited neighbors of C with dummies
W
A
Append M neighbors
A
C
D
Sort
C
Append M neighbors
C
J
K
Sort
C
W
B
ef
ef
M
Truncate
ef
M
Truncate
ef
C
B
H
J
C
F
H
J
Extract C[0] and
C
A
H
I
append M neighbors
H
I
C
D
Sort
C
D
H
Extract C[0] and
D
H
J
K
Sort
D
H
J
Step 5
T
T
M
Truncate
T
T
M
Truncate
T
Append M neighbors
Append M neighbors
A
A
D
A
A
D
A
A
D
V
A
C
D
A
C
D
A
A
D
C
H
J
L
M
M
M
2M
2M
V
A
Initial with dummy node
(c) Oblivious data structures

**Figure 5: Overview of Oblivious HNSW. (a) Each layer runs exactly** \(ef+\Delta\) **steps for data-independent termination. (b) Per-layer replication and reshuffling hide cross-layer access patterns. (c) Oblivious data structures maintain the HNSW search state.**

