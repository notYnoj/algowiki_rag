<tbc>our method on joint novel-view synthesis of RGB radiance and LSEG [33] 512- wide semantic features. Due to the limited resolution of LSEG feature maps, we render and predict at the RGB resolution, but bilinearly downsample the spatial dimension of the resulting feature maps in order to supervise on ground truth features. We compare against Feature 3DGS [82], a hybrid method relying on 128-wide semantic feature vector per primitive plus a CNN to jointly downsample the spatial dimension and upsample the feature dimension of the resulting rasterized image up to the full 512 dimensions, and another set of 48 SH basis weights for regular RGB color. Results for the aggregated MipNeRF360 dataset can be seen in Tab. 4. We afford Feature-3DGS twice our training time budget, up to 7K iterations, slightly more than in the original paper (5K), to accommodate for the larger-scale datasets. We further ablate the per-primitive feature dimensionality for this task in Tab. 8. Our results show substantial improvement over Feature 3DGS, and the capability to easily scale upwards or downwards in performance or memory, in a completely detached manner from the nature of the data being encoded. It is particularly interesting to note how small the drop in RGB quality is, which points to either high correlation among feature vectors or excessive free bandwidth in our RGB experiments. Our features can then be used in downstream tasks such as scene editing or semantic segmentation.

3DGUT-MCMC
Spherical Voronoi
Ours
Ground truth

**Fig.6:** Comparison between our and previous works on radiance field reconstruction on scenes from MipNeRF360 [2], Tanks and Temples [30]. Our method models high frequency detail and view dependent effects to a higher degree than previous works.

