This observation suggests the possibility that the discrepancy in estimated scaling exponents is due to the range of fitted data. Indeed, around 80% of our models with known training compute estimates lie between \(\sim 4\times 10^{17}\) FLOP and 10<sup>22</sup> FLOP. This suggests that a large fraction of our data lies within the regime where it is hard for our model to distinguish between the exponents from Hoffmann et al. 2022 and Kaplan et al. 2020.

Another possible explanation for this discrepancy that we considered is that it is due to the omission of an irreducible loss term in our core model, resulting in an omitted variable bias. However we do not put much weight on this explanation for our fits--in our robustness check using models with an irreducible loss term (see section H), we obtain very similar scaling exponents to those obtained in our core model.

## D Significance of the transformer architecture

Similarly to the doubling times for effective compute, we consider the predicted Compute-Equivalent Gains by applying the same modification in Equation 7 to the top 10 models from our cross validation exercises. Most models yield estimates within a similar ballpark as our core model, with some models yielding relatively noisy estimates. That said, one model (model 12 with \(\delta=0.02\)) predicts a notably larger efficiency contribution from the transformer, and this suggests that there is plausibly a fairly large degree of cross-model uncertainty present. These results are shown in Figure 10.

## E Dataset

### E.1 Performance measure and dataset

A key component of measuring progress in machine learning algorithms is the presence of a performance metric or benchmark. Since our focus is language modeling, token-level perplexity is a natural choice for this metric, for which we choose three benchmarks: WikiText-103, WikiText-2, and Penn Treebank. Note that WT2 and WT103 are both constructed from articles on Wikipedia. The two benchmarks share the same validation and testing set, while WikiText-103 has a much larger vocabulary and training set. In total, our dataset is constructed from 226 papers, from which we collect around 410 models that have reported token-level perplexity. Of these models, 370 contain sufficient information to be considered for analysis (perplexity, parameter size, publication date, and size of dataset).

### E.2 Perplexity

A standard metric for LLM performance is the measured test perplexity on standard datasets. For a language model, this is defined in as the exponential of the cross-entropy _L_ between the model predictions and the test set, i.e. Perplexity=_e<sup>L</sup>_.

\begin{tabular}{ccc}
 & Estimate & 95% CI \\
\(\alpha_\text{const}\) & 0.506

(0.496) & -0.027,1.314 \\
\(\alpha_\text{const,PTB}\) & 0.030

(0.165) & -0.176,0.180 \\
\(\alpha_\text{const,WT2}\) & 0.000

(0.123) & -0.097,0.399 \\
\(\alpha_\text{year}\) & -0.035

(0.037) & -0.076,0.049 \\
\(\alpha_\text{param}\) & 0.079<sup>∗</sup>

(0.054) & 0.040,0.226 \\
\(\beta_\text{const}\) & 1.103<sup>∗</sup>

(0.421) & 0.000,1.376 \\
\(\beta_\text{const,PTB}\) & 0.107

(0.084) & -0.003,0.259 \\
\(\beta_\text{const,WT2}\) & 0.112

(0.112) & -0.079,0.306 \\
\(\beta_\text{year}\) & 0.055

(0.027) & -0.024,0.076 \\
\(\beta_\text{data}\) & 0.029<sup>∗</sup>

(0.018) & 0.018,0.076 \\
\(\gamma\) & 2.972<sup>∗</sup>

(0.251) & 2.580,3.492 \\
\end{tabular}

3: Parameter estimates from the model described in equation 7, reported to 3 decimal places. We report 95% confidence intervals for all of the parameter estimates by bootstrapping 100 iterations. \* corresponds to a p value below 5%.

