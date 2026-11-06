<tbc>_u_ stores its _B_ outgoing neighbors in a fixed-width _row_ row(_u_) pre-sorted by vector distance from _u_. Under any disk _c_, out-of-disk entries in row(_u_) are ignored while surviving in-disk (_active_) entries remain sorted by vector distance. Retaining all active entries defines the complete active projection \(\mathcal{H}_\infty(c)\), which sets the recall ceiling on _c_; scanning row(_u_) sequentially and taking only the first \(\ell\) active entries reconstructs a degree-\(\ell\) _recovery graph_ \(\mathcal{H}_\ell(c)\subseteq\mathcal{H}_\infty(c)\) that caps per-step vector evaluations at \(\ell\), with minimum connectivity budget given by the _cut-rank threshold_ \(\ell_\mathrm{SC}(c)\).

To keep \(\mathcal{H}_\infty(c)\) connected across all \(\Omega(n^2)\) disks on both POI catalogs with mostly unique coordinates and photo archives where thousands of records share a landmark coordinate \[1\], we group co-located objects into _coordinate fibers_. If a vertex simply linked to its geographically closest objects, a dense landmark would consume its entire neighbor budget on co-located ties. Because all members of a fiber lie at the same distance from any query center, any disk admits a fiber _either in full or not at all_. This property decomposes active connectivity into query-independent _intra-fiber connectivity_ and _inter-coordinate quotient connectivity_, both satisfied at polylogarithmic degree under a marked-site model. Guided by this analysis, REACH builds one width-_B_ row per vertex offline from global vector candidates and a fiber-aware geographic stream, and answers queries online through an _O(n_) spatial seed grid and a two-phase _filter-then-score_ kernel. Our contributions are:

\(\bullet\) **Theoretical Foundation:** We prove that 2D disks induce \(\Omega(n^2)\) active sets (Theorem 2.2) and admit no contiguous order (Proposition 2.3). We then define \(\mathcal{H}_\ell(c)\) and cut rank \(\ell_\mathrm{SC}(c)\) (Theorem 3.3), prove fiber closure and route decomposition (Lemma 3.4, Theorem 3.5), and establish polylogarithmic degree bounds for strong connectivity and compact-disk \(\alpha\)-shortcut routing (Theorem 3.7, Corollary 3.8).<tbc>

\(\bullet\) **Graph Index and Query Algorithms:** We develop REACH’s dual-source row assembly (Algorithm 1), which combines global vector candidates with a 3D kd-tree geographic stream, bounds coordinate ties through intra-fiber \(\alpha\)-pruning, and reuses vector<tbc>

<tbc>survivors as zero-cost witnesses (Proposition 4.2), paired with a two-phase first-\(\ell\)-active expansion algorithm (Algorithm 2) and an _O(n_) grid seed directory.<tbc>

\(\bullet\) **Comprehensive Evaluation:** Across four datasets up to 10<sup>7</sup> objects and six selectivities (\(\bar{\sigma}\in[10^{-5},1]\)), one REACH index per dataset achieves 2.49\(\times\) higher geometric-mean QPS than the best per-setting baseline at 0.95 Recall@10 on selective queries (fastest in 14/16 selective cells, 6.33\(\times\) over CubeGraph, 3.56\(\times\) over Geo-Partition), builds 3.8\(\times\)-11.9\(\times\) faster than CubeGraph, and uses 37%-45% less space on three of the four datasets.

## 2 Preliminaries

**Data Model and GFANN Queries.** Let \(\mathcal{D}=\{o_v=(x_v,s_v):v\in V\}\) be a dataset of _n_=|_V_| objects with identifiers _V_={1_,...,n_}. Each object \(v\in V\) has a feature vector \(x_v\in\mathcal{X}\subseteq\mathbb{R}^D\) measured by Euclidean distance \(d(x,y)=\|x-y\|_2\) and a geographic coordinate \(s_v=(\lambda_v,\phi_v)\in\mathcal{S}\subseteq\mathbb{S}^2\) measured by great-circle distance \(\Delta(s,t)\) (notation in Appendix B.1). A spatial filter _c_=(_g,r_) with center \(g\in\mathcal{S}\) and radius _r\>_0 defines the closed disk \(\Omega_c=\{s\in\mathcal{S}:\Delta(s,g)\le r\}\) and the _active set_ \(\mathcal{A}(c)=\{v\in V:\Delta(s_v,g)\le r\}\) of size _m_=|A(_c_)| and selectivity \(\sigma(c)=m/n\). Given a GFANN query _q_=(_x<sub>q</sub>,c<sub>q</sub>,k_) with _k<sub>q</sub>_=min{_k,m_}, the exact answer \(T_k(q)\subseteq\mathcal{A}(c_q)\) consists of the _k<sub>q</sub>_ active objects closest to _x<sub>q</sub>_ under \(v\prec_qw\Longleftrightarrow(d(x_q,x_v),v)\prec_\mathrm{lex}(d(x_q,x_w),w)\).

**Proximity Graphs, Beam Search, and Path Erosion.** To avoid scanning all _m_ active vectors in _O(mD_) time, ANN systems build a directed proximity graph _G_=(_V,E_) offline \[13, 17, 25\]: each vertex _u_ collects vector-proximate candidates and applies \(\alpha\)-witness diversification (discarding _w_ if an earlier neighbor _v_ satisfies \(\alpha d(x_v,x_w)\le d(x_u,x_w)\)) to cap out-degree at _B_ \[41\], forming _u_’s _row_ row(_u_). At query time, best-first _beam search_ maintains a pool of at most _L_ candidates ordered by \(d(x_q,\cdot)\) and expands the closest unvisited vertex until no pool candidate is closer than the _k_-th best result (Recall\(@k=|R\cap T_k(q)|/k_q\)). Effective search requires _directed reachability_ (which sets the recall ceiling) and _distance-contracting_<tbc>

Query disk
(a) Store only 2 neighbors
(b) Recover 2 active neighbors
c = (g, r)
target t
h1
h2
h2
h2
h3
h4
h4
t
h1
V3
h5
V3
t
h5
V3
V1
V3
V1
V1
V4
V4
V4
h3
h3
V2
t
S
V2
S
V2
h3
h5
seed s
h3
h5
seed s
h3
h2
h2
h4
h5
ordered row
v1: no active exits
ordered row
h7
S
h1
V1
h5
V2
S
h1
V1
h5
V2
(s, g) ≤ r
V1
h5
h2
V2
S
V1
h5
h2
V2
S
inside = active
first 2 slots: no route to t
skip inactive first 2 active route
active node / edge
inactive context
filtered edge
route
not stored in (a)

**Figure 1: Filter-induced path erosion and active-edge recovery from entry seed** _s_ **to target** _t_ **under budget** \(\ell=2\) **(Example 2.1). Left: disk** _c_=(_g,r_) **activates** A(_c_)={_s,v_<sub>1</sub>_,v_<sub>2</sub>_,v_<sub>3</sub>_,v_<sub>4</sub>_,t_} **(green) and deactivates** {_h_<sub>1</sub>_,...,h_<sub>7</sub>} **(grey). Cards (a) and (b) place these objects in vector space alongside the stored rows of** _s_ **and** _v_<sub>1</sub>**: _(a)_ storing only two neighbors truncates** row(_v_<sub>1</sub>) **to** \[_h_<sub>5</sub>_,h_<sub>2</sub>\]**, leaving** _v_<sub>1</sub> **with no active exits; _(b)_ scanning wider ordered rows skips inactive entries (**_h_<sub>1</sub>_,h_<sub>5</sub> **in** row(_s_) **and** _h_<sub>5</sub>_,h_<sub>2</sub> **in** row(_v_<sub>1</sub>)) **to recover the first** \(\ell=2\) **active neighbors (**\[_v_<sub>1</sub>_,v_<sub>2</sub>\] **for** _s_**,** \[_v_<sub>2</sub>_,s_\] **for** _v_<sub>1</sub>**), forming** H<sub>2</sub>(_c_) **and restoring route** \(s\rightarrow v_2\rightarrow v_3\rightarrow v_4\rightarrow t\) **(orange).**

