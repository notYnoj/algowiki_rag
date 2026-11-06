<tbc>**Example 4.** Suppose we are given E={_R_(1,0)_,R_(0,1)}. In this case, there is no ranking function because E contains a cycle \(1\rightarrow 0\rightarrow 1\) witnessing non- termination. We call such a cycle an _explicit cycle_.

**Example 5.** Let E={_R_(-1,1)_,R_(1,0)_,R_(-1,-2)_,R_(2,3)} (Fig. 6). Our synthesizer proceeds as follows. (1) Our synthesizer generates the set \(H:=\{x\ge 1,x\ge 0,\dots\}\) of halfspaces. (2) Our synthesizer tries to find a ranking function of the form _f(x_)=_ax+b_ (with the trivial segmentation), but there is no such. (3) Our synthesizer refines the current segmentation with \((x\ge 1)\in H\) because \(x\ge 1\) "looks good" (i.e. is the best with respect to a quality measure).

We have reached the point where the naive extension of decision tree learning explained in Example 3 no longer works: although all constraints contained in each leaf of the decision tree admit an affine ranking function, there is no piecewise affine ranking function for E of the form _f(x_)=**if** \(x\ge 1\) **then** _ax+b_ **else** _cx+d_.

More specifically, in this example, the leaf representing \(x\ge 1\) contains _R_(2,3), and the other leaf representing \(\neg(x\ge 1)\) contains _R_(-1,-2). The example _R_(2,3) admits an affine ranking function _f_<sub>1</sub>(_x_)=-_x_+2, and _R_(-1,-2) admits _f_<sub>2</sub>(_x_)=_x_+1, respectively. However, the combination \(f(x)=\mathbf{if}x\ge 1\) **then** _f_<sub>1</sub>(_x_) **else** _f_<sub>2</sub>(_x_) is not a ranking function for E. Moreover, there is no ranking function for E of the form \(f(x)=\mathbf{if}x\ge 1\) **then** _ax+b_ **else** _cx+d_.

It is clear that this failure is caused by the _crossing examples R_(-1,1) and _R_(1,0). It is not that every crossing example is harmful. However, in this case, the set {_R_(-1,1)_,R_(1,0)} forms a cycle between the leaf for \(x\ge 1\) and the leaf for \(\neg(x\ge 1)\) (see Fig. 6). This "cycle" among leaves--in contrast to _explicit_ cycles such as {_R_(1,0)_,R_(0,1)} in Example 4--is called an _implicit cycle_.

Once an implicit cycle is found, our synthesizer cuts it by refining the current segmentation. Our synthesizer continues the above steps (1-3) of decision tree learning as follows. (4) Our synthesizer selects \((x\ge 0)\in H\) and cuts the implicit cycle {_R_(-1,1)_,R_(1,0)} by refining segmentations. (5) Using the refined segmentation, our synthesizer obtains \(f(x)=\mathbf{if}x\ge 1\) **then** -_x_+2 **else if** \(x\ge 0\) **then** 0 **else** _x_+3 as a ranking function for E.

As explained in Example 4,5, handling (explicit and implicit) cycles is crucial in decision tree learning for transition examples. Moreover, our _cycle detection theorem_ (Theorem 17) claims that if there is no explicit or implicit cycle, then one can find a ranking function for E without further refinement of segmentations.

Fig.6: Two examples R(-1,1) and R(1,0) make an implicit cycle between x 1 and (x 1).

