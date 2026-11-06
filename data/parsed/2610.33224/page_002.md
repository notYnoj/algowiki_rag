<tbc>noise), provided _M_=O(_k_log(_N/k_)).

Compressive Sensing has since enjoyed a long series of successes in Signal Processing \[12, 5, 34\], though has become more of a background player in modern systems design, and it is rare to see application outside of practical acquisition systems like single-pixel optical imaging \[26\], Astronomy \[7\], WiFi or wireless sensor networks \[4\], to name a few.

In classical Compressive Sensing, a signal \(x\in\mathbb{R}^N\) (e.g., an image in JPEG \[44\]) admits a _k_-sparse representation \(s\in\mathbb{R}^N\) under a sparsifying basis or dictionary \(F\in\mathbb{R}^{N\times N}\) such that _x=Fs_. Instead of acquiring all _N_ ambient samples and compressing them post hoc, compressive sensing directly acquires \(M\checkmark N\) non-adaptive linear measurements via a pseudorandom measurement matrix \(A\in\mathbb{R}^{M\times N}\):

\(y=Ax=AFs\) (1)

The sparse coefficient vector _s_ is then reconstructed from _y_ by applying convex \(\ell_1\)-regularized recovery algorithms \[42, 6, 43, 21, 15\], after which the original signal _x=Fs_ can be synthesized if needed.

In our nearest-neighbor setting (Section 1.3), the paradigm is even more direct: the sparse vector \(s\in\mathbb{R}^N\) is _itself_ the primary object of interest. Specifically, _s_ is the database affinity vector whose coordinates indicate the nearest neighbors of a query. Consequently, recovering _s_ directly from compressed measurements _y=As_ immediately reveals the nearest-neighbor candidates (and their approximate distances) without requiring secondary reconstruction of an underlying signal _x_. Because _A_ is pseudorandom and the database features are known _a priori_, the server’s linear operator can be precomputed offline, leaving only the compact vector \(y\in\mathbb{R}^M\) to be transmitted to the client.

## 1.3 Nearest Neighbor Search as Sparse Signal Recovery

Consider a database \(T=\{t_1,t_2,\dots,t_N\}\subset\mathbb{R}^D\) of _N_ vectors and a query point \(q\in\mathbb{R}^D\). For a nearest-neighbor query we are interested in the domain of distances from the query point to the points in the database, most specifically with the closest point. While the pairwise distance vector \(d\in\mathbb{R}^N\) with entries _d<sub>i</sub>_=dist(_q,t<sub>i</sub>_) is completely dense, the corresponding _k_-nearest neighbor indicator vector \(s\in\{0,1\}^N\) is, by construction, exactly _k_-sparse. In particular, for 1-NN retrieval, _s_ is a 1-hot vector containing a single non-zero entry among _N_ coordinates.

From this perspective, nearest neighbor search can be cast as the recovery of a sparse affinity signal from compressed linear projections. In our formulation, the target signal \(s\in\mathbb{R}^N\) is not merely an uninformative binary 0/1 indicator, but a continuous _local affinity vector_ whose entries _s<sub>i</sub>_=sim(_q,t<sub>i</sub>_) concentrate their mass within the query’s local Voronoi neighborhood. This continuous mass is a key feature: its relative amplitudes preserve metric resolution and local ranking among adjacent points within<tbc>

<tbc>the cell (as visualized in Figure 2), while decaying rapidly to zero across distant background points to enforce effective sparsity.

The server compresses this affinity field into \(M\checkmark N\) linear measurements \(y=As\in\mathbb{R}^M\) via a pseudorandom measurement matrix \(A\in\mathbb{R}^{M\times N}\). The core challenge is designing feature embeddings F and G that guarantee that distances are meaningful, but that decay quickly enough such that _s_ is sufficiently sparse for stable Compressive Sensing recovery, allowing the server to compute _y=As_ without ever computing the full _N_-dimensional vector _s_.

While the raw query \(q\in\mathbb{R}^D\) is generally dense, and can be performed via linear operations simply (e.g., _d=u<sup>T</sup>u+v<sup>T</sup>v_-2(_u<sup>T</sup>v_) for vectors _u_ and _v_), modern machine learning provides effective non-linear feature embeddings that induce sparsity in an expanded feature space R_<sup>B</sup>_ (\(B\gg D\)). Specifically, Kernel Methods (e.g., Random Fourier Features \[36\]) and Locality Sensitive Hashing (e.g., FlyHash \[20\]) allow sparsified continuous metric distances to be approximated via linear inner products:

\(\mathrm{sim}(q,t_i)\approx\langle\mathcal{G}(t_i),\mathcal{F}(q)\rangle\)

Where G and F are sparsity-enhancing feature transforms. By stacking the _N_ transformed database vectors into a database feature matrix \(G=\mathcal{G}(T)\in\mathbb{R}^{N\times B}\), where row _i_ is G(_t<sub>i</sub>)<sup>T</sup>_, the uncompressed affinity vector \(s\in\mathbb{R}^N\) across the entire database is then simply the matrix-vector product:

\(s=GF(q)=\left[\begin{array}{ c }
\langle\mathcal{G}(t_1),\mathcal{F}(q)\rangle \\
\vdots \\
\langle\mathcal{G}(t_N),\mathcal{F}(q)\rangle
\end{array}\right]\in\mathbb{R}^N\) (2)

By pre-multiplying this database feature matrix by a pseudorandom measurement matrix \(A\in\mathbb{R}^{M\times N}\), we construct the **Holographic Sensing Matrix**:

\(H:=AG\in\mathbb{R}^{M\times B}\) (3)

It’s useful to pause and note the connection to Holography and physical intuition behind it. Specifically for an isolated vector pair \(\langle\mathcal{G}(t_i),\mathcal{F}(q)\rangle\), _a priori_, the computation shares no information with any neighbors and<tbc>

