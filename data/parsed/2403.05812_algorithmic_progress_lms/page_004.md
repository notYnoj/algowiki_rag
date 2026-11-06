<tbc>decomposition of the main contributors to increased performance, such as improvements in how efficiently data or free parameters in the model are used. In this sense, our core approach is similar to that in Erdil and Besiroglu 2022.

The starting point is the scaling law from Hoffmann et al. 2022, which relates the training loss _L_ of a dense transformer to its number of parameters _N_ and the training dataset size _D_:

\(L=E+\frac{A}{N^\alpha}+\frac{B}{D^\beta},\) (1)

where _L_ is per-token cross entropy loss on the dataset, and _E_, _A_, _B_, \(\alpha\) and \(\beta\) are constants. _E_ represents the ‘irreducible loss’ of the dataset, while the second and third terms, \(\frac{A}{N^\alpha}\) and \(\frac{B}{D^\beta}\), capture the errors that are due to the finiteness of the model or dataset, respectively.

Following Erdil and Besiroglu 2022 and Hernandez and T. Brown 2020, we quantify algorithmic progress in terms of reductions of the resources (_N_ and _D_) required to achieve the same level of performance over time. To measure this, we introduce the concepts of "effective data" _D_eff and "effective model size" _N_eff into the model:<sup>1</sup><tbc>

\(N_\mathrm{eff}\equiv N\mathrm{exp}(\alpha'(Y-Y_0)),\text{and}D_\mathrm{eff}\equiv D\mathrm{exp}(\beta'(Y-Y_0)),\) (2)

<tbc>where _Y_ is the current year, _Y_<sub>0</sub> is some reference year<sup>2</sup>, and \(\alpha'\) and \(\beta'\) characterize the rate of algorithmic progress for model size and dataset size, respectively. In other words, we assume that continued algorithmic progress results in an exponential increase in _D_eff and _N_eff over some time interval _Y-Y_<sub>0</sub>, even with fixed _D_ and _N_. Plugging these into the original scaling law gives:

\(L=E+\frac{A}{N^{\alpha_\mathrm{param}}}+\frac{B}{D_\mathrm{eff}^{\beta_\mathrm{data}}}=E+\frac{A}{N^{\alpha_\mathrm{param}}}e^{-\alpha_\mathrm{year}(Y-Y_0)}+\frac{B}{D^{\beta_\mathrm{data}}}e^{-\beta_\mathrm{year}(Y-Y_0)},\) (3)

where _A_, _B_, \(\alpha_\mathrm{param}\), \(\alpha_\mathrm{year}\), \(\beta_\mathrm{data}\) and \(\beta_\mathrm{year}\) are constants. In relation to equation 2, we have that \(\alpha'=\alpha_\mathrm{year}/\alpha_\mathrm{param}\) and \(\beta'=\beta_\mathrm{year}/\beta_\mathrm{data}\). Algorithmic progress is thus captured as a constant exponential trend that multiplies with each of the two terms in the scaling law. In doing so, we are able to estimate the rate at which fewer ‘resources’ (_N_ and _D_) are required to achieve the same level of performance over time. Furthermore, given that the physical compute is approximately given by _C_≈6_ND_ (Hoffmann et al. 2022; Kaplan et al. 2020), we can similarly define an "effective compute" which is determined from the effective parameters and effective data.

## 2.2 Estimation approach

### 2.2.1 Model selection

We estimate variants of the augmented scaling law presented in equation (3) on our dataset of language model evaluations. We perform extensive cross-validation exercises to identify the variant of the model that fits the data best. The goal of this exercise is to consider different models that capture different effects (e.g. different scaling behavior across different model architectures, different forms of algorithmic progress, etc.).

Concretely, we consider dataset-specific coefficients (_A,B_), rates of algorithmic progress (e.g. \(\alpha_\mathrm{year},\beta_\mathrm{year}\)), different scaling coefficients for different architectures, regularization (\(\alpha_\mathrm{param},\beta_\mathrm{data}\)), and more. The model variants we consider generally do not contain an irreducible loss term (i.e. _E_=0) since this is poorly estimated on our data, and because it does not change our estimated doubling times in practice--we check the robustness of this change in appendix H. In total, we evaluate around 90 different model specifications through leave-one-out-cross validation and pick the models that perform best on relevant out-of-sample metrics, see Appendix J for more details. In the end, the model we select is model 7, where the coefficients _A_ and _B_ are benchmark specific, but estimates of algorithmic progress and scaling exponents (e.g. \(\alpha\) and \(\beta\)) are not. This model achieves an _R_<sup>2</sup> of around 0.91 between predictions and held-out test data.

A further important consideration is the possibility of alternative forms of algorithmic progress. In particular, in section 2.1 we model algorithmic progress as causing exponential increases in an "effective" budget, e.g. of parameters. But one could also observe progress through changes in scaling exponents (i.e. \(\alpha_\mathrm{param}\) and \(\beta_\mathrm{data}\)). There are _a priori_ reasons to suspect that this might be the case--for instance, one notable innovation is due to a change in scaling laws such as those introduced in Kaplan et al. 2020 and Hoffmann et al. 2022. Different model architectures, such as recurrent neural networks and transformers, are also known to have different scaling behaviours (see for instance Tay et al. 2022 and Droppo and Elibol 2021).

<sup>1</sup>This is not an original idea--for example, Hernandez and T. Brown 2020 and Erdil and Besiroglu 2022 use the concept of "effective compute" to calculate doubling times for compute efficiency in computer vision, and Davidson 2023 incorporates a similar idea into an integrated economic model. <sup>2</sup>Note that the "years" in our model do not need to be integers, i.e. "fractions of a year" are allowed and are determined based on the specific publication date of a model.

