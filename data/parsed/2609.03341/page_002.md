<tbc>modified at resolutions finer than the sizes of the reconstructed Gaussians, and editing geometry is difficult because it is not clear how to non-rigidly transform Gaussian primitives based on user manipulations.

Recent efforts to decouple appearance and geometry in Gaussian splatting have extended 3DGS to include either global [27] or per-primitive [3,16,18,22,23, 30] UV maps. However, these techniques are still unable to enable both geometry deformations and appearance editing. Learned global UV maps from 3D surface points to 2D UV coordinates are no longer valid after geometry deformations, and per-primitive UV maps have difficulties handling deformations that are finer than the size of the Gaussian primitives.

We focus on another point-based representation that uses attention to render a point cloud [2,14,31], which effectively avoids those limitations by modeling scenes as a collection of infinitesimal points with learned features. These methods render rays with a cross-attention mechanism between the ray and the _K_ points closest to the ray. This defines the aggregated feature of a ray as the interpolation of the features from those _K_ nearest points, which enables editing scene geometry since these interpolation weights are still valid after deformations of the scene points. While attention-based point representation is better suited for geometry editing than 3DGS [31], appearance editing is still challenging as it is not possible to locally edit textures by modifying the optimized point features.

In this paper, we propose PointGT, a representation that extends the attention- based point renderer PAPR [31] to enable simultaneous editing of geometry and appearance. Our key contributions are:

Multi-view Captures
Point Representation & UV Mapping
Simultaneous Geometry and Texture Editing

**Fig.1: Overview** Given multi-view captures (left), PointGT reconstructs a point- based 3D representation and learns a global UV mapping onto 2D charts (middle left). By maintaining a deformation-aware correspondence between canonical and deformed space, PointGT ensures persistent texture edits under non-rigid geometry changes. Users can simultaneously deform and retexture a reconstructed dress (top) or a real- world table (bottom), with geometry and appearance fully decoupled and editable.

