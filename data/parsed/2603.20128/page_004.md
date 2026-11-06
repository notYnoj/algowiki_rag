ping in 2D condition.<br>
**Camera-Conditioned Weight Prediction.** To interpolate the hashed features, we predict adaptive weights conditioned not only on the geometric relation of \(\mathbf{Q}_{i,n}^l\) to its sur rounding vertices but also on the camera embedding **a**<sup>_C<sub>n</sub>_</sup>. Specifically, a lightweight two-layer MLP takes as input the relative offset of \(\mathbf{Q}_{i,n}^l\) within its voxel together with **a**<sup>_C<sub>n</sub>_</sup>, and outputs interpolation weights:

\([\mathbf{w}_{i,n,1}^l,\dots,\mathbf{w}_{i,n,K}^l]=\text{MLP}_w\big(\mathbf{Q}_{i,n}^l,\mathbf{a}^{C_n}\big).\) (5)

**Feature Aggregation.** The final feature vector corresponding to \(\mathbf{Q}_{i,n}^l\) is then computed as the weighted sum of its hyper-vertex features:

\(\mathbf{v}_{i,n}^l=\sum_{k=1}^K\mathbf{w}_{i,n,k}^l\cdot\hat{\mathbf{v}}_{i,n,k}^l.\) (6)

**Multi-Scale Feature Representation.** Repeating this process across all _L_ resolution levels yields a set of view- dependent feature vectors. Concatenating them forms the final point-wise, multi-scale representation for viewpoint **C**_<sub>n</sub>_:

\(\mathbf{v}_{i,n}=[\mathbf{v}_{i,n}^1,\mathbf{v}_{i,n}^2,\dots,\mathbf{v}_{i,n}^L].\) (7)

### 3.3 . Global Feature Fusion

To ensure that high-resolution outputs are both detail- rich and consistent across views, we integrate global low- resolution (LR) image features into the view-dependent feature representations **v**_<sub>i,n</sub>_. This is achieved through a two-stage fusion mechanism that combines viewpoint- conditioned features with scene-level global context.

**Stage 1: Camera-Aware Feature Enhancement.** From the previous step, each query point **Q**_<sub>i,n</sub>_ is represented by its multi-resolution, view-dependent feature vector \(\mathbf{v}_{i,n}=[\mathbf{v}_{i,n}^1,\dots,\mathbf{v}_{i,n}^L]\). To explicitly encode viewpoint information, we fuse these features with the camera embedding **a**<sup>_C<sub>n</sub>_</sup>. Specifically, the features and embedding are concatenated and passed through a mapping network Gcam:

\(\mathbf{f}_{i,n}^\text{inter}=\mathcal{G}_\text{cam}(\mathbf{v}_{i,n},\mathbf{a}^{C_n}),\) (8)

yielding an intermediate representation that encodes both local multi-scale textures and viewpoint cues.

**Stage 2: Global LR Feature Integration.** While \(\mathbf{f}_{i,n}^\text{inter}\) captures local and view-dependent details, it lacks holistic scene context. To address this, we extract global image features from the LR input **I**LR using a CNN-based encoder GCNN:

\(\mathbf{f}_\text{LR}=\mathcal{G}_\text{CNN}(\mathbf{I}^\text{LR}).\) (9)

These global features provide structural and semantic guidance, ensuring that reconstructed HR outputs remain coherent across views.

**Final Fusion.** We then combine the intermediate features \(\mathbf{f}_{i,n}^\text{inter}\) with the global LR features **f**LR through a fusion network Gfuse:

\(\bar{\mathbf{v}}_{i,n}=\mathcal{G}_\text{fuse}(\mathbf{f}_{i,n}^\text{inter},\mathbf{f}_\text{LR}),\) (10)

producing global-context aware feature vectors \(\bar{\mathbf{v}}_{i,n}\) that guide HR reconstruction with both local and global consistency.

**Decoding.** Finally, the fused feature vectors are decoded into HR color values through a two-layer MLP:

\(\hat{\mathbf{C}}_{i,n}^\text{HR}=\text{MLP}_c(\bar{\mathbf{v}}_{i,n}).\) (11)

Training is performed by minimizing the pixel-wise Mean Squared Error (MSE) between predictions and ground-truth HR colors:

\(\mathcal{L}=\|\hat{\mathbf{C}}_{i,n}^\text{HR}-\mathbf{C}_{i,n}^\text{HR}\|_2^2.\) (12)

This global fusion strategy ensures that fine details from local patches are preserved, while structural context from the LR image enforces multi-view coherence across synthesized HR outputs.

## 4 . Experiment

### 4.1 . Implementation Details

Our framework is implemented in PyTorch, implementation requirement depends on the output resolution. We trained on NVIDIA A100 GPUs with a batch size of 8. We adopt the Adam optimizer with an initial learning rate of 0.00125. The model is trained for \(\ge\)200 epochs/iterations depending on the dataset sizes. Training requires approximately 0.7 hours per scene, while inference achieves 0.7 seconds per image. Detailed implementation requirement will be provided in the supplementary materials.

**Camera Pose Embedding (a**<sup>**C**_<sub>n</sub>_</sup>**, Eqn. 1).** We encode each camera pose **C**_<sub>n</sub>_ into a compact representation using a three-layer MLP. The first two layers have 64 neurons with ReLU activations, followed by a final 16-dimensional output layer with Tanh activation to ensure bounded values in \[-1,1\].

**Texture Encoder Network (**\(\mathcal{G}_\text{\textbf{I}}^l\)**, Eqn. 2).** For each resolution level _l_, the texture encoder is a two-layer MLP that processes vectorized LR image patches. Each hidden layer contains 128 neurons with ReLU activation, and the output is a compact texture code of dimension _F_=3.

**Camera-Aware Mapping Network (G**<sub>**cam**</sub>**, Eqn. 8).** To integrate viewpoint information, we concatenate the multi- resolution feature vector **v**_<sub>i,n</sub>_ with the camera embedding **a**<sup>_C<sub>n</sub>_</sup>, and feed the result into a four-layer MLP. Each layer has 64 neurons with Tanh activation. The hidden layers internally allocate 32 dimensions to camera embedding features, ensuring effective fusion between spatial and viewpoint cues.

