We evaluated _FastWCLQ2_, _SCCWalk4L_ and our own _AClique_ tool, with full results available in the Supplementary Materials. Here we focus on the best performing tool, _SCCWalk4L_.

The input graphs come from the modified graph preprocessing and node reduction steps outlined above. We colour code the results by the quality of the clique found, defined as the size of the maximum clique found from the approximate tool divided by the maximum clique as found by _CliSAT_ (expressed as a percentage).

The results from _SCCWalk4L_ are shown in Figure 2. Of 385 experiments, only 2 failed to find the maximum clique. However the first of those failures did have the maximum clique correctly found by both _FastWCLQ2_ and _Aclique_ so there is room for a multi-algorithm approach. None the less, this shows that some particular cliques are hard to resolve. Remember too that we would need to run _SCCWalk4L_ 100s of times to build a consensus tree.

Our _AClique_ tool fell between _FastWCLQ2_ and _SCCWalk4L_ for quality of results, but returned many cliques in a single run. It is likely the results could be improved further with more advanced techniques.

There is also some doubt over the randomness of results given by repeated running of the approximate MWC solvers with different random seeds. On a test graph with 291 nodes, 10,000 runs of _SCCWalk4L_ found 834 distinct cliques with maximum weight, of 896 possible. This may still be sufficient to produce the same consensus tree, but random sampling should have given us all cliques with significantly fewer trials, demonstrating a significant sampling bias. This was not universally the case though, with another graph giving all cliques rapidly<tbc>

1000
100
10
Time (s)
1
x
0.1
Correct weight > = 99% of maximum weight < 99% of maximum weight
0.01
0
500
1000
1500
2000
2500
3000
No. Nodes

Figure 2: Benchmarks of the approximate solver _SCCWalk4L_. This returns a single clique after a time limit of 1000s. Colours represent the quality of result, showing perfect maximum cliques, imperfect cliques found with at least 99% of the maximum clique size, and cliques found below 99%. Times shown are the time to find the best solution, which is typically considerably less than the fixed specified execution time.

