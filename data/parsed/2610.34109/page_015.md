<tbc>a 32-bit latitude-longitude bounding box (inflated outward by 1 ULP via nextafter) followed by one 3D dot product \(\langle\mathbf{u}_{s_o},\mathbf{u}_{g_q}\rangle\ge cos(r_q/R_\oplus)\).

**Dataset Preparation and Baseline Tuning Protocol.** On Overture-1M, text embeddings are computed with MiniLM-L6-v2 over concatenated name, category, and address fields from Overture Maps release 2026-06-17.0 and unit-normalized in float32; on Yfcc-Clip, 512-dimensional OpenCLIP ViT-B/32 features \[33\] are used directly without post-normalization. On Sift-Geo-1M and SpaceV-Geo-10M, synthetic coordinates are generated independently of the vectors with longitude uniform on \([-125^\circ,-66^\circ]\) and \(sin(\phi)\) uniform on \([sin24^\circ,sin50^\circ]\) (uniform surface area across the contiguous US), using NumPy PCG64 seeds 2026072203 (SIFT) and 2026072204 (SpaceV).  3 lists the fixed construction parameters of REACH. For CubeGraph \[44\], we evaluate three profiles (layers, _M_, _efC_, cross-degree) with minimum leaf size 50: _P_<sub>0</sub>=(6,16,200,2), _P_<sub>1</sub>=(6,32,400,4), and _P_<sub>2</sub>=(8,32,400,4), selecting _P_<sub>0</sub> on Overture-1M and _P_<sub>2</sub> on the other three datasets. For Geo-Partition, we sweep grid cell widths \(\{1^\circ,0.5^\circ,0.25^\circ\}\) with cell-local HNSW parameters _M_=32, _efC_=200, selecting \(0.25^\circ\) on Overture-1M and Sift-Geo-1M and \(0.5^\circ\) on Yfcc-Clip and SpaceV-Geo-10M. Vector-First uses HNSW with _M_=32, _efC_=200,<tbc>

<tbc>and ACORN \[28\] uses \(M=32,\gamma=12,M_\beta=32\). At query time, REACH sweeps \(\ell\in\{8,16,32,64,96,128,160,192,\infty\}\) and 12 beam sizes \(L\in[16,1024]\) (extended to 4096 at \(\bar{\sigma}=10^{-2}\) and 2048 at \(\bar{\sigma}=10^{-1}\) on SpaceV-Geo-10M); CubeGraph, Geo-Partition, and Vector-First sweep \(EF=64\cdot 2^i\) (\(0\le i\le 4\)) and over-fetch \(10\cdot 4^j\) (\(0\le j\le 5\)) with intermediate points near the Pareto knee, while ACORN sweeps _EF_.

**Detailed Recovery-Budget and Query-Work s (Exp-4).**  4 reports the full recovery-budget sweep on Overture-1M at \(\bar{\sigma}=10^{-1}\) and fixed _L_=16, and  5 reports the minimum mean vector distance calculations required to reach Recall@\(10\ge 0.99\) across all 24 workload cells (complementing Exp-4 in Section 5). In  4, raising \(\ell\) from 96 to \(\infty\) changes Recall@10 by only 0.0047 while tripling vector-distance evaluations and reducing QPS by \(2.8\times\); across all 24 cells, only the two unfiltered (\(\bar{\sigma}=1\)) cells on SpaceV-Geo-10M (0.105) and Overture-1M (0.016) exhibit a maximum-recall gap above 0.0032 between \(\ell=64\) and \(\ell=\infty\). In  5, on all three 10<sup>6</sup> datasets, as \(\bar{\sigma}\) grows from 10<sup>-5</sup> to 1, the evaluated fraction of A(_c<sub>q</sub>_) drops monotonically from ∼1.0 (with Yfcc-Clip’s 1.76 ratio at 10<sup>-5</sup> caused by boundary coordinate ties making _m<sub>q</sub>\>m_<sub>tar</sub>) to 0.004-0.02. On SpaceV-Geo-10M, consistent with the uniform-site transition analyzed in Exp-1(3), reaching 0.99 recall evaluates 75%-77% of the active set at \(\bar{\sigma}\in\{10^{-3},10^{-2}\}\) (up to _L_=4096), and at \(\bar{\sigma}=10^{-1}\) (_m_<sub>tar</sub>=10<sup>6</sup>) search reaches 0.9804 recall at \(\ell=64\), _L_=2048 (99,366 evaluations, or 0.10_m_<sub>tar</sub>; 0.9823 at \(\ell=\infty\)) and 0.9561 recall in 23,766 evaluations (0.024_m_<sub>tar</sub>), before global vector edges take over at \(\bar{\sigma}=1\) (38,734 evaluations, or 0.004_m_<sub>tar</sub>).

\begin{tabular}{cccccccc}
**Dataset** & 10<sup>-5</sup> & 10<sup>-4</sup> & 10<sup>-3</sup> & 10<sup>-2</sup> & 10<sup>-1</sup> & & 1 \\
Overture-1M & 10 (1.00) & 95 (.95) & 851 (.85) & 4746 (.47) & 11194 (.11) & 21329 (.02) & \\
Yfcc-Clip & 18 (1.76) & 73 (.73) & 484 (.48) & 1977 (.20) & 2673 (.03) & 3543 (.004) & \\
Sift-Geo-1M & 10 (1.00) & 51 (.51) & 321 (.32) & 2292 (.23) & 5470 (.05) & 3685 (.004) & \\
SpaceV-Geo-10M & 90 (.90) & 822 (.82) & 7731 (.77) & 74975 (.75) & - & 38734 (.004) & \\
\end{tabular}

OFFLINE
1 Dual-source build
2 Physical rows
3 Geographic directory
d(xu, )
u
+
w
y
u
a
b
C
d
e
f
merge
Cv(u)
fibers
fixed width B
coordinates
ID buckets
ONLINE
rows
seeds
4 Geographic predicate
5 First l active: l = 3
6 Beam search
Cq
b
A(cq)
a
a
C
a
b
C
d
e
f
C
a
C
1
2
3
stop
u
e
d
d
e
d
f
keep
A
C
d
d(xq, )
next vertex: repeat scan
active
inactive
visited: no rescore
vector source
geographic source
unread

**Figure 9: Six-module overview of REACH. Offline, dual-source assembly produces fixed-width vector-sorted rows, while geographic coordinates populate a separate cell directory. Online, the disk predicate and stored row feed first-**\(\ell\)**-active scanning; the directory supplies entry seeds directly to beam search. The shared** \(\ell=3\) **example counts visited** _a_**, skips inactive** _b_**, and stops at** _d_**, sending only** _A_=\[_c,d_\] **to vector scoring. The beam traverses** H<sub>3</sub>(_c<sub>q</sub>_)**, including edge** \(u\rightarrow a\)**, and repeats the scan at its next expanded vertex.**

** 5: Minimum mean vector distance calculations required to reach Recall**\(@10\ge 0.99\)**; values in parentheses show the ratio to** \(m_\mathrm{tar}=\lceil\bar{\sigma}n\rceil\) **("--" indicates** 0.99 **recall is not reached within the tested** \(L\le 2048\) **cap).**

