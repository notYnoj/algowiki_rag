<tbc>too bright, or overly uniform in color. We then compute perceptual scores for these six views and sort the data accordingly, removing the bottom 20% of lowest-ranked samples. _(2) Single-surface Filtering_: We render 6 canonical-view Canonical Coordinate Maps (CCM) \[77, 37\] to detect single- surface geometry. Specifically, we check whether corresponding pixels on opposite views map to the same 3D point. If the ratio of such pixel matches exceeds a threshold, the object is classified as single-surfaced. _(3) Small Object Filtering_: We filter out data where the target object occupies too small an area in frontal views. This occurs in two scenarios: improper object orientation (e.g., a supine human where only feet are visible in front view), or distant objects in multi-object scenes that become too small after normalization. Specifically, we calculate the percentage of valid alpha-channel pixels in frontal views and discard samples with less than 10% pixels coverage. _(4) Transparent Object Filtering_: We exclude objects with transparent materials, as they are typically modeled using alpha-channel planes (e.g., for tree leaves). These transparent surfaces cause misalignment between rendered RGB images and actual geometry, adversely affecting model training. Our filtering method detects and removes assets whose Principled BSDF shaders contain alpha channels. _(5) Wrong Normal Filtering_: We identify and remove data with incorrect normals, which would otherwise create holes during watertight conversion. Our method renders 6-view normal maps in camera space and detects erroneous normals by checking whether any normal vectors form obtuse angles with their corresponding camera position. _(6) Name and Mesh Type Filtering_: We also filter out data labeled as point clouds by name or mesh type, as these scan-derived datasets typically contain noisy geometry and are difficult to convert into watertight meshes.

## Enhanced mesh-to-SDF

Training a Shape VAE \[91, 9\] requires watertight mesh to enable the extraction of SDF (Signed Distance Function) field from the processed meshes, which serve as geometric supervision \[92\]. CLAY \[92\] introduced a "visibility check" method for Mesh-to-SDF conversion, which first splits the space into _N_<sup>3</sup> grids. Each grid center checks the visibility using depth test and utilizes a mask with size _N_<sup>3</sup> to indicate whether the grid is considered invisible. However, for the non-manifold objects with holes, like the windows on the wall, it is easy to encounter floaters inside the converted mesh. To address this challenge, we implement a robust classification scheme by incorporating the concept of the winding number \[53\] as in CraftsMan3D \[38\], which is an effective tool for determining whether points are inside or outside a shape. For each point sampled within the voxel grid, we compute its generalized winding number<sup>1</sup>, considering points with values above our empirically determined threshold of 0.75. The resulting winding number mask is then combined with the original visibility test through logical conjunction to generate the final occupancy mask for MarchingCubes \[50\]. Experimental results as show in Fig. 3 (b) demonstrate this approach achieves a 20% watertight conversion success rate improvement on the Objaveverse dataset \[18\].

## Training Data Conversion

(1) Data for VAE: Following the Dora \[9\], we employ the Sharp Edge Sampling (SES) strategy to enhance point sampling in geometrically salient regions. Specifically, we combine uniformly sampled points _P<sub>uniform</sub>_ with additional points _P<sub>a</sub>_ sampled from salient areas,<tbc>

<sup>1</sup>https://libigl.github.io/tutorial/#generalized-winding-number

Web Captured 3D Assets
Single Texture Filtering
Single Surface Filtering
Small Objects Filtering
Step1X-3D
Vis. Check
-1,200k
-90k
-380k
5,000k+
Dark
Single Surf
Orientation
Watertight
Watertight
Uniform
Single Surf
Low Score
Single Surf
Scale
79.20%
Filtered 3D Assets
Name and Mesh Type Filtering
Wrong Normal Filtering
Transparent Objects Filtering
Success Rate
72.40%
-990k
-340k
-300k
62.80%
2,000k+
PCD
Angle > 90'
Transparent
Step1X-3D
Vis. Check
Vis. Check
PCD
Angle > 90'
Transparent
(a) Data Filtering Scheduler
(b) Mesh to SDF Process

Figure 3: **Data curation pipeline**. (a) we filter bad quality data from web captured 3D assets (_e.g._, Objaveverse, ABO, Thingiverse, and self-collected assets). (b) improved conversion rate of mesh-to-SDF.

