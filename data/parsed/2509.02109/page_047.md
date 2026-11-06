## A.9.5 Neural Style Transfer

We note that the optimiser choice and EM variant (between Algorithms 1 and 2) do not change the results qualitatively. In our experiments, we use Adam and use standard EM Algorithm 1.

### Choice of the number of components _K_.

We choose _K_=3 in our experiments. When using _K_=1 Gaussian component, the style transfer objective in Eq. (23) simplifies to

\(min_{X\in\mathbb{R}^{3\times H\times W}}\sum_{\ell=1}^3\lambda_\ell\left(\|m_{s,\ell}(X)-m_{t,\ell}\|_2^2+d_\mathrm{BW}^2\left(\Sigma_{s,\ell}(X),\Sigma_{t,\ell}\right)\right),\)

where \(m_{s,\ell}(X)\) and \(\Sigma_{s,\ell}(X)\) are the empirical means and covariances of source features VGG\(_{1\dots\ell}(X)\). We similarly define \(m_{t,\ell}\) and \(\Sigma_{t,\ell}\) for the target image _Y_ . As there are only one source and target Gaussian, there is no need for an EM algorithm, we simply estimate the means and covariance and apply Gaussian OT. To evaluate the influence of _K_, we take two content images (the Eiffel tower and Gatys’ \[GEB15\] picture of Tuebingen), and two style images (_The Great Wave_ and _The Starry Night_). We compute their features corresponding to first layers \(1,\cdots,\ell\) of VGG, for \(\ell\in\{1,\cdots,3\}\). We fit Gaussian mixtures on these features with varying number of components _K_, and we evaluate corresponding log-likelihoods as a measure of model quality. Results are presented in Fig. 27: most of them elbow around _K_=3, the value we retain in our experiments. We set \(\varepsilon_r=0.1\) (as the dominant eigenvalue of the target covariance matrices empirically lies between 10<sup>2</sup> and 10<sup>3</sup>).

See Fig. 28 for a comparison of style transfer with _K_=1 and _K_=3. Taking higher values of _K_ does not yield significant improvement in the results. Yet, for Fig. 28a, the sky is less uniform with _K_=1 and the bottom-left corner is more blurry. For Fig. 28c, the sky differs a bit between _K_=1 and _K_=3. In Fig. 29, we illustrate some gradient descent iterations, and observe the progressive refinement of the stylisation. It appears that the colour correspondance is achieved quite early, with stylistic details appearing later in the optimisation.

## A.9.6 Texture Synthesis

Consider a (space-periodic) target texture \(u\in[0,1]^{h\times w\times C}\). Our objective is to produce a (space- periodic) texture \(x\in[0,1]^{H\times W\times C}\). To initialise, we sample a stationary Gaussian field \(Z\in\mathbb{R}^{H\times W\times C}\)<tbc>

x107
layer 1
0.0
layer 2
layer 3
-0.2
-0.4
-0.6
log-likelihood
-0.8
-1.0
-1.2
1
2
3
4
5
K

x107
layer 1
layer 2
layer 3
0
log-likelihood
-1
-2
1
2
3
4
5
K

x107
0.50
0.25
0.00
log-likelihood
-0.50
-0.75
layer 1
layer 2
layer 3
-1.00
1
2
3
4
5
K

x107
0.0
layer 1
layer 2
layer 3
-0.5
log-likelihood
-1.0
-1.5
-2.0
-2.5
1
2
3
4
5
K

(a) Eiffel Tower

(b) Tuebingen

(c) The Great Wave

(d) The Starry Night

Figure 27: Four images and their corresponding log-likelihood vs. _K_ plots, for VGG layers \(\ell\in\{1,\cdots,3\}\).

