# The Power Watershed as a Differentiable Layer

33<tbc>

<tbc>reaches the limit’s labels at p = 100 for 53 CG iterations, \(|\Delta\text{I}|\) at p = 50 for 115, the rank at p = 50 for 259. On the natural image the rank and \(|\Delta\text{I}|\) get closer to the limit than the squared cost ever does (1-2 % of the free pixels at p = 100-200 against 4 % at p = 500) for about twice the iterations, but with the float64 reference already failing there. What the transforms do change is where the gradient dies: with the rank, 90 % of the gradient mass sits on 20 edges by p = 50, at the very p where the limit is first reached, while with the squared cost 6 000 edges still carry it at the corresponding point. So for annealing, the squared cost, which spends the dynamic range on the strong edges, is the better path: the limit is reached while the gradient is still alive. The rank normalisation keeps its other role, fixing the output distribution of a learned cost head so that p means the same thing on every image.

### I The WS layer as a tunable softmax (no training, 256<sup>2</sup>)

Simulated U-Net output: ground truth elastically displaced by up to 3 px, blurred (\(\sigma=4\) px), soft logits with smooth noise; four scenes \(\times\) noise \(\sigma\in\{0.05,0.1\}\times\{\text{image edge on the true boundary, image edge shifted by 4 px}\}\). Edge costs from the image, unaries \(\alpha(-\text{log s},-\text{log}(1-\text{s}))\), \(\alpha\in\{0.03,0.1,0.3,1\}\). Converged solves (implicit layer) for \(\text{p}\in[1,500]\), the exact limit, and truncated layers. Figures: `results/softmax/figures/`.

(BF<sub>2</sub> = boundary F-score at 2 px tolerance, computed against the ground truth.)

- **Crisper and more correct.** With \(\alpha\le 0.1\) and the image edge where the true boundary is, the WS layer turns a 0.96 boundary score into 1.00 at p = 200 and in the limit, with the thin protrusion that the soft prediction rounds off fully recovered (`examples.png`), and the output goes from mostly soft to binary. This is the "better, tunable softmax": p is the temperature, and sharpening is spatially coupled through the edges rather than per pixel.<tbc>

- **The unary scale is a real hyperparameter.** With \(\alpha=1\) the unaries of confident pixels compete with the noise edges, nothing attaches to a label before the whole image has merged, and both large p and the limit collapse to one label. In the trained setting the network sets this scale itself through the logit magnitude.<tbc>

**-** **The failure mode is as predicted.** When the true boundary is 4 px away from the image edge, \(\text{p}\le 10\) is harmless but larger p snaps the boundary to the wrong edge and the limit is poor (BF<sub>2</sub> 0.002 at \(\alpha=0.1\)). The WS layer is only as good as its edge costs, which argues for learning them.

\begin{tabular}{cccccccccc}
noise & image edge & \(\alpha\) & soft prediction & BF<sub>2</sub> & best p & BF<sub>2</sub> & at best p & soft pixels at best p & limit BF<sub>2</sub> & limit IoU \\
0.05 & aligned & 0.1 & 0.958 & 200 & **1.000** & 0.3 % & **1.000** & 1.000 & \\
0.05 & aligned & 1 & 0.958 & 50 & 0.954 & 21 % & 0.000 & 0.08 & \\
0.1 & aligned & 0.1 & 0.958 & 200 & 0.968 & 2.4 % & 0.870 & 0.966 & \\
0.05 & shifted 4 px & 0.1 & 0.963 & 1 & 0.959 & 100 % & 0.002 & 0.865 & \\
0.1 & shifted 4 px & 0.03 & 0.955 & 2 & 0.955 & 100 % & 0.688 & 0.920 & \\
\end{tabular}

