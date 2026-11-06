<tbc>formed by column, row and (single) diagonal sorting, first conceived as a means to reuse column sorts when filtering a large raster image.

Defining s3(_a,b,c_) to be either the three swaps (_a,b_)(_b,c_)(_a,b_) (as in the original [5]) or (_a,c_)(_a,b_)(_b,c_) (reworked to be a 2-op!), we can find the median by s3(1,4,7), s3(2,5,8), s3(3,6,9), s3(1,2,3), s3(4,5,6), s3(7,8,9), s3(3,5,7), where this sequence of operators is executed from left to right.

## 2.1 Original design

The first version gives the 21-link network in Figure 5 below.

In Figure 6, we re-arrange the links in Figure 5 to highlight _stages_, i.e., links that can be executed in parallel. (Stages correspond to delay time in [4].) This does not change the overall swap statistics:

\begin{tabular}{ccc}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{tabular}

21
21
9.771
0.35
1
X
2
2-4
3
3-4
4
2-4
5
X
6
6-8
7
6-7
8
6-8
9
X

Figure 4: Labeling of cells in the \(3\times 3\) box.

Figure 5: A 21-link network to determine the median. The probabilities of swapping are: 1/2 at link 1, 2/3 at link 2, 1/3 at link 3, 1/2 at link 4, 2/3 at link 5, 1/3 at link 6, 1/2 at link 7, 2/3 at link 8, 1/3 at link 9, 1/2 at link 10, 2/3 at link 11, 1/3 at link 12, 1/2 at link 13, 2/3 at link 14, 1/3 at link 15, 1/2 at link 16, 2/3 at link 17, 1/3 at link 18, 19/70 at link 19, 5/14 at link 20, 1/7 at link 21. This results in 9<sup>27</sup>/35≈9.771 swaps on average.

