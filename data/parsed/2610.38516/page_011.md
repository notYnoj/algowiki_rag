# The Power Watershed as a Differentiable Layer

<tbc>at moderate _p_. On learned costs the exact solution tends smoothly to the limit, but the costs are tuned to the training temperature: the instance model peaks there and loses 0.07 F<sub>1</sub> at the limit, the binary models lose 0.05 IoU while their instance scores improve, so the deployed solution needs to be the finite-_p_ solve. As a binary last layer, the WS layer is level with a thresholded U-Net. With the instances as labels its partition is, at the training temperature, a watershed of its learned costs between markers, and it matches the same network followed by a tuned marker watershed as baseline; every gain it showed was matched once the baseline received the same supervision. What the end-to-end training adds is hedging, which improves tolerance to imperfect markers and improves performance when annotations are scarce, at the price of some boundary precision and of no longer being able to use the limit. Marker extraction remains a discrete step: the partition loss rewards a marker for the pixels it takes, not for being a nucleus, and three attempts to learn the selection did not help. In future work, we will study the influence of weak or scribble supervision and markers learned without ground-truth instances, where a post-hoc watershed cannot compete, together with training regimes that reconcile the hedging with the limit, and 3D applications. We release the code and the complete experimental record, negative results included.

#### Acknowledgements.

Funding was provided by our respective institutions. In particular, the work of L. Najman was partially supported by Khalifa University of Science and Technology under Award No. KU-INT-FSU-2026-004-8471000027. Computing cluster access was provided by the Mésocentre Paris-Saclay. Anthropic’s Claude  assistant was used for running the experiments, early drafting and verifying the correctness of the article.

### References

