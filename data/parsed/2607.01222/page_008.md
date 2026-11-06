### Network Architecture.

The sequence **_S_** is fed into the OrbitPainter network. As shown in Figure 2(b), OrbitPainter consists of _N_ Transformer blocks. Each block contains two parallel attention modules: a standard full-attention module and a proposed _Geometry-Aware Sparse Attention_ module (introduced in Section 3.2). The full-attention module processes the entire sequence \(S=\mathrm{Concat}_T(F_I,\mathbf{x}'_t)\), while the sparse attention module operates only on the video-related tokens \(\mathbf{x}'_t\) to better capture geometry-aware correspondences.

### Training Objective.

We adopt Flow Matching as the training objective. The model learns to predict the velocity **u**_<sub>t</sub>=d_**x**_<sub>t</sub>/dt_ by minimizing the mean squared error between the predicted velocity **v**_<sub>t</sub>_ and the ground-truth velocity:

\(\mathcal{L}=\mathbb{E}_{t,\mathbf{x}_0,F^{RGB}}\|\mathbf{v}_t-\mathbf{u}_t\|^2.\) (7)

## 3.2 Geometry-Aware Sparse Attention

We formulate 3D texture generation as a video generation problem, where the goal is to synthesize horizontal and vertical orbit-scan videos conditioned on a reference image prior and 3D geometry priors. This setting differs from conventional video generation tasks, which typically rely only on appearance priors (e.g., a reference image) without explicit geometric information. The availability of 3D geometry priors therefore provides an opportunity to guide the generation process more effectively.

In standard video diffusion models, the attention module performs full spatiotemporal attention. As illustrated in Figure 2(b), each query token attends to all tokens across both spatial and temporal dimensions. This design is necessary because traditional video generation lacks structural priors that could constrain the attention space.

In our setting, the video frames are generated from orbit scans of a 3D asset, and explicit geometric priors are available. This enables us to leverage the underlying 3D geometry to guide the attention mechanism. Specifically, each spatiotemporal token in the latent video corresponds to a surface point on the 3D mesh. Given a query token, we can recover its corresponding 3D location through the position-map representation. Based on this 3D correspondence, we restrict the attention to tokens that correspond to nearby or identical surface locations across different frames, rather than attending to all tokens in the video, as illustrated in Figure 2(b).

We refer to this module as _Geometry-Aware Sparse Attention_. In practice, given a query spatiotemporal token T , we first re-project it onto the underlying 3D geometry using its associated 3D position, thereby identifying the corresponding voxel location (_i,j,k_) in the 3D space. We then define a local neighborhood around (_i,j,k_) with an expansion radius _r_ (set to 3 by default). For tokens in other video frames, we select those whose associated 3D positions fall within this neighborhood. Only these tokens are used as keys in the attention computation for the query token T , while all other tokens are ignored.

