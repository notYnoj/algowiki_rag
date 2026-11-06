<tbc>**Text-based Generation.** Using natural language as guidance is one of the most popular and convenient ways to control 3D texture synthesis, owing to the accessibility of text as an interface. In text-guided texturing, a user provides a description (prompt) of the desired texture, and the model conditions generation on this input to produce a semantically matching result (Fig. 14). Text is typically incorporated via a pretrained encoder that converts the prompt into a conditioning representation, which is then injected into the generation pipeline. Many systems use vision-language models such as CLIP [R\*21] or dedicated text encoders like T5 [RSR\*20], which are usually pretrained on large text or image-text datasets and may either be used as is or fine-tuned for the task at hand.

Text guidance provides high-level, intuitive control, allowing users to specify abstract concepts and attributes that are otherwise difficult to quantify. Its drawback is ambiguity; text can be under- specified or open to multiple interpretations. Diffusion-based methods can help mitigate this, as large text-to-image models like Stable Diffusion [RBL\*22] are trained on vast datasets and can translate rich textual cues into detailed imagery. Leveraging such models allows text-guided 3D texturing to inherit this semantic knowledge.

**Image-based Generation.** Using an image example as guidance provides a more concrete and precise specification of texture style. Instead of describing the appearance in words, the user provides one or more reference images, and the model generates a texture that matches their visual characteristics. Such guidance can capture details that are difficult to express textually, _e.g._, specific patterns, artistic styles, or complex color gradients. In image-based texture generation, the reference image is typically encoded into a conditioning representation using a visual encoder [R\*21, SZ15], or incorporated through image-conditioning modules [YZL\*23], which then guide texture generation toward the desired style/appearance.

The advantage of image guidance lies in its specificity, meaning that it is generally less ambiguous than text. A reference image can convey fine texture details (for instance, the floral pattern on a dress or the wood grain of a chair) that would be tedious to describe verbally, making this a highly practical form of guidance.

**Textured 3D Shape-based Generation.** A more structured form of stylistic guidance uses a textured 3D shape, or a mesh-aligned appearance representation, to guide the texturing of another mesh. In this setting, appearance is specified directly in 3D or in an aligned surface domain, rather than through a text prompt or<tbc>

<tbc>a single reference image. Such guidance is particularly useful for tasks such as texture alignment and transfer across related shapes [CYF22], as well as generating variations of an existing textured asset and, in some cases, transferring learned appearance statistics to new geometries [MEM24].

Overall, using textured 3D shapes as guidance is less common than text or image inputs, mainly because such exemplars are relatively scarce and often task-specific. When available, however, they can provide detailed and geometrically aligned appearance information. Future systems may combine multiple forms of guidance, _e.g._, text prompts, reference images, and partial or complete 3D textures, to provide users with finer control over 3D texture creation.

## 4. Neural 3D Mesh Texturing

In this section, we review works on _Neural 3D Mesh Texturing_ and organize them according to recurring methodological families, while also reflecting the field’s evolution over time. We begin with foundational neural mesh texturing methods that laid the ground- work for later approaches by using differentiable rendering, weak 2D supervision, and adversarial learning to generate textures from limited 2D supervision. We then discuss optimization-based methods, which iteratively refine textures using pretrained priors such as vision-language or diffusion models. Finally, we review accelerated diffusion-based methods, which can be further categorized by inference-time strategy into iterative view-by-view pipelines, synchronized multi-view approaches, and feed-forward methods. This taxonomy reflects a trade-off space between quality, speed, and controllability, and highlights the evolution from slower but flexible optimization to more scalable generation while maintaining consistency across the 3D surface. We provide a summary of representative works in _Neural 3D Mesh Texturing_ in Tab. 1.

### 4.1. Foundational Neural Mesh Texturing

Early works on neural 3D mesh texturing demonstrated that neural networks can learn to synthesize realistic textures on 3D surfaces or in surface-aligned representations from limited or indirect supervision. Many of these methods rely on differentiable rendering to bridge the 2D-3D gap, often leveraging unpaired or weakly paired 2D images to learn how to assign realistic textures to 3D meshes. Broadly, these approaches can be grouped into image-driven texturing, texture super-resolution and completion, neural texture representations in function space, and adversarial or GAN-based synthesis pipelines.

**Image-driven Texture Transfer and Reconstruction.** _Photo- Shape_ [PRFS18] is an early large-scale effort in this direction, automatically assigning photorealistic appearance to collections of un- textured 3D shapes by mining product photographs and material exemplars. Its system retrieves images and materials with appearance similar to a target mesh and aligns them to the shape, enabling large-scale creation of textured ShapeNet-style [CFG\*15] assets. Around the same time, Kanazawa _et al._ [KTEM18] introduced a category-specific mesh predictor that jointly infers 3D geometry and a corresponding UV texture map from a single image via differentiable rendering, without relying on ground-truth 3D supervision. The model deforms a fixed template mesh with a shared<tbc>

"wooden barrel"
"metal CD player"
"orange backpack"
"bagel"
"briefcase"
"sci-fi metal helmet"
"golden Porsche"
"banana"
Meshes without textures
Generated textures with text prompts

**Figure 14:** _Text-conditioned texture generation. Given untextured meshes (left), Text2Tex synthesizes textures guided by text prompts (right). Figure reproduced from [CSL\*23]._

