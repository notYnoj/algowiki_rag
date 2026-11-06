## 5 Applications of Differentiable EM

In this section, we propose numerous larger-scale applications of the differentiation of the EM algorithm presented in Section 2. Our goal is to illustrate the versatility of the proposed approach, rather than to achieve state-of-the-art results on these applications. In Appendix A.9.7, we also present an EM-MW\(_2^2\)-regularised generative model.

### 5.1 Barycentre Flow in 2D

Wasserstein barycentres \[AC11\] and their notoriously challenging computation \[CD14; Álv+16; AB22; TDG24\] are active fields of research. In this section, we illustrate the use of differentiable EM to flow a point cloud towards a barycentre of GMMs. Given _M_ point clouds \(Y_i\in\mathbb{R}^{n\times 2}\), our goal is to optimise a point cloud \(X\in\mathbb{R}^{n\times 2}\), initialised as random normal noise, towards a barycentre (with uniform weights) of GMMs (\(\nu_i\)) fitted from (_Y<sub>i</sub>_). Specifically, we solve

\(min_{X\in\mathbb{R}^{n\times 2}}\sum_{i=1}^M\text{MW}_2^2\left(\mu(F_X^T(\theta_0)),\nu_i\right)\)

with respect to _X_. The GMMs \(\nu_i\) are fitted beforehand, and \(\mu(F_X^T(\theta_0))\) is the current EM estimate of the optimised cloud _X_. We illustrate the results in Fig. 7, where _M_:=3, _K_:=2 and _n_:=500. This method can be adapted to compute more general barycentres, as presented in Appendix A.9.3.

### 5.2 Colour Transfer

Colour transfer is a well-known imaging task where OT techniques have been used extensively \[Rei+02; Del04; PK07; PKD07; PPC10; Rab+12; RFP14\], it consists in transforming the RGB colour distribution of a source image to match that of a target image. We propose the following approach: we initialise an image _X_ as the source image, and optimise it to minimise the MW\(_2^2\) cost between a GMM fitted on _X_ (seen as an RGB point cloud), and a target GMM \(\nu\in\text{GMM}_3(K)\) fitted on the colour distribution of the target image. Specifically, we minimise \(X\longmapsto\text{MW}_2^2(\mu(F_X^T(\theta_0)),\nu)\) for some initialisation \(\theta_0\). _Warm-Start EM_ method from Algorithm 3, choose _K_:=10 components and use fixed uniform GMM weights (Algorithm 2 for EM) to avoid being trapped in a local minimum, as seen in Section 3.3. We present some results in Fig. 8, and provide additional discussions about the optimisation choices in Appendix A.9.4, along with a comparison to a (computationally expensive) Entropic OT alternative. Even with only _K_=10 components, the colour transfer preserves both details and global consistency, and in the resulting colour scheme, the source image appears to exhibit stronger contrast in this example.

Balanced OT methods may be sensitive to outliers in the distributions, leading to artifacts in the colour transfer results if colour aberrations are present in the target. Unbalanced OT methods \[LMS18\] can mitigate this issue \[Chi+18a; Bon+24\]. We now consider the unbalanced variant of the<tbc>

Initial cloud
Final barycenter
Target #1
Target #2
Target #3

Figure 7: EM-MW\(_2^2\) flow displacing particles in order to make their EM output approach a barycentre of three target GMMs.

