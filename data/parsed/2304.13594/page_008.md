<tbc>There are multiple different types of sorting networks each with varying space complexity. The ability to implement networks with the divide-and-conquer paradigm allows for sorting networks that scale more efficiently than previous differentiable sorting methods. In particular, Petersen et al. (2021) uses the odd-even and bitonic sorting networks. The latter allows construction of networks with size complexity O(_nlog_<sup>2</sup>_n_) verses the O(_n_<sup>2</sup>) in previous differentiable sorting methods. Examples for Odd-Even and Bitonic sorting networks with _n_=8 are shown in Figure 2.

### A.2.1 RELATION TO RANKING AND PARTIAL LIKELIHOOD

Differentiable sorting has so far only been applied in the context of uncensored ranking, where we know the true rank for every instance in an input set. It is possible to directly relate Diffsurv with ranking losses. Expanding out the cross entropy loss out we find

\(\mathcal{L}=\sum_c^n\left(\frac{1}{n}\sum_i^nq_{ci}log(p_{ci})\right),\) (10)

where _q<sub>ci</sub>_=1 only when _i_ is the true rank otherwise 0. Each _p<sub>ci</sub>_ is always a function of the difference in pairs of inputs _x<sub>i</sub>_ and _x<sub>j</sub>_. This is complicated by the products of intermediate values _a<sub>i</sub>_ introduced by the sorting network but denoted as

\(p_{ci}=\prod_{(a_i,a_j)\in\mathcal{P}_l:l=1}^n\sigma(f_\theta(a_i)-f_\theta(a_j))\) (11)

where P_<sub>l</sub>_ to denotes the set of comparisons to be made at each layer of the sorting network. With risk set of size 2, the loss returns to the same recognisable log-sigmoid ranking loss, and Cox negative log partial likelihood with risk set size 2.

### A.3 NON-PROPORTIONAL HAZARDS

Our current implementation of Diffsurv is limited to proportional hazards, which may not fully capture the complexity of certain survival analysis problems, particularly when non-proportional hazards are present. In this context, we explore alternative approaches that address this limitation.

Previously, we briefly mentioned continuous-time extensions of partial likelihood to enable non- proportional hazards Kvamme et al. (2019). This can be achieved by directly modeling temporal covariates as \(f_\theta=exp(h_\theta(x_i,T_i))\).

Another class of methods focuses on discretizing the time-to-event variable and modeling the probability mass function (PMF) of event times. For instance, the DeepHit model Lee et al. (2018) employs a neural network architecture to learn the relationships between input features and discretized time-to-event outcomes. Time discretization facilitates modeling of non-proportional hazards but introduces two significant challenges: 1) sensitivity to the choice of time intervals, which can affect the model’s accuracy and interpretability, and 2) increased computational complexity, as predictions must be made for each time interval. These models can be computationally expensive, especially for deep learning-based models like DeepHit, making them less suitable for high-dimensional and large-scale datasets, such as the imaging dataset used in this study.

Several future work proposals arise from these observations. First, differentiable sorting could explore the approach of directly modeling temporal covariates, resulting in a time-parameterized predicted permutation matrix. Second, extending Diffsurv to discrete time could be achieved by parameterizing a predicted permutation matrix for each time discretization. Finally, in models like DeepHit, the ranking loss term could be replaced with a Diffsurv loss, offering another promising direction for future research in survival analysis.

### A.4 TRAINING AND EVALUATION

During training, we use the Adam optimizer Kingma & Ba (2017) with a learning rate of 10<sup>-3</sup>, early stopping with patience of 10 epochs and a maximum of 10<sup>5</sup> training steps. As in Goldstein & Langholz (1992) and Kvamme et al. (2019), we ensure that each risk set contains a valid risk set by<tbc>

