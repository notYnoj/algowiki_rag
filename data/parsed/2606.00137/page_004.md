<tbc>tion can be increased (_e.g._, by using higher-resolution UV images) without altering the underlying geometry, allowing appearance fidelity to scale with available storage and bandwidth budgets.

While traditional pipelines represent appearance as one or more raster texture images in UV space (_e.g._, albedo/normal/roughness maps), some neural methods replace or augment these images with _learned_ representations. A representative example is _neural textures_--high-dimensional feature maps stored on a mesh (often still in UV space) and optimized jointly with a neural renderer, enabling the renderer to decode view-dependent appearance from learned features rather than directly from RGB texels [TZN19]. Other works represent texture implicitly as a continuous function over surface coordinates or 3D points (Sec. 2.5.1), but parameterization (UVs, seams, and chart layout) remains central whenever supervision or outputs are baked back into a 2D atlas.

Several alternatives to UV-based parameterization exist. _Per-face texturing_ (_e.g._, Ptex [BL08]) stores signals on individual faces without requiring a global UV layout, reducing seam management and atlas packing overhead, but it can introduce discontinuities when filtering across face boundaries. _Per-vertex colors_ are simple and compact, but the achievable detail is constrained by mesh resolution (vertex density) and connectivity (triangle distribution), and interpolation across faces can blur high-frequency signals [AHH\*18]. _Volumetric or procedural textures_ avoid UV maps entirely, but they introduce challenges in authoring, editing, and manual control. Consequently, in practice, UV-based parameterization remains the most portable representation across offline and real-time rendering pipelines and continues to serve as the standard substrate for current texture libraries and authoring workflows [YKSH19].

Parameterization itself is also an active research problem that can materially affect downstream texturing quality, since distortion, seam placement, and chart fragmentation can influence both downstream learning behavior and the visibility of seams after synthesis. Classical methods target conformality and distortion control (_e.g._, least-squares conformal maps [LPRM02], angle-based flattening [SLMB05], and boundary-first parameterization [SC17]), often coupled with seam optimization to reduce fold-overs and atlas fragmentation [LLC\*18]. More recently, learned and task-adaptive approaches have emerged that automate or adapt parameterization toward data-driven objectives [LL22, LAKH23, WWS\*25]: _Flatten Anything_ proposes an unsupervised neural architecture that learns free-boundary surface parameterizations and can adaptively infer reasonable cuts and UV boundaries even from unstructured surface samples [ZHWH24], while _Auto-Regressive Surface Cutting_ (SeamGPT) formulates seam generation as next-token prediction to produce semantically cleaner, less fragmented seam layouts for UV unwrapping [LCL\*25]. Such methods complement robust classical solvers by reducing manual charting effort and by producing atlases better matched to modern texturing pipelines.

For these reasons, this survey considers mesh parameterization a foundational step for neural 3D mesh texturing: it decouples geometry from appearance by defining a 2D signal domain in which textures are stored (as images or learned features), optimized or regularized during learning, and consumed by renderers [YKSH19, SSGH01, Wil83]. Given the breadth of mesh parameterization research, we limit our discussion to aspects most relevant to texture

representation and learning, and refer readers to dedicated surveys for a comprehensive overview [SPR06, HPS08, FH05].

## 2.3. Differentiable Mesh Rendering

Rendering converts a 3D scene into a 2D image by simulating what a camera would observe. Given a triangle mesh with associated materials and lighting, a forward rendering pipeline determines which surface points are visible and computes their appearance in the image. In rasterization-based rendering, mesh vertices are transformed from object space to camera space, projected onto the image plane, assembled into screen-space primitives, and resolved for visibility using a depth buffer [AHH\*18]. In ray- or path-traced rendering, rays are cast through the scene to determine visible surface points and their light transport interactions [PJH23]. The visible points are then shaded by evaluating a material model under incident illumination [Kaj86], while textures are sampled--with filtering to reduce aliasing--to provide spatially varying parameters such as color or roughness [PJH23]. The resulting pixel values are finally composited with a background (solid color, image, or environment map) and written to an output image or framebuffer.

Differentiable rendering makes parts of the rendering process amenable to gradient-based optimization, enabling end-to- end learning of geometry, materials, and textures from image supervision (Fig. 5). A central challenge is the discontinuities inherent to visibility and rasterization. Classical approaches address this by introducing differentiable approximations or surrogate gradients, as in OpenDR [LB14], or by reformulating rasterization to expose stable derivatives, as in Neural Mesh Renderer [KUH18], Soft Rasterizer [LLCL19], and analytical treatments such as DIB-R [CGL\*19]. In path-traced settings, differentiability is achieved via Monte Carlo estimators that handle visibility boundaries and other discontinuities [LADL18, LHJ19, ZMY\*20, PJH23]. These advances are embodied in modern research renderers and toolchains: Mitsuba 2/3 [NDVZJ19] with its Dr.Jit compiler [JSRV22] supports forward- and reverse-mode differentiation for full light transport, while rasterization-based back ends such as nvdiffrast [LHK\*20] and deep-learning libraries like PyTorch3D [RRN\*20] and Kaolin [JSL\*19] provide efficient GPU pipelines for differentiable rendering.

Forward Rendering Process
Inputs
Occlusion
Shading
Light Transport
3D-to-2D Perspective Projection
Visuality Parameters
Output Image
Material Parameters
Lighting
Input Image
Conting Parameters
Outputs
Differentiable Occlusion
Differentiable Shading
Differentiable Transport
Differentiable View Projection
Differentiable Rendering Process

**Figure 5:** _Differentiable rendering enables backpropagation of image-space losses through the rendering pipeline (occlusion, shading, light transport, and projection) to optimize scene parameters (geometry, materials, lighting, and viewpoint). Figure reproduced from [BN25]._

