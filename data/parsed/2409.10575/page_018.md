<tbc>to the fact that, in addition to leveraging PDB as its base algorithm, TBLS-E introduces further constraints on tie-breaking adjustments to better balance satisfaction. These results support the effectiveness of TBLS-E in identifying more equitable matchings while maintaining matching sizes comparable to those achieved by its original algorithm TBLS.

Finally, we evaluate the execution times of different local search algorithms in solving small-sized and large-sized MAX-SMTI problems. For these comparisons, the maximum number of iterations is set to 3,000 for all the algorithms. Figure 3a illustrates the execution times for small-sized MAX-SMTI problems. Although all these algorithms, except LTIU, complete their searches within an average of 0.2 seconds, our TBLS algorithm performs the fastest in most configurations. This gap becomes more pronounced as the problem size increases, which is shown in Figure 3b. For large-sized<tbc>

100
Max #Wins: 100
Algorithm with the Most Wins
TBLS
80
(Measured by #Singles)
60
TBLS-E
#Wins
40
20
GSA2
AS
GSM
PDB
MCS
0
0
2
4
6
8
10
12
14
Overall Average #Singles across 100 Configurations

100
Max #Wins: 100
Algorithm with the Most Wins
80
TBLS-E
(Measured by SECost)
60
#Wins
40
PDB
20
TBLS
MCS
AS
GSA2
GSM
0
0
170
340
510
680
850
Overall Average SECost across 100 Configurations

60
Max #Wins: 60
Algorithm with the Most Wins
100
Max #Wins: 100
Algorithm with the Most Wins
48
80
(Measured by Time)
TBLS
36
(Measured by Time)
TBLS
60
#Wins
24
#Wins
40
TBLS-E
TBLS-E
12
20
MCS
AS
MCS
AS
0
0
1.6
3.2
4.8
6.4
8.0
0
2.0
4.0
6.0
8.0
10.0
Overall Average Time (Sec.) across 60 Configurations
Overall Average Time (Sec.) across 100 Configurations

(a) Number of singles

(b) Sex equality cost

**Fig. 2** Solution quality comparison for large-sized MAX-SMTI problems

(a) Small-sized MAX-SMTI - execution times

(b) Large-sized MAX-SMTI - execution times

**Fig. 3** Execution time comparison of local search algorithms for MAX-SMTI problems

