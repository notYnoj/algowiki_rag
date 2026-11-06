HEIR compiler \[3\] automatically synthesizes diagonal ciphertext rotations and hoists plaintext weights, yielding optimal SIMD slot packing across OpenFHE backends.<tbc>

• **Noise Growth**: Minimal invariant noise budget, permitting compact RLWE parameter sets at OpenFHE’s `HEStd\_128\_classic` security standard \[2\] (_N_ring=16,384 for 8,192-slot blocks and _N_ring=32,768 for 16,384-slot blocks).<tbc>

## 6.2 End-to-End Encrypted Deployment (Wikipedia 500k)

Upon receiving Enc(_y_), the client decrypts the _M_- dimensional measurement vector \(y\in\mathbb{R}^M\) within its secure local enclave and launches parallel GPU-accelerated FISTA to recover \(\hat{s}\in\mathbb{R}^N\).

For the following algorithm discussion, we deployed the full encrypted pipeline on a 500,000-vector Wikipedia semantic demonstration search index (_N_=500,000, _D_=768 MPNet embeddings reduced to 128 dimensions by PCA) to validate the protocol at scale ( 2). This deployment is a systems demonstration, not an accuracy benchmark: retrieval quality is evaluated on the standard suites of  1 and  3, which have published ground truth.

Because _y=H_F(_q_) is a pure matrix-vector product, Holo-NN provides four complementary encrypted execution surfaces with contrasting latency, hardware, state, and bandwidth profiles:

• **Holo-NN: LinPIR (Exact-Integer BFV RLWE, CPU)**: Built on Google’s HintlessPIR/LinPIR engine \[31\] with two 56-bit CRT plaintext moduli and a single cyclic-subgroup generator, a _B_=8,192 column strip incurs a fixed 1.24 s query baby-step Galois rotation cost (across both CRT primes) with 0.0545 s of marginal row-accumulation work per 1,024 rows on a single core. Sharding the 32,768 rows across 4 cores of the Xeon W-2135 (4 parallel \(8,192\times 8\),192 shards) completes the Wikipedia-500k query in **3.29** s end to end (**1.78** s server compute; or **4.39** s end to end / **2.88** s server compute on a single CPU thread) -- 10.0\(\times\) faster end-to-end (17.9\(\times\) faster in server compute) than the 12-thread CPU CKKS path -- while requiring **zero persistent server-side rotation keys**, because its 1.45 MB Galois evaluation key per prime (3.10 MB total upload including query cipher<tbc>

\begin{tabular}{ccccccccccc}
**Dataset** & **Metric Space \& Transform** & _N_ & _D_ & _B_ & **Regime** & _M_ & _M/N_ & _K_<sup>∗</sup> & **Rec@1** & **Rec@_K_<sup>∗</sup> & **Rec@50** \\
\multirow{3}{*}{**SIFT-1M**} & \multirow{3}{*}{Euclidean RFF} & \multirow{3}{*}{1,000,000} & \multirow{3}{*}{128} & \multirow{3}{*}{16,384} & **75.0%** & 380,100 & 38.01% & **8** & 62.00% & **94.10%** & 99.20% \\
 & & & & & **85.0%** & 445,200 & 44.52% & **11** & 67.60% & **98.00%** & 99.80% \\
 & & & & & **95.0%** & 631,200 & 63.12% & **19** & 72.30% & **99.70%** & 100.00% \\
 & & & & & **99.9%** & 1,294,900 & 129.49% & **50** & 82.10% & **100.00%** & 100.00% \\
\multirow{3}{*}{**MNIST-784**} & \multirow{3}{*}{Pixel Manifold RFF} & \multirow{3}{*}{60,000} & \multirow{3}{*}{784} & \multirow{3}{*}{8,192} & **75.0%** & 6,000 & 10.00% & **30** & 23.37% & **75.42%** & 79.95% \\
 & & & & & **85.0%** & 9,000 & 15.00% & **30** & 32.22% & **86.02%** & 90.54% \\
 & & & & & **95.0%** & 12,000 & 20.00% & **40** & 39.14% & **93.80%** & 94.95% \\
 & & & & & **99.9%** & 16,000 & 26.67% & **50** & 46.46% & **97.79%** & 97.79% \\
\multirow{3}{*}{**GloVe-25**} & \multirow{3}{*}{Angular FlyHash (AFH)} & \multirow{3}{*}{1,183,514} & \multirow{3}{*}{25} & **75.0%** & 95,000 & 8.03% & **500** & 18.00% & **82.60%** & 63.30% \\
 & & & & **85.0%** & 130,000 & 10.98% & **500** & 20.60% & **89.00%** & 70.20% \\
 & & & & **95.0%** & 200,000 & 16.90% & **500** & 24.90% & **94.80%** & 78.70% \\
 & & & & **99.9%** & 300,000 & 25.35% & **500** & 26.60% & **97.50%** & 84.30% \\
\multirow{3}{*}{**Last.fm-64**} & \multirow{3}{*}{Raw MIPS (no lifting)} & \multirow{3}{*}{292,385} & \multirow{3}{*}{65} & **75.0%** & 20,000 & 6.84% & **50** & 6.60% & **57.60%** & 57.60% \\
 & & & & **85.0%** & 28,000 & 9.58% & **50** & 8.90% & **71.10%** & 71.10% \\
 & & & & **95.0%** & 40,000 & 13.68% & **50** & 14.40% & **82.30%** & 82.30% \\
 & & & & **99.9%** & 60,000 & 20.52% & **50** & 22.30% & **93.30%** & 93.30% \\
\end{tabular}

\begin{tabular}{cccc}
**Execution surface** & **Wire / query** & **Latency** & **Server keys** \\
Plaintext (no encryption) & 0.16 MB & 1.14 s & 0 MB \\
**Holo-NN: LinPIR** (CPU, BFV \[31\] exact-int.) & **31.41** MB & **3.29** s (4.39 s<sup>§</sup>) & **0** MB \\
**Holo-NN: CKKS-CPU** (OpenFHE \[1\], 12-thr) & 1.60 MB & 32.9 s & 299 MB<sup>∗</sup> \\
**Holo-NN: CKKS-GPU** (Phantom \[45\], 1\(\times\) RTX 3090) & **1.60** MB & **1.68** s<sup>∗</sup> & 85 MB<sup>∗</sup> \\
**Holo-NN: HEIR-GPU** (Cheddar \[3, 17\], 1\(\times\) RTX 3090) & **0.79** MB & **0.134** s<sup>§</sup> & **75** MB<sup>∗</sup> \\
\end{tabular}

1: Multi-Scale Benchmark Results across 4 Datasets and 4 Operating Tiers (_M,K_<sup>∗</sup>). Rec@_k_ is 1-recall@_k_: the fraction of queries whose true nearest neighbor appears among the top _k_ candidates returned by FISTA.

2: Deployed encrypted Wikipedia-500k demonstrator (_N_=500,000, _B_=8,192, _M_=32,768, 4 blocks of \(8,192\times 8\),192). Latency is end-to-end wall clock; wire cost is total serialized request plus response ciphertexts.

<sup>§</sup> First figure (3.29 s end-to-end; 1.78 s server compute) is sharded across 4 CPU cores (\(4\times 8\),\(192\times 8\),192 shards in parallel on the 6-core Xeon W-2135); parenthetical figure (4.39 s end-to-end; 2.88 s server compute) is single-threaded on 1 core. \(^\circ\) On \(1\times\) RTX 3090 (24 GB VRAM), Phantom holds all 4 64-bit RNS blocks (12.0 GiB plaintexts, 17.1 GiB total VRAM) and evaluates all 4 blocks in **1.54** s of server compute (**1.68** s end-to-end across 10 queries, or 0.385 s/block; vs. 6.95 s across \(2\times\) RTX 2080 Ti GPUs). <sup>‡</sup> HEIR/Cheddar \[3, 17\] uses 32-bit RNS words (`uint32.t`, log<sub>2</sub>(_QP_)≈91 bits), halving wire footprint to **0.79** MB (256 KiB query \(+4\times 128\) KiB responses) and reducing plaintext VRAM by \(3\times\) to 4.00 GiB (8.1 GiB total VRAM). It evaluates a single \(8,192\times 8\),192 block in **12.58** ms on RTX 3090 (**5.33** ms on NVIDIA H100; 8.67 ms RTX 3090 / 2.51 ms H100 at \(4,096\times 4,096\)), completing all 4 Wikipedia blocks in **50.5** ms of server compute and **0.134** s end-to-end (100% Top-1 parity with plaintext). <sup>⋆</sup> At _N_ring=16,384, OpenFHE stores 190 64-bit RNS BSGS rotation keys (299.0 MB), Phantom stores 27 NAF/dyadic keys (84.9 MB), and Cheddar stores 190 32-bit RNS hoisted BSGS keys (74.7 MB).

