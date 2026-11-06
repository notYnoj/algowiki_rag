<tbc>_SCCWalk4L_ results (Figure 12) are very good, bar the occasional troublesome graph. It is clear that the maximum time given could be reduced from 1000s for many smaller graph sizes, with relatively few needing more than 100s.

The results of our own genetic algorithm based clique finder, _AClique_, are shown in Figure 13. This uses of a population of 96 cliques which are mutated and mated at random, along with randomised hill-climbing techniques, to build up the population. We periodically introduce new random cliques to avoid local maxima. This is purely random sampling and iterative improvements, with no branch and bound techniques. Despite this performance is in between _FastWCLQ2_ and _SCCWalk4L_ for time vs quality. While it struggles to find the correct maximum clique on many larger graphs it is rarely far away. However the key benefit is returning 100s or 1000s of cliques of the same maximum size found in a single execution run. We could combine many repeated runs of _SCCWalk4L_ with different random seeds to produce a similar result, perhaps even better, but we have not evaluated this and compare instead against _AClique_.

Sccwalk4L
10
1
Time (s)
0.1
Correct
Incorrect; > = 99.5%
Incorrect; > = 99%
Incorrect; < 99%
0.01
0
500
1000
1500
2000
2500
3000
100
10
Time (s)
1
0.1
0.01
0
500
1000
1500
2000
2500
3000
1000
100
Time (s)
10
1
0.1
0.01
0
500
1000
1500
2000
2500
3000
No. Nodes

Figure 12: Benchmarks of the approximate solver _SCCWalk4L_. This returns a single clique after a given maximum time limit. We chart the results for 10, 100 and 1000 seconds of time. Colours represent the quality of result, showing perfect maximum cliques, imperfect cliques found of size \(\ge\) 99.5%, cliques found of size between 99% and 99.5%, and cliques found below 99%. Times shown are the time to find the best solution, which is typically considerably less than the specified execution time.

