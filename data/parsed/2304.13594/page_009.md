<tbc>sampling controls for a given case. Each batch consists of a number of risk sets such that the input data has shape (batch size, risk set size, covariate shape).

For the survSVHN task, the hazard function \(h_\theta\) for both the Cox Partial Likelihood baseline and \(f_\theta\) for Diffsurv, is a fixed sized convolutional neural network with a batch size of 100. Steepness is determined by risk set size _n_, \(\beta=2n\) for Odd-even networks and \(\beta=log_2(n)(1+log_2(n))\) for Bitonic. The only hyperparameter optimized for Diffsurv is the choice of sorting network. Both sorting network were evaluated on the validation set but only the resulting models with higher validation c-index were used on the test set. This was repeated for each risk set size.

For the real-world datasets, the hazard function \(h_\theta\) and \(f_\theta\) for Diffsurv is Multi-layer Perceptron network. Hyperparameters: number of hidden layers, size of hidden layers, dropout rate, batch size and learning rate are determined by a small hyperparameter sweep of 100 trails on random 80:20 splits for each dataset and method. Hyperparameter optimization for Diffsurv also included sorting network and steepness.

Full hyperparameter ranges and resulting best models are provided along with further implementation details at `https://github.com/andre-vauvelle/diffsurv-ea`.

During evaluation, the sorting network is not used since we only need to evaluate the ranks of the trained risk scores. Similarly, case-control sampling is not used. We measure the ranking performance of the models using the concordance index Harrell et al. (1982).

## A.5 POSSIBLE PERMUTATION MATRIX

In order to account for censoring, we propose utilizing a possible permutation matrix _Q<sub>p</sub>_. We provide a visualization for example risk set size 7 in Figure 3, which corresponds with Equation 12. It is also possible to represent such connections as a graph. Further, this possible permutation graph G_<sub>p</sub>_, is the complement of the order graph G_<sub>o</sub>_ typically used for C-index. Both graphs are visualised in Figure 4

\(Q_p=\left(\begin{array}{ c c c c c c c c c c }
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
0 & 1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1
\end{array}\right)\) (12)

## A.6 REAL WORLD DATASETS

• **FLCHAIN dataset:** A dataset containing information on patients with monoclonal gammopathy of undetermined significance (MGUS), focusing on serum free light chain (FLC) levels to study their prognostic significance in predicting disease progression.<tbc>

• **NWTS dataset:** A dataset from a series of clinical trials on the treatment and outcomes of children with Wilms’ tumor, a type of kidney cancer, aiming to improve understanding of tumor biology and optimize treatment strategies.<tbc>

• **SUPPORT dataset:** A dataset from a multicenter study investigating the prognosis and treatment preferences of seriously ill hospitalized adults, with the goal of improving end- of-life care and informing decision-making processes.<tbc>

• **METABRIC dataset:** A dataset comprising genomic and clinical data on breast cancer patients, focused on uncovering novel molecular subtypes for more precise prognostication and personalized treatment strategies.

## A.7 SURVSVHN DATASET

