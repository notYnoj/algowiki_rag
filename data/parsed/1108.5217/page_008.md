## 3.2 Results for Tompa’s Database for PMSprune and DME

There are 56 datasets in the database used in \[TLB<sup>+</sup>\]. Due to limitations of DME and PMS we could not test all the datasets. PMS does not work for datasets which have only one sequence in them. s 3 and  4 show the 7 Statistical Measures for all the 9 Scoring methods we used. The tables represent the values for the Best Motif that we found in Mus09r and Hm26r datasets, respectively. From  2 it is observed that although the sensitivity of DME algorithm is very good PMS performs better than DME in all the cases. The specificity for DME is better than PMS in most of the cases but the difference is 1.5% or less.

5 compares the performance of results from all the 9 scoring techniques. We do the comparison in the following manner: For each dataset we compare the 7 Statistical Measures for all the 9 scoring techniques and find out which technique gave the best result for that measure. Then we count the total number of times the scoring technique gave the best result for that Statistical Measure. The numbers in  4 represent the count of best performance for each technique for each measure. The sum of each column is 45 which is the total number of datasets that we tested.

6 shows the average values of each statistical measure over all the datasets for all the 9 scoring techniques. It is observed that the average value of nucleotide as well as site Sensitivity for PMS is better than DME. There is at least a difference of 8% or more for nSn and 10% or more<tbc>

\begin{tabular}{cccccccc}
**Scoring Technique** & **nSn** & **nSp** & **sSn** & **nPPV** & **sPPV** & **nPC** & **nCC** \\
PMS SumMin & 0.6139 & 0.9227 & 0.6149 & 0.3240 & 0.9988 & 0.2692 & 0.4009 \\
DME SumMin & 0.4385 & 0.9354 & 0.5380 & 0.2907 & 0.9986 & 0.2118 & 0.3093 \\
BestDME SumMin & 0.4385 & 0.9354 & 0.5380 & 0.2907 & 0.9986 & 0.2118 & 0.3093 \\
PMS SumMinD & 0.7718 & 0.8910 & 0.7769 & 0.2993 & 0.9986 & 0.2750 & 0.4340 \\
DME SumMinD & 0.5788 & 0.8899 & 0.6659 & 0.2409 & 0.9983 & 0.2050 & 0.3161 \\
BestDMESumMinD & 0.4385 & 0.9354 & 0.5380 & 0.2907 & 0.9986 & 0.2118 & 0.3093 \\
PMS SumMin500 & 0.4386 & 0.9408 & 0.4167 & 0.3125 & 1.0000 & 0.2232 & 0.3251 \\
PMS SumMinD500 & 0.4386 & 0.9408 & 0.4167 & 0.3125 & 1.0000 & 0.2232 & 0.3251 \\
DME SumMin500 & 0.0877 & 0.9440 & 0.0833 & 0.0877 & 1.0000 & 0.0459 & 0.0327 \\
\end{tabular}

\begin{tabular}{cccccccc}
**Scoring Technique** & **nSn** & **nSp** & **sSn** & **nPPV** & **sPPV** & **nPC** & **nCC** \\
PMS SumMin & 0.3889 & 0.8745 & 0.4970 & 0.2516 & 0.9999 & 0.1803 & 0.2184 \\
DME SumMin & 0.0658 & 0.9192 & 0.1265 & 0.0811 & 0.9995 & 0.0377 & -0.0166 \\
BestDME SumMin & 0.1020 & 0.9646 & 0.1383 & 0.2381 & 0.9992 & 0.0769 & 0.0987 \\
PMS SumMinD & 0.3889 & 0.8745 & 0.4970 & 0.2516 & 0.9999 & 0.1803 & 0.2184 \\
DME SumMinD & 0.0658 & 0.9192 & 0.1265 & 0.0811 & 0.9995 & 0.0377 & -0.0166 \\
BestDMESumMinD & 0.1020 & 0.9646 & 0.1383 & 0.2381 & 0.9992 & 0.0769 & 0.0987 \\
PMS SumMin500 & 0.3447 & 0.8695 & 0.4678 & 0.2229 & 1.0000 & 0.1565 & 0.1776 \\
PMS SumMinD500 & 0.3447 & 0.8695 & 0.4678 & 0.2229 & 1.0000 & 0.1565 & 0.1776 \\
DME SumMin500 & 0.0669 & 0.9663 & 0.0851 & 0.1777 & 1.0000 & 0.0511 & 0.0525 \\
\end{tabular}

3: Result for Dataset Mus09r

4: Result for Dataset Hm26r

