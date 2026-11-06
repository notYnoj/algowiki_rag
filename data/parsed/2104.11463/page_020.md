<tbc>other tools could not; they are examples that do not require segmentations. Further analysis of these benchmarks indicates the following strengths of our framework: (1) the ability to handle nonlinear constraints (to some extent) thanks to the example-based synthesis and the recent development of SMT solvers; and (2) the ability to find a long lasso-shaped non-terminating trace assembled from multiple transition examples. See Appendix A for details.

## 7 Related Work

There are a bunch of works that synthesize ranking functions via constraint solving. Among them is a counterexample-guided method like CEGIS [28]. CEGIS is sound but not guaranteed to be complete in general: even if a given constraint has a solution, CEGIS may fail to find the solution. A complete method for ranking function synthesis is proposed in [19]. They collect only extremal counterexamples instead of arbitrary transition examples to avoid infinitely many examples. A limitation of their method is that the search space is limited to (lexicographic) affine ranking functions.

Another counterexample-guided method is proposed in [32] and implemented in SeaHorn. This method can synthesize piecewise affine functions, but their approach is quite different from ours. Given a program, they construct a _safety_ property that the number of loop iterations does not exceed the value of a candidate ranking function. The safety property is checked by a verifier. If it is violated, then a trace is obtained as a counterexample and the candidate ranking function is updated by the counterexample. The main difference from our method is that their method uses trace examples while our method uses transition examples (which is less expensive to handle). FreqTerm [15] also uses the connection to safety property, but they exploit syntax-guided synthesis for synthesizing ranking functions.

Aside from counterexample-guided methods, constraint solving is widely studied for affine ranking functions [26], lexicographic affine ranking functions [5, 7, 23], and multiphase affine ranking functions [6, 8]. Their implementation includes RankFinder and iRankFinder. Farkas’ lemma or Motzkin’s transposition theorem are often used as a tool to transform \(\exists\forall\)-constraints to \(\exists\)-constraints.

100
100
100
10
10
10
MuVal
MuVal
MuVal
1
1
1
1
1
10
100
1
10
100
10
100
10
100
AProve
irrankfinder v1.3.2
Ultimate Automizer

Fig.7: Scatter plots of runtime. Ultimate Automizer and AProVE sometimes gave up before the time limit, and such cases are regarded as 300s.

