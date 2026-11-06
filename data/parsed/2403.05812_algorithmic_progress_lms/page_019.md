## F Quantifying training data _D_

One important degree of freedom in the modeling process is how to define the "training data". In particular, there we consider three possible definitions:

1. **Training dataset size:** The number of tokens in the dataset on which the language model was trained. This definition ignores the possibility of improvements in performance from training for multiple epochs, and is the approach taken in Erdil and Besiroglu 2022.<tbc>

2. **Tokens seen:** The total number of tokens seen during the course of training a language model--this is the definition adopted in Hoffmann et al. 2022. This is equivalent to the training dataset size if the model is trained for one epoch on the training set, which is fairly common practice but not totally ubiquitous. In fact, it is possible that more recent models are being pushed towards training with multiple epochs on the same data--e.g. GPT-4 was reportedly trained for 2 epochs on text and 4 epochs on code (Patel and Wong 2023). In cases where the tokens seen is not directly reported in paper, we estimate it via tokens seen ≈ num. epochs \(\times\) training dataset size.<tbc>

3. **Tokens seen with diminishing returns:** One problem with the previous approach is that seeing data repeatedly may yield diminishing returns. Muennighoff et al. 2023 find that the benefits in loss reduction drop significantly when training on more than 4 epochs.

In order to test the robustness of our most important result (compute doubling times) to this degree of freedom, we repeat our doubling times analysis as in section 3.1 but account for the number of training epochs. We then replace _D_ either with tokens seen (epochs times training dataset size) or tokens seen with diminishing returns. For each case we consider two possibilities--either we drop datapoints for which the epoch number is unknown (this drops around 90 datapoints), or we impute the epoch number as 1. We report our core parameter estimates in s 6 and 7, and our doubling time estimates in  5.

From the results in  5, we see that the model estimates are broadly consistent with each other. When dropping datapoints with unknown epochs, the median estimates do appear to become slightly shorter, but importantly the overall 95% confidence interval spans a slightly larger range compared to the default model using dataset size. Our overall uncertainty is therefore fairly similar under this degree of freedom. If we instead impute epoch values when they are unknown, we obtain results that appear significantly more similar to our core results (e.g. in terms of the median estimate), but with more probability mass on long doubling times.

We ultimately opt to quantify training data in terms of dataset size for simplicity, and this analysis suggests that our results are robust to this change.

## G Doubling times via optimal scaling

In the main paper we calculated doubling times for effective compute based on a closed form solution for the doubling times, given by Equation 6. However, this equation was derived simply by considering changes in _D_eff, and it is not clear _a priori_ whether or not the effective compute is optimally allocated between _N_eff and _D_eff to minimize the cross entropy loss. In addition, calculating compute efficiency doubling times is less straightforward for models which also include changing scale exponents \(\alpha_\mathrm{param}\) and \(\beta_\mathrm{data}\) (i.e. models 14 and 15 in our cross validation analysis, see J). We thus supplement our previous calculation with an alternative approach, which instead enforces the condition of compute-optimal scaling.

We approach this in two stages:

1. First, we calculate the reduction in cross entropy loss \(\Delta L\) given a doubling in compute budgets and under compute-optimality. Let the initial compute budget be _C_. We solve an optimization problem<tbc>

<tbc>\(L_1=\mathrm{min}_{(N,D)}L(N,D),\) \(\text{(9)}\)<tbc>

\begin{tabular}{cc}
Definition & _C_eff doubling times (months) \\
Dataset size (section 3.1) & \[4.5, 8.4, 14.3\] \\
Tokens seen & \[1.4, 3.5, 20.9\] \\
Tokens seen + impute & \[4.8, 9.1, 16.9\] \\
Tokens seen w. dim. returns & \[1.7, 5.7, 28.0\] \\
Tokens seen w. dim. returns + impute & \[4.8, 9.2, 18.1\] \\
\end{tabular}

5: Estimated effective compute doubling times using the core model (equation 8), using three different definitions of "training data". Numbers in the square brackets correspond to the \[2.5th, 50th, and 97.5th percentile\] after bootstrapping 100 times.

