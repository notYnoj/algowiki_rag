<tbc>Online Resource 2, whereas the results corresponding to Section 5.3.3 are included in Online Resource 3.

## 5.3.1 MAX-SMTI problems

First, we compare the solution quality of different algorithms in solving small-sized MAX-SMTI problems, including 60 configurations. The maximum number of iterations is set to 3,000 for TBLS and TBLS-E, and 50,000 for LTIU, AS, and MCS, to fully leverage the capabilities of the latter three local search algorithms.

Figure 1a displays the number of singles produced by various algorithms in solving small-sized MAX-SMTI problems. Our TBLS algorithm achieves the highest number of wins and the lowest average number of singles across 60 configurations. TBLS-E closely follows, also demonstrating excellent performance with an average number of singles very similar to that of TBLS. Furthermore, TBLS-E stands out as the top performer measured by SECost, as illustrated in Figure 1b. In almost all configurations, TBLS-E achieves the fairest matchings, significantly outperforming other algorithms.

Next, we assess the solution quality in addressing large-scale MAX-SMTI problems across 100 configurations, maintaining the same settings for the maximum number of iterations as used for small-sized MAX-SMTI problems. Due to its slow performance, LTIU is excluded from this evaluation. As the instances become harder, the performance gap between algorithms widens. Regarding the number of singles, TBLS remains the winner in most configurations, with approximately 0.2 fewer singles than the second-place TBLS-E and about 1.6 fewer singles than the third-place GSA2, as shown in Figure 2a. As illustrated in Figure 2b, TBLS-E consistently leads in most configurations, with an average SECost approximately 100 lower than MCS, which ranks second among the algorithms specifically designed for the MAX-SMTI problems.

It is noteworthy that the proposed TBLS-E algorithm outperforms both PDB and all other algorithms, achieving the lowest SECost in 95% of small-sized configurations and 78% of large-sized configurations. This improved performance can be attributed<tbc>

60
Max #Wins: 60
Algorithm with the Most Wins
TBLS
48
TBLS-E
36
(Measured by #Singles)
LTIU
#Wins
24
AS
MCS
12
GSA2
GSM
PDB
0
0
0.3
0.7
1.0
1.3
1.7
2.0
Overall Average #Singles across 60 Configurations

60
Max #Wins: 60
Algorithm with the Most Wins
TBLS-E
48
(Measured by SECost)
36
#Wins
24
PDB
LTIU
12
MCS
GSA2
AS
TBLS
GSM
0
0
24
48
72
96
120
Overall Average SECost across 60 Configurations

(a) Number of singles

(b) Sex equality cost

**Fig. 1** Solution quality comparison for small-sized MAX-SMTI problems

