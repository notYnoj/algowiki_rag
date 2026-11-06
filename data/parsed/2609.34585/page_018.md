<tbc>ing followed by self-relabeling (ours), and the suffixes "+ search", "+ sampler", and "+ evolution" name the objective-guided gradient search of T2T and Fast T2T, the RLSA sampler applied after COExpander, and the evolutionary loop of DDEA. U + search is Moco’s meta-optimizer loop. In  2, MCTS denotes the search of Fu et al. (2021) at the time limit of the respective codebase (Appendix D), and RRC, PRC, revisers, and conquer are the iterative neural reconstruction loops of LEHD, SIL, GLOP, and UDC.

**Reference solvers.** KaMIS, Concorde, and LKH-3 are listed with the CPU times reported by Qiu et al. (2022) and Fu et al. (2021), divided by the number of instances, and are not comparable with the GPU times of the other rows.

## F FULL ABLATIONS

7 lists every variant behind the findings of Section 3.5.

## G SELF-RELABELING DETAILS

Figure 5 traces the training labels of the runs of  3 over the epochs of self-relabeling.

**A decoder mismatch pitfall.** Relabeling with one-shot decoding produces the best one-shot model among all our checkpoints, but it inverts the benefit of sequential peeling. At the same training stage, the supervised model still gains 3 to 5 points from peeling, while the relabeled model loses 1 to 3. Our conjecture is that training toward the model’s own argmax sets makes scores mean "in my preferred set" rather than "safe in any near-optimal set", so top-score commitments strand later rounds. Relabeling and selecting checkpoints with the deployment decoder removes the inversion and gives our best MIS checkpoint, the one behind the rows of  1.

MIS ER-[700-800]
TSP-500
KaMIS labels 44.52
Self-relabel from scratch
Mean training label size (
44
Mean training label length (
18.0
41
17.5
38
17.0
35
Self-relabel continuation
LKH-3 labels 16.53
Self-relabel from scratch
32
16.5
0
2000
4000
6000
8000
10000
12000
0
500
1000
1500
2000
Self-relabeling epoch
Self-relabeling epoch

Figure 5: Training labels under self-relabeling, for the runs of  3. Mean size (MIS, left) or length (TSP-500, right) of the training labels against the epochs of self-relabeling, for the continuation of the supervised MIS checkpoint and for the label-free chains from random initialization. Vertical lines mark the warm-started stages of a chain. Each stage restarts its labels from the model’s own first pass, which produces the steps in the curves. The dotted line is the mean of the solver labels.

