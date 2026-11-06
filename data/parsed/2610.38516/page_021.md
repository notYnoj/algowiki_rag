image 3xHxW
U-Net 32-64-128-256
logit 1xHxW
migmoid
threshold at 0.5
mask
instances
BCE loss
connected components
image 3xHxW
U-Net last 1x1 conv: 3 channels
image
image
migmoid, averaged onto h/v edges
ch. 1-2: edge maps, weights w e e pce
ch. 0: logit s
unaries
a 1 = (1 s)po
unaries
a 0 = (1 s)po
p annealed 5 50 during training
p
solutions (L(w) + diag(a +a1))x = a1 unrolled: K PCG steps implicit: to tolerance + adjoint
WS layer
p [0, 1
potentials xP E [0, 1
deployment: exact PW on the same weights (spanning forest, p = 0)
BCE on xP +0.5 BCE on s
gradients to the edge maps, the logit and a

(a) Plain U-Net: one logit, sigmoid, threshold; instances by connected components.

(b) Binary WS layer: a three-channel head gives the unaries and the edge costs; the layer solves the RW system at the annealed temperature _p_; the exact PW is the deployment option.

**Fig.3.** The pipelines of the binary experiments (Sect. 4.3).

