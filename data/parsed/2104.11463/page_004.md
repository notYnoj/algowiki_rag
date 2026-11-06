<tbc>into account the constraints imposed on the leaf labels affected by those examples (the affected leaf labels are \(f_1(\widetilde{x})\) and \(f_3(\widetilde{x})\) in the case of _e_<sub>4</sub>).

### Our Algorithm: Cycle-Based Decision Tree Learning for Transition Examples

We use what we call the _cycle detection theorem_ (Theorem 17) as a theoretical tool to handle such crossing examples. The theorem claims the following: if there is no piecewise affine ranking function with the current segmentation of the domain (such as the one in Fig. 2b given by _h_<sub>1</sub> and _h_<sub>2</sub>), then this must be caused by a certain type of cycle of constraints, which we call an _implicit cycle_.

In our decision tree learning algorithm, when we do not find a piecewise affine ranking function with the current segmentation, we find an implicit cycle and refine the segmentation to break the cycle. Once all the implicit cycles are gone, the cycle detection theorem guarantees the existence of a candidate piecewise affine ranking function with the segmentation.

We integrate this decision tree learning algorithm in the CEGIS architecture (Fig. 1) and use it as a synthesizer. Our implementation of this framework gives promising experimental results on existing benchmark sets.

### Contribution

Our contribution is summarized as follows.

- We provide a decision tree-based synthesizer for ranking functions integrated into the CEGIS architecture. Our synthesizer uses transition examples to find candidate piecewise affine ranking functions. A major challenge here, namely handling constraints arising from crossing examples, is coped with by our theoretical observation of the cycle detection theorem.<tbc>

**-** We implement our synthesizer for ranking functions implemented in MuVal and report the experience of using MuVal for termination and non- termination analysis. The experiment results show that MuVal’s performance is comparable to state-of-the-art termination analyzers [7,10,13,21] from Termination Competition 2020, and that MuVal can prove (non-)termination of some benchmarks with which other analyzers struggle.

### Organization.

Section 2 shows the overview of our method via examples. Section 3 explains our target class of predicate constraint satisfaction problems and how to encode (non-)termination problem into such constraints. In Section 4, we review CEGIS architecture, and then explain simplification of examples into positive/negative examples. Section 5 proposes our main contribution, our decision tree-based ranking function synthesizer. Section 6 shows our implementation and experimental results. Related work is discussed in Section 7, and we conclude in Section 8.

## 2 Preview by Examples

We present a preview of our method using concrete examples. We start with an overview of the general CEGIS architecture, after which we proceed to our main contribution, namely a decision tree learning algorithm for transition examples.

