ever, quantitative recovery performance ( 2) reveals a shift in dynamics. While the NCA restores global patterns, fine-grained details often converge to alternative local configurations. This microscale divergence, reflected in the local SSIM and local LPIPS scores, explains why regenerated textures exhibit lower metric values than initial generations despite appearing perceptually seamless.

Ablation studies on damage scale ( 2, rows 1-3) show successful regeneration up to 25 px and robust generalization up to 35 px across diverse texture categories. Recovery is visually superior for irregular textures, where stochasticity masks structural variations. Beyond a 45 px threshold, regeneration becomes stochastic as damage exceeds the receptive field’s capacity for context inference, occasionally resulting in convergence to degraded steady states. Fig. 4 illustrates these outcomes, comparing successful 25 px recovery with a failed 35 px instance.

Grafting experiments demonstrate how textures can be generated and combined. Unlike interpolation, which blends textures to create a new one \[13\], grafting combines distinct textures onto a single surface.

We perform texture grafting using two distinct methods:

1. Method 1: Initializing with multiple genomes.<br>
This approach involves initializing a single NCA at timestamp _t_=0. Significantly, different genomes are assigned to specific spatial regions within this NCA. This allows distinct textural properties, dictated by their respective genomes, to emerge and interact from the very beginning of the evolution process.

2. Method 2: Patch transfer during evolution.<br>
In this method, we first evolve an NCA driven by a particular genome. At a specific timestamp during its evolution, a selected patch (a region of the texture) is extracted. This patch is then transferred and integrated into another NCA, which is being driven by a different genome. This technique enables dynamic blending or juxtaposition of textures evolved under separate rules.

It can be observed that because the combined automaton continues to evolve iteratively, the shape, location, and area of these patches naturally change over time, which in certain situations could constitute a disadvantage.

Fig. 5 illustrates six textures generated through grafting techniques. We observe that the automaton can develop patches of specific genomes. Moreover, we see a communion where the two or more genomes collide, forming a consistent boundary transition area of cells, whether visualized as a barrier (as seen in Fig. 5d) or a smooth transition (the other examples in Fig. 5). Nevertheless, the transition behavior between genomes remains consistent across the intersection line. The smoothness of the transition between boundaries can be clearly observed in Fig. 5e. As illustrated in Figs. 5d and 5f, the NCA successfully handles the grafting of multiple (in this case, three) distinct textures simultaneously.

While our model achieves seamless grafting, the textures exhibit a dynamic drift over time. In long-term simulations, "genomic competition" may cause one texture to encroach upon another due to asymmetric stability between genomes; the more robust attractor expands across the periodic domain (Fig. 5a, Fig. 6). These instabilities are significantly mitigated by increasing the texture dimension, as larger grids provide a spatial buffer of "pure" genomic states that anchors the textures and reduces boundary drift (Fig. 5e).

Reconstruction success at the transition zone depends heavily on the scale of damage. The NCA restores the graft<tbc>

\begin{tabular}{cccccc}
Patch & \multirow{2}{*}{GDM \(\downarrow\)} & \multicolumn{2}{c}{LPIPS \(\downarrow\)} & \multicolumn{2}{c}{SSIM \(\downarrow\)} \\
radius (px) & & global & local & global & local \\
\[5-15\] & 1.385 & 0.224 & 0.023 & 0.078 & 0.25 \\
\[15-25\] & 1.373 & 0.222 & 0.0312 & 0.075 & 0.25 \\
\[25-35\] & 1.472 & 0.241 & 0.072 & 0.071 & 0.255 \\
\[35-45\] & 1.643 & 0.278 & 0.068 & 0.078 & 0.294 \\
\[45-55\] & 1.945 & 0.330 & 0.070 & 0.069 & 0.329 \\
\end{tabular}

timestamp
99 Evolution
100 Damage
300 Recovery
500 Recovery

(a)
(b)
(c)
(d)
(e)
(f)

** 2**. Quantitative assessment of texture regeneration at step 500.

**Fig. 4**. Successful and unsuccessful regeneration of textures.

**Fig. 5**. Examples for grafted textures using multiple-texture NCAs.

