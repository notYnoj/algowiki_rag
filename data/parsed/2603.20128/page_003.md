<tbc>At each resolution level _l_, we extract local patches containing the HR query coordinates: \(\mathbf{P}_i^l=\mathbf{I}^\text{LR}(\mathbf{r}_i^l)\), where \(\mathbf{P}_i^l\) denotes the sampled patch around location \(\mathbf{r}_i^l\). These multi- scale patches capture progressively finer spatial context for high-resolution reconstruction, as shown in Fig. 1.

To incorporate viewpoint information, we embed each camera pose **C**_<sub>n</sub>_ into a latent code via a lightweight MLP:<tbc>

\(\mathbf{a}^{\text{C}_n}=\text{MLP}_a(\mathbf{C}_n),\) (1)

<tbc>which produces a compact representation of the viewing direction. This latent code is injected into the patch encoder \(\mathcal{G}_\text{T}^l\) to produce pose-aware texture tokens:<tbc>

\([\unknown_1^l,\unknown_2^l,\dots,\unknown_F^l]=\mathcal{G}_\text{T}^l(\mathbf{P}_i^l,\mathbf{a}^{\text{C}_n}).\) (2)

<tbc>Finally, hierarchical view-texture query tokens are constructed by concatenating spatial coordinates with the corresponding texture tokens:

\(\mathbf{Q}_{i,n}^l=[\mathbf{x},\mathbf{y},\unknown_1^l,\dots,\unknown_F^l]=[\mathbf{q}_1^l,\dots,\mathbf{q}_S^l].\) (3)

## 3.2 . Camera-Aware Feature Integration

Given the hierarchical view-texture query tokens \(\mathbf{Q}_{i,n}^l\), our goal is to generate point-wise, view-dependent feature vectors that incorporate both multi-scale spatial context and camera information. This is achieved through a unified hashing and implicit interpolation process.

### Hyper-Vertex Retrieval.

For each query token \(\mathbf{Q}_{i,n}^l\) at resolution level _l_, we locate its enclosing hyper-vertices \(\mathbf{V}_{i,n}^l=\{\mathbf{V}_{i,n,k}^l\}_{k=1}^K\) on the discretized multi-resolution grid, where _K_=2_<sup>d</sup>_ and _d_ is the dimension of **Q**_<sup>l</sup>i,n_. Each hyper-vertex \(\mathbf{V}_{i,n,k}^l\) is then mapped to a latent feature vector via a unified hash table:<tbc>

\(\hat{\mathbf{v}}_{i,n,k}^l=\text{Hash}(\mathbf{V}_{i,n,k}^l).\) (4)

<tbc>Unlike level-specific hash mappings, our unified design uses a single shared hash table across all _L_ levels, significantly reducing memory usage while preserving multi-scale representation. Fig. 2 illustrates such cross-level hash map<tbc>

