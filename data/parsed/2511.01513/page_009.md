## 4.1 Editing results

To demonstrate the editing capabilities of our approach, we use anomaly-free images that were not seen during training - neither for the contrastive learning, nor for the diffusion model. We illustrate firstly the intermediate steps in our texture-editing method in Fig. 5. The resulting image is very close to the original texture outside of the edited region; as shown in the supplementary (Fig. 25), virtually all existing differences are caused by the limited capacity of the pretrained variational autoencoder from Stable Diffusion [Rombach et al. 2022]. Notably, thanks to our noise-mixing method, the edited region is integrated seamlessly in the texture, matching the previous appearance underneath the roughened region and at the boundaries. We include more editing results in Fig. 6.

Thanks to the seamless integration of the edited region, our noise- mixing lends itself to high-resolution editing at interactive rates (see video in the supplementary material). This is achieved by running the diffusion only for the texture patch that contains the feature label to be painted. To this end, we save the diffusion trajectory during generation or inversion and only use the slice of the noise estimates that corresponds to the edited patch. Saving the noise history for the diffusion process makes it possible to forego inversion for each edit,<tbc>

Labels
Feature reference
Image analogies
Gatys et al. [2016]
Wang et al. [2022b]
Zhou et al. [2023]
Chen et al. [2021a]
Ours

Native class
Non-native classes

Fig. 9. Qualitative comparison for label-conditioned texture generation.

Fig. 10. Feature transfer to real images of texture classes non-native to each feature. Due to the novel surrounding, cues on scale are missing, so feature scale may vary across transfers, particularly visible with the crack feature.

