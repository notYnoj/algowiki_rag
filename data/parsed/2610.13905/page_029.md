<tbc>in Algorithm 4 to have large entries despite the fact that \(\|A\|\|B\|\) is fixed, thereby promoting potentially catastrophic cancellation in the sum reduction used to obtain \(\widehat{C}\) from the intermediate products. Once again, we include the classical algorithm in Figure 4 as a baseline.

## 5.3 Stability with Alternative Bases

Alternative basis exact matrix multiplication is already known to be fast and stable \[53\]. Section 4 demonstrated that the theoretical bounds of \[53\] extend to APA matrix multiplication; here, we show that these algorithms are stable in practice as well.

For this experiment, we test three algorithms corresponding to different sizes: Schönhage’s \(\langle 3,3,3;21\rangle\) and two algorithms found in our search: \(\langle 2,2,3;10\rangle\) and \(\langle 2,2,5;17\rangle\). These were selected to show the range of potential stability loss predicted by Theorem 4.6; the \(\langle 2,2,5;17\rangle\) algorithm is the worst - meaning its error bound grows the most when comparing with/without alternative bases - while \(\langle 3,3,3;21\rangle\) shows the least growth and \(\langle 2,2,3;10\rangle\) is somewhere in the middle. For simplicity, we only compare each algorithm to itself with and without alternative bases, both run on the same set of input matrices _A_ and _B_. As in the previous experiment, the entries of these matrices are drawn from N(0,1) and the reported error matches the setup described in Section 5.1.

Figure 5 shows relative performance for all three algorithms. Note that the horizontal axes on these<tbc>

Error by input, one panel per scheme (worse-case input in black)
Smirnov (3,3,3;20)
Schönhage (3,3,3;21)
100
100
Error
Error
10-10
10-10
1
2
3
4
5
1
2
3
4
5
Recursion level L (matrix size n = 3L)
Recursion level L (matrix size n = 3L)
Our (3,3,3;21)
100
Unif(-1, 1)
Unif(0, 1)
N(0, 1)
Error
worse-case input theoretical bound
10-10
1
2
3
4
5
Recursion level L (matrix size n = 3L)

Figure 4: A repeat of Figure 3, with results grouped by algorithm instead of input type. An additional "worse-case" input is included here, constructed as described in the text. Note that all three panels share a vertical scale.

