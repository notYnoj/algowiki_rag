<tbc>We present an alternative method that leverages recent advancements in continuous relaxations of sorting operations, enabling end-to-end training of neural networks with ordering supervision (Grover et al., 2019; Blondel et al., 2020; Petersen et al., 2021). This involves incorporating a sorting algorithm into the network architecture, where the order of the samples is known, but their exact values are unsupervised. Here, we introduce _Diffsurv_, an extension of differentiable sorting methods that enables end-to-end training of survival models with censored data.

Briefly, our contributions are summarised:

• Our primary contribution is the extension differentiable sorting methods to account for censoring by introducing the concept of possible permutation matrices.<tbc>

• We empirically demonstrate that our new differentiable sorting method improve risk ranking performance across multiple simulated and real-worlds censored datasets.<tbc>

• We demonstrate that differentiable sorting of censored data enables the development of new methods with practical applications, using the example of end-to-end learning for top-k risk stratification.

## 2 METHODS

A dataset with censored event times is summarized as \(\mathcal{D}=\{t_i,x_i,\delta_i\}_{i=1}^N\). For a patient _i_, _t<sub>i</sub>_ is the observed minimum of the unobserved true survival time \(t_i^*\) and the censoring time \(c_i^*\), \(\delta_i\) is the event indicator that is 1 if an event is observed (\(t_i^*\le c_i^*\)) or 0 if the data is censored (\(t_i^*>c_i^*\)). Covariates are \(x_i\in\mathbb{R}^d\) representing a 1-dimensional vector of size _d_ or larger dimensional tensors such as image data. _N_ is the total number of patients. As previously mentioned, it is common to subsample total possible risk set, we use _n_ to represent the subsampled risk set size.

In order to train models based on ordering information using differentiable sorting algorithms Petersen (2022), we can minimize the cross-entropy between the ground truth orders represented by true permutation matrix **_Q_** and a doubly-stochastic predicted permutation matrix **_P_**. This makes it possible to interpret each element _P<sub>ij</sub>_ of the predicted permutation matrix as the predicted probability of permuting from a randomly assigned rank _i_ to a true rank _j_.

There are multiple methods of relaxing sorting algorithms to produce **_P_**, we will follow Petersen et al. (2021) by using differentiable sorting networks. Sorting networks are a family of sorting algorithms that consist of two basic components: wires and conditional swaps. Wires carry values to be compared at conditional swaps, if one value is bigger than the other, the values carried forward are swapped around. For a random sample of patients to be ordered, each layer of the sorting network can be considered an independent permutation matrix **_P_**_<sub>l</sub>_ with elements given by<tbc>

\(P_{l,ii}=P_{l,jj}=\sigma(z_j-z_i)\text{and}P_{l,ij}=P_{l,ji}=1-\sigma(z_j-z_i).\) (1)

