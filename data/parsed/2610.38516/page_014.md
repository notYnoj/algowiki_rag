## A Questions a reader may ask

The main text had to be short. This section answers, in order, the questions that the authors and their reviewers asked while writing it, with pointers to where the evidence is.

### What is the WS layer, in one sentence?

A seeded Random Walker at a finite inverse temperature _p_, with unaries, whose edge costs and unaries are produced by the network, trained through, and whose \(p\rightarrow\infty\) limit is the Power Watershed of the same costs. At the temperature it is trained at, its partition between markers is a marker watershed of its learned contour map (Appendix D,  5: identical to three digits on 2523 patches). The finite temperature adds one thing a watershed does not have: the solve can hedge, i.e. discount a weak marker through the soft unaries and share contested pixels between neighbours.

### A post-hoc marker watershed also turns a U-Net into an instance segmenter with any number of labels.

_What is new?_ Where the partition happens. In HoVer- Net-style pipelines the watershed runs after training, on maps the network was trained to predict; the loss never sees the partition. In the WS layer the partition over a per-image label set is a layer of the network, and the cross-entropy over that label set trains the edge costs, the foreground and the marker attachments through the solve (Sect. 4.4). Two properties of the (_p,q_) family make this cheap: the Random Walker’s cost is affine in the number of labels (one shared matrix, one right-hand side per label), and the limit is one spanning forest whatever that number (Sect. 3), where graph cuts are exact for two labels only. The number of labels is set per image by the markers, not by the output layout. The markers themselves remain a discrete step; see below.

### The baseline’s watershed is "tuned".

_Does that mean a second training?_ No: a grid search over a few scalars on 300 patches of a held-out fold (fold 3, used neither for training nor for testing), scored by PQ, five minutes in all. The baseline has four choices (marker threshold, minimum marker area, prominence of the distance maxima, and the relief: the contour map, the negative distance map or their sum; 135 settings). The WS layer’s marker extraction is chosen the same way with the first three (72 settings); its _p_ schedule is fixed. So the honest contrast is not "end to end versus tuned": both pipelines tune how markers are read off the distance map; only the baseline also tunes the assignment step, which the WS layer learns (Appendix D). The tuning stage is where the baseline is brittle: at a tenth of the training data its grid search picks a high marker threshold and leaves a quarter of the nuclei unmarked, while the WS layer keeps a permissive threshold at every data size because its trained solve absorbs the spurious markers (Appendix E).

### "The same network": is the baseline’s U-Net trained the same way?

Same architecture, same three output heads, same targets and training recipe, without the solve in the loop. The baseline U-Net predicts a foreground logit (cross-entropy against the binary nucleus mask), a two-channel contour map (the edge target:

