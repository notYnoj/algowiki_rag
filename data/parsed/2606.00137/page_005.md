## 2.4. Physically Based Rendering and PBR Material Maps

Physically based rendering (PBR) aims to model light-material interaction using physically grounded scattering and transport principles, so that appearance remains predictable under changing illumination and viewpoints. In the rendering equation formulation \[Kaj86\], outgoing radiance is determined by emitted radiance together with incident radiance modulated by the surface scattering function. For opaque surfaces, this scattering is typically modeled by a _bidirectional reflectance distribution function_ (BRDF), and more generally by a BSDF when transmission is included \[PJH23, Vea97\]. The BRDF describes how incident light from one direction is reflected into another at a surface point \[NRH\*77\]. In modern PBR systems, this reflectance is commonly modeled using energy-conserving microfacet models \[CT81, Bur12, PJH23\]. This perspective distinguishes _geometry_ (shape and surface normals) from _material_ parameters that govern diffuse and specular response, Fresnel effects \[Sch94, BW99\], and the distribution of micro-surface orientations.

A single RGB texture is often treated as a "color" signal (_e.g._, diffuse/albedo) and may implicitly bake lighting, specular highlights, or other view-dependent effects, limiting relightability. In contrast, a PBR material is typically represented by a _set of texture maps_ in UV space that parameterize a shading model. Modern real- time pipelines commonly adopt a metallic-roughness parameterization (as in Khronos glITF), where `baseColor` serves as diffuse albedo for dielectrics (non-metals) and specular reflectance color for conductors (metals), while `metallic` and `roughness` control reflectance behavior and highlight sharpness \[Khrb, GA, Khra\]. Additional maps such as normal, ambient occlusion, emissive, and, in broader PBR workflows, height/displacement can further enrich appearance; optional extensions such as clearcoat, sheen, transmission, and volume provide additional control over layered and transmissive effects \[GA, Khrb\] (Fig. 6). We use _PBR material genera_<tbc>

<tbc>_tion_<tbc>

<tbc>to refer to methods that explicitly synthesize such multi-map material representations rather than only a single RGB texture.

Generating high-quality PBR materials is harder than predicting a single RGB texture because multiple channels must be both _individually plausible_ and _mutually consistent_. First, material maps are tightly coupled: normal detail should be consistent with roughness and specular response, and metallic regions should exhibit physically consistent baseColor/reflectance behavior \[Bur12, GA\]. Second, disentangling intrinsic material from illumination is ill- posed when supervision is limited to rendered RGB images, often causing "baked-in" shading artifacts that break under relighting. Third, real materials can be spatially varying and layered (paint/clearcoat, fabrics, skin/hair), and their appearance depends on the target shader and renderer conventions (color space, parameter ranges, map packing), making cross-system generalization nontrivial \[GA, Khrb\]. Finally, large-scale paired datasets of geometry with calibrated, multi-map ground-truth materials remain comparatively scarce relative to RGB imagery, complicating evaluation and often encouraging simplified supervision or incomplete material factorization \[DAD\*18\]. These issues motivate current research directions that incorporate geometry cues, multi-view consistency, priors from image generative models, and renderer-aware training to better support relightable, editable PBR materials.

## 2.5. Neural Network Paradigms

Many neural mesh texturing pipelines can be understood through a small set of recurring paradigms for representing and generating surface appearance. We briefly introduce these paradigms-- predicting textures or material maps in UV space, modeling appearance as a continuous function over the surface, and generating view-space images or latents that are later baked onto the mesh--as background for the methods surveyed in later sections.

## 2.5.1. Neural Fields

Neural fields, also referred to as coordinate-based neural representations, model signals as continuous functions of space, optionally extended with direction, time, or other conditioning variables, and parameterized by a neural network. Formally, a neural field is a function

\(f_\theta:\mathbb{R}^n\rightarrow\mathbb{R}^m\)

that maps a coordinate--such as a 3D point \(\mathbf{x}\in\mathbb{R}^3\) or a tuple (**x**,**d**) with \(\mathbf{d}\in\mathbb{S}^2\) (_i.e._, a unit vector in R<sup>3</sup>) denoting a viewing direction--to a value representing signed distance, occupancy, color, or material parameters \[XTS\*22\]. Unlike classical, explicitly sampled representations (_e.g._, images, voxel grids, or vertex- attached attributes on meshes), a neural field encodes content in network weights and can be queried at arbitrary spatial resolution. This formulation yields a compact, differentiable, and resolution- independent representation well suited to inverse problems from images \[MON\*19, PFS\*19\]. Neural fields can be optimized end- to-end from image supervision via differentiable rendering. Consequently, Neural Radiance Fields (NeRFs) instantiate this idea for view synthesis by learning a mapping<tbc>

\(f_\theta(\mathbf{x},\mathbf{d})\mapsto(\unknown,\mathbf{c}),\)

Leather
Cloth
Ceramic
Wood
Marble
Fire
Microfiber
Chromium

**Figure 6:** _Representative PBR materials rendered under identical geometry and lighting. Varying material map parameters (e.g., base color/albedo, roughness, metallic, normals, and emissive terms) yield distinct, relightable appearances such as leather, cloth, ceramic, wood, marble, microfiber, and chromium, illustrating how PBR materials extend beyond a single RGB texture. Figure reproduced from \[wol16\]._

