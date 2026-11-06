**5 Applications of Differentiable EM 16**<tbc>

5.1 Barycentre Flow in 2D ..... 16<tbc>

5.2 Colour Transfer ..... 16<tbc>

5.3 Neural Style Transfer ..... 17<tbc>

5.4 Texture Synthesis ..... 17<tbc>

**A Supplementary Material 26**<tbc>

A.1 Discussion on the Invertibility Assumption ..... 26<tbc>

A.2 Postponed Proofs ..... 27<tbc>

A.3 Specific GMMs Used in Section 3.2 and Section 4.5 ..... 27<tbc>

A.4 Discussion on Gradient Ground Truths ..... 28<tbc>

A.5 Numerical Comparison of Warm and Cold Initialisation ..... 29<tbc>

A.6 Explicit Differential Expressions ..... 30<tbc>

A.7 Local Minima in (GMM)-OT ..... 34<tbc>

A.8 Differentiating the Matrix Square Root ..... 42<tbc>

A.9 Experimental Details and Additional Results ..... 43

## 1 Introduction

The Expectation-Maximisation (EM) algorithm \[DLR77\] is a ubiquitous tool in statistics to fit mixture models on data \[BE94; End03; VH10; Ng13\]. Numerous variants of the EM algorithm have been proposed in the statistics and machine learning communities \[DH97; Fri98; FH02; CJJ05; GTG07; VR08; CM09; Cap11; SCR12; GVS17; ZAC21; Kim22\], and are the focus of various monographs \[MK07; MP00\]. From a theoretical standpoint, the EM algorithm is only known to converge under specific conditions \[Wu83; Boy83; MK07; XHM16\], and its behaviour is still not completely understood in full generality. In machine learning, Gaussian priors have been used for latent space representations \[Ras03; KW14; RMW14; HJA20\] with resounding success, while Gaussian Mixture Models (GMMs) are used more sparingly \[NB06; VM19; Yua+20\].

Beyond the difficulties of GMM estimation, the core challenge is that the EM algorithm is not easily integrated into end-to-end learning pipelines, as its differentiation with respect to the input data is not straightforward. Theoretical ties between the EM algorithm and an alternate minimisation of an energy involving Entropic Optimal Transport \[Cut13\] were recently highlighted \[RW18; Men+20; Die+24; VL25\]. To our knowledge, these connections do not provide insight into the differentiation of the EM algorithm. In this paper, we tackle the theory and practice of differentiating the EM algorithm, in the hope of sparking further research in this direction, beyond the various applications that we present.

### Why differentiate EM with respect to data?.

Surprisingly, while EM is well-known and extensively studied, the question of its differentiation seldom appears in the literature. To the best of our knowledge, the first work in this direction is \[Kim22\], which rewrites a Bayesian variant of EM which is related to the Optimal Transport Kernel Embedding \[Mia+21\]. Differentiating EM with respect to data allows one to include it as a layer in a neural network, as was explored in \[HSF18\]. Combined with a differentiable metric between mixtures (such as Optimal Transport), this enables the use of EM for a differentiable loss function between datasets. This would permit _supervised_ generative or feature learning tasks, for instance as generalisations of the non-supervised clustering technique proposed in \[AM25\].

Given its iterative nature, a natural approach to differentiating EM is with automatic differentiation \[Wen64; Lin70; RHW86; GW08\], which is a powerful method for complex optimisation problems. Since EM is a likelihood maximisation problem, the optimisation of the EM output is a "bi-level" problem. Numerous automatic differentiation methods for bi-level iterative minimisation were studied in \[Gil92; Bec94; Sha+19; MO20; BPV22; BPV24\]. Another approach to bi-level optimisation involving fixed-point problems is the _implicit method_ \[Lui+18; BKK19; LVD20; Bol+21; Blo+22;<tbc>

