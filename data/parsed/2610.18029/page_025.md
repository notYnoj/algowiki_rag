## A Approximate Classical Solvers

We chart the time taken to find the first occurrence of the best clique found, with runs of fixed times for 10, 100 and 1000 seconds per sequence subset. This time may be considerably less than the specified timeout, but the program still runs to the full timeout while looking for a better result. Thus the graphs can be seen as an indication of the typical timeout needed to be confident the correct result has been found. (This is most obvious with the later SCCWalk4L results.) The input graphs come from the modified graph preprocessing and node reduction steps outlined above. We colour code the results by the quality of the clique found, defined as the size of the maximum clique found divided by the actual maximum clique as found by _CliSAT_ (expressed as a percentage).

_FastWCLQ2_ results are shown in Figure 11. Despite being reviewed favourably by others, it appears to dislike our dense graphs and gives poor results even with the maximum time of 1000 seconds. In the 10 second runs it also took noticeably longer than the maximum time limit. We assume this is a constant time component loading and preprocessing the graphs as it was not significant in the longer trials.

Fastwclq2
100
10
Time (s)
1
Correct
0.1
"<awk '$4<$3*1.000&& $4>=$3*0.995' qfastwclq2-10.txt" using 2:5
"<awk '$4<$3*0.995&& $4>=$3*0.99' qfastwclq2-10.txt" using 2:5
"<awk '$4<$3*0.99' qfastwclq2-10.txt" using 2:5
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

Figure 11: Benchmarks of the approximate solver _FastWCLQ2_. This returns a single clique after a given maximum time limit. We chart the results for 10, 100 and 1000 seconds of time. Colours represent the quality of result, showing perfect maximum cliques, imperfect cliques found of size \(\ge 99.5\%\), cliques found of size between 99% and 99.5%, and cliques found below 99%. Times shown are the time to find the best solution, which is typically considerably less than the specified execution time.

