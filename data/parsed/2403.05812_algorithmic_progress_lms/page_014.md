## C.1 Comparing our estimates to earlier work

Given that our core model is similar to previously proposed language model scaling laws, we can compare our estimates to see how well they correspond to prior work. In particular, the estimates for \(\alpha_\mathrm{param}\) and \(\beta_\mathrm{data}\) in  2 suggest that cross entropy loss scales roughly as _C_<sup>-1/20</sup>, where _C_ is training compute. In comparison, Kaplan et al. 2020 find a scaling exponent of around -0.048, and Hoffmann et al. 2022 estimate values of around -0.3. Given that our model is constructed based on the scaling law in Hoffmann et al. 2022, we might _a priori_ have expected our estimated to match those more closely--so what explains the difference?

One way to understand this discrepancy is to consider the scaling laws on the same plot, shown in Figure 9. Here we observe that the scaling laws strongly diverge for compute values below around 10<sup>18</sup> to 10<sup>19</sup> FLOP (and the same is true for values greater than 10<sup>22</sup> FLOP). However, between these two regimes the scaling laws appear much more similar in slope.

\begin{tabular}{ccc}
 & Estimate & 95% CI \\
\(\alpha_\mathrm{const}\) & 0.913<sup>∗</sup>

(0.235) & 0.000,1.208 \\
\(\alpha_\mathrm{const},\mathrm{PTB}\) & 0.000

(0.076) & -0.008,0.185 \\
\(\alpha_\mathrm{const},\mathrm{WT2}\) & 0.055

(0.118) & -0.119,0.176 \\
\(\alpha_\mathrm{year}\) & 0.004

(0.021) & -0.058,0.032 \\
\(\alpha_\mathrm{param}\) & 0.068<sup>∗</sup>

(0.022) & 0.045,0.127 \\
\(\beta_\mathrm{const}\) & 0.771<sup>∗</sup>

(0.225) & 0.233,1.293 \\
\(\beta_\mathrm{const},\mathrm{PTB}\) & 0.176

(0.108) & -0.006,0.285 \\
\(\beta_\mathrm{const},\mathrm{WT2}\) & 0.095

(0.120) & -0.081,0.317 \\
\(\beta_\mathrm{year}\) & 0.036

(0.023) & -0.002,0.080 \\
\(\beta_\mathrm{data}\) & 0.040<sup>∗</sup>

(0.011) & 0.023,0.062 \\
\end{tabular}

Cross entropy loss
Chinchilla
Kaplan
Ours
B year
3.6 x 1017 FLOP
1.2 x 1022 FLOP
0.125
6
0.100
95.2%
0.075
4.8%
5
0.050
4
0.025
3
0.000
-0.025
2
-0.050
1014
1016
1018
1020
1022
-0.10
-0.08
-0.06
-0.04
-0.02
0.00
0.02
0.04
0.06
FLOP
a year

2: Parameter estimates from the model described in equation 8, rounded to 3 decimal places. We report 95% confidence intervals for all of the parameter estimates by bootstrapping 100 iterations. \* corresponds to a p value below 5%.

Figure 9: (a) (Left) Comparison of scaling law predictions from our preferred model and previous work, specifically Kaplan et al. 2020 and Hoffmann et al. 2022. The grey lines represent scaling laws based on bootstraps of our proposed model. The two vertical dotted lines indicated the 10th to 90th percentile range of training compute values in our dataset. (b) (Right) Estimated values of \(\alpha_\mathrm{year}\) and \(\beta_\mathrm{year}\) from 1000 bootstraps. 95.2% of the bootstrapped estimates lie to the right of the line \(\alpha_\mathrm{year}+\beta_\mathrm{year}=0\).

