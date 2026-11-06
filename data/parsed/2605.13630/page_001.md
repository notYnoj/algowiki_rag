TEXTURE REGENERATING AND GRAFTING USING GENOME-DRIVEN NEURAL CELLULAR AUTOMATA

_Mirela Magdalena Catrina, Ioana Cristina Plajer, Alexandra Băicoianu_

Transilvania University of Braşov, Faculty of Mathematics and Informatics <br>
29 Eroilor, 500036, Braşov, Romania

**ABSTRACT**

This study significantly advances multi-texture synthesis using Neural Cellular Automata (NCAs) by introducing a novel training methodology that enables robust self-regeneration of textures in damaged regions. This inherent healing mechanism, essential for dynamic and adaptive systems, extends beyond traditional computer graphics applications, highlighting the fundamental self-organizing properties of NCAs. Furthermore, we present a versatile grafting technique, enabling the seamless combination of distinct textures. This is achieved efficiently during the inference phase, without requiring specialized retraining, through precise initialization of the NCA’s genome channels. Our findings demonstrate the generation of high-quality, complex textures with fluid transitions, show- casing a powerful and efficient paradigm for dynamic texture composition and self-repair in autonomous systems.

**_Index Terms_--** Neural cellular automaton, genome coding, pooling strategy, regeneration, grafting.

## 1. INTRODUCTION

In the fields of computer graphics and broader image generation, texture synthesis occupies a key position. The goal of generating a texture that conforms to a specific spatial dimension while accurately reproducing a given pattern is a computationally demanding and intricate process. Consequently, a multitude of methodologies have been proposed to address this task. Moreover, transcending the singular objective of synthesis, the field faces more advanced challenges, specifically the restoration of distorted textures or the cohesive combination of multiple textures into a novel pattern. Within this work, we define texture grafting as the seamless integration of a textural segment into a broader textural context. This process entails embedding a selected region from one texture into another, ensuring visual coherence and continuity across the newly formed interface.

Historically, classical approaches to texture synthesis have relied on techniques such as Markov random fields [1, 2], wavelet-based decompositions [3], or more recently, image stitching algorithms [4]. However, the landscape of<tbc>

<tbc>texture synthesis has been significantly transformed in recent years by the emergence of machine learning-based approaches, which offer demonstrably superior visual fidelity and considerably greater flexibility. Notable examples include models grounded in classical Convolutional Neural Networks (CNN) [5], Generative Adversarial Networks (GAN) [6, 7], and Transformers [8]. In a broader sense, virtually any general-purpose image generation model [9] holds the potential to be adapted for the specific requirements of texture generation.

Despite the extensive and consistent research dedicated to basic texture synthesis, the specialized domains of texture regeneration, blending, and specifically grafting, remain significantly under-explored. It is highly probable that modern generative neural architectures could be effectively leveraged for these purposes by extending and refining existing strategies originally developed for general image synthesis.

While generative neural network models generally produce highly accurate and high-quality results, this performance is achieved at a significant cost in terms of computational power and training resources. In this context, Neural Cellular Automata (NCA) stand out as a promising alternative, offering a simpler and more efficient computational paradigm. Their inherent capabilities for local pattern generation, self-organization, and robust emergent behavior position them as a powerful tool, potentially alleviating the high resource demands associated with large-scale generative models. Significant progress in texture synthesis and regeneration has been achieved through NCA-based approaches in recent years, with notable contributions from works including [10, 11, 12]. The outcomes are highly promising, consistently showing substantially reduced computational costs.

A significant limitation inherent in most existing NCA approaches is the requirement for training a distinct automaton for each individual texture. Consequently, this design choice impedes seamless interpolation between textures and complicates grafting operations, often necessitating explicit stitching. In [13], is presented a novel NCA-based approach to texture synthesis that employs a genomic encoding embedded in a subset of the automaton’s cell channels. This genomic encoding enables a single NCA to be trained on multiple textures and facilitates smooth interpolation between them.

