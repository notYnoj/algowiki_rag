1. Generate a set _H_ of halfspaces from the given set E of examples. This _H_ serves as the vocabulary for internal nodes. Set the initial segmentation to be the one-node tree (i.e. the trivial segmentation).<tbc>

2. Try to synthesize a piecewise affine ranking function _f_ for E with the current segmentation--that is, try to find suitable leaf labels. If found, then use this _f_ in a candidate well-founded relation \(R(\widetilde{x},\widetilde{x'})=f(\widetilde{x})>f(\widetilde{x'})\wedge f(\widetilde{x})\ge 0\).<tbc>

3. Otherwise, refine the current segmentation with some halfspace in _H_, and go to Step 2.

The key step of our synthesizer is Step 3. We show a few examples.

**Example 3.** Suppose we are given E={_R_(1,0)_,R_(-2,-1)} as a set of examples. Our synthesizer proceeds as follows: (1) Our synthesizer generates the set \(H:=\{x\ge 1,x\ge 0,x\ge-2,x\ge-1\}\) from the examples in E. (2) Our synthesizer tries to find a ranking function of the form _f(x_)=_ax+b_ (with the trivial segmentation), but there is no such ranking function. (3) Our synthesizer refines the current segmentation with \((x\ge 0)\in H\) because \(x\ge 0\) "looks good". (4) Our synthesizer tries to find a ranking function of the form \(f(x)=\text{\textbf{if}}x\ge 0\text{\textbf{then}}ax+b\text{\textbf{else}}cx+d\), using the current segmentation. Our synthesizer obtains \(f(x)=\text{\textbf{if}}x\ge 0\text{\textbf{then}}x\text{\textbf{else}}-x\) and use this _f(x_) for a candidate solution.

How can we decide which halfspace in _H_ "looks good"? We use _quality measure_ that is a value representing the quality of each halfspace and select the halfspace with the maximum quality measure.

Fig. 5 shows the comparison of the quality of \(x\ge 0\) and \(x\ge-2\) in this example. Intuitively, \(x\ge 0\) is better than \(x\ge-2\) because we can obtain a simple ranking function **if** \(x\ge 0\) **then** _x_ **else**-_x_ with \(x\ge 0\) (Fig. 5a) while we need further refinement of the segmentation with \(x\ge-2\) (Fig. 5b). In Sect. 5, we introduce a quality measure for halfspaces following this intuition.

Our synthesizer iteratively refines segmentations following this quality measure, until examples contained in each leaf of the decision tree admit an affine ranking function. This approach is inspired by the use of information gain in the decision tree learning for invariant synthesis.

Example 3 showed a natural extension of a decision tree learning method for invariant synthesis. However, this is not enough for transition examples, for the reasons of _explicit_ and _implicit cycles_. Here are their examples.

f(x)
-2
-1
0
1
2

-2
-1
0
1
2

(a) Good (\(x\ge 0\))

(b) Bad (\(x\ge-2\))

Fig.5: Selecting halfspaces. Transition examples are shown by red arrows. Boundaries of halfspaces are shown by dashed lines.

