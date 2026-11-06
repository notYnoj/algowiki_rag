former Block (LTB) and the Global Transformer Block (GTB), which process the features _F<sub>SLR</sub>_ from the encoder.

In the Local Transformer Block (LTB), we first use a Batch Normalization (BN) layer to stabilize and accelerate training, and then use a Pixel Mixer (PM) layer to enhance the aggregation of local information. Specifically, PM divides the feature channels into four equally sized groups, and each group undergoes a specific shift sequence (left, right, top, bottom) to introduce locality and spatial correlations. This approach allows us to quickly capture and integrate knowledge from surrounding areas while improving the effective information exchange mechanisms between feature channels. The entire process of the Local Transformer Block (LTB) can be expressed as:

\(F_L=MLP(PM(BM(F_{LR}^S))),\) (2)

where PM denotes the Pixel Mixer, BM represents Batch Normalization, and MLP refers to the multi-layer perceptron used for further feature transformation, \(F_{LR}^S\) being the input encoded features of the structure estimation branch.

In the Global Transformer Block (GTB), we construct an effective global dependency model based on self-attention (SA). We employ stripe window self-attention (SWSA) to effectively capture multi-scale symmetries and similarities present in the image. Firstly, self-attention is computed for each stripe window:

\(F_{out}^n=\text{Softmax}\left(\frac{Q^n\cdot(Q^n)^T}{\text{scale}}\right)\cdot V^n,\) (3)

where _n_ denotes the _n_-th stripe window, with \(Q^n=F_{LR}^S\cdot W_Q\) and \(V^n=F_{LR}^S\cdot W_V\) being linear transformations of \(F_{LR}^S\) using weight matrices _W<sub>Q</sub>_ and _W<sub>V</sub>_. Subsequently, the outputs of all stripe windows are concatenated along the channel dimension:

\(F_{out}=[F_{out}^1;F_{out}^2;\dots;F_{out}^n].\) (4)

Next, _F<sub>out</sub>_ undergoes further feature transformation through a multi-layer perceptron (MLP):

\(F_G=MLP(F_{out}).\) (5)

Finally, the features obtained from these two modules are concatenated:

\(F_{SEB}=F_L+F_G.\) (6)

## 3.3. Texture Estimation Branch

Due to the spatial variability of image deformation and the discontinuity of SCIs, we propose the texture estimation branch (TEB) to predict the features of image deformation effectively. We employ non-uniform B-splines for feature embedding and multiply the estimated local texture by the local Jacobian matrix of the coordinate transformation to<tbc>

<tbc>predict the features of the distorted image. Specifically, the implicit neural representation of non-uniform B-splines is:

\(I_\text{warp}[y;\theta,\psi]=\sum_{t\in N}w_tf_\theta(g_\psi(z_t,y-f(x_t),s)),\) (7)

where \(z=E_\phi(I_\text{LR})\), and _N_ is a set defined as \(N=\{N|N=[f^{-1}(y)+\left[\frac{m}{w},\frac{n}{h}\right]]|[m,n]\in[-1,1]\}\).In this context, _w<sub>t</sub>_ represents the weight of the local set, \(z_t\in\mathbb{R}^D\) is a latent variable for index _t_, \(x_t\in X\subset\mathbb{R}^2\) is a coordinate of _z<sub>t</sub>_, and _s_ is the cell value represented by a superscript factor. The local grid \(\delta_y=y-f(x_t)\) represents the query point \(y=f(x)\in\mathbb{R}^2\). The function \(g_\psi(z_t,\delta_y,s)\) represents the B- spline texture coefficients estimator (BTC), which includes three estimators: the coefficient estimator \(g_c:\mathbb{R}^D\rightarrow\mathbb{R}^C\), the structure estimator \(g_k:\mathbb{R}^D\rightarrow\mathbb{R}^{2C}\), and the dilation estimator \(g_d:\mathbb{R}^{10}\rightarrow\mathbb{R}^C\). The encoding function \(g_\psi:(\mathbb{R}^D,\mathbb{R}^2,\mathbb{R}^{10})\rightarrow\mathbb{R}^C\) is defined as :

\(g_\psi(z_t,\delta_y,s)=c_t\odot\text{vec}\left[\beta_n((\delta_y-k_t)\odot d)\right],\) (8)

where _c<sub>t</sub>=g<sub>c</sub>(z<sub>t</sub>_), _k<sub>t</sub>=g<sub>k</sub>(z<sub>t</sub>_), and _d=g<sub>d</sub>(s_). To enable the model to represent distorted images, we linearize the given coordinate transformation into an affine transformation: \(\delta_y=J_f(x_j)\delta_x\). Here,\(J_f(x_j)\in\mathbb{R}^{2\times 2}\) represents the Jacobian matrix of the coordinate transformation _f_ at _x<sub>j</sub>_.

Our model can then extract B-spline information from distorted images by utilizing the local grid in the input coordinate space \(\delta_x\) rather than in \(\delta_y\). In arbitrary-scale super- resolution (SR) tasks, the pixels in the upsampled image are square and spatially invariant. However, when the image undergoes warping, the pixels in the resampling image can have arbitrary shapes and spatial transformations. To effectively represent and compute pixel shapes, we represent the pixel shape \(s(y)\in\mathbb{R}^{12}\) (where R<sup>4</sup> denotes pixel direction and R<sup>4</sup> denotes pixel curvature) with the gradient of the coordinate transformation at point _y_ as follows:

\(s(y)=[J_f^{-1}(y),H_f^{-1}(y)],\) (9)

where \(J_f^{-1}(y)\in\mathbb{R}^{2\times 2}\) and \(H_f^{-1}(y)\in\mathbb{R}^{2\times 2\times 2}\) represent the numerical Jacobian matrix in the pixel direction and the numerical Hessian tensor in the pixel curvature, which are used to describe edge positions and pixel shapes, respectively.

Therefore, we redefine the implicit neural representation of non-uniform B-splines in Eq. 8 as follows:

\(F_{TEB}=c_t\odot\text{vec}\left[\beta_n((J_f(x_j)\delta_x-k_t)\odot g_d(s(y)))\right].\) (10)

## 3.4. Structure-Texture Fusion Module

We design a structure-texture fusion module that integrates the most relevant texture features into structural fea<tbc>

