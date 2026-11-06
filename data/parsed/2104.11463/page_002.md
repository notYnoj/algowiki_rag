<tbc>CEGIS has been applied not only to program verification tasks (synthesis of inductive invariants [17,18,24,25], that of ranking functions [19], etc.) but also to constraint solving (for CHC [12,14,27,35], for pwCSP(T) [29,30], etc.). The success of CEGIS is attributed to the degree of freedom that synthesizers enjoy. In CEGIS, synthesizers receive a set of individual examples that synthesizers can use in various creative and speculative manners (such as machine learning). In contrast, in other methods such as [5-8,23,26], synthesizers receive logical constraints that are much more binding.

_Segmented Synthesis in CEGIS-Based Termination Analysis_ The choice of a _candidate space_ for candidate solutions \(\sigma\) is important in CEGIS. A candidate space should be _expressive_: by limiting a candidate space, the CEGIS architecture may miss a genuine solution. At the same time, _complexity_ should be low: a larger candidate space tends to be more expensive for synthesizers to handle.

This tradeoff is also in the choice of the type of examples: using an expressive example type, a small number of examples can prune a large portion of the candidate space; however, finding such expressive examples tends to be expensive.

In this paper, we use _piecewise affine functions_ as our candidate space for ranking functions. Piecewise affine functions are functions of the form

\(f(\widetilde{x})=\left\{\begin{array}{ c c } \widetilde{a}_1\cdot\widetilde{x}+b_1 & \widetilde{x}\in L_1 \\ \vdots & \widetilde{a}_n\cdot\widetilde{x}+b_n \widetilde{x}\in L_n \end{array}\right.\) (1)

where {_L_<sub>1</sub>_,...,L<sub>n</sub>_} is a partition of the domain of \(f(\widetilde{x})\) such that each _L<sub>i</sub>_ is a polyhedron (i.e. a conjunction of linear inequalities). We say _segmented synthesis_ to emphasize that our synthesis targets are piecewise affine functions with case distinction. Piecewise affine functions stand on a good balance between expressiveness and complexity: the tasks of synthesizers and validators can be reduced to linear programming (LP); at the same time, case distinction allows them to model a variety of situations, especially where there are discontinuities in the function values and/or derivatives.

We use _transition examples_ as our example type ( 1). Transition examples are pairs of program states that represent transitions; they are much cheaper to handle compared to _trace examples_ (finite traces of executions until termination) used e.g. in [15,32]. The current work is the first to pursue segmented synthesis of ranking functions with transition examples; see  1.

Synthesizer: a candidate solution σ constraints C find a candidate solution σ that is consistent with E Validator: Is σ a solution for C? No: a set E of examples No solution (Validator adds new examples to E) Yes: answer O

Fig.1: the CEGIS architecture

