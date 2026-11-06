<tbc>this experiment uses a setting favorable to BlindLCA; that is, we excluded images that contain more than a single anomaly type per image. Nonetheless, our approach consistently yields better metrics.

## S11 Discussion on the choice of generative model

Our feature painting framework is composed of several components that work together to enable the authoring and editing of<tbc>

<tbc>textures with prominent features, which are learned from a small number of images. The generative model is the component that links the anomaly segmentation to the various desired capabilities of the system (see points 2-4 in the introduction). We choose to pose the generation as an image-to-image translation task (spatial labels to texture) using a diffusion model, and combine it with our noise-mixing and noise-uniformization to facilitate editing, feature<tbc>

\begin{tabular}{ccccccc}
**Texture** & \multicolumn{3}{c}{**Ours**} & \multicolumn{3}{c}{**BlindLCA**} \\
 & Acc. \(\uparrow\) & IoU \(\uparrow\) & F1 \(\uparrow\) & Acc. \(\uparrow\) & IoU \(\uparrow\) & F1 \(\uparrow\) \\
Tile & **0.97** & **0.70** & **0.80** & 0.96 & 0.54 & 0.67 \\
Wood & 0.96 & **0.48** & **0.56** & **0.97** & 0.41 & 0.50 \\
Leather & **0.99** & **0.47** & **0.57** & 0.99 & 0.39 & 0.50 \\
Carpet & **0.99** & **0.42** & **0.53** & 0.99 & 0.39 & 0.49 \\
Grid & **0.98** & **0.30** & **0.38** & 0.53 & 0.17 & 0.25 \\
\end{tabular}

\begin{tabular}{cccccc}
Model (FID \(\downarrow\)) & Tile & Carpet & Grid & Wood & Leather \\
SD + ControlNet & 95.76 & 166.52 & 162.45 & 81.14 & 102.86 \\
EDM2 & 41.60 & 132.12 & 125.70 & 38.67 & 126.05 \\
EDM2 + DTD & 46.23 & 88.31 & 92.69 & 34.24 & 103.33 \\
EDM + DTD & 50.04 & 57.14 & 81.82 & 68.29 & 105.88 \\
\end{tabular}



Fig. 17. Visualization of the generated tiled textures starting from white noise (left column) and our noise-uniformization method (right column). The multi-diffusion synthesizes tileable textures of 2048\(\times\)2048, which are then tiled to form 4096\(\times\)4096 images.

4. Detailed quantitative results and comparison.

5. Quantitative comparison of texture synthesis with different diffusion models. "+ DTD" denotes that the model was pretrained using the DTD \[Cimpoi et al. 2014\] textures dataset.

