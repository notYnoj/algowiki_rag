<tbc>computed from the feature maps following the formulation in [8], and the optimization is carried out using the L-BFGS (Limited-memory BFGS) algorithm [15].

The feature representations between the input image and the exemplar images at a given network layer are based on feature map activations denoted by \(F_{ab}^l\), where \(F_{ab}^l\) is the activation of the _a_-th filter at spatial position _b_ in layer _l_. As described in [8], this formulation enables the model to capture patterns where individual spatial positions are interpreted as instances of a more general feature representation. Formally, the feature maps at layer _l_ can be arranged into a matrix \(F^l\in\mathbb{R}^{N^l\times K^l}\), where _N<sup>l</sup>_ is the number of filters and _K<sup>l</sup>_ is the flattened spatial dimensionality of each feature map. However, in our setting we are not primarily interested in exact spatial correspondences, but rather in style similarity so that damaged texture regions can be plausibly restored. Consequently, raw feature maps are insufficient, and Gram matrices must be employed to capture spatially invariant second-order statistics of the features. A Gram matrix is defined as:

\(G_{ab}^l=\sum_iF_{ai}^lF_{bi}^l\) (1)

As a consequence, for each exemplar the corresponding part of the loss function is defined as:

\(L_{exemplar_i}(I_{damaged},I_{exemplar_i})=\frac{1}{4(N^l)^2(K^l)^2}\sum\left(G_{damaged}^l-G_{exemplar_i}^l\right)^2\) (2)

where _I<sub>damaged</sub>_ is the inscription texture to be recovered and _I<sub>exemplar<sub>i</sub></sub>_ is one of the exemplar textures. On each layer we keep the minimum loss value \(L_l^\mathrm{Min}\) where _l_ symbolizes the _l_-th contributory layer along all pairs of degraded inscription and training exemplars (in Figure 3 each layer’s final loss value is noted as the sum minimized over all candidates _L_<sub>exemplar<sub>_i_</sub></sub>) and Layer loss is calculated as:

\(L_l^\mathrm{Min}=\mathrm{min}_l^EL_{\mathrm{exemplar}_i}(I_\mathrm{damaged},I_{\mathrm{exemplar}_i}).\) (3)

where _E_ is the number of exemplars for which we calculate all _L_<sub>exemplar<sub>_i_</sub></sub>. Then the total loss function is formulated as:

\(L_{total}=\sum_l^{N_{all}}w_lL_l^\mathrm{Min}.\) (4)

where _N_<sub>all</sub> is the number of layers included in the loss and _w<sub>l</sub>_ is the weight associated with layer _l_.

Our method correlates feature maps from layers (see Figure 3) _layer_1_,AvgPool_1_,AvgPool_2_,AvgPool_3, and _AvgPool_4. We report experiments in Appendix A (see in particular Figure 22, which shows that, for inscription restoration, these layers contribute more to producing visually high-quality results. Each layer’s contribution to the loss is weighted by a corresponding factor; the procedure used to determine these weights is described in Subsection 3.3.

In Figure3 the MESA architecture is presented. For each layer contributing to the loss function, we compute the Gram matrices of both the input inscription texture and all training exemplars, using structurally identical network instances. In a second step, we evaluate the mean squared distance between the Gram matrices of the input and each exemplar, and we retain, for each layer, the minimum distance as that layer’s contribution to the main style loss. In this way, we encourage similar feature representations across the selected contributing network layers. The damaged image is fed to the first network instance in Figure 3, while the remaining instances receive the clean training exemplars, thereby forcing the network to minimize the discrepancy between the exemplars and the input image by replacing degraded texture regions.

