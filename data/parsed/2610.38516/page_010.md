<tbc>0.006-0.013 behind with isolated scorers [1, §S, U]). Finally, the exact limit of this model reaches only F<sub>1</sub> 0.724 and PQ 0.585. Solved exactly at increasing _p_, the same system traces the path: F<sub>1</sub> peaks at the training _p_=20 and falls monotonically to the limit, which the solve reaches by _p_≈500, while SQ stays at 0.81: a higher _p_ removes the hedging, discounted markers become objects again, and the count error rises from 0.18 to 0.27 (Appendix G). The model trained from true markers is the mirror image, within 0.006 F<sub>1</sub> of its limit but behind on its own markers ( 3): a deployable limit and tolerance to imperfect markers pulled in opposite directions in every schedule we tried.

## 5 Conclusion

The Random Walker at finite _p_ gives the Power Watershed a differentiable form that is exact rather than a surrogate: every _p_ yields a convex problem differentiated through one adjoint solve, the multi-label problem is exact at a cost affine in the number of labels and as \(p\rightarrow\infty\) the solution converges to that of the combinatorial algorithm. A conditioning study shows what this path costs: the solve and the gradient both degrade as _p_ grows, so training happens<tbc>

image
instances
marker map
layer, predicted markers
exact limit, same markers
layer, true markers
Fig.2.
PanNuke, 128-px crops around touching nuclei, the WS layer trained from its own markers. Columns: image, ground-truth instances, predicted marker map, the multi-marker WS layer’s partition from the predicted markers, the exact limit from the same markers, and the layer with the ground-truth markers (oracle). Label maps in random colours with black contours.

