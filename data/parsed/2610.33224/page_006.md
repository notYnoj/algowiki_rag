<tbc>The server thus produces the exact Compressive Sensing measurement vector \(y\in\mathbb{R}^M\) of the latent sparse similarity signal \(s\in\mathbb{R}^N\), without ever materializing or inspecting the full _N_-dimensional vector _s_. Crucially, because the server operator _H_ is strictly linear, cryptographic deployment does not require deep Fully Homomorphic Encryption or bootstrapping; any Linearly Homomorphic Encryption (LHE) or Ring-LWE SIMD scheme suffices to evaluate \(y=H\cdot\text{Enc}(\mathcal{F}(q))\) directly over ciphertexts.

### 3.4 Client Enclave Sparse Recovery & Candidate Reranking

Upon receiving the _M_-dimensional measurement vector _y_, the client recovers the sparse similarity vector \(\hat{s}\in\mathbb{R}^N\) by solving the non-negative \(\ell_1\)-regularized inverse problem (LASSO \[42\]):

\(\hat{s}=argmin_{s\ge 0}\frac{1}{2}\left\|As-y\right\|_2^2+\lambda\left\|s\right\|_1\) (18)

The client solves this convex optimization problem locally (or within a secure enclave) using any popular sparse recovery algorithm, such as Orthogonal Matching Pursuit (OMP) \[43\], Iterative Shrinkage-Thresholding (ISTA) \[21\], or the GPU-accelerated **Fast Iterative Shrinkage-Thresholding Algorithm (FISTA)** \[6\] as we do in this work:

\(u^{(k)}=z^{(k)}-\frac{1}{L}A^T\left(Az^{(k)}-y\right)\) (19)

\(s^{(k+1)}=\mathcal{S}_{\lambda/L}\left(u^{(k)}\right)=max\left(0,u^{(k)}-\frac{\lambda}{L}\right)\) (20)

\(t_{k+1}=\frac{1+\sqrt{1+4t_k^2}}{2}\) (21)

\(z^{(k+1)}=s^{(k+1)}+\frac{t_k-1}{t_{k+1}}\left(s^{(k+1)}-s^{(k)}\right)\) (22)

with initial conditions _s_<sup>(0)</sup>=_z_<sup>(1)</sup>=0_,t_<sub>1</sub>=1, Bai-Yin spectral step size \(L=\left\|A^TA\right\|_2\approx(1+\sqrt{N_\text{block}/M_\text{block}})^2\) \[46\], and Donoho-Johnstone universal threshold \(\lambda=\frac{1}{M_\text{block}}\sqrt{2N_\text{block}lnN_\text{block}/D}\) \[23\].

Upon convergence, the client extracts the top _K_<sup>∗</sup> coordinates with the highest recovered affinity scores:

\(\text{Top-}K^*(\hat{s})\subset\{1,2,\dots,N\}\) (23)

When only candidate IDs are required (or when the client caches lightweight metadata locally), retrieval terminates here in a single round trip. When full record payloads or exact metric reranking over the _K_<sup>∗</sup> candidates is required, the client issues a secondary Private Information Retrieval (Batch PIR, e.g., via HintlessPIR \[31\]) re-query for those _K_<sup>∗</sup> indices and computes exact distances locally without revealing the candidate support to the server.

### 3.5 Offline Index Tuning & Data- Dependent Operating Curves

In practice, the dimensions _M_ (measurement count), _B_ (feature embedding width), and _K_<sup>∗</sup> (candidate verification budget) establish an operational tradeoff between accuracy, communication bandwidth, and computation. While Compressive Sensing theory establishes that _M_ scales logarithmically with ambient dimension for a fixed sparsity level \((M=\mathcal{O}(k_\text{eff}ln(\frac{N}{k_\text{eff}}))\) \[24, 25\]), the effective sparsity _k_eff of the affinity vector _s_=G(_T_)F(_q_)--and the magnitude of background cross-talk across non-neighbors-- is inherently _data- and manifold-dependent_, varying with intrinsic dimensionality, metric concentration, and kernel bandwidth.

Crucially, because the holographic grating _H=A_G(_T_) is constructed offline on the server, with the full database _T_ in hand, Holo-NN requires no brittle closed-form heuristics to guess _M_ or _K_<sup>∗</sup> in the blind. Much like tuning graph degree or probe budgets (e.g., `efSearch` \[35\], `nprobe` \[30, 28\]) in traditional plaintext ANN indices, the index operator has ample offline compute during index construction to profile recall across a validation query split and select the exact (_M,B,K_<sup>∗</sup>) operating point along the dataset’s empirical bandwidth-accuracy Pareto curve.

## 4 Asymmetric Neural Hashing & Geometric Duality

### 4.1 The Double-Quantization Pathology in Symmetric Sparse Coding

High-dimensional semantic vectors (such as word embeddings and neural sentence representations) reside on continuous manifolds where continuous kernel functions often suffer from high-density concentration. To create sparse anchor representations, neural hashing algorithms draw inspiration from biological olfactory circuits \[20\], projecting inputs from low-dimensional projection neurons into an expanded Kenyon cell layer (\(B\gg D\)) and applying winner-take-all (_k_-WTA) competitive inhibition.

In conventional symmetric sparse coding, both the database points and the query vector are pruned to an identical top-_k_ active anchor budget (\(k_\text{db}=k_q\checkmark B\)). However, symmetric hard sparsification induces a severe **double-quantization pathology**: if a salient anchor ranks just above the top-_k_ cutoff in a database vector but falls slightly below the cutoff in the query vector, their dot product vanishes completely. This sharp thresholding causes false-negative dropouts across high-dimensional semantic benchmarks.

To circumvent this limitation in compressed sensing environments, we apply an **Asymmetric FlyHash (AFH)**, breaking the symmetry between database encoding and query representation. In this approach, the functions applied to query F and database G are different, with the<tbc>

