**Appendices**

## Appendix A

In  2, we show the 3! = 6 initial memory configurations in the left column (Stage 0), corresponding to the network in Figure 1(a). The progress of the sorting network is recorded in each row, with swaps that occurred highlighted in bold. This network has 3 stages, the maximum number of swaps, which occurred for the initial configuration of (3,2,1) is 3. The average number of swaps is the total number of swaps (9), divided by the number of configurations (6), resulting in 9/6 = 1.5. Finally, we consider the number of swaps at each stage, namely 3,4, and 2, divided by the number of configurations, giving, the ratios 3/6 = 0.5, 4/6 ≈ 0.666667, and 2/6 ≈ 0.333333,<tbc>

\begin{tabular}{ccccc}
\multicolumn{4}{c}{Memory contents} & \\
Stage 0 & Stage 1 & Stage 2 & Stage 3 & Number of \\
(initial) & (2-3 swap) & (1-2 swap) & (2-3 swap) & swaps \\
(1,2,3) & (1,2,3) & (1,2,3) & (1,2,3) & 0 \\
(1,3,2) & (1,**2**,**3**) & (1,2,3) & (1,2,3) & 1 \\
(2,1,3) & (2,1,3) & (1,**2**,3) & (1,2,3) & 1 \\
(2,3,1) & (2,**1**,**3**) & (1,**2**,3) & (1,2,3) & 2 \\
(3,1,2) & (3,1,2) & (1,**3**,2) & (1,**2**,**3**) & 2 \\
(3,2,1) & (3,**1**,**2**) & (1,**3**,2) & (1,**2**,**3**) & 3 \\
Number of swaps & 3 & 4 & 2 & 9 \\
\end{tabular}

\begin{tabular}{ccccc}
\multicolumn{4}{c}{Memory contents} & \\
Stage 0 & Stage 1 & Stage 2 & Stage 3 & Number of \\
(initial) & (1-3 swap) & (1-2 swap) & (2-3 swap) & swaps \\
(1,2,3) & (1,2,3) & (1,2,3) & (1,2,3) & 0 \\
(1,3,2) & (1,3,2) & (1,3,2) & (1,**2**,3) & 1 \\
(2,1,3) & (2,1,3) & (1,2,3) & (1,2,3) & 1 \\
(2,3,1) & (1,3,2) & (1,3,2) & (1,**2**,3) & 2 \\
(3,1,2) & (2,1,3) & (1,2,3) & (1,2,3) & 2 \\
(3,2,1) & (1,2,3) & (1,2,3) & (1,2,3) & 1 \\
Number of swaps & 3 & 2 & 2 & 7 \\
\end{tabular}

2: The behaviour of the network from Figure 1(a).

3: The behaviour of the network from Figure 2(a).

