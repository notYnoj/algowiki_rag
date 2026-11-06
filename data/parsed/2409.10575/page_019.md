<tbc>MAX-SMTI problems, TBLS and TBLS-E are the top performers in nearly all configurations. On average, the first-place TBLS and the second-place TBLS-E run about 2.5 and 1.2 times faster than the third-place MCS, respectively.

## 5.3.2 MAX-HRT problems

We begin by evaluating the solution quality of different algorithms for solving MAX- HRT problems of small and large sizes. The maximum number of iterations is still set to 3,000 for TBLS. To maximize the performance of other local search algorithms, the maximum number of iterations is set to 5,000 for both HR and MCA.

Figure 4a and Figure 4b illustrate the number of unassigned positions produced by various algorithms in addressing small-sized and large-sized MAX-HRT problems, respectively. Overall, TBLS outperforms all other algorithms in both problem scales, consistently yielding matchings with the fewest unassigned positions. Notably, for large-sized MAX-HRT problems, TBLS produces approximately 1.8 fewer unassigned positions than the second-place algorithm, HPA, and about 11.8 fewer unassigned positions than HR, the second-best among all local search algorithms.

Additionally, the experimental results reveal that existing local search algorithms suffer a notable decline in performance with increasing problem size _n_. This phenomenon is more obvious for the MAX-HRT problem, as illustrated in Figure 4. One possible explanation is that as input size grows, the solution space expands substantially, and local optima become more difficult to escape. In contrast, our proposed algorithms, TBLS and TBLS-E, maintained robust performance on both problems with larger input sizes. This may be explained by their distinct neighborhood structures: TBLS and TBLS-E employ tie-breaking strategies, whereas other local search algorithms rely on removing blocking pairs. These findings suggest that tie-breaking based neighborhood structures facilitate more effective exploration of the solution space, thereby enhancing both solution quality and robustness, particularly in large-scale instances.

140
Max #Wins: 140
TBLS
112
(Measured by #Unassigned Positions)
84
#Wins
56
HPA
28
HR
MCA
Algorithm with the Most Wins
ASBM
HA
0
0
0.4
0.8
1.2
1.6
2.0
Overall Average #Unassigned Positions across 140 Configurations

100
Max #Wins: 100
TBLS
Algorithm with the Most Wins
80
(Measured by #Unassigned Positions)
60
#Wins
40
20
HPA
ASBM
HA
HR
MCA
0
0
4
8
12
16
20
Overall Average #Unassigned Positions across 100 Configurations

(a) Small-sized MAX-HRT - number of unassigned positions

(b) Large-sized MAX-HRT - number of unassigned positions

**Fig. 4** Solution quality comparison for MAX-HRT problems

