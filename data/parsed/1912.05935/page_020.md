<tbc>selected and one free position that is in it. Continuing in a similar way, the following sequence of decisions was formed ( 1). Indices of selected rows are in bold.

In this particular example, in 11 cases out of 12, there was a situation when in the list of remaining free rows there was at least one row in which only one free position remained. If we did not use the minimum risk rule, we would not be able to get to the end. Since one "wrong move" in choosing the index of a free row, it would most likely lead to the destruction of the only free position that existed in one of the remaining free rows. This is the reason that when using only the _randSet_ & _randSet_ or _rand_ & _rand_ algorithm to get the complete solution, in the last stages, the solution goes to a dead end.

It should be noted that the minimum risk algorithm has a simple everyday meaning, and is often used in decision-making. For example, the doctor first of all operates on the patient whose condition is most critical for life, similarly, the farmer, during a severe drought, trying to save the crop, first of all watered those areas that are in the most critical condition ...

## 7 Algorithm Performance Analysis.

To evaluate the efficiency of the algorithm for various values of _n_, a rather lengthy computational experiment was performed over the total time. Initially, a fairly fast algorithm was developed for generating arrays of solutions of _n_-Queens Problem for an arbitrary value of _n_. Then, based on this program, large samples of solutions were formed for a basic list of n values. The sizes of the obtained samples of _n_-Queens Problem solutions, respectively, were equal: (10) - 1000, (20, 30, ..., 90, 100, 200, 300, 500, 800, 1000, 3000,<tbc>

\begin{tabular}{ccccccccccccc}
Step & row & row & row & row & row & row & row & row & row & row & row & row \\
89 & **25(1)** & 12(2) & 22(2) & 82(2) & 88(2) & 7(3) & 64(3) & 3(4) & 76(4) & 91(4) & 4(5) & 96(5) \\
90 & 7(2) & **12(2)** & 22(2) & 82(2) & 88(2) & 3(3) & 64(3) & 76(3) & 4(4) & 91(4) & 96(4) & \\
91 & **22(1)** & 3(2) & 7(2) & 82(2) & 88(2) & 64(3) & 76(3) & 91(3) & 4(4) & 96(4) & & \\
92 & **88(1)** & 3(2) & 7(2) & 82(2) & 91(2) & 64(3) & 76(3) & 4(4) & 96(4) & & & \\
93 & **3(1)** & 7(2) & 76(2) & 82(2) & 91(2) & 4(3) & 64(3) & 96(4) & & & & \\
94 & **76(1)** & 4(2) & 7(2) & 82(2) & 91(2) & 64(3) & 96(4) & & & & & \\
95 & 4(1) & **91(1)** & 7(2) & 82(2) & 64(3) & 96(3) & & & & & & \\
96 & **4(1)** & 82(1) & 7(2) & 64(3) & 96(3) & & & & & & & \\
97 & **7(1)** & 82(1) & 64(2) & 96(3) & & & & & & & & \\
98 & **82(1)** & 64(2) & 96(2) & & & & & & & & & \\
99 & 64(1) & **96(1)** & & & & & & & & & & \\
100 & **64(1)** & & & & & & & & & & & \\
\end{tabular}

1: Demo of using the minimum risk rule (_n_=100).

