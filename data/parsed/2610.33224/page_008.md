All benchmarks are evaluated on an NVIDIA GeForce RTX 3090 GPU (24 GB VRAM) and an Intel Xeon W- 2135 host (6 cores / 12 threads) across four representative operating points (75.0%,85.0%,95.0%,99.9% nominal recall tiers). At each tier, (_M,K_<sup>∗</sup>) represents the empirically profiled Pareto-optimal measurement budget and candidate cutoff along the dataset’s bandwidth-recall frontier. To prevent client-side FISTA from materializing a monolithic \(M\times N\) sensing matrix (which would require 1.52 TB of float32 memory at _N_=10<sup>6</sup>_,M_=380,100), million- vector corpora are partitioned into _P_=100 disjoint blocks of _N_<sub>block</sub>=10,000 vectors (_M_<sub>block</sub>=_M/P_). Each block’s sensing matrix \(A_b\in\mathbb{R}^{M_\mathrm{block}\times N_\mathrm{block}}\) is drawn from the normalized Bernoulli ensemble \(\pm 1/\sqrt{M_\mathrm{block}}\) and generated on the fly from a shared 128-bit PRNG seed (\(\le\) 152 MB in GPU VRAM, fitting even on lightweight 4 GB client GPUs), enabling batched GPU FISTA across all _P_ blocks in _\<_ 0.4 s per query.

### 5.2 Multi-Scale Target Recall Benchmark Results

1 illustrates how achieved recall tracks the sparsity induced by the feature transform across each data manifold. On spatially structured Euclidean manifolds (**SIFT-1M** and **MNIST-784**), Random Fourier Features concentrate affinity within a tight local radius, reaching 94.10%-100.00% on SIFT-1M and 75.42%-97.79% on MNIST-784 at 10.0%-26.7% sub-Nyquist compression (noting that pushing unclustered SIFT-1M to 100.0% crosses the Nyquist boundary _M/N\>_100%, whereas practical encrypted deployments operate at \(M/N\le 50\%\) where 1-recall@10 already reaches 98.5%, as swept in  4). On the angular semantic hypersphere (**GloVe-25**), Asymmetric FlyHash resolves crowding to achieve 82.60%- 97.50% at _M/N_=8.03%-25.35%. By contrast, **Last.fm- 64** (F=G=id, no feature lifting) provides no non-linear sparsification mechanism, causing background cross-talk to degrade recovery (57.60%-93.30%) and marking the boundary of the method’s applicability.

## 6 Encrypted Retrieval System Implementation & SOTA Comparison

Holo-NN is designed for blind cloud retrieval across four complementary Ring-LWE encrypted execution backends: (1) exact-integer BFV homomorphic matrix-vector evaluation via Google’s **HintlessPIR / LinPIR** engine \[31\], (2) depth-1 modulus-switched approximate homomorphic encryption on CPU via **OpenFHE** \[1\] under the Cheon- Kim-Kim-Song (CKKS) scheme \[16\] compiled through **HEIR** \[3\], (3) 64-bit RNS GPU-accelerated CKKS evaluation on a single NVIDIA GeForce RTX 3090 GPU (24 GB VRAM) via **Phantom** \[45\] with a fused 128-bit lazy-<tbc>

<tbc>reduction BSGS inner-product kernel, and (4) 32-bit RNS double-hoisted GPU CKKS evaluation on a single RTX 3090 GPU (and NVIDIA H100) lowered via **HEIR** \[3\] to **Cheddar** \[17\].

The encrypted retrieval pipeline executes via a strictly linear four-step protocol:

1. **Offline Precomputation (Server)**: The server computes the holographic index \(H=AG=\mathcal{AG}(T)\in\mathbb{R}^{M\times B}\) once across all database embeddings and pre- encodes its diagonals in NTT evaluation form.<tbc>

2. **Query Encryption (Client)**: The client lifts query \(q\rightarrow\mathcal{F}(q)\) and encrypts Enc(F(_q_)) into SIMD ciphertext slots.<tbc>

3. **Blind Linear Evaluation (Server)**: The server evaluates \(\mathrm{Enc}(y)=H\cdot\mathrm{Enc}(\mathcal{F}(q))\) via diagonal NTT plaintext-ciphertext multiplication with zero bootstrapping--using single-generator cyclic query rotations and rotation-free row accumulation under LinPIR, or Baby-Step Giant-Step (BSGS) evaluation followed by single-limb modulus switching (`Compress`) under CKKS.<tbc>

4. **Client Recovery & Optional PIR Reranking**: The client decrypts _y_=Dec(Enc(_y_)) locally, reconstructs sparse coefficients \(\hat{s}=\text{FISTA}(y,A,\lambda,L)\) and extracts the top _K_<sup>∗</sup> candidate IDs (issuing an optional secondary Batch PIR re-query for those _K_<sup>∗</sup> records when exact-distance reranking or document payloads are needed; Section 3.4).

### 6.1 Degree-1 Blind Linear Arithmetic & Compiler Optimizations

Prior FHE-based vector search systems evaluate non-linear Euclidean distances or polynomial approximations of cosine similarity under homomorphic encryption. Evaluating polynomial approximations of degree \(d\ge 12\) requires deep homomorphic circuits, inducing large noise growth that necessitates expensive **FHE bootstrapping** operations (often requiring 10-60 seconds per ciphertext).

In Holo-NN, the server’s blind evaluation is strictly linear:

\(\mathrm{Enc}(y)=H\cdot\mathrm{Enc}(\mathcal{F}(q))\) (24)

Because _H_ is plaintext and Enc(F(_q_)) is a degree-1 ciphertext, the server executes only homomorphic plaintext- ciphertext multiplications, additions, and slot rotations:

• **Multiplicative Depth**: Exactly **1** (Degree-1 linear operator).<tbc>

• **FHE Bootstrapping**: **0 bootstrapping operations** required throughout the entire query lifecycle.<tbc>

• **Compiler Optimization via HEIR**: Lowering the matrix-vector multiplication through the MLIR-based<tbc>

