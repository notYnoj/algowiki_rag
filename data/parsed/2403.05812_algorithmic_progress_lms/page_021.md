## I Autocorrelation

Our dataset was constructed by searching for papers with models that reported perplexity data on WT103, PTB, or WT2. In our initial data collection, we sometimes also included multiple models originating from the same paper. In some extreme instances, more than ten models from a single paper were included; for example, we incorporated 14 models from the paper "OPT: Open Pre-trained Transformer Language Models." This poses concerns of autocorrelation, which might for instance result in us underestimating the uncertainty in our individual parameter estimates.

In the main body of the paper we approached this issue by retaining only three models per paper in our analysis, which resulted in the exclusion of approximately 35 models. Here we consider an alternative approach for addressing autocorrelation, where we explicitly quantify the correlations between models from the same paper. We then use this information to establish a multivariate normal likelihood function, which we maximize to obtain parameter estimates.

First, let us define the residuals as \(\epsilon=\mathbf{x}-\hat{\mathbf{x}}\). The original loss function that we are using is the mean squared error, i.e. where the loss is given by \(E[\epsilon^T\epsilon]\). We want to modify our approach so that we take into account the correlations between different datapoints. The approach we take is to take an approach similar to generalized least squares and multiplicative attention--rather than consider just \(\epsilon^T\epsilon\), we consider \(\epsilon^TP\epsilon\), where _P_ is a correlation matrix.

We do this using a maximum-likelihood approach, where \(\epsilon^T\Sigma\epsilon\) placed in a multivariate normal distribution, given by<tbc>

\(f(\epsilon;\theta)=\frac{1}{\sqrt{(2\pi)^kdet(\Sigma)}}exp\left(-\frac{1}{2}\epsilon^T\Sigma^{-1}\epsilon\right),\) (13)

<tbc>where \(\Sigma\) is a covariance matrix for the data. Our goal is to choose the appropriate parameters \(\theta\) such that the resulting \(\epsilon=\mathbf{x}-\bar{\mathbf{x}}\) maximizes this distribution. This includes the original parameters in the model from equation 3 as well as the correlation \(\rho\) between models from the same paper. We define the loss function as the negative of the logarithm of this distribution (dropping constants which do not matter for the resulting minimization problem):<tbc>

\(l(\theta)=\frac{1}{2}logdet\Sigma+\frac{1}{2}\epsilon^T\Sigma^{-1}\epsilon.\) (14)

<tbc>In order to apply this to our data we need to specify the structure of the covariance matrix \(\Sigma=\sigma^{2n}P\) (and thus \(\Sigma^{-1}=\sigma^{-2n}P^{-1}\). We can accordingly write the loss function as<tbc>

\(l(\theta)=\frac{1}{2}logdetP+\frac{n}{2}log\sigma^2+\frac{1}{2\sigma^{2n}}\epsilon^TP^{-1}\epsilon.\) (15)

\begin{tabular}{ccc}
 & Estimate & 95% CI \\
\(\gamma\) & -0.000

(0.072) & -0.006,0.250 \\
\(\gamma\)PTB & 0.105

(0.100) & -0.002,0.356 \\
\(\gamma\)WT2 & -0.044

(0.154) & -0.520,0.004 \\
\(\alpha_\text{const}\) & 0.934<sup>∗</sup>

(0.250) & 0.000,1.318 \\
\(\alpha_\text{const,PTB}\) & 0.001

(0.056) & -0.041,0.146 \\
\(\alpha_\text{const,WT2}\) & 0.147

(0.128) & -0.066,0.392 \\
\(\alpha_\text{year}\) & 0.008

(0.022) & -0.062,0.038 \\
\(\alpha_\text{param}\) & 0.068<sup>∗</sup>

(0.020) & 0.043,0.132 \\
\(\beta_\text{const}\) & 0.763<sup>∗</sup>

(0.253) & 0.001,1.278 \\
\(\beta_\text{const,PTB}\) & 0.118

(0.100) & -0.003,0.324 \\
\(\beta_\text{const,WT2}\) & 0.001

(0.135) & -0.173,0.346 \\
\(\beta_\text{year}\) & 0.032

(0.024) & -0.010,0.075 \\
\(\beta_\text{data}\) & 0.040<sup>∗</sup>

(0.014) & 0.021,0.075 \\
\end{tabular}

8: Parameter estimates from the model described in equation 12, reported to 3 decimal places. We report 95% confidence intervals for all of the parameter estimates by bootstrapping 100 iterations. \* corresponds to a p value below 5%.

