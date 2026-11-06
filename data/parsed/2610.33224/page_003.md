<tbc>therefore the _s<sub>i</sub>_ would need to be exhaustively calculated for a full comparison. (This is the primary mechanism behind the proof that any sorting algorithm’s complexity floor is O(_N_log_N_)). In Holography, however, information in one basis is "smeared out" across a complementary basis (e.g., the Fourier Transform) ensuring that every sample contains fractional information about every point in the conjugate basis. Here _H_ plays this role, dispersing distances across multiple measurements that, collectively and in far fewer number than _N_, can infer the signal of interest.

The linear framing cleanly separates the problem into an offline precomputation and an online linear query evaluation:

\(y=H\mathcal{F}(q)=\left(AG\right)\mathcal{F}(q)=A\left(G\mathcal{F}(q)\right)=As\in\mathbb{R}^M\) (4)

Here, _H_ is computed once offline and stored permanently. Given a query F(_q_), the evaluator simply computes the linear product _y=H_F(_q_), producing the compressed measurements \(y\in\mathbb{R}^M\) without ever materializing the uncompressed _N_-dimensional vector _s_. The querier, knowing only the pseudorandom matrix _A_, can then recover the sparse affinity vector \(\hat{s}\) directly from _y=As_ via standard convex recovery algorithms (discussed below) in a fully local environment, without ever needing to know or download the holographic database matrix _H_.

Moreover, because of the lossy nature of the initial transform, we can, with judicious design of the matrix _A_, precisely control the accuracy of the final output and more importantly, allow for an algorithmically tunable tradeoff between accuracy and cost.

By synthesizing Compressive Sensing with non-linear feature embeddings, this forms the basis of **Holo-NN**, a strictly linear approximate nearest neighbor retrieval framework designed for regimes where server storage and parallel compute are inexpensive relative to network bandwidth and client storage, and both query privacy and index protection are paramount.

## 1.4 Summary of Contributions

1. **Holographic Retrieval tion**: We reformulate ANN search as a single-round-trip (1-RTT), non-interactive linear Compressive Sensing problem (_y=H_F(_q_)) utilizing an offline precomputed holographic matrix \(H=AG(T)\in\mathbb{R}^{M\times B}\).<tbc>

2. **Asymmetric Neural Hashing & Geometric Duality**: We characterize the manifold duality governing sparse feature lifting--showing why continuous Random Fourier Features sparsify spatial Euclidean manifolds while discrete hyperplane competition is required on high-dimensional semantic hyperspheres-- and introduce Asymmetric FlyHash (_k<sub>q</sub>\>k_db) to eliminate double-quantization dropouts at zero encrypted wire overhead (Section 4 and Section 5).<tbc>

3. **Multi-Backend Encrypted Implementation & SOTA Comparison**: We implement Holo-NN across four complementary cryptographic backends-- stateless exact-integer **LinPIR (BFV)** \[31\] on CPU (3.29 s across 4 cores or 4.39 s single-threaded on Wikipedia-500k, and 3.1-8.0 s of server compute across 6 cores on SIFT-1M, with zero server keys), depth-1 mod-switched **OpenFHE CKKS** \[1\] on CPU (1.60 MB wire), **Phantom CUDA CKKS** \[45\] on a single NVIDIA RTX 3090 GPU (1.68 s end-to- end / 1.54 s server on Wikipedia-500k, and 9.5-29.7 s on SIFT-1M), and 32-bit RNS **HEIR/Cheddar CUDA CKKS** \[3, 17\] on a single RTX 3090 GPU (0.79 MB wire in 0.134 s end-to-end / 50.5 ms server on Wikipedia-500k, and 2.10-5.37 MB wire in 0.26-0.82 s on SIFT-1M)--and benchmark against SANNS \[14\], PRECO \[40\], Tiptoe \[29\], Pacmann \[48\], Panther \[32\], Compass \[49\], and Onyx \[37\] across all published recall conventions (2.10-11.13 MB CKKS wire on SIFT-1M in 1 RTT, 8.3\(\times\)-44.2\(\times\) below Panther’s 92.9 MB, 159\(\times\)-843\(\times\) below SANNS’s 1.77 GB, and below Compass’s 12.2 MB over 8 RTTs).<tbc>

Holo-NN 2D Voronoi Boundary Reconstruction across A Priori Regimes
N =50 Database Points
32,400 Evaluation Grid Queries
True Voronoi Analytical Boundaries Overlaid (Solid Thin White)
75.0% Target Regime (R = 75.0%)
85.0% Target Regime (R = 85.0%)
Keff = 2, M = 13(26% DB), B = 8k Boundary Acc: 66.1%
Keff = 3, M = 17(54% DB), B = 16k Boundary Acc: 75.8%
1.00
1.00
0.75
0.75
0.50
0.50
0.25
0.25
0.00
0.00
Spatial Y
Spatial Y
-0.25
-0.25
-0.50
-0.50
-0.75
-0.75
-0.75
-1.00
-1.00
-1.00
-0.75
-0.50
-0.25
0.00
0.25
0.50
0.75
1.00
-1.00
-0.75
-0.50
-0.25
0.00
0.25
0.50
0.75
1.00
Spatial X
Spatial X
95.0% Target Regime (R = 95.0%)
99.9% Target Regime (R = 99.9%)
Keff = 5, M = 24(48% DB), B = 32k Boundary Acc: 85.1%
Keff = 10, M = 33(66% DB), B = 65k Boundary Acc: 90.9%
1.00
1.00
0.75
0.75
0.50
0.50
0.25
0.25
0.00
0.00
Spatial Y
Spatial Y
-0.25
-0.25
-0.50
-0.50
-0.75
-0.75
-0.75
-1.00
-1.00
-0.75
-0.50
-0.25
0.00
0.25
0.50
0.75
1.00
-1.00
-0.75
-0.50
-0.25
0.00
0.25
0.50
0.75
1.00
Spatial X
Spatial X

Figure 2: Holo-NN 2D Voronoi spatial boundary reconstruction across increasing measurement budgets (75.0%,85.0%,95.0%,99.9% recall regimes).

