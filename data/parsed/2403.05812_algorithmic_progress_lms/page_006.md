<tbc>\(D_\mathrm{eff}=D\mathrm{exp}\left[\frac{\beta_\mathrm{year}}{\beta_\mathrm{data}}(Y-Y_0)\right]\), so the doubling time for _D_<sub>eff</sub> is determined by the time _Y-Y_<sub>0</sub> where _D_<sub>eff</sub>=2_D_. Thus we have:<tbc>

\(T_D=Y-Y_0=\frac{\beta_\mathrm{data}}{\beta_\mathrm{year}}\mathrm{ln}2.\) (4)

<tbc>The doubling times for parameter efficiency can be determined similarly, giving<tbc>

\(T_N=\frac{\alpha_\mathrm{param}}{\alpha_\mathrm{year}}\mathrm{ln}2,\) (5)

<tbc>which we can use to work out the doubling times for effective compute. In particular, since the total compute in FLOP, _C_, required during training is approximately 6_ND_, the growth rates are related via _g<sub>C</sub>=g<sub>N</sub>+g<sub>D</sub>_. Here _g<sub>C</sub>_ is the growth rate in effective compute, _g<sub>N</sub>_ is the growth rate in effective parameters, and _g<sub>D</sub>_ is the growth rate in effective data. Since doubling times are inversely related to growth rates, we therefore have that

\(T_C=\left(\frac{1}{T_N}+\frac{1}{T_D}\right)^{-1},\) (6)

where _T<sub>C</sub>_, _T<sub>N</sub>_, and _T<sub>D</sub>_ are the doubling times (due only to algorithmic progress in pre-training) for effective compute, effective parameters, and effective data respectively. Based on this approach, using our preferred model, we find that the median doubling time for effective compute is 8.4 months, with a 95% confidence interval of 4.5 to 14.3 months.

We further check the robustness of this result by looking at the predictions from different models. In particular, because we perform model selection using leave-one-out cross-validation, we can compare the predictions of our preferred model with the predictions from other models we considered.<sup>4</sup> Concatenating the doubling time estimates from the top ten models according to our cross-validation exercise, we find a median doubling time of 7.8 months \[95% CI: 1.5 to 17.6 months\], which is similar to our preferred model.

<sup>4</sup>Note that our preferred model is model 7, whereas the model that performs best in cross validation is model 10. We opt for model 7 given that it performs essentially as well in cross validation (MSE test loss of 0.0486 for model 7 compared to 0.0485 for model 10) but uses two fewer parameters. In addition, model 7 can be used to back out a single rate of algorithmic progress, rather than dataset-specific rates, which makes the results easier to interpret. More details about the models and their performance can be found in appendix J.

\begin{tabular}{ccccccccccccccccc}
**Degree of Freedom** & **1** & **2** & **3** & **4** & **5** & **6** & **7** & **8** & **9** & **10** & **11** & **12** & **13** & **14** & **15** \\
Progress in Efficiency Along _N_ & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> \\
Progress in Efficiency Along _D_ & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> \\
Dataset Specific Exponents & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> \\
Dataset Specific Constants & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> & \<|unk|\> \\
\end{tabular}

Density
0.20
Model 7
3.5
Median: 8.4 Aggregated Median: 7.9
3.0
0.15
2.5
2.0
0.10
1.5
0.05
1.0
0.5
0.00
0.0
10
7
15
8
12
9
5
13
6
11
4
3
1
2
Double time (months)
Statistical model structure
Better cross-validation performance
Worse cross-validation performance

(a) **Core estimates.** Doubling times from our preferred model, and aggregate of top ten models.

(b) **Robustness across model specification.** Swarm plots showing model estimates of the rate of algorithmic progress across distinct model structures. For each model, we choose the regularization strength \(\delta\) that performs best in leave-one-out cross validation.

(c) **Summary of all model structures** and the degrees of freedom included. Efficiency gains are captured by exponential decrease in the relevant error terms, except models indicated by <sup>_T_</sup>, which have time-varying exponents. For a full specification, see  10.

Figure 3: Estimates of algorithmic progress of models selected by cross validation. Figure 3a shows aggregated estimates over doubling times, and Figure 3b illustrates via swarm plots sorted from left to right in order of decreasing cross validation performance (increasing MSE test loss). Note that model 14 is omitted from Figure 3b --we elaborate on our reasoning in appendix J.2.

