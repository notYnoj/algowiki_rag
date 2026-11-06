## 3.1. Structural Guidance

Structural guidance provides geometric cues that inform the model about _where_ specific content should appear on the mesh. It does not define the artistic style of those elements, but helps ensure that generated textures remain consistent with the underlying geometry and part layout of the mesh. Because it is tied to the 3D surface, such guidance is often derived from the input mesh or from mesh-aligned intermediate representations. Regardless of model design or stylistic conditioning, many methods condition the generation process on structural information to avoid textures that conflict with geometry. Several forms of structural guidance have been explored, including geometric edges derived from mesh attributes (normals, depth, connectivity) [PWMAZ24] (Fig. 12), depth maps [RMA\*23,CSL\*23], normal maps [YHK\*24], canonical UV layouts of SMPL/SMPL-X human templates [LMR\*15, PCG\*19,LZT\*24], and silhouettes [YDPT21]. More generally, any representation that provides a correspondence between 3D surface regions and 2D texture locations can serve as structural guidance. The choice and integration of such cues usually depend on the task and model design.

## 3.2. Stylistic Guidance

Stylistic guidance defines _what_ the texture should look like-- its color palette, materials, patterns, or overall appearance-- independent of geometry. It specifies the desired appearance of the texture and is typically provided through an external conditioning signal, such as text, reference images, or exemplar textures. Texture generation can also proceed without such input, _i.e._, unconditionally, in which case the style of the output is drawn solely from the learned training distribution. Conversely, when conditioning is provided, the model is guided to match the specified stylistic attributes.

### 3.2.1. Unconditional Texture Generation

Unconditional texture generation produces textures without explicit stylistic guidance, instead sampling appearance from a learned distribution, typically from random noise or a latent code. In this setting, the model may still be conditioned on the mesh or other structural inputs, but it is not given user-specified appearance cues. Without such high-level conditioning, specific attributes cannot be directly controlled; however, varying the random seed or latent input allows diverse sampling from the learned distribution, with limited control possible through latent-space manipulations, as in 2D GANs [KLA19,KLA\*20] (Fig. 13).

The main advantage of unconditional generation is its simplicity and ability to produce diverse textures without user input. However, the absence of explicit appearance control is a major limitation, making it less practical when a specific target style is required. On the positive side, unconditional generation is often relatively straightforward to integrate, since randomness can be introduced through latent or noise inputs without requiring additional conditioning signals.

### 3.2.2. Conditional Texture Generation

Conditional texture generation provides explicit control over the style or appearance of the output through additional input cues. The model receives external conditioning signals that specify the desired texture and uses them to guide generation. Stylistic guidance can take various forms--such as text, reference images, exemplar textures, or textured 3D assets. Conditioning greatly expands user control and broadens the range of possible tasks (_e.g._, texture transfer, domain-specific texturing, and style interpolation), but also introduces challenges: the model must faithfully reproduce the specified style while maintaining coherence with the underlying mesh structure. The choice of conditioning modality often influences the model architecture, training strategy, and target applications.

Conditional texture generation is often evaluated along two dimensions: (_i_) the intrinsic quality and realism of the generated texture, and (_ii_) its faithfulness to the input guidance. High-quality textures that deviate from the prompt, or prompt-faithful results that lack realism, are both inadequate; achieving both plausibility and guidance adherence remains a central goal of conditional methods.

Input Mesh (M) Mesh Depth Edge Map (Iedge) Texture Image (Itex) Textured View from Depth Textured View from Edges

Learn Joint Texture Distribution Infer Texture for Input Shape Texturify 3D Shape Distribution Real Images Input Shape Generated Texture Proposals on Input Shape

**Figure 12:** _Depth vs. edges for structural guidance. Depth maps are typically smooth and provide coarse structural cues. In contrast, geometric edges derived from mesh attributes (e.g., normals, depth discontinuities, and connectivity) are more detailed and aligned with mesh geometry, improving mesh–texture consistency. Figure reproduced from [PWMAZ24]._

**Figure 13:** _Unconditional texture generation with Texturify. The model learns a distribution of plausible textures conditioned on 3D shape from real-image supervision, and infers diverse texture proposals for a given input shape. Figure reproduced from [STM\*22]._

