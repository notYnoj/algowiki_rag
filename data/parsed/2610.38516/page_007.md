<tbc>snaps the boundary to the wrong edge (BF<sub>2</sub> 0.002 in the limit). The WS layer is only as good as its edge costs, which argues for learning them.

### 4.3 Real images: a binary last layer

A small U-Net (32-64-128-256 channels) is trained for 30 epochs with Adam on PanNuke [18,17] (nucleus versus background, 256<sup>2</sup>, fold 1 for training, all 2523 patches of fold 2 for testing). Variants: the plain U-Net with binary cross-entropy (BCE), and a U-Net whose logits feed the WS layer as unaries, with edge costs from the image gradient or from a second head of the same network (two more output channels of its last 1\(\times\)1 convolution, through a sigmoid, averaged onto the edges). The WS layer is implemented as 20 unrolled PCG steps with _p_ annealed geometrically from 5 to 50 and the loss BCE on the WS layer output plus 0.5 BCE on the logits. The output of the WS layer is evaluated as trained, converged at the final _p_, and as the exact limit.

2 presents the outcome. A binary WS layer with learned costs is 0.01 IoU and 0.02 BF<sub>2</sub> below a thresholded U-Net in the unrolled mode and level with it in the implicit mode; the same holds on Oxford-IIIT Pet [30], with objects a hundred pixels across [1, §J]. Image-gradient costs are useless on photographs and on cell images alike, as their limit floods whole regions. The exact limit of the learned costs is however deployable at a cost of 0.05 IoU, with a better object-count error than the U-Net. Inside the trained model the WS layer does what it should (its own logits fragment into 350 components per patch where the

image
soft prediction
p=5
p=20
p=100
p=500
PW limit
ground truth
w0.05 wits 0 w0.1
w0.05 wits 0 w0.1
w0.1 wits 0 w0.1
w0.1 wits 0 w0.1

**Fig.1.** Simulated soft predictions (ground truth warped by up to 3 px, blurred over 4 px, soft logits) through the WS layer, \(\alpha=0.1,256^2\), noise 0.05; image edge on the true boundary (upper row) or 4 px away (lower row). Columns: image, soft prediction, _x<sup>p</sup>_ for _p_=5,20,100,500, the exact limit, ground truth. The thin protrusion is recovered; with the edge in the wrong place the layer snaps to it. The two lower rows repeat the scenes with noise 0.1.

