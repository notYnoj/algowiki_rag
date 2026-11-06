<tbc>exponential time function for survival times. Risks are calculated as the logarithm of house numbers, standardized and scaled for a mean survival time of 30. We introduce censoring by randomly selecting 30% of house numbers and replacing true times with values sampled uniformly between (0_,t<sub>i</sub>_\] (See Figure 5). Risk is predicted from the images with a convolutional neural network with the same hyperparameters as Petersen et al. (2021), with _z<sub>i</sub>=f_<sub>CONV</sub>(**_x_**_<sub>i</sub>_). We also evaluate on four real-world healthcare datasets from Kvamme et al. (2019). Each dataset has a fairly small number of patients (\(N\le 8,873\)) and a flat vector of covariates as input. Further details in Appendix A.6. For these datasets, a fully connected neural network is used to find the risk, _z<sub>i</sub>=f_<sub>MLP</sub>(**_x_**_<sub>i</sub>_). Further details on the training and evaluation procedures can be found in Appendix A.4.

The results presented in  1 demonstrates that Diffsurv achieves equal to or better performance on all datasets analyzed. Additionally, when Diffsurv is optimized for predicting the top 10% of highest risk individuals, it outperforms Cox’s partial likelihood on all four datasets. There is a significant improvement in the top 10% highest-risk prediction when comparing models based on Cox’s Partial Likelihood (\(\mu=.825\), \(\sigma=.005\)) and Diffsurv optimized for Top-k prediction (\(\mu=.944\), \(\sigma=.008\)) on the survSVHN dataset.

## 4 CONCLUSION

Diffsurv represents a significant step in the field of survival analysis with censored data. Our experiments demonstrate the effectiveness of differentiable sorting methods in improving survival analysis predictions, particularly in censored datasets with Diffsurv matching or improving performance against Cox partial likelihood on all datasets. Additionally, Diffsurv has the potential to drive the development of new methods, such as the top-k risk stratification method presented in this work. It is noteworthy that while our method has shown promising results, further investigation is necessary to fully understand its potential and limitations. For instance, it would be valuable to examine the scalability of the method with larger real-world datasets and its capability to handle more complex censored scenarios. Further research could also investigate the integration of Diffsurv into clustering models. With its ability to handle censored data and its end-to-end training capability, Diffsurv presents a promising approach to survival analysis and holds great potential for enhancing risk prediction in real-world applications.

\begin{tabular}{cccccc}
Method & n=2<sup>†</sup> & n=4 & n=8 & n=16 & n=32 \\
Diffsurv & .918 (.003) & **.934** (.002) & **.940** (.001) & **.943** (.002) & **.941** (.002) \\
Cox Partial Likelihood & .913 (.002) & .925 (.002) & .931 (.002) & .933 (.002) & .930 (.003) \\
\end{tabular}

\begin{tabular}{ccccc}
 & FLCHAIN & NWTCO & SUPPORT & METABRIC \\
Size & 6,524 & 4,028 & 8,873 & 1,904 \\
Censored Proportion & 69.9% & 85.8% & 32.0% & 42.1% \\
\multicolumn{5}{c}{Risk Stratification} \\
Diffsurv & .787 (.012) & .691 (.018) & **.599** (.004) & .623 (.012) \\
Cox Partial Likelihood & .787 (.016) & .690 (.014) & .584 (.004) & .615 (.018) \\
\multicolumn{5}{c}{Top 10% prediction} \\
Diffsurv (Top-k) & **.952** (.014) & .926 (.007) & **.571** (.012) & **.771** (.059) \\
Cox Partial Likelihood & .937 (.014) & .919 (.026) & .478 (.032) & .561 (.039) \\
\end{tabular}

1: Results for semi-synthetic and real-world datasets. Bold indicates significantly higher performance (t-test with a significance level of 0.01).

(a) Semi-synthetic survSVHN Dataset Results. Mean (and standard deviation) over 5 trails with different seeds. Metric is C-index. <sup>†</sup> When _n_=2 both methods are equivalent to the ranking loss.

(b) Real-world datasets results. Mean (and standard deviation) over 5-folds measured in C-Index for the risk stratification task and proportion correctly predicted for the Top-k task.

