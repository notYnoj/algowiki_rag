<tbc>tion mechanism. For instance, PAPR represents a scene as _N_ learnable points \(\mathcal{P}=\{(\mathbf{p}_j,\mathbf{f}_j)\}_{j=1}^N\), where \(\mathbf{p}_j\in\mathbb{R}^3\) is the spatial position and \(\mathbf{f}_j\in\mathbb{R}^h\) is a feature vector. To render ray **r**_<sub>i</sub>_, PAPR selects the _K_ points nearest to it by perpendicular distance as the local neighborhood. A learned cross-attention mechanism then assigns a softmax weight _a<sub>ij</sub>_ to each neighbor point _j_, and the ray’s feature \(\mathbf{f}_i^\mathrm{ray}\) is computed as the weighted sum of their features:

\(\mathbf{f}_i^\mathrm{ray}=\sum_{j=1}^Ka_{ij}\mathbf{f}_{ij},\) (1)

where **f**_<sub>ij</sub>_ denotes the feature associated with the _j_-th selected neighbor point **p**_<sub>ij</sub>_ for ray _i_. The aggregated feature map is then decoded by a UNet \[17\] to predict the RGB colors. Given the same attention weights, these methods typically predict the intersection point \(\mathbf{x}_i\in\mathbb{R}^3\) where the ray hits the surface by interpolating the point positions:

\(\mathbf{x}_i=\sum_{j=1}^Ka_{ij}\mathbf{p}_{ij}.\) (2)

Note that **x**_<sub>i</sub>_ is an _attention-weighted average_ of point positions, not a true geometric intersection: its quality depends on how concentrated the weights are and how well-placed the supporting points are. This sensitivity motivates the geometry regularizers introduced in Sec. 4.1.

### Canonical and deformed space.

We call the point positions after training the **canonical positions** \(\mathbf{p}_j^\mathrm{can}\). The corresponding **canonical intersection**

\(\mathbf{x}_i^\mathrm{can}=\sum_{j=1}^Ka_{ij}^\mathrm{can}\mathbf{p}_{ij}^\mathrm{can}\) (3)

is what the UV mapping is trained on. At edit time, a non-rigid deformation displaces each point to \(\mathbf{p}_j^\mathrm{def}\), producing a **deformed intersection**

\(\mathbf{x}_i^\mathrm{def}=\sum_{j=1}^Ka_{ij}^\mathrm{def}\mathbf{p}_{ij}^\mathrm{def}\) (4)

in deformed space, where direct UV lookup is no longer valid. Bridging this gap is the central problem addressed in Sec. 4.3.

### 3.2 Neural UV Mapping

Neural UV mapping methods (like Nuvo \[20\] and NeuTex \[25\]) parameterize surface textures by learning continuous mappings from 3D space to 2D texture atlases. For example, Nuvo learns a multi-chart UV atlas and texture map from a set of surface points G (in our setting, \(\mathcal{G}=\{\mathbf{x}_i^\mathrm{can}\}\)). It uses cycle-consistency

