## 2 Background & Problem tion

### 2.1 Threat Model & Security Setting

We consider a client-server architecture where an untrusted server S hosts a large-scale database \(T=\{t_1,t_2,\dots,t_N\}\subset\mathbb{R}^D\) of _N_ high-dimensional feature vectors, and a client holds a confidential query vector \(q\in\mathbb{R}^D\).

The objective is to retrieve the approximate nearest neighbor \(q^*=\mathrm{argmin}_{t_i\in T}\mathrm{dist}(q,t_i)\) under standard metric spaces--specifically Euclidean distance ∥_q-t<sub>i</sub>_∥<sub>2</sub> (e.g., via RFF) or angular cosine similarity \(\frac{\langle q,t_i\rangle}{\left\|q\right\|_2\left\|t_i\right\|_2}\) (e.g., via FlyHash)--subject to basic privacy constraints:

1. **Query & Access-Pattern Privacy**: Under standard IND-CPA Ring-LWE encryption, the server S learns nothing about the client’s query _q_. Crucially, unlike graph- or tree-based private search that leaks data-dependent branching paths, the server’s execution trace (_y=H_F(_q_)) is strictly _data-oblivious_: it touches every measurement channel uniformly in a single linear pass, and hence the holographic naming, eliminating memory access-pattern leakage.<tbc>

2. **Index Protection (Bounded Single-Query Leakage)**: The client never downloads the raw database _T_ or the holographic index _H_. For an honest- but-curious client issuing a query _q_, the single _M_- dimensional response \(y=A\mathcal{F}(q)\in\mathbb{R}^M\) (\(M\checkmark N\)) is an underdetermined linear projection with an (_N-M_)-dimensional null space in R_<sup>N</sup>_, enabling sparse recovery of the \(K^*\checkmark N\) local Voronoi neighbors without transmitting raw vectors _T_. Defending against an adaptive malicious client that issues O(_B_) chosen basis queries to reconstruct _H_ (or inspects ciphertext error terms) is orthogonal to our core primitive and requires standard query rate-limiting, noise flooding for circuit privacy, and zero-knowledge proofs of query well-formedness.<tbc>

3. **Operational Model**: We target deployment settings where server-side storage and high-throughput parallel compute are abundant, but client storage and network bandwidth across wide area networks (WAN) and multi-round cryptographic communication overheads are the dominant system bottlenecks.

### 2.2 Compressive Sensing & Restricted Isometry Property

Compressive Sensing \[22, 10, 27\] enables the stable, high probability, reconstruction of an _N_-dimensional sparse signal<tbc>

\(s\in\mathbb{R}^N(|\mathrm{support}(s)|\le k\checkmark N)\) (5)

<tbc>from an underdetermined measurement vector \(y\in\mathbb{R}^M\) with \(M\checkmark N\) and support the number of non-zero entries:

\(y=As\) (6)

where \(A\in\mathbb{R}^{M\times N}\) is a measurement operator satisfying the **Restricted Isometry Property (RIP)** \[9, 11\] of order _k_. Specifically, there exists an isometry constant \(\delta_k\in(0,1)\) such that for all _k_-sparse vectors _s_:

\((1-\delta_k)\left\|s\right\|_2^2\le\left\|As\right\|_2^2\le(1+\delta_k)\left\|s\right\|_2^2\) (7)

In practice, _A_ is drawn from appropriately chosen random ensembles, most commonly:

\(A\in\{-1,+1\}^{M\times N}\text{(Bernoulli)}\) (8)

\(A\sim\mathcal{N}\left(0,\frac{1}{M}\right)^{M\times N}\text{(Gaussian)}\) (9)

Though, given that Bernoulli amounts to random sums and negations of existing column entries, this distribution is typically the most efficient choice.

Because _A_ is pseudorandom, any entry (_i,j_) or column can be evaluated on the fly in O(1) time by both client and server using a Pseudorandom Function (PRF) _F<sub>k</sub>(i,j_) keyed by a compact shared seed _k_ (e.g., 128-bit AES-CTR), eliminating any requirement to transmit or materialize _A_ in memory or GPU VRAM.

### 2.3 Kernel Lifting & Distance Approximations

In metric nearest neighbor search, non-linear geometric distances (_L_<sub>2</sub> Euclidean distance or cosine similarity) can be directly evaluated via linear operations in the raw feature space R_<sup>D</sup>(u<sup>T</sup>u+v<sup>T</sup>v_-2_u<sup>T</sup>v_), but they are typically dense in _N_. To bridge this gap, feature mapping functions \(\mathcal{F},\mathcal{G}:\mathbb{R}^D\rightarrow\mathbb{R}^B\) lift continuous vectors into an expanded _B_-dimensional space (\(B\gg D\)) where a localized similarity kernel sim(_q,t<sub>i</sub>_)--defined as a positive, monotonically decreasing function of metric distance dist(_q,t<sub>i</sub>_) that vanishes outside a local neighborhood--is preserved as a linear inner product:

\(\mathrm{sim}(q,t_i)\approx\langle\mathcal{F}(q),\mathcal{G}(t_i)\rangle\) (10)

While many kernel feature mappings exist, two are of particular use for our purposes:

1. **Gaussian Radial Basis Function via Random Fourier Features**: Approximating a radial distance function, Gaussian Radial Basis Function (RBF) \[39\] via Random Fourier Features (RFF) \[36\] allows _L_<sub>2</sub> minimization over a tunable radius without the need for an interactive rounding procedure. Via Bochner’s theorem \[8\], shift-invariant kernels such as the RBF \(K(x,y)=\mathrm{exp}(-\gamma\left\|x-y\right\|_2^2)\) are approximated by<tbc>

