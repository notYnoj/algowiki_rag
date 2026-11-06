Figure 7 compares the scalability of three local search algorithms on instances of the MAX-HRT problem. It is worth noting that TBLS produces perfect matchings for nearly all instances across various input sizes, whereas HR yields an average of 37 unassigned positions, and MCA fails to find stable matchings for instances when _n_ exceeds 7,000. Moreover, as illustrated in Figure 7b, TBLS consistently outperforms the other two algorithms in terms of running time. Based on the observed trends over the tested input sizes (from 1,000 to 10,000), there is no evidence suggesting that the growth rate of TBLS’s running time will surpass that of the other two algorithms as the input size increases.

200
TBLS
TBLS-E
175
AS
MCS
150
Average Number of Singles
125
100
75
50
25
0
1000
2000
3000
4000
5000
6000
7000
8000
9000
10000
n

TBLS
TBLS-E
40
AS
MCS
30
Average Time (Sec.)
20
10
0
1000
2000
3000
4000
5000
6000
7000
8000
9000
10000
n

60
TBLS
HR
50
MCA
40
Average Number of Singles
30
20
10
0
1000
2000
3000
4000
5000
6000
7000
8000
9000
10000
n

TBLS
10
HR
MCA
8
Average Time (Sec.)
6
4
2
0
1000
2000
3000
4000
5000
6000
7000
8000
9000
10000
n

(a) Number of singles

(b) Execution times

**Fig. 6** Scalability of four local search algorithms on MAX-SMTI problems

(a) Number of unassigned positions

(b) Execution times

**Fig. 7** Scalability of three local search algorithms on MAX-HRT problems

