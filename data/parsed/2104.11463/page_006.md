(ii) The validator receives the candidate solution and finds out that the candidate solution is not a genuine solution. The validator finds that the assignment \(x=1,x'=0\) is a counterexample for (3), and thus adds _R_(1,0) to E to prevent the same candidate solution in the next iteration.<tbc>

(iii) The synthesizer receives the updated set E={_R_(1,0)} of examples, finds a ranking function _f(x_)=_x_ for E (i.e. for the transition from _x_=1 to \(x'=0\)), and returns a candidate solution \(R(x,x')=x>x'\wedge x\ge 0\).<tbc>

(iv) The validator checks the candidate solution, finds a counterexample \(x=-2,x'=-1\) for (2), and adds _R_(-2,-1) to E.<tbc>

(v) The synthesizer finds a ranking function _f(x_)=|_x_| for E and returns \(R(x,x')=|x|>|x'|\wedge|x|\ge 0\) as a candidate solution. Note that the synthesizer have to synthesize a piecewise affine function here, but details are deferred to Sect. 2.2.<tbc>

(vi) The validator accepts the candidate solution because it is a genuine solution for C.

## 2.2 Handling Cycles in Decision Tree Learning

We explain the importance of handling cycles in our decision tree-based synthesizer of piecewise affine ranking functions.

In what follows, we deal with such decision trees as shown in Fig. 4: their internal nodes have affine inequalities (i.e. half- spaces); their leaves have affine functions; and overall, such a decision tree expresses a piecewise affine function (Fig. 4). When we remove leaf labels from such a decision tree, then we obtain a template of piecewise functions where condition guards are given but function bodies are not. We shall call the latter a _segmentation_.

### Input and output of our synthesizer.

The input of our synthesizer is a set E of transition examples (e.g. E={_R_(1,0)_,R_(-2,-1)}) as explained in Sect. 2.1. The output of our synthesizer is a well-founded relation \(R(\widetilde{x},\widetilde{x'}):=f(\widetilde{x})>f(\widetilde{x'})\wedge f(\widetilde{x})\ge 0\) where \(\widetilde{x}\) is a sequence of variables and \(f(\widetilde{x})\) is a piecewise affine function, which is represented by a decision tree (Fig. 4). Therefore our synthesizer aims at _learning_ a suitable decision tree.

### Refining segmentations and handling cycles.

Roughly speaking, our synthesizer learns decision trees in the following steps.

