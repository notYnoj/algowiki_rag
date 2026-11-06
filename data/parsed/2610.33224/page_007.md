<tbc>latter being significantly sparser than the former:

1. **Database Grating (**\(k_\mathrm{db}\checkmark B\)**)**: The server’s precomputed database feature representation \(G=\mathcal{G}(T)\in\mathbb{R}^{N\times B}\) maintains a strict, ultra-sparse support (\(k_\mathrm{db}\checkmark B\) per row). This ensures that the offline holographic matrix \(H=AG\in\mathbb{R}^{M\times B}\) remains compact and computationally efficient.<tbc>

2. **Query Aperture (**_k<sub>q</sub>\>k_<sub>db</sub>**)**: The client projects the query _q_ through a broader activation aperture (\(k_q=\alpha_\mathrm{aperture}\cdot k_\mathrm{db}\) with \(\alpha_\mathrm{aperture}>1\)).

Opening the query aperture is free in bandwidth terms across both plaintext and encrypted deployments. In plaintext, transmission communicates only the non-zero coordinates of F(_q_), so cost grows with _k<sub>q</sub>_ from a negligible base. Under homomorphic encryption, the query is a _dense SIMD ciphertext_ spanning all _B_ slots whose byte size depends only on _B_ and the RNS limb count and is therefore completely independent of _k<sub>q</sub>_--transmitting only the active coordinates is not an option, since the support of F(_q_) must remain hidden from the server. In both regimes, the broad query aperture allows all potentially relevant semantic dimensions while the server’s sharp database grating acts as a spatial filter, eliminating false-negative dropouts with no additional communication overhead.

### 4.2 Geometric Duality: Continuous Euclidean RFF vs. Discrete Hyperplane Competition

Empirical and theoretical investigations reveal idiosyncratic, data-dependent structures governing feature transform selection. That is, while arguments for _a priori_ parameter selection can be made, the dominating influences on the parameter choices for a dataset come from the structure, distribution and density of the data manifold, in addition to its ambient dimension _D_. MNIST-784 (_D_=784) falls squarely in the first regime while GloVe-25 (_D_=25) falls squarely in the second, as _D_ alone does not predict which transform applies.

1. **Spatially Structured Metric Manifolds (low intrinsic dimension)**: In Euclidean metric spaces with physical or spatial structure (e.g., 2D spatial seeds, MNIST-784 pixel spaces, and SIFT-128 image descriptors), pairwise Euclidean distances show meaningful local contrast. In this regime, Random Fourier Features (RFF) with Gaussian RBF kernels \(K(x,y)=\mathrm{exp}(-\gamma\|x-y\|_2^2)\) create genuine physical sparsity because spatial volume scales as O(_r<sup>D</sup>_). Points outside the local kernel radius \(r>3/\sqrt{2\gamma}\) decay exponentially toward zero, enabling high-fidelity metric nearest neighbor recovery (Figure 2 and  1).<tbc>

2. **Unstructured Semantic Hyerspheres (intrinsic dimension** ≈**ambient** _D_**)**: On unconstrained<tbc>

<tbc>hyperspherical manifolds, pairwise Euclidean distances concentrate sharply around \(\sqrt{2}\) as _D_ grows, since \(\|x-y\|_2^2=2-2\langle x,y\rangle\) and \(\langle x,y\rangle\rightarrow 0\) by measure concentration on the sphere. Continuous exponential kernels suffer from amplitude collapse, where the true neighbor similarity signal drops below the finite-sample RFF Monte Carlo noise floor \(\mathcal{O}(1/\sqrt{B})\).

In contrast, Asymmetric FlyHash partitions high- dimensional space via nearly orthogonal random hyperplanes. Discrete _k_-WTA competition creates implicit Voronoi cells, preserving semantic locality without exponential amplitude attenuation and remaining robust to the curse of dimensionality. Moreover, because feature strength is preserved within each Voronoi cell, a local "in-cell Euclidean metric" breaks ties and further increases NN accuracy.

## 5 Algorithmic ANN Benchmark Evaluation

### 5.1 Benchmark Datasets & Experimental Setup

To validate the algorithmic accuracy and theoretical predictions of Holo-NN independently of cryptographic backends, we evaluate Holo-NN across four standard nearest- neighbor benchmark suites spanning Euclidean (_L_<sub>2</sub>) and angular (cosine) metric spaces:

1. **SIFT-1M (**_N_=1,000,000_,D_=128**)**: The canonical computer vision benchmark evaluated under **Euclidean (**_L_<sub>2</sub>**) distance** across the first _Q_=1,000 of the 10,000 official test queries. Vectors are mean- centered, globally rescaled, and lifted via Random Fourier Features (_B_=16,384, \(\gamma=8.0\)), mapping Euclidean proximity to real-valued inner products.<tbc>

2. **MNIST-784 (**_N_=60,000_,D_=784**)**: Handwritten digit pixel vectors evaluated under **Euclidean (**_L_<sub>2</sub>**) distance** across _Q_=10,000 test queries, lifted via mean-centered Random Fourier Features (_B_=8,192, \(\gamma=2.0\)).<tbc>

3. **GloVe-25 (**_N_=1,183,514_,D_=25**)**: Web-crawl word embeddings evaluated under **angular cosine similarity** across _Q_=1,000 test queries, lifted via Asymmetric FlyHash (_B_=65,536) to resolve angular crowding on the unit hypersphere.<tbc>

4. **Last.fm-64 (**_N_=292,385_,D_=65**)**: Sparse user- music interaction preference vectors evaluated under **maximum inner product (MIPS)** across _Q_=1,000 test queries. Because the inner product is already linear, we apply no feature lifting (F=G=id, _B=D_=65) and operate directly on the raw vectors. This dataset therefore has no sparsification mechanism, and serves as our boundary case.<tbc>

