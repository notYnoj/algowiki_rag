After evaluating the solution quality, we shift our focus to analyzing execution time performance. The maximum number of iterations is set to 3,000 for all the algorithms. Figures 5a and Figure 5b show the execution times for small-sized and large-sized MAX-HRT problems, respectively. In both problem scales, TBLS emerges as the algorithm with the highest number of wins, indicating that it runs the fastest in a large number of configurations. In particular, for large-sized MAX-HRT problems, TBLS operates approximately 2.6 times faster than MCA and about 3.2 times faster than HR.

## 5.3.3 Scalability

In this section, we increase the input size _n_ from 1,000 to 10,000 to evaluate the scalability of our proposed algorithms in comparison with other local search methods. Since this experiment is intended to observe the trend in running time, the maximum number of iterations for each algorithm is set to 3,000. We use the average number of singles or unassigned positions to assess the solution quality of the algorithm, as defined in Equation (1). If an algorithm fails to produce any stable matching for a given input size, no data point is shown for that algorithm at that size in the figure reporting the average number of singles or unassigned positions.

As shown in Figure 6a, the AS and MCS algorithms are unable to produce stable matchings for the MAX-SMTI instances within the given number of iterations when the input size exceeds 2,000 and 3,000, respectively. Since our algorithms resolve all ties, they are guaranteed to find a stable matching regardless of the number of iterations or the instance size. Figure 6b depicts the relationship between the input size and the running time for solving MAX-SMTI problems. All four algorithms exhibit growth in time that is slightly faster than linear as the input size increases from 1,000 to 10,000. However, our proposed algorithms appear to have a more moderate growth rate in execution time. Compared with the other two local search algorithms, TBLS and TBLS-E achieve significantly better solution quality and substantially lower running times, demonstrating greater scalability.

140
Max #Wins: 140
Algorithm with the Most Wins
100
Max #Wins: 100
Algorithm with the Most Wins
TBLS
112
80
TBLS
(Measured by Time)
84
60
#Wins
(Measured by Time)
#Wins
56
40
28
MCA
20
HR
MCA
HR
0
0
0.04
0.08
0.12
0.16
0.20
0
0.8
1.6
2.4
3.2
4.0
Overall Average Time (Sec.)
Overall Average Time (Sec.) across 140 Configurations
across 100 Configurations

(a) Small-sized MAX-HRT - execution times (b) Large-sized MAX-HRT - execution times

**Fig. 5** Execution time comparison of local search algorithms for MAX-HRT problems

