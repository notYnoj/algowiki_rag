<tbc>**2D Gaussian Parameterized Tokens.** A standard 2D Gaussian function _p(x,y_) is given by:

\(p(x,y)=\frac{\hat{p}(x,y)}{Z}=\frac{1}{Z}exp\left(-\frac{1}{2(1-\rho^2)}\left(\frac{(x-\mu_x)^2}{\sigma_x^2}-\frac{2\rho(x-\mu_x)(y-\mu_y)}{\sigma_x\sigma_y}+\frac{(y-\mu_y)^2}{\sigma_y^2}\right)\right),\) (1)

where _Z_ is the normalization constant, \(\sigma_x,\sigma_y>0\) are the standard deviations along the _x_- and _y_-axes, and \(\rho\in[-1,1]\) denotes the correlation coefficient. The means \(\mu_x,\mu_y\in\mathbb{R}\) determine the center.

To reduce computation and focus on local regions, we modify the standard 2D Gaussian by restricting its spatial support to a bounded region centered at \((\mu_x,\mu_y)\) and omitting the normalization constant. This design removes unnecessary computation while preserving fine details in the region of interest. Specifically, the modified Gaussian function is defined as:

\(\mathbf{g}(x,y)=\left\{\begin{array}{ c c }
\hat{p}(x,y), & \text{if}|x-\mu_x|\le s\sigma_x\text{and}|y-\mu_y|\le s\sigma_y, \\
0, & \text{otherwise},
\end{array}\right.\) (2)

where _s_ is a hyperparameter controlling the spatial support of the Gaussian function.

Using **g**, we represent an image **x** via _l_ Gaussian parameterized tokens \(\mathbf{z}\in\mathbb{R}^{l\times c}\), as shown in Fig. 1 (c). Each token contains two components **z**_<sub>i</sub>_={**g**_<sub>i</sub>,_**f**_<sub>i</sub>_}. The first component \(\mathbf{g}_i=\{\sigma_x^{(i)},\sigma_y^{(i)},\rho^{(i)},\mu_x^{(i)},\mu_y^{(i)}\}\) (gray cuboids in Fig. 1 (c)) encodes spatial position and devia tion of the Gaussian function. The second component \(\mathbf{f}_i\in\mathbb{R}^{(c-5)}\) (orange cuboids) holds texture features, capturing detailed visual information from the corresponding region. This enables joint encoding of geometric and visual characteristics across image regions.

**Splitting-Based Rendering.** Inspired by GS \[18, 4\], we render GPS-tokens into 2D feature maps using splatting-based rendering. This is possible because each 2D Gaussian is continuous and can be sampled into 2D features. For example, given _l_ Gaussian-parameterized tokens \(\{\mathbf{z}_0,\mathbf{z}_1,\cdots,\mathbf{z}_{l-1}\}\), the _k_-th channel of the rendered 2D feature map at (_x,y_) can be obtained as follows:

\(R(x,y,k)=\sum_{i=0}^{l-1}r_i(x,y,k)=\sum_{i=0}^{l-1}\mathbf{g}_i(x,y)\times\mathbf{f}_i[k].\) (3)

**Advantages over Bounding Boxes and Segmentation Maps.** Alternative approaches to representing image regions often rely on bounding boxes or segmentation maps. Bounding boxes define regions using axis-aligned rectangles, while segmentation maps assign discrete labels to individual pixels. Compared with them, our Gaussian-parameterized tokenization offers several key advantages. First, each 2D Gaussian models anisotropic shapes with only five parameters (\(\mu_x,\mu_y,\rho,\sigma_x,\sigma_y\)), enabling a compact and geometry-adaptive representation that is both expressive and lightweight - reducing<tbc>

(a) The overall framework of GPSToken
Extracting features
Initializing Gaussians
Decoder
SA Token Refinement
SA Token Initialization
g init
z = {g, f}
Gaussian parameters g
Input
Output
Textual features f
Image Features
Rendering Process
Config
Until enough regions
Append
MLP
Pop
g init
f
g init
+
+
MLP
Block
Block
Attn Block
MLP
The one is most complex
x N
g
Divide
(b) Spatially-adaptive Token Initialization
(c) Spatially-adaptive Token Refinement

Figure 2: (a) The overall framework of our GPSToken. (b) Spatially-adaptive Token Initialization. (c) Spatially-adaptive Token Refinement.

