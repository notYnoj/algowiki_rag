Input: pool C<sub>v</sub>(u) sorted by \(d(x_u,\cdot)\); fibers F(z) streamed by \(\Delta(s_u,z)\)<br>
Output: fixed-width row row(u) of width B=B<sub>v</sub>+B<sub>g</sub> sorted by \(\prec_u\)<br>
\(P\leftarrow[]\); \(g\leftarrow 0\)<br>
foreach \(v\in C_v(u)\) while |P|\<B<sub>v</sub> do<br>
   if d(x<sub>v</sub>,x<sub>w</sub>)\>d(x<sub>u</sub>,x<sub>v</sub>)/\(\alpha\forall w\in P\) then append v to P<br>
back-fill P up to B<sub>v</sub> with closest unused \(v\in C_v(u)\)<br>
foreach coordinate z in nondecreasing \(\Delta(s_u,z)\) while g\<B<sub>g</sub> do<br>
   W \(\leftarrow[]\); t \(\leftarrow 0\)<br>
   foreach \(v\in F(z)\backslash\{u\}\) in vector order while g\<B<sub>g</sub> and<br>
   t\<C<sub>tie</sub> do<br>
   t \(\leftarrow t+1\)<br>
   if \(\exists w\in W:d(x_v,x_w)\le d(x_u,x_v)/\alpha\) then continue<br>
   append v to W<br>
   if \(v\notin P\) then append v to P; \(g\leftarrow g+1\)<br>
back-fill P up to B with unused \(v\in C_v(u)\), then sentinels \(\perp\)<br>
return P sorted by (d(x<sub>u</sub>,x<sub>v</sub>),v), with sentinels \(\perp\) last

**Algorithm 2:** Expand\((u,q,\ell)\): Two-phase first-\(\ell\)-active expansion

Input: \(u\in\mathcal{A}(c_q)\); query q=(x<sub>q</sub>,c<sub>q</sub>,k); budget \(\ell\); visited set V<br>
Output: scored active neighbor list D for the search beam<br>
\(A\leftarrow[]\); \(j\leftarrow 0\); \(D\leftarrow[]\)<br>
foreach \(v\in\text{row}(u)\) in stored vector-distance order do<br>
   if \(v=\perp\) then break<br>
   if \(\Delta(s_v,g_q)>r_q\) then continue<br>
   \(j\leftarrow j+1\) // active rank rank<sub>u,c<sub>q</sub></sub>(v)<br>
   if \(v\notin\mathcal{V}\) then append v to A<br>
   if \(j=\ell\) then break<br>
foreach \(v\in A\) do<br>
append<br>
(<br>
_v,_<br>
_d_<br>
<br>
<br>
<br>
_x<sub>q</sub><br>
<br>
<br>
_x<sub>v</sub>_<br>
<br>
<br>
)<br>
to<br>
\(D;\mathcal{V}\leftarrow\mathcal{V}\cup\{v\}\)<br>
return D

computed only for \(v\in A\) (at most \(min\{\ell,B\}\) vector evaluations vs. at most B scalar checks in Phase 1). Because j increments on every active entry (including visited \(a\in\mathcal{V}\) in Figure 4), beam search traverses the exact static subgraph \(\mathcal{H}_\ell(c_q)\), where \(\ell_\text{exact}(c)=\ell_\text{SC}(c)\), \(\ell_\text{safe}=B\), and \(Pr\{\ell_\text{SC}(c)\le B\}\ge 1-\delta\).

**Practical Selection of** \(\ell\)**, Spatial Seeding, and Dynamic Updates.** Because \(\ell_\text{SC}(c)\) has a median of 48 on selective queries (Exp- 3), a fixed default \(\ell=64\) (or \(\ell=32\) for \(\tilde{\sigma}\le 10^{-3}\)) stays within 0.0032 of the full-row (\(\ell=\infty\)) recall ceiling across all 20 filtered cells in our benchmark; alternatively, using the empirical active fraction \(\tilde{\sigma}(c_q)\) observed during seeding, the rule \(\ell(\hat{\sigma})=min\{B,\lceil\ell_0+B_v\hat{\sigma}\rceil\}\) (\(\ell_0\in[32,64]\)) sets \(\ell\) automatically. To seed the beam, a \(0.5^\circ\times 0.5^\circ\) grid directory \[14, 34\] scans Chebyshev rings around g<sub>q</sub> to collect \(\tau=16\) active seeds in \(1.2\mu\)s using \<0.4% of graph memory (Appendix B.2; graph-descent seeding is compared in Exp-5). For dynamic updates, inserting u<sub>new</sub> updates its grid cell and 3D tree in O(logM) time, builds row(u<sub>new</sub>) through one beam search and a local coordinate stream, and inserts u<sub>new</sub> into reverse neighbors’ sorted rows; deletions set a tombstone bit skipped in Phase 1.

## 5 Experiments

### 5.1 Experimental Setup

**Datasets, Workloads, and Baselines.**  1 lists the four datasets: Overture-1M (US POIs from Overture Maps 2026-06- 17.0, max fiber 41), Yfcc-Clip (Web photos with 64.6% repeated coordinates, max fiber 5,726), and SIFT-Geo-1M and SpaceV- Geo-10M (paired with uniform US coordinates independent of the vectors). We test six selectivities \(\tilde{\sigma}\in\{10^{-5},10^{-4},10^{-3},10^{-2},10^{-1},1\}\): \(\tilde{\sigma}\in[10^{-5},10^{-3}]\) (10-10<sup>4</sup> objects) represents street- or walking-scale radii, \(\tilde{\sigma}\in[10^{-2},10^{-1}]\) (10<sup>4</sup>-10<sup>6</sup> objects) city- or metropolitan-scale radii, and \(\tilde{\sigma}=1\) unfiltered search, setting r<sub>q</sub> to the \(m_\text{tar}=\lceil\tilde{\sigma}n\rceil\)-th spatial-neighbor distance from g<sub>q</sub>. We report Recall@10 and single-threaded QPS over 1,000 queries per cell against five baselines: (1) _Spatial-First_ (exact spatial filter followed by vector scan); (2) _Vector-First_ (global HNSW \[25\] with post-filtering); (3) _Geo-Partition_ (grid of cell-local HNSW indexes, tuning widths \(\{1^\circ,0.5^\circ,0.25^\circ\}\) per dataset); (4) _CubeGraph_ \[44\] (hierarchical spatial-tree graph, tuning profiles P<sub>0</sub>,P<sub>1</sub>,P<sub>2</sub> per dataset); and (5) _ACORN_ \[28\] (\(M=32,\gamma=12,M_\beta=32\); _Spatial-First_ and _Geo-Partition_ also instantiate the primitives of Mesh \[37\]). Across all datasets, REACH uses one fixed profile: \(B=384,B_v=128,B_g=256,K_\text{vec}=192,\alpha=1.2,C_\text{tie}=4096,\tau=16\), sweeping \(\ell\in[8,\infty]\) and \(L\in[16,1024]\) (4096 at 10<sup>-2</sup> and 2048 at 10<sup>-1</sup> on 10<sup>7</sup>; Appendix B.3) on a 64-core AMD 3990X (220 GiB RAM, GCC 11.2 -03 -march=native; https://anonymous.4open.science/r/GeoSearch-new-1730/).

### 5.2 Experimental Results

**Exp-1: End-to-End Query Throughput (Figure 5).** Across the 16 selective cells (\(\tilde{\sigma}\in\{10^{-5},10^{-4},10^{-3},10^{-2}\}\)), one REACH index per dataset ranks fastest in 14 of 16 cells at 0.95 Recall@10, achieving \(2.49\times\) higher geometric-mean QPS than the best baseline in each cell (\(6.33\times\) over CubeGraph, \(3.56\times\) over Geo-Partition across selective cells where both reach 0.95 recall). _(1) Performance on selective disks_: At \(\tilde{\sigma}=10^{-5}\) (0.95 recall), REACH reaches 60,760 QPS (Overture-1M), 44,255 QPS (Sift-Geo-1M), 41,191 QPS (Yfcc- Clip), and 8,901 QPS (SpaceV-Geo-10M), beating the best baseline per panel (Geo-Partition at 23,627, 18,029, 11,552 QPS on 10<sup>6</sup>, and CubeGraph at 1,842 vs. 988 QPS on 10<sup>7</sup>) by \(2.57\times\), \(2.45\times\), \(3.57\times\), \(4.83\times\) (\(\)30.5\(\times\), \(95.2\times\) over CubeGraph on Overture-1M, Yfcc-Clip). At \(\tilde{\sigma}=10^{-4},10^{-3}\), REACH reaches 21,495, 6,336 QPS on Overture-1M (\(2.94\times\), \(4.04\times\) over Geo-Partition; \(26.0\times\), \(14.0\times\) over CubeGraph) and 21,046, 8,707 QPS on Yfcc-Clip (\(3.77\times\), \(4.92\times\) over Geo-Partition; \(39.9\times\), \(11.5\times\) over CubeGraph). _(2) Baseline limitations: Vector-First_ is fast at \(\tilde{\sigma}=1\) (1,411-3,020 QPS) but misses 0.95 recall in all 12 cells with \(\tilde{\sigma}\le 10^{-3}\) due to path erosion; _Spatial-First_ reaches 384-396 QPS at 10<sup>-5</sup> (\(105\times\)-\(154\times\) slower) and \(2.1-19.5 QPS at<tbc>

\begin{tabular}{ccccc}
**Dataset** & & _n_ & _D_ & **Embeddings (f32, L2)** & **Coordinates** \\
Overture-1M & & 10<sup>6</sup> & 384 & POI MiniLM-L6-v2 & real; 98.9% distinct \\
Yfcc-Clip & \(9.98\times\) & \(10^5\) & 512 & CLIP ViT-B/32 \[33, 38\] & real; 35.4% distinct \\
Sift-Geo-1M & & 10<sup>6</sup> & 128 & official SIFT1M \[18\] & synth.; 100% distinct \\
SpaceV-Geo-10M & & 10<sup>7</sup> & 100 & official SpaceV \[36\] & synth.; 100% distinct \\
\end{tabular}

**Algorithm 1:** AssembleRow(_u_): Dual-source row construction

** 1: Benchmark datasets (**1,000 **base-disjoint queries per cell).**

