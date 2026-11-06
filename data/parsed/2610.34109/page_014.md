<tbc>_from u to v of total hop length at most_

\(O\left(\frac{D}{\rho_c}\right)+1+\left\lceil log_\alpha\left(\frac{D_x}{\varepsilon_\alpha}\right)\right\rceil.\)

Proof. Because every cell of diameter at most \(\rho_c/3\) in the tiling of \(\Omega_c\) contains at least one active site and every active vertex retains a representative of every active coordinate within distance \(\rho_c\) (Theorem 3.7(b)), walking along the cells covering a geodesic from _s<sub>u</sub>_ to _s<sub>v</sub>_ in \(\Omega_c\) produces a chain of \(O(D/\rho_c)\) inter-coordinate hops from _u_ to an active vertex \(u'\in\mathcal{A}(c)\) with \(\Delta(s_{u^\prime},s_v)\le\rho_c\). Because \(\Delta(s_{u^\prime},s_v)\le\rho_c\), the local witness argument in the proof of Corollary 3.8 supplies one hop from \(u'\) to a witness \(w\in F(s_v)\) followed by at most \(\lceil log_\alpha(D_x/\varepsilon_\alpha)\rceil\) contracting hops inside _F(s<sub>v</sub>_) to reach _v_. \(\sqcap\sqcup\)

## B Additional System and Experimental Details

### B.1 Summary of Notation and System Overview

2 summarizes the notation used throughout the paper, and Figure 9 illustrates the six-module offline and online workflow of REACH. Offline construction produces two persistent data structures: the 4_nB_-byte table of vector-sorted rows and the _O(n_) spatial grid seed directory. Online, the query disk _c<sub>q</sub>_ defines the activity predicate evaluated during sequential row scanning, while the grid directory supplies \(\tau\) initial active seeds inside A(_c<sub>q</sub>_).

### B.2 Grid Directory and Entry Seeding

Algorithm 3 presents the spatial entry seeding procedure. The grid directory partitions latitude \([-90^\circ,90^\circ]\) and longitude \((-180^\circ,180^\circ]\) into cells of resolution \(w_\phi=w_\lambda=0.5^\circ\) (\(360\times 720=259,200\) cells)<tbc>

<tbc>and stores vertex identifiers in a contiguous array indexed by a prefix-sum offset table \[14, 34\]. Construction requires two linear counting passes (_\<_0.6 s at _n_=10<sup>7</sup>). At query time, Algorithm 3 expands Chebyshev rings \(\rho=0,1,\dots\) around the cell containing _g<sub>q</sub>_, where \(\text{mindist}(\kappa,g_q)\) is the exact minimum great-circle distance from _g<sub>q</sub>_ to cell \(\kappa\), halting once \(\tau=16\) active seeds are collected or \(min_{\kappa\in\mathcal{K}_\rho}\text{mindist}(\kappa,g_q)>r_q\). The zero-auxiliary-storage seeding alternative evaluated in Exp-5 replaces the grid directory with _N<sub>a</sub>_=256 anchor vertices selected via farthest-point sampling on the 3D unit sphere and descends the physical REACH graph using \(\Delta(\cdot,g_q)\) until \(\tau=16\) active vertices inside \(\Omega_{c_q}\) are reached.

### B.3 Spherical Numerics, Hyperparameters, and Work Scaling

Each coordinate \(s=(\lambda,\phi)\) is pre-converted into its 3D unit vector \(\mathbf{u}_s=(cos\phi cos\lambda,cos\phi sin\lambda,sin\phi)\). At query time, the disk predicate \(\Delta(s_v,g_q)\le r_q\) in Algorithm 2 is evaluated through<tbc>

\begin{tabular}{cc}
**Symbol** & **Description** \\
\multicolumn{2}{c}{_Data and query model_ (Section 2)} \\
D_,V,n_ & object collection, vertex set {1_,...,n_}, and cardinality \\
X,S & _D_-dimensional vector space and spherical geographic domain \\
_x<sub>v</sub>,s<sub>v</sub>_ & feature vector and geographic position of object _v_ \\
\(d(\cdot,\cdot),\Delta(\cdot,\cdot)\) & Euclidean vector distance and spherical great-circle distance \\
\(c=(g,r),\Omega_c\) & disk condition (center _g_, radius _r_) and its spherical region \\
A(_c),m_, \(\sigma(c)\) & active object set, active size |A(_c_)|, and selectivity _m/n_ \\
_q_=(_x<sub>q</sub>,c<sub>q</sub>,k),T<sub>k</sub>(q_) & GFANN query and its exact top-_k_ active ground-truth set \\
\multicolumn{2}{c}{_Recovery graph and two-scale theory_ (Section 3)} \\
_G_=(_V,E),_row(_u_) & directed physical graph and vector-sorted neighbor row of _u_ \\
_C<sub>u</sub>(c_) & active entries in row(_u_) under disk _c_, i.e., \(row(u)\cap\mathcal{A}(c)\) \\
\(\mathcal{H}_\infty(c)\) & complete active projection _G_\[A(_c_)\] of the stored rows \\
\(\mathcal{H}_\ell(c),\ell\) & recovery graph (first \(\ell\) active row entries) and recovery budget \\
\(\ell_\mathrm{SC}(c)\) & exact cut-rank budget threshold for strong connectivity \\
_F(z),M,_\(\delta\) & coordinate fiber {_v:s<sub>v</sub>=z_}, distinct site count, failure budget \\
_K<sub>f</sub>,d<sub>X</sub>_ & per-fiber candidate cap (min{_B<sub>g</sub>,C_<sub>tie</sub>}) and intrinsic dimension \\
\(\chi_u(z),L_u(\rho)\) & new geographic edges from _F(z_) and cumulative quota used within \(\rho\) \\
\(\varepsilon_\alpha,a_\alpha,h_c,\rho_c\) & vector separation scale, per-fiber quota cap, crowding bound, and linking radius \\
\multicolumn{2}{c}{_REACH index construction and search_ (Section 4)} \\
_B,B<sub>v</sub>,B<sub>g</sub>_ & fixed row width (_B=B<sub>v</sub>+B<sub>g</sub>_), vector quota, and geographic quota \\
_K_<sub>vec</sub>, \(\alpha\), _C_<sub>tie</sub> & vector pool size, diversity parameter (\(\alpha>1\)), and fiber scan cap \\
_L,_ \(\tau\) & beam search list size (_ef_<sub>search</sub>) and spatial entry seed count \\
\end{tabular}

\begin{tabular}{cc}
\multicolumn{2}{c}{**Algorithm 3:** Seed(_c<sub>q</sub>_): Active entry seed lookup from the grid directory} \\
\multicolumn{2}{c}{**Input:** disk condition _c<sub>q</sub>_=(_g<sub>q</sub>,r<sub>q</sub>_); grid directory K; target seed count \(\tau\)} \\
\multicolumn{2}{c}{**Output:** active seed set \(I(q)\subseteq\mathcal{A}(c_q)\) with \(|I(q)|\le\tau\)} \\
\multicolumn{2}{c}{\(I\leftarrow\emptyset\); \(\rho\leftarrow 0\)} \\
\multicolumn{2}{c}{**while** \(|I|<\tau\) **do**} \\
\multicolumn{2}{c}{\(\mathcal{K}_\rho\leftarrow\) grid cells at Chebyshev ring distance \(\rho\) from the cell of _g<sub>q</sub>_} \\
\multicolumn{2}{c}{**if** \(\mathcal{K}_\rho=\emptyset\) **_or_** \(min_{\kappa\in\mathcal{K}_\rho}\text{mindist}(\kappa,g_q)>r_q\) **then break**} \\
\multicolumn{2}{c}{**foreach** \(\kappa\in\mathcal{K}_\rho\) **_with_** \(\text{mindist}(\kappa,g_q)\le r_q\) **do**} \\
\multicolumn{2}{c}{**foreach** \(v\in\mathcal{K}[\kappa]\) **do**} \\
\multicolumn{2}{c}{**if** \(\Delta(s_v,g_q)\le r_q\) **then** \(I\leftarrow I\cup\{v\}\)} \\
\multicolumn{2}{c}{**if** \(|I|=\tau\) **then break**} \\
\multicolumn{2}{c}{**if** \(|I|=\tau\) **then break**} \\
\multicolumn{2}{c}{\(\rho\leftarrow\rho+1\)} \\
\multicolumn{2}{c}{**return** _I_} \\
\end{tabular}

\begin{tabular}{ccc}
**Parameter** & **Value** & **Role in construction / search** \\
_K_<sub>vec</sub> & 192 & NN-Descent vector candidate pool size \\
_B<sub>v</sub>_ & 128 & global-vector source quota \\
_B<sub>g</sub>_ & 256 & nearest-first geographic stream quota \\
\(\alpha\) & 1.2 & intra-source and intra-fiber diversity parameter \\
_C_<sub>tie</sub> & 4096 & per-fiber scan cap (_K<sub>f</sub>_=min{_B<sub>g</sub>,C_<sub>tie</sub>}) \\
_B_ & 384 & fixed row width (_B=B<sub>v</sub>+B<sub>g</sub>_) \\
\(\tau\) & 16 & active entry seeds fetched per query \\
\end{tabular}

\begin{tabular}{cccccc}
\(\ell\) & Recall@10 & Vector calcs / query & Row scans / query & QPS \\
8 & 0.3730 & 113 & 657 & 16,864 \\
16 & 0.5896 & 207 & 1,380 & 9,667 \\
32 & 0.7788 & 405 & 2,264 & 5,441 \\
64 & 0.8576 & 845 & 3,047 & 3,243 \\
96 & 0.8691 & 1,330 & 3,649 & 2,257 \\
128 & 0.8695 & 1,813 & 4,229 & 1,734 \\
160 & 0.8707 & 2,294 & 4,823 & 1,405 \\
192 & 0.8725 & 2,775 & 5,433 & 1,179 \\
\(\infty\) & 0.8738 & 4,157 & 7,249 & 797 \\
\end{tabular}

** 2: Summary of frequently used notation.**

** 3: REACH construction hyperparameters, held fixed across all datasets and selectivities.**

** 4: Impact of recovery budget** \(\ell\) **on OVERTURE-1M at** \(\bar{\sigma}=10^{-1}\) **and fixed** _L_=16 **(**\(\ell=\infty\) **scans all** _B_=384 **entries).**

