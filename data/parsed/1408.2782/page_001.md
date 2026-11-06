Fast distributed almost stable matchings

Rafail Ostrovsky<sup>∗</sup>

Will Rosenbaum<sup>†</sup>

June 17, 2021

**Abstract**

In their seminal work on the Stable Marriage Problem, Gale and Shapley [4] describe an algorithm which finds a stable matching in _O(n_<sup>2</sup>) communication rounds. Their algorithm has a natural interpretation as a distributed algorithm where each player is represented by a single processor. In this distributed model, Floréen, Kaski, Polishchuk, and Suomela [3] recently showed that for bounded preference lists, terminating the Gale-Shapley algorithm after a constant number of rounds results in an _almost_ stable matching. In this paper, we describe a new deterministic distributed algorithm which finds an almost stable matching in _O_(log<sup>5</sup>_n_) communication rounds for _arbitrary_ preferences. We also present a faster randomized variant which requires _O_(log<sup>2</sup>_n_) rounds. This run-time can be improved to _O_(1) rounds for "almost regular" (and in particular complete) preferences. To our knowledge, these are the first sub-polynomial round distributed algorithms for any variant of the stable marriage problem with unbounded preferences.

## 1 Introduction

### 1.1 Historical Background

In their seminal work, Gale and Shapley [4] consider the following problem. Members of disjoint sets of _n men_ and _n women_ each rank all members of the opposite sex. The men and women (which we collectively call _players_) wish to form a _matching_--a one-to-one correspondence between the men and women--which is _stable_ in the sense that it contains no _blocking pairs_: pairs of players who mutually prefer each other to their assigned partners in the matching. Gale and Shapley showed that a stable matching always exists by giving an explicit algorithm for finding one. The centralized Gale-Shapley algorithm runs in time \(\tilde{O}(n^2)\), and this run-time is asymptotically optimal for centralized algorithms [5]. The Gale-Shapley algorithm easily generalizes to the case of _incomplete preferences_ where each player ranks only a subset of the members of the opposite sex [5].

The Gale-Shapley algorithm has a natural interpretation as a distributed algorithm, where each player is represented by a separate processor which privately holds that player’s preferences. The communication links between players are formed by pairs of players who appear on each other’s preference lists. This model is natural in, for example, social networks where players

<sup>∗</sup>University of California, Los Angeles (Departments of Computer Science and Mathematics). Work supported in part by NSF grants 09165174, 1065276, 1118126 and 1136174, US-Israel BSF grant 2008411, OKAWA Foundation Research Award, IBM Faculty Research Award, Xerox Faculty Research Award, B. John Garrick Foundation Award, Teradata Research Award, and Lockheed-Martin Corporation Research Award. This material is based upon work supported by the Defense Advanced Research Projects Agency through the U.S. Office of Naval Research under Contract N00014-11-1-0392. The views expressed are those of the author and do not reflect the official policy or position of the Department of Defense or the U.S. Government. <sup>†</sup>University of California, Los Angeles (Department of Mathematics).

