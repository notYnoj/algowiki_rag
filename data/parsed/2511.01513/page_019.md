<tbc>transfer, and large texture generation. Alternatively, the generative task could be formulated as inpainting, to naturally support editing. While arbitrary-size texture generation could in this case be formulated as out-painting, it is not clear how the other capabilities could be obtained. For example, it is not trivial to enable feature transfer, or to ensure that the painted feature is consistent with the initial texture (see Fig. 12 and Fig. 10).

Another possible approach is to use an autoencoder or a VAE and encode the different types of features in latent space. A texture synthesis method that leverages this idea is TextureMixer \[Yu et al. 2019\]. This approach could potentially be used within our framework by using the pixel-level anomaly segmentation masks to extract the rare features in a format compatible with TextureMixer’s training process. Nevertheless, it is unclear to what extent such method can adapt to thin structures (such as cracks) or how it can be extended to support feature transfer.

Other generative approaches, such as autoregressive models or flow-matching could be similarly considered. In general, however, we consider it out of the scope of this paper to incorporate all these methods in our framework to evaluate their performance on the various capabilities. That being said, our choice of diffusion model is made without loss of generality within that category (spatially- conditioned diffusion models). Our system uses EDM \[Karras et al. 2022\] as the backbone for texture synthesis and editing; nonetheless, the proposed noise-mixing and noise-uniformization algorithms can be applied using virtually any diffusion model. In our experiments, we use EDM because we find it to strike a good balance between image quality and speed. In the following, we provide a quantitative comparison between EDM and two alternative diffusion models, namely Stable Diffusion (SD) \[Rombach et al. 2022\] and EDM2 \[Karras et al. 2024\]. In order to evaluate the image quality for a certain texture, we generate 100 images of the normal class and take 64 patches of size 128×128 from every image. In the same manner, we also extract patches from the real images without anomalies, which were not seen during training. Finally, the distribution of the generated and real patches are compared using the Fréchet Inception Distance (FID) \[Heusel et al. 2017\]. We evaluate the three different models and in  5. It can be seen that pretraining the models on the DTD \[Cimpoi et al. 2014\] dataset improves synthesis quality; however, rather surprisingly, Stable Diffusion performs worse despite its large scale pretraining. Note that we have experimented with both full-model fine-tuning and ControlNet \[Zhang et al. 2023\], and we observed superior performance with the later. We further evaluate the models ability to generate realistic prominent features on the textures in  6. As the number of anomalous patches in MVTec is very small, and all anomalous images have been used for training the diffusion models, it is unfeasible to use FID in this case. Therefore, we evaluate the models based on the ability of a segmentation network to correctly classify the generated features. We train a CNN on the MVTec ground-truth labels and generate a<tbc>

\begin{tabular}{cccccc}
Model (Acc \(\uparrow\)) & Tile & Carpet & Grid & Wood & Leather \\
SD + ControlNet & 92.34 & 48.99 & 41.22 & 95.72 & **98.27** \\
EDM2 & 94.40 & 93.86 & 90.58 & 95.49 & 86.82 \\
EDM & **96.63** & **97.94** & **91.66** & **96.17** & 97.84 \\
\end{tabular}

\begin{tabular}{ccc}
Method & Throughput (img/s) \(\uparrow\) & Latency (ms) \(\downarrow\) \\
SD + ControlNet & 0.8 & 2720 \\
EDM2 & **1.4** & 2430 \\
EDM & 1.3 & **982** \\
\end{tabular}

Input labels
Synthesis

Fig. 18. Additional results on feature-conditioned texture generation by our model.

6. Quantitative comparison of texture feature painting using different diffusion models; EDM and EDM2 were pretrained on DTD \[Cimpoi et al. 2014\]. The models are evaluated by the accuracy of a image-to-class segmentation network trained with ground-truth labels.

7. Timing of different diffusion models

