<tbc>fashion. In particular, Wu et al. (2023) and Trippe et al. (2022) have done this for the single-motif case by conditioning on a fixed partial view of the protein backbone. However, while they have laid the foundation, their methods are not directly applicable in the event of multiple motifs, which is an important but challenging design task. Moreover, SMC-aided diffusion posterior samplers have not been sufficiently compared in the protein domain, where scaffolding tasks are severely ill-posed and high-dimensional but with solutions that can be quantitatively evaluated. We aim to address these concerns.

In this work, we make the following contributions:

• We propose a set of _guidance potentials_ for various scaffolding tasks. Notably, we explore alternatives to masking for guiding the denoising process. These potential functions permit a natural extension to scaffolding multiple motifs while having comparable, if not better, single-motif in-silico performance than masking. Additionally, we provide a potential function for developing monomers with possibly loose internal symmetries that achieves designability in the cyclic and dihedral case.<tbc>

• We provide a thorough comparison of recent SMC-aided diffusion posterior samplers on motif scaffolding. We identify their design choices, report their empirical costs, and compare them to a baseline in the bootstrap particle filter.<tbc>

• We demonstrate that it is possible to jointly scaffold multiple motifs in zero-shot by pairing a reconstruction guidance-based SMC sampler with one of our proposed potentials. We also point towards possible improvements in sampler efficiency for future research.

The rest of this paper is organised as follows. In Section 2, we introduce some background to our methods, namely inverse problems, diffusion posterior sampling, and motif scaffolding. We also briefly review relevant literature and existing methods in relation to our algorithms. In Section 3, we present our proposed potentials across several scaffolding tasks while highlighting the intuition behind them. In Section 4, we describe our experimental setup and elucidate our findings. Finally, we highlight limitations and future work in Section 5.

## 2 Background

### Inverse Problems.

Commonplace in many scientific disciplines, _inverse problems_ require estimating a latent quantity \(\mathbf{x}\in\mathbb{R}^D\) given its measurement \(\mathbf{y}\in\mathbb{R}^d\), an often ill-posed problem. Formally, we define it as<tbc>

\(\mathbf{y}=\mathcal{A}(\mathbf{x})+\mathbf{n},\) (1)

<tbc>for some possibly nonlinear measurement function \(\mathcal{A}:\mathbb{R}^D\rightarrow\mathbb{R}^d\) and noise \(\mathbf{n}\sim\mathcal{N}(\mathbf{0},\sigma_v^2\mathbf{I})\). Eq. (1) analogously defines a likelihood<tbc>

\(g(\mathbf{y}|\mathbf{x})\propto exp\left(-\frac{1}{2\sigma_v^2}\|\mathbf{y}-\mathcal{A}(\mathbf{x})\|^2\right),\)

<tbc>that we generally express in this work as

\(g(\mathbf{y}|\mathbf{x})\propto exp\left(-\eta\cdot L_\mathcal{A}(\mathbf{x};\mathbf{y})\right),\)

for some \(\eta>0\) and potential \(L_\mathcal{A}:\mathbb{R}^D\rightarrow\mathbb{R}\). We adopt this notation to define arbitrary potentials but remark that our formulations largely remain Gaussian. Conveniently, the composition of several inverse problem constraints can then be represented by summing together individual potentials. Because inverse problems are often underdetermined, we may assume access to a prior distribution on the latent variable _q_(**x**) and aim to sample from the posterior distribution _q_(**x**|**y**), which is given under Bayes’ rule as \(q(\mathbf{x}|\mathbf{y})\propto q(\mathbf{x})g(\mathbf{y}|\mathbf{x})\).

### Diffusion Models.

Diffusion models (Sohl-Dickstein et al., 2015; Song et al., 2020; Ho et al., 2020) are a class of generative models that learn the _time reversal_ of a diffusion process applied to a target distribution _q_(**x**<sub>0</sub>), the end result of which is a Gaussian _q_(**x**_<sub>T</sub>_)=N(**0**,**I**). This involves learning the _score_ function \(\nabla_{\mathbf{x}_t}logq(\mathbf{x}_t)\), an otherwise intractable quantity, by parameterising it with a neural network. The time reversal forms a bridge between a simple Gaussian and the target distribution, which permits sampling from the target by progressively moving Gaussian samples in the direction of the score. As such, trained diffusion models can be used as priors for complex data distributions and their associated inverse problems.

