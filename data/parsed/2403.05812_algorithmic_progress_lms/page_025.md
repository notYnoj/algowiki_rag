\(\alpha'_\text{const}=\alpha_\text{const}+\alpha_\text{const,PTB}x_\text{PTB}+\alpha_\text{const,WT2}x_\text{WT2}\)<br>
\(\alpha'_\text{year}=\alpha_\text{year}+\alpha_\text{year,PTB}x_\text{PTB}+\alpha_\text{year,WT2}x_\text{WT2}\)<br>
\(\alpha'_\text{param}=\alpha_\text{param}+\alpha_\text{param,PTB}x_\text{PTB}+\alpha_\text{param,WT2}x_\text{WT2}\)<br>
\(\beta'_\text{const}=\beta_\text{const}+\beta_\text{const,PTB}x_\text{PTB}+\beta_\text{const,WT2}x_\text{WT2}\)<br>
\(\beta'_\text{year}=\beta_\text{year}+\beta_\text{year,PTB}x_\text{PTB}+\beta_\text{year,WT2}x_\text{WT2}\)<br>
\(\beta'_\text{data}=\beta_\text{data}+\beta_\text{data,PTB}x_\text{PTB}+\beta_\text{data,WT2}x_\text{WT2}\)<br>
\(\alpha_\text{param}^*=\alpha_\text{param,NT}(1-x_T)+\alpha_\text{param,T}x_T\)<br>
\(\beta_\text{data}^*=\beta_\text{data,NT}(1-x_T)+\beta_\text{data,T}x_T\)<br>
\(\alpha_\text{param}^\dagger=\alpha_\text{param}+\alpha_\text{rate}logY\)<br>
\(\beta_\text{data}^\dagger=\beta_\text{data}+\beta_\text{rate}logY\)

Here _x_PTB, _x_WT2, and _x<sub>T</sub>_ are dummy variables for PTB, WT2, and the transformer respectively. _Y_ is the year, and \(\alpha_\text{rate}\) and \(\beta_\text{rate}\) are constants that determine how quickly scaling exponents (\(\alpha_\text{param}\) and \(\beta_\text{data}\)) change over time.

Models 1 to 11 are all constructed using a similar set of rules:

• \(\alpha_\text{const}\) and \(\beta_\text{const}\) determine the coefficients of the parameter and data reducible loss terms respectively<tbc>

• \(\alpha_\text{year}\) and \(\beta_\text{year}\) capture algorithmic progress in parameters and data<tbc>

• \(\alpha_\text{param}\) and \(\beta_\text{data}\) determine the scaling behavior with respect to _N_ and _D_ respectively

All of these parameters may be set as benchmark-specific (e.g. by writing \(\alpha'_\text{const}\) in lieu of \(\alpha_\text{const}\)).

The remaining models are defined using a different set of rules:

• Model 12 is defined in similar fashion but in ‘Hicks-neutral’ fashion, such that the same degree of efficiency gain is seen across both parameters and data.<tbc>

• Model 13 models different scaling exponents \(\alpha_\text{param}\) and \(\beta_\text{data}\) for transformer vs non-transformer models<tbc>

• Model 14 captures only algorithmic progress via changes in the scaling exponents \(\alpha_\text{param}^\dagger\) and \(\beta_\text{data}^\dagger\)<tbc>

• Model 15 captures algorithmic progress via \(\alpha_\text{year}\) and \(\beta_\text{year}\), as well as changes in the scaling exponents<tbc>

• Models 16 and 17 do not capture algorithmic progress, and are used as a baseline for goodness-of-fit comparisons. Model 16 is modeled off equation 34, and model 17 modifies this to include transformer-specific scaling exponents. This is described in more detail in Appendix J.2<tbc>

• Model 18 is a model that only considers the total compute, via the approximation _C_=6_ND_. This is discussed in more detail in Appendix J.1.<tbc>

• Model 19 includes a term that accounts for different vocabulary sizes. We discuss this in Appendix E.2.2.<tbc>

• Model 20 is the same as model 7, but rather than using purely the training dataset size, it defines "training data" in a way that accounts for the number of epochs of training. Where the number of training epochs is unknown, we impute an epoch count of 1. This model is presented in more detail in Appendix F.

We chose to include models 16 to 20 in the cross validation analysis to help the robustness checks performed in different appendices.

