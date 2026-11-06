# Example-Based Feature Painting on Textures

ANDREI-TIMOTEI ARDELEAN, Friedrich-Alexander-Universität Erlangen-Nürnberg, Germany<br> TIM WEYRICH, Friedrich-Alexander-Universität Erlangen-Nürnberg, Germany

In this work, we propose a system that covers the complete workflow for achieving controlled authoring and editing of textures that present distinctive local characteristics. These include various effects that change the surface appearance of materials, such as stains, tears, holes, abrasions, discoloration, and more. Such alterations are ubiquitous in nature, and including them in the synthesis process is crucial for generating realistic textures. We introduce a novel approach for creating textures with such blemishes, adopting a learning-based approach that leverages unlabeled examples. Our approach does not require manual annotations by the user; instead, it detects

the appearance-altering features through unsupervised anomaly detection. The various textural features are then automatically clustered into semantically coherent groups, which are used to guide the conditional generation of images. Our pipeline as a whole goes from a small image collection to a versatile generative model that enables the user to interactively create and paint features on textures of arbitrary size. Notably, the algorithms we introduce for diffusion-based editing and infinite stationary texture generation are generic and should prove useful in other contexts as well.<br> Project page: `reality.tf.fau.de/pub/ardelean2025examplebased.html`

Authors’ Contact Information: Andrei-Timotei Ardelean, Friedrich-Alexander- Universität Erlangen-Nürnberg, Erlangen, Germany, timotei.ardelean@fau.de; Tim Weyrich, Friedrich-Alexander-Universität Erlangen-Nürnberg, Erlangen, Germany, tim.weyrich@fau.de.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM 1557-7368/2025/12-ART183<br> https://doi.org/10.1145/3763301

CCS Concepts: • **Computing methodologies** \(\rightarrow\) **Texturing**; **Anomaly detection**; _Image segmentation_.

Additional Key Words and Phrases: Texture synthesis, Anomaly clustering, Conditioned generation

**ACM Reference Format:**

Andrei-Timotei Ardelean and Tim Weyrich. 2025. Example-Based Feature Painting on Textures. _ACM Trans. Graph._ 44, 6, Article 183 (December 2025), 24 pages. https://doi.org/10.1145/3763301



Fig. 1. Our method generates large textures with non-stationary features learned from a small number of images. The type and shape of the painted features can be freely controlled: the figure is the result of an interactive editing session (see supplementary video). The scene uses free 3D models from cgtrader.com.

