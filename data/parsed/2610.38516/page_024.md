<tbc>and every pixel takes the label of its largest probability _x<sup>k</sup>_. During training the same solve is differentiated, the loss being the per-pixel cross-entropy of the label probabilities against the instance map (seam pixels weighted six times), added to the three direct losses above; _p_ is annealed from 5 to 20. The training markers are the ground-truth nuclei eroded by 2-3 px for the first ten epochs, then a mix, and the model’s own extracted markers from epoch 15; nuclei that receive no marker are given to the background label in the loss, as they would be at test time. The extraction is thus inside the training loop but outside the gradient: the solve’s gradient reaches the edge-cost channels through _w_ and the foreground channel through the unaries _a<sup>k</sup>=s<sup>p</sup>_ and _a_<sup>0</sup>=(1-_s)<sup>p</sup>_, never the distance channel, which learns only from its own squared error. A variant that puts the selection in the gradient path (every regional maximum above _t_=0.1 a candidate, with a strength \(\sigma_k\) computed from the mean distance logit over the candidate by a sigmoid with learned offset and temperature, entering as \(a^k=(\sigma_ks)^p\), duplicates and background candidates pushed towards zero strength by the cross-entropy) lost 0.063 F<sub>1</sub> and 0.048 PQ against this recipe on fold 2: the strengths barely separated true from spurious candidates, and the gradient reaching the distance channel doubled the share of unmarked nuclei (26% against 12.7%; extended report, Sect. 14).

The baseline’s tuning picks a high threshold: it misses a fifth of the nuclei but keeps spurious markers rare, because its watershed turns every marker inside the foreground into an object. The WS layer’s tuning picks a low one: it detects more nuclei and lets its solve, trained on such markers, absorb the spurious ones. An extended grid (_t_ from 0.4 to 0.7) gives the baseline the same choice; the WS layer’s _t_=0.2 is the lowest value of its grid, and for the earlier distance-head model of the record an extended grid down to _t_=0.1 still chose 0.2.

## Separating the markers from the final step.

To compare the two final steps with everything else held fixed, and in particular without any HoVer-Net-style post-processing on the WS layer’s side, the two models were crossed ( 5): each model’s markers through each final step, all on fold 2.

Three things follow. First, given the WS layer’s own markers and its own output foreground, a plain marker watershed reproduces the WS layer to three<tbc>

\begin{tabular}{ccc}
 & U-Net + marker watershed & U-Net + WS layer \\
grid searched (_t / a / h_) & 0.1-0.5 / 4, 9, 16 / 0.1-0.3 & 0.2-0.7 / 1, 4, 9, 16 / 0.05-0.2 \\
chosen _t_, _a_, _h_ & 0.5, 4, 0.2 & 0.2, 4, 0.2 \\
final step & watershed of _c-d_ in {_s\>_0.5} & multi-marker RW, _p_=20 \\
markers: one / none / several & 76.6 / 21.8 / 1.6% & 85.5 / 12.7 / 1.8% \\
background markers per patch & 1.6 & 4.3 \\
\end{tabular}

** 4.** Marker extraction chosen on fold 3, and the markers it produces on fold 2. "One / none / several": the fraction of ground-truth nuclei covered by exactly one, no, or several markers; "background": markers per patch that touch no nucleus.

