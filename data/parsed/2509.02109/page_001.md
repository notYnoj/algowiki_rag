# Differentiable Expectation-Maximisation and Applications to Gaussian Mixture Model Optimal Transport

Samuel Boïté<sup>∗</sup><sup>1</sup>, Eloi Tanguy<sup>∗</sup><sup>1</sup>, Julie Delon<sup>1</sup>, Agnès Desolneux<sup>2</sup>, and Rémi Flamary<sup>3</sup>

<sup>1</sup>Université Paris Cité, CNRS, MAP5, F-75006 Paris, France

<sup>2</sup>Centre Borelli, CNRS and ENS Paris-Saclay, F-91190 Gif-sur-Yvette, France

<sup>3</sup>CMAP, CNRS, Ecole Polytechnique, Institut Polytechnique de Paris

29th September 2025

\*: equal contribution.

**Abstract**

The Expectation-Maximisation (EM) algorithm is a central tool in statistics and machine learning, widely used for latent-variable models such as Gaussian Mixture Models (GMMs). Despite its ubiquity, EM is typically treated as a non-differentiable black box, preventing its integration into modern learning pipelines where end-to-end gradient propagation is essential. In this work, we present and compare several differentiation strategies for EM, from full automatic differentiation to approximate methods, assessing their accuracy and computational efficiency. As a key application, we leverage this differentiable EM in the computation of the Mixture Wasserstein distance MW<sub>2</sub> between GMMs, allowing MW<sub>2</sub> to be used as a differentiable loss in imaging and machine learning tasks. To complement our practical use of MW<sub>2</sub>, we contribute a novel stability result which provides theoretical justification for the use of MW<sub>2</sub> with EM, and also introduce a novel unbalanced variant of MW<sub>2</sub>. Numerical experiments on barycentre computation, colour and style transfer, image generation, and texture synthesis illustrate the versatility of the proposed approach in different settings.

** of Contents**

**1 Introduction 2**<tbc>

**2 Differentiation of the Expectation-Maximisation Algorithm 4**<tbc>

2.1 Main Ideas of the EM Algorithm ..... 4<tbc>

2.2 Fixed-Point tion and Differentiability ..... 5<tbc>

2.3 Gradient Computation Methods ..... 6<tbc>

**3 Gaussian Mixture Model Optimal Transport 8**<tbc>

3.1 Reminders on GMM-OT ..... 8<tbc>

3.2 Stability of MW\(_2^2\) With Respect to GMM Parameters ..... 9<tbc>

3.3 Minimisation of EM - MW\(_2^2\): Local Optima and Weight Fixing ..... 10<tbc>

3.4 Unbalanced GMM-OT ..... 11<tbc>

**4 Illustrations and Quantitative Study of Gradient Methods 12**<tbc>

4.1 Practical Implementation ..... 12<tbc>

4.2 Flow of EM - MW\(_2^2\) with Fixed Weights in 2D ..... 12<tbc>

4.3 Flow of EM - MW\(_2^2\) in 2D: Discussion on Uniform Weights ..... 13<tbc>

4.4 Stochastic EM - MW\(_2^2\) Flow with Fixed Weights ..... 14<tbc>

4.5 Quantitative Study of EM Convergence and Gradients ..... 14<tbc>

