different branch instructions. This results in improved branch predictability for most software implementations, especially those in which branch profiling does not enter into software design. Where branch profiling does take place, however, the gains are often only marginal [14, pp. 245-248]. Thus, although large processors and general purpose processors generally include dynamic prediction, many small processors and low-power processors forgo dynamic prediction, as this feature’s sophistication requires the usage of significant additional semiconductor area for the associated logic.

Dynamic branch prediction often results in complex processor behavior. Often several predictors will be used for the same branch instruction instance; the predictor in a given iteration will be based on the history of that branch instruction instance and/or other branches. In the problem we are concerned with, however, this does not result in as many complications as one might expect; the probability of a given branch outcome conditional on the branches that precede it is identical to the probability of the branch outcome overall. In the case of previous branch outcomes for the same search instance --<tbc>

<tbc>i.e., those of ancestors in the tree -- any given outcome is conditioned on the same events -- i.e., the events that lead to the branch being considered. In the case of branches for previous items, if items are independent, so are these branches. In the case of branches outside of the algorithm, these can also be assumed to be either fixed given or independent of the current branch.

Thus, as long as each branch predictor is assigned at most one of the decision tree branches, prediction can be modeled as a random process. This process will result in each predictor converging to a stationary distribution, which can be analyzed and optimized for. Unfortunately, such a random process will necessarily perform worse than optimized static prediction, although, in most instances, the difference will not be too great.

The cost of each branch result can be determined by the expected time of the branch, based on the costs involved and the probability that the branch is correctly predicted. Simple analysis of the stationary distribution of a branch prediction Markov chain, e.g., [16], can yield the expected time for a<tbc>

3
1
1
3
1
3
1
3
1
3
1
(a) Fixed-length representation (b) Proportional representation

2
2
2
2
11
11
2
2
11
11
11
11
2
11
2
2
11
11
11
11
2
2
11
11
2
11
11
(a) Edge order restricted (b) Edge order unrestricted

Fig. 1. Two representations of optimal branch trees

Fig. 2. Optimal branch trees for two restriction types for _p_=(1615201561)/128 with _c_=(112)

