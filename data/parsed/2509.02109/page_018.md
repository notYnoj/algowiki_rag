<tbc>as the target texture. We then optimise a weighted sum of Mixture Losses over different scales in the patch space (we refer the reader to Appendix A.9.6 for a full explanation). When doing multi-scale synthesis, we simply choose to downscale the images by a factor 2_<sup>s</sup>_ for _s_ between 0 and _S_, so that the image downscaled by a factor 2_<sup>S</sup>_ has size at least \(16\times 16\). In our experiments, we choose to fit _K_=4 Gaussian components in our mixtures. As illustrated in Fig. 10, this corresponds (roughly) to the elbow of the model’s log-likelihood and gives more convincing results. As for patch sizes, notice that choosing a patch size of 1 amounts to optimising the colour intensities directly, i.e. performing standard colour transfer. In Fig. 11, we compare the results of taking \(4\times 4\) and \(8\times 8\) patches. The mono-scale variant is functional for simple textures, as presented in Appendix A.9.6. A strength of this approach is that it deals with multiple scales at once, whereas [LDD23; Hou+23] go through each scale successively. This provides a simpler approach that is less sensitive to the transition method between scales.

## Conclusion and Outlook

In this work, we have provided multiple strategies to differentiate the Expectation-Maximisation algorithm, and illustrated their use in several applications. The overall practical message is that when possible, the Warm-Start method is to be preferred, and when not applicable, the Automatic Differentiation method is a good off-the-shelf solution. A core limitation of our methods (and EM to a lesser extent) is the computational cost when the dimension is large: our applications were limited to _d_≈1000. For very high dimensional cases, one could consider sparse covariance representations such as [BC25; Szw+25]. While we recommend using fixed uniform GMM weights, learnable weights remain an option. Further numerical and algorithmic tweaks could be considered to avoid issues with local optima. Finally, we focused on Gaussian Mixtures, but any mixture with differentiable densities could be considered. Note that for a seamless extension, one still requires closed-form expressions for the E and M steps.

VGG-19 Encoder 64 (truncated)
Dimension Sample size
Content image (optimized)
X
128
256
1
2
3
Style image
S
95536
16384
262144
Z
Mixture Loss
(a) Model architecture
(b) Source im.
(c) Generated im.
(d) Style im.





x106
1.05
1.00
log-likelihood
0.95
1
2
3
4
5
6
7
8
9
10
K

Figure 9: Style transfer method inspired by [GEB15]: setup and example result.

(a) _K_=1 components

(b) _K_=4 components

(c) Log-likelihood of fit

Figure 10: Choosing the number of components _K_ for texture synthesis.

