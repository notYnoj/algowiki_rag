## Decision Tree Learning for CEGIS-Based Termination Analysis: a Challenge

In this paper, we represent piecewise affine functions (1) by the data structure of _decision trees_. The data structure suits the CEGIS architecture (Fig. 1): iterative refinement of candidate solutions can be naturally expressed by growing decision trees. The main challenge of this paper is the design of an effective synthesizer for decision trees--such a synthesizer _learns_ decision trees from examples.

In fact, decision tree learning in the CEGIS architecture has already been actively pursued, for the synthesis of _invariants_ as opposed to ranking functions \[12,14,18,22,35\]. It is therefore a natural idea to adapt the decision tree learning algorithms used there, from invariants to ranking functions. However, we find that a naive adaptation of those algorithms for invariants does not suffice: they are good at handling _state examples_ that appear in CEGIS for invariants; but they are not good at handling transition examples.

More specifically, when decision tree learning is applied to invariant synthesis (Fig. 2a), examples are given in the form of program states labeled as positive or negative. Decision trees are then built by iteratively selecting the best halfspaces--where "best" is in terms of some quality measures--until each leaf contains examples with the same label. One common quality measure used here is an information-theoretic notion of _information gain_.

We extend this from invariant synthesis to ranking function synthesis where examples are given by transitions instead of states (Fig. 2b). In this case, a major challenge is to cope with examples that cross a border of the current segmentation--such as the transition _e_<sub>4</sub> crossing the border _h_<sub>1</sub> in Fig. 2b. Our decision tree learning algorithm should handle such crossing examples, taking<tbc>

\begin{tabular}{ccc}
candidate space \\ example type & trace examples & transition examples \\
affine ranking functions & \[15,32\] & \[19\] \\
piecewise affine ranking functions & \[15,32\] & our method \\
\end{tabular}

e2
h1
e1
h1
e2
e1
e4
e5
e3
h2
e3
h1
h1
f1(x)
h2
+
h2
f2(x)
f3(x)
+
{e4 , e5
{e3
{e2}
{e3}
(a) For invariants
(b) For ranking functions

1: ranking function synthesis by CEGIS

Fig.2: Decision tree learning

