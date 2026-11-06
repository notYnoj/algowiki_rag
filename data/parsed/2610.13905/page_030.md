plots correspond to the inner dimension of the multiplication and not the number of recursive steps as in Figures 3 and 4. Once again, empirical performance results are represented with dashed lines while the bounds implied by Theorem 4.6 are shown with solid lines. The gap between the latter indicates how much worse Theorem 4.6 predicts the stability of the algorithm to be under alternative bases. While this gap can be quite large (particularly for \(\langle 2,2,5;17\rangle\), which, again, was chosen for this reason) we see essentially no difference in the practical performance. This is shown precisely in  4, which confirms that the empirical results shown in Figure 5 are not simply compressed due to the scale of the plots. In total this re-affirms an observation made in \[53\] for the fast exact setting: the predicted loss of stability under alternative bases is primarily an artifact of the analysis from Section 4, and specifically the fact that the stability factor (i.e., Theorem 4.3) is strictly larger when alternative bases are used.

## 5.4 Effectiveness of Truncation

For our final experiment, we explore the impact of the truncation approach (outlined in Section 4.4) on the stability of an alternative basis APA algorithm. Accordingly, we run Algorithm 5, evaluating an APA algorithm a fixed _r_ times and taking \(\varepsilon_j=\beta\cdot e^{2\pi ij/r}\) for some \(0<\beta<1\). The idea here is that, if \(\beta\) is small enough to make the uncanceled remainder negligible but not so small that it introduces instability, we<tbc>

Standard vs alternative basis, one panel per algorithm (N(0, 1) inputs)
Schönhage (3, 3, 3; 21)
Our (2, 2, 3; 10)
10-5
100
10-10
10-10
Error
Error
10-15
3
9
27
81
243
2
4
8
16
32
64
Inner dimension k
Inner dimension k
Our (2, 2, 5; 17)
1010
standard basis
100
alternative basis
standard basis bound
alternative basis bound
Error
10-10
classical O(n3) product
10-20
2
4
8
16
32
Inner dimension k

Figure 5: Empirical/predicted error for various APA matrix multiplications algorithms with and without alternative bases. As in Figures 3 and 4, dashed lines mark practical results and solid lines represent the bound implied by Theorem 4.6. Again, the error of the classical _O(n_<sup>3</sup>) algorithm is included for reference (in grey).

