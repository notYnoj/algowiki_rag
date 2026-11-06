bound on _k_, there must be at most 4 vertices (internal, i.e. not starting with _v_<sub>1</sub>) that are a local maximum with depths _D_, i.e., the preceding and following element in _L_ have smaller depths. The first vertex with depths _D_ must be the left child of some node _v_, and it is a leaf. Hence, its two right siblings exist, and because the next vertices on _L_ have depths \(\le D\), the siblings cannot have children. This shows the statement of the lemma.

**Lemma 17.** _Let L be a list of consecutive subproblems on the backbone, and assume there is no spill-in from the left to the first or from the right to the last (because of finished subproblems or the instance ending). Then at least one of the subproblems must be unaffected._

_Proof._ There are |_L_|-1 internal pivots over which a spill-in into subproblems could happen, but there are |_L_| subproblems. By the pigeon-hole principle, there must be a subproblem without spill-in, i.e., unaffected.

**Lemma 18.** _[Not too many affected subproblems] Let a be the number of active subproblems on the backbone at some stage of InversionSort and let u be the number of the unaffected subproblems. There exists a constant c such that_ \(Pr[a\le cu(logN)^2]\ge 1-1/N^3\).

_Proof._ Let _L_ be a list of consecutive active subproblems on the backbone. If we can show the statement of the lemma for each individual such list, the lemma follows.

If \(a=|L|\le c(logN)^2\), the claim follows from Lemma 17 because there is at least one unaffected subproblem.

Otherwise let _h=O_(log_N_) be the height of the refinement tree. By Lemma 16, there are at least \(a'=a/(4h+2)\) many subproblems corresponding to a vertex whose children are leafs. Now, by Lemma 9, one of the boundaries is chosen uniformly at random, and its probability of having spill-over to the left is 1/4, and so is for spill-over to the right. Now encode, from left to right, these spill-overs by a 1-bit if it is different from the previous. Let _k_ be the number of 1s in this sequence, and observe that the number of ones is a lower bound on the number of subsequences with the same direction of spill-over. Every other of these subsequences must have an unaffected subproblem. \(\mathbb{E}[k]=a'/2\ge c(logN)^2)/h\ge 2logN\) if the constant _c_ is sufficiently large. Hence, by a Chernoff bound, with probability 1-_N_<sup>3</sup>, we get \(u\ge a'/4\ge a/(12h)\gg a/c(logN)^2\) and \(u\ge a/c(logN)^2\) for sufficiently large _c_.

