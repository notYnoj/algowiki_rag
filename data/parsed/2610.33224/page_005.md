projecting vectors onto random Gaussian frequencies \(W\sim\mathcal{N}(0,2\gamma I)\) to produce \(\mathbf{f}(x)\in\mathbb{R}^B\):<tbc>

\(\mathbf{f}(x)=\frac{1}{\sqrt{B/2}}\left[\begin{array}{ c }
cos(Wx) \\
sin(Wx)
\end{array}\right]\) \(\text{(11)}\)

The RBF acts as a spatial bandpass filter: points within a Euclidean radius \(\propto 1/\sqrt{\gamma}\) produce positive inner products, while distant points decay exponentially toward zero, inducing physical sparsity.<tbc>

2. **FlyHash (Biologically Inspired Sparse Hashing)**: Serving as an angular analog to the Euclidean RBF, FlyHash \[20\] has frequently \[33, 38\] been used to approximate cosine similarity across directional semantic embeddings. Inspired by the _Drosophila_ olfactory circuit \[13\], continuous vectors are projected onto random sparse binary hyperplanes \(W\in\{0,1\}^{B\times D}\) and can be sparsified via winner-take-all (_k_-WTA) competitive inhibition to yield a binary code, as in traditional applications, or a sparse gated projection as in our work \(\mathbf{f}(x)\in\mathbb{R}^B\) whose _j_-th coordinate is:<tbc>

\(\mathbf{f}(x)_j=[\text{WTA}_k(Wx)]_j\)<br>
\(=\left\{\begin{array}{ c c }
(Wx)_j & \text{if}(Wx)_j\in\text{Top-}k(Wx) \\
0 & \text{otherwise}
\end{array}\right.\) \(\text{(12)}\)

Much like RBF creates localized hyperspheres in Euclidean space, FlyHash creates localized angular cones on the hypersphere, mapping angular proximity directly to the inner product overlap \(\langle\mathbf{f}(x),\mathbf{f}(y)\rangle\) of sparse representations while remaining resilient to high-dimensional metric concentration.

Throughout the remainder of this paper, the query mapping \(\mathcal{F}:\mathbb{R}^D\rightarrow\mathbb{R}^B\) and database mapping \(\mathcal{G}:\mathbb{R}^D\rightarrow\mathbb{R}^B\) denote these localized feature liftings--instantiated via RFF for Euclidean metric manifolds or Asymmetric FlyHash (Section 4) for directional semantic embeddings.

## 3 The Holo-NN Retrieval Architecture

### 3.1 Feature Projections & Shared Feature Space (F,G)

Given database points \(t_i\in T\) and query _q_, the client and server apply complementary localized feature mappings \(\mathcal{F},\mathcal{G}:\mathbb{R}^D\rightarrow\mathbb{R}^B\) (instantiated via RFF or Asymmetric FlyHash as detailed in Section 4). These mappings are constructed to satisfy two properties: (1) _Metric Locality_, preserving local neighborhood similarity \(\langle\mathcal{G}(t_i),\mathcal{F}(q)\rangle\approx\text{sim}(q,t_i)\), and (2) _Zero-Mean Background Incoherence_, where global mean-centering \((\mathcal{G}(t_i)\leftarrow\mathcal{G}(t_i)-\mu)\) ensures that background inner products vanish in expectation \((\mathbb{E}[\langle\mathcal{G}(t_j),\mathcal{F}(q)\rangle]=0)\). Stacking the _N_ transformed<tbc>

<tbc>database vectors produces the database embedding matrix:

\(G=\mathcal{G}(T)=\left[\begin{array}{ c }
\mathcal{G}(t_1)^T \\
\mathcal{G}(t_2)^T \\
\vdots \\
\mathcal{G}(t_N)^T
\end{array}\right]\in\mathbb{R}^{N\times B}\) (13)

The uncompressed affinity vector \(s\in\mathbb{R}^N\) between query _q_ and all _N_ database points is:

\(s=G\mathcal{F}(q)=\left[\begin{array}{ c }
\langle\mathcal{G}(t_1),\mathcal{F}(q)\rangle \\
\vdots \\
\langle\mathcal{G}(t_N),\mathcal{F}(q)\rangle
\end{array}\right]\in\mathbb{R}^N\) (14)

Because F and G act as localized spatial or angular bandpass filters, _s_ is _k_eff_-compressible_ (approximately sparse): its _k_eff largest positive components capture the local Voronoi neighborhood around _q_, while the residual background tail decays rapidly below the universal soft-thresholding floor \(\lambda\).

### 3.2 Offline Server Database Grating

Rather than storing or scanning \(G\in\mathbb{R}^{N\times B}\) at query time, the server pre-multiplies the database feature matrix with the pseudorandom measurement matrix \(A\in\mathbb{R}^{M\times N}\):

\(H=AG=A\mathcal{G}(T)\in\mathbb{R}^{M\times B}\) (15)

The resulting matrix _H_ is the **Holographic Sensing Matrix**. It compresses the _N_-point database into _M_ linear measurement channels across the _B_ feature dimensions. This computation is executed strictly **offline**, once, during index construction and stored permanently on the server. Given the offline pre-computation of _H_, the function of the server benefits from theoretical or empirical optimization on algorithm parameters and hash choice. Further, because this computation is embarrassingly parallel, it can be seamlessly partitioned and executed in batch or form the basis for hierarchical design as needed.

### 3.3 Non-Interactive Linear Query Evaluation (_y=H_F(_q_))

At query time, the client computes its _B_-dimensional feature representation F(_q_) locally and transmits it to the server (either in sparse-plaintext for bandwidth- constrained ANN, or encrypted under a Linearly Homomorphic Encryption scheme as detailed in Section 6). The server then executes a single linear matrix-vector evaluation:

\(y=H\mathcal{F}(q)\in\mathbb{R}^M\) (16)

By association:

\(y=H\mathcal{F}(q)=(AG)\mathcal{F}(q)=A(G\mathcal{F}(q))=As\) (17)

