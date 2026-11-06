<tbc>thus reducing the time to about 1.5 seconds per edit. More details and high-resolution examples are included in the supplementary, S6.

### 4.2 Synthesizing materials

So far we have described our approach and demonstrated its capabilities in terms of plain RGB textures. All our components, however, easily extend to other modalities, such as material maps for synthesizing SVBRDFs. We include in Fig. 11 a simple example, where the input data consists of a single SVBRDF, captured with a smartphone using MaterialGAN [Guo et al. 2020].

## 5 Ablations

We ablate our thresholding method, described in Eq. (1), and our stratified selection of negative pairs for contrastive learning. The results of this experiment are summarized in  1 and show that the introduced mechanisms are vital for an accurate segmentation.

Our noise-mixing technique is ablated in Fig. 12, by comparing our method with two variants. In the first case, we simply use the inverted noise as input for the diffusion model with the new conditioning map **_c_**. In the second, we also constrain the latents outside the edit to perfectly match the original image. Both variants unfavorably alter the texture beyond the desired edit. Additionally, we include in the suppl. material (S11) a discussion of our choice of diffusion model used as backbone for the feature painting.

## 6 Limitations

Naturally, the realism of the generated results depends on the plausibility of the input mask. Fig. 19 in the supplementary shows an exhaustive combination of input masks and generated texture features, demonstrating the versatility, but also limitations of the method. Overall, we believe that it shows that our method still extrapolates commendably beyond the mask shapes observed during training. A different limitation is that our pipeline is not end-to-end trainable, meaning that imperfect segmentations from our automatic feature clustering can cause different features to be mapped to the same label. In practice, this causes the model to _choose_ what feature is being painted based on the shape of the conditioning label. Finally, while our method has fast inference times, training the diffusion model for a new texture class can take 6 to 12 hours.

## 7 Conclusion

Our framework learns and disentangles the stationary characteristics from the prominent features given only a small collection of textures. After training, we are able to generate tileable textures of arbitrary size and to paint features on similar and dissimilar images with realistic transitions. These functionalities are bundled in a single model that can be controlled interactively for iterative authoring. While the main focus of our work is asset creation, the utility of the method extends to various areas, such as, image augmentations, long-tail image generation, and generating fake anomalies for self- supervised anomaly detection. Moreover, our editing method and noise uniformization algorithm can be leveraged in more general contexts, as shown in S2 (supplementary material).

## Acknowledgments

This project has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Sklodowska-Curie grant agreement No 956585.

\begin{tabular}{cccc}
 & Accuracy \(\uparrow\) & IoU \(\uparrow\) & F1-score \(\uparrow\) \\
Ours w/o equation (1) & 0.963 & 0.320 & 0.407 \\
Ours w/o stratified negatives & 0.794 & 0.367 & 0.451 \\
Ours & **0.978** & **0.473** & **0.566** \\
\end{tabular}

Input
Output

Original
Mask
Inv + **c**
Forced + **c**
Ours

Fig. 11. Synthesizing new material maps using our pipeline from a single SVBRDF. Please see the supplementary GIF for a high-resolution rendering.

Fig. 12. Ablation of noise-mixing. Note that our edit better preserves the structure of the original texture, while maintaining the realism of the feature.

1. Ablation of our feature detection and clustering components. Metrics are computed under optimal matching to the ground-truth classes.

