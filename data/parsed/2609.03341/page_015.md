<tbc>ically, we compare our deformation-aware canonical transfer (Eq. 13) against the naïve alternative that directly interpolates canonical neighbor positions using deformed-space attention weights (Eq. 11). Figure 7b shows that the naïve transfer leads to discontinuous UV jumps and visible texture drift/popping under non-rigid deformations, while our transfer better preserves correspondence and keeps texture edits attached.

### 6 Conclusion and Limitation

We presented PointGT, a representation based on PAPR that enables simultaneous editing of geometry and texture for point-based representations. PointGT successfully achieves this by learning a UV mapping which maps 3D points to a learned 2D texture map. To improve geometry accuracy, we introduced two novel geometry regularizers, which have been demonstrated to improve the geometry significantly. We also introduced a novel correspondence mechanism to maintain UV mapping under deformation, which has been demonstrated to be highly effective. Comparison with baselines showed that PointGT preserves texture edits under large deformations while the baseline exhibits artifacts and surface discontinuities. Furthermore, we showed that PointGT outperforms competitive baselines on novel view synthesis with a much smaller number of primitives. Our method currently relies on an optimization-based UV parameterization [20], which can struggle to produce clean and low-distortion charts for objects with complex topology, which we believe could be alleviated by learning-based UV- mapping methods [11,12] in the future.

### 7 Acknowledgments

This research was enabled in part by support provided by NSERC, the BC DRI Group, the Digital Research Alliance of Canada and the Canada CIFAR AI Chairs Program.

= 0
= 0.01
= 0.4

**Fig.8:** Learned UV mapping under different weights of the proposed distortion loss.

