<tbc>add a logarithmic term in _N_, _d_, and _M_ at the base layer: \(\overline{\Delta^{(0)}}=\left\lceil log_2(Nd/M)\right\rceil+C\). In our experiments, we set _C_=7, which covers more than 95% of cases across the 50K tests.

We therefore apply this fixed-step rule: 1+7=8 search steps at each upper layer and \(\lceil log_2(N\cdot d/M)\rceil+ef^{(0)}+7\) at the base layer. Since \(\overline{\Delta^{(\ell)}}\) may be larger than the actual number of residual steps, and since the second termination condition in line 4 of Algorithm 1 may trigger early termination, the search may otherwise stop before completing \(\overline{\Delta^{(\ell)}}\) steps. In this case, we continue the search using dummy nodes. When dummy nodes are treated as candidates during the search, they are assigned sentinel distances that rank worse than all real candidates, and thus never affect the result set _W_. Overall, our strategy yields an oblivious search procedure. Here, the number of search steps is _O_(1) at each upper layer and \(O\left(log(N\cdot d/M)\right)\) at the base layer. Since HNSW has _O_(log_N_) layers, this gives a total of \(O\left(log(N\cdot d/M)+logN\right)\) search steps per query.

## 4.2 Making Data Structures Oblivious

We next make the data structures of HNSW oblivious. Recall that each layer individually maintains three structures: the visited set _V_ , the candidate set _C_, and the result set _W_. However, the sizes and update frequencies of the three sets are inherently data- and query-dependent during search. We therefore redesign them into oblivious counterparts.

### 4.2.1 Oblivious Result Set W.

The result set _W_ is easier to make oblivious than _C_ and _V_ because original HNSW already bounds its size by _ef_. The only data-dependent behavior is the conditional insertion rule, i.e., inserting a node into _W_ when it improves the current _ef_ results and passes the visited check (line 13 in Algorithm 1). We remove this data-dependent condition by obliviously considering every node for insertion, at a cost of _O(ef_) per node.<sup>2</sup> Overall, this naive approach costs \(O(M\cdot ef)\) in each iteration. For practical efficiency, we instead insert all _M_ elements, apply oblivious sorting, and then reduce the size back to _ef_, incurring only _O(ef_log<sup>2</sup>(_ef_)) complexity. Since log<sup>2</sup>(_ef_) is much smaller than _M_ in our setting, this approach outperforms the naive alternative in practice.

### 4.2.2 Oblivious Visited Set V.

The visited set _V_ records explored nodes to prevent later revisits. In the original HNSW, _V_ is a dynamic set whose size and insertion pattern are both query- and data- dependent, since nodes are inserted only when first encountered and their growth is unpredictable. To eliminate this dependence, we observe that _V_ can safely contain duplicate nodes. We therefore replace the set, whose size is unpredictable, with a list whose size increases by exactly one after each exploration. More precisely, each iteration appends all _M_ neighbors, regardless of whether they have appeared before, so that _V_ contains exactly \(M\cdot T+1\) entries after _T_ iterations. A full linear scan of this list performs a visited check at a cost of _O(MT_), which is scalable and independent of _N_.

### 4.2.3 Oblivious Candidate Set C.

The candidate set _C_ stores the nodes awaiting expansion and is also a fully dynamic set. In the original HNSW, its size is inherently data-dependent: each iteration extracts one node from the set but may insert zero, a few, or up to _M_ new nodes. The insertion condition is also data-dependent, since neighbors are added to _C_ only when they pass the visited check and could improve the result set _W_ (line 10, 13 in Algorithm 1). To make _C_ oblivious, we leverage the fixed iteration _T_ established in Section 4.1. Since at most _T_ candidates will be extracted, entries beyond the top-_T_ positions cannot be used and need not be retained. We therefore replace the dynamic set with a fixed-length array of size _T_. In every iteration, all _M_ neighbors, whether real or dummy after the visited check, are appended to _C_. We then perform an oblivious sort by distance and retain only the top-_T_ entries. As we discussed earlier, since dummy nodes carry a maximum distance _d_max, they always expand to other dummy nodes. They cannot influence the result set _W_ even if they are selected after the real nodes are exhausted in _C_. This fixed-size and fixed-update design of _C_ eliminates data-dependent behavior while preserving original HNSW’s functionality.

## 4.3 Making Access Patterns Oblivious

The HNSW search process involves two types of data access: vector access and graph access. During the search, a node first incurs a vector access where its distance to the query is evaluated. If the node is later selected for expansion (extracted from the candidate list _C_), it then incurs a graph access to retrieve its neighbor list. A straightforward way to make both accesses oblivious is to store the graphs and the vector database in DORAM. However, this incurs significant overhead, as each access requires \(O(logN_\ell)\) time.

To design a more efficient solution, we recall that achieving oblivious access requires two properties: data anonymization, which can be easily achieved through pre-shuffling, and non-repetitive access, where no address is revisited within a query. In this single- query setting, we assume that both graph and vector data have been anonymized through offline reshuffling. Therefore, if each item is retrieved at most once, the access is oblivious. We now analyze where repeated accesses arise and how to avoid them.

Within a single layer, both graph and vector accesses are non- repetitive. The visited set prevents revisiting any node, so its neighbor list and its vector are retrieved at most once. Across layers, the search may revisit a logical node because each layer builds a separate, increasingly refined neighborhood structure, and the same node provides different information at each layer. So its data<tbc>

<sup>2</sup>One could reduce this to _O_(polylog(_ef_)) using more sophisticated oblivious algorithms [1], but these become advantageous only when _ef_ is very large (\(\ge 10^4\)), which is far beyond our setting.

SIFT-1M
MNIST-60K
DEEP-image-9.99M
Yandex-DEEP-1B
Turing-1B
GIST-1M
Fashion-60K
BIGANN-1B
SPACEV-1B
SSNPP-1B
k=5
k= 10
k= 25
k= 50
k= 100
e= 3
e= 2
e= 1
e= 0 (base)
base-log2 Nd M
7
7
7
7
7
7
7

**Figure 4: Per-layer residual** \(\Delta\) **at** _M_=128, \(ef^{(\ell\ge 1)}=1\), \(ef^{(0)}=k+10\), **on the** 10 **datasets. The bottom row of each panel shows the base-layer step count minus** \(\lceil log_2(Nd/M)\rceil\)**.**

