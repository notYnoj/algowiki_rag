## What is shared.

Both models are the same U-Net (32-64-128-256 channels) with a four-channel last layer, trained with the same recipe: fold 1, 30 epochs, batch 16, the eight flips and rotations as augmentation, Adam with learning rate 10<sup>-3</sup> and cosine decay, one seed. The four channels and their direct supervision are identical:

- channel 0, the foreground logit, whose sigmoid _s_ is trained with a binary cross-entropy against the nucleus mask;<tbc>

**-** channels 1-2, the contour (or edge-cost) head, trained against the map of instance boundaries derived from the instance masks (the edge target of Sect. 4.3), seams between touching nuclei weighted five times;<tbc>

**-** channel 3, the distance head of Naylor et al. [28]: for every nucleus pixel the Chebyshev distance to the nucleus boundary, capped at 12 px and divided by the nucleus’s maximum, so that every nucleus peaks at 1; sigmoid output, squared error.

Test markers are extracted from the predicted distance map _d_ by the same procedure for both models:

1. seeds are the regional maxima of _d_ of prominence at least _h_ (the _h_-maxima), kept where _d\>t_, one seed per plateau;<tbc>

2. each seed is grown into a basin by a watershed of -_d_ inside {_d\>t_}, so that two touching nuclei whose maxima are separated by a valley deeper than _h_ get two markers even when the valley stays above _t_;<tbc>

3. basins smaller than _a_ pixels are dropped.

The result is a label map with one connected marker region per detected nucleus. The three parameters are chosen separately for each model by the panoptic quality of its final output on 300 evenly spaced patches of fold 3, which is used neither for training nor for testing. Both procedures are therefore identical; the markers are not, because each model predicts its own _d_ and has its own tuned parameters ( 4).

## The baseline’s final step.

A marker watershed (4-connected) of a relief _r_ from the markers, inside the foreground mask {_s\>_0.5}; foreground components that contain no marker are left unlabelled. The relief is chosen on fold 3 among the contour map _c_ (mean of the two contour channels), -_d_, and _c-d_; the choice hardly matters (PQ 0.654-0.655 on fold 2 for the three). This is the post-processing of HoVer-Net [22] applied to Naylor et al.’s distance map; it receives no gradient. Keeping the unmarked foreground components as extra instances lowers F<sub>1</sub> to 0.780 and PQ to 0.637 and raises AJI to 0.666, so they are dropped.

## The WS layer’s final step.

The multi-marker Random Walker of Sect. 3 at the final temperature _p_=20, solved to convergence: every marker region _k_ attaches its pixels to label _k_ with the unary _a<sup>k</sup>=s<sup>p</sup>_, the background label attaches every pixel with (1-_s)<sup>p</sup>_ (the costs -log_s_ and -log(1-_s_) clipped at 8), the edge weights are _e_<sup>-_pc<sub>e</sub>_</sup> with _c<sub>e</sub>_ the edge costs of channels 1-2 (times a learned scale),

