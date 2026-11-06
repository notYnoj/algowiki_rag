<tbc>into Cherry’s preprocessing step. This allows us to exploit Cherry’s reductions and re-use them all until no further improvements in graph size via these reductions can be achieved.

Carrying out these reductions on the SARS-CoV-2 samples we have previously discussed, we see an approximately 20% reduction in both the number of vertices and edges simply for the degree 1 reductions. Including the degree 2 reductions drops the graph sizes further, to around only 60% of the original number of vertices and edges.

For the instance constructed from 819 SARS-CoV-2 samples, the original complement graph contains 440 vertices and 1868 edges. The degree one rules reduce this to 357 vertices and 1473 edges. Including the degree two rules gives a residual graph with 281 vertices and 1076 edges.

Thus, relative to the original residual graph, the combined deterministic reductions remove 36.1% of the logical variables and 42.4% of the conflict edges. The first quantity is the corresponding reduction in the logical qubit count of the direct encoding. At fixed QAOA depth, the second quantity is the corresponding reduction in the number of logical two-qubit cost interactions in each cost layer.

\begin{tabular}{ccccc}
 & \multicolumn{2}{c}{Vertices} & \multicolumn{2}{c}{Edges} \\
 & Number & Percentage of Original & Number & Percentage of Original \\
Original & 440 & - & 1868 & - \\
Degree 1 Reduction & 357 & 81.1% & 1473 & 78.9% \\
Degree 2 Reduction & 281 & 63.9% & 1076 & 57.6% \\
\end{tabular}

Original Degree 1 Reduction Degree 2 Reduction
400
300
Number of Vertices
200
100
0
100
200
300
400
500
600
700
800
Number of Samples

Original Degree 1 Reduction Degree 2 Reduction
1750
1500
1250
1000
Number of Edges
750
500
250
0
100
200
300
400
500
600
700
800
Number of Samples

(a) Vertices

(b) Edges

Figure 7: Numbers of vertices and conflict edges before and after the degree one and degree two reductions on the SARS-CoV-2-derived instances. All reductions retain reconstruction records for the complete optimum family.

1: Effect of the deterministic reductions on the complement graph for the instance constructed from 819 SARS-CoV-2 samples. The percentage columns give the residual size relative to the graph entering the new reduction stage.

