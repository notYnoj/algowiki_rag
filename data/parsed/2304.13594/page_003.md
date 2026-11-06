<tbc>These elements represent conditional swaps between two patient risk values (_z<sub>i</sub>,z<sub>j</sub>_) and use a dif ferentiable relaxation of the step function such as the logistic-sigmoid, where \(\sigma:x\rightarrow\frac{1}{1+e^{-\beta x}}\). The inverse temperature parameter \(\beta>0\) is introduced so when \(\beta\rightarrow\infty\) the functions tend to the exact min and max functions. The indices being compared are determined by the sorting network and the final predicted probability matrix is the product of each layer of sorting operations, \(\mathbf{P}=(\prod_{l=1}^n\mathbf{P}_l^\mathsf{T})^\mathsf{T}\). For the base case, _n_=2, Diffsurv is equivalent to the pairwise ranking loss and Cox partial likelihood. Further details on the relations between Diffsurv and baselines is in Appendix A.2.1.

The introduction of censored patients means we no longer have access to a ground truth permutation matrix **Q**. We cannot determine the exact rank of patients who are censored before another who experienced an event. To address this challenge, we propose a novel extension of differentiable sorting to censored data. Our approach considers the set of _possible permutations_ for each patient, taking into account uncertainty about the true ranking. In Figure 3, we show an example of observed and censored events and the resulting set of possible permutations that can be represented as a permutation matrix **_Q_**_<sub>p</sub>_.

For a right-censored sample _i_, we only know that the rank must be lower than the rank of all other samples with an event time lower than the censoring time of _t<sub>i</sub>_, i.e. they must be ranked after prior events. For another sample _j_ with an event at _t<sub>j</sub>_, we know that the rank must be lower than other samples with an event time lower than _t<sub>j</sub>_, and higher than the rank of other samples either with an event time higher than _t<sub>j</sub>_ or with a censoring time higher than _t<sub>j</sub>_. We do not know how the rank of _j_ compares to samples with censoring time lower than _t<sub>j</sub>_. If it is possible for patient i to permute to rank j, then _Q<sub>pij</sub>_=1, otherwise _Q<sub>pij</sub>_=0.

Given the possible permutation matrix **Q**_<sub>p</sub>_ and the predicted permutation matrix **P**, the vector of probabilities **_p_** of a patient being ranked within the set of possible permutations can be computed. Although the ground truth ranks are unknown, the range of possible ranks is known, and the model can be optimized to maximize the sum of the predicted permutation probabilities for the possible ranks of each sample. Noted here as the column-sum of the element-wise product \(\circ\), between **Q**_<sub>p</sub>_ and **P**.

\(\mathbf{p}=\sum_{j=1}^n(\mathbf{Q}_p\circ\mathbf{P})_{i,j}.\) (2)

The cross-entropy loss can then be easily applied

\(\mathcal{L}=\sum_{i=1}^ny_ilog(p_i)\) (3)

where _y<sub>i</sub>_ is the true label of the set of possible ranks.

Finally, we demonstrate how the algorithmic supervision of sorting algorithms enables the development of novel methods in survival analysis, using the example of top-k risk prediction. In practical settings, it is often not necessary to rank all samples correctly. Rather, it is essential to identify the samples with the highest risk, such as by a healthcare provider, to prioritize care and interventions. With Diffsurv, top-k risk prediction is straightforward to implement by optimizing possible permutations within the top-k ranks, whereby **_Q_**_<sub>p</sub>_ is adjusted such that only the top-k patient’s possible permutations are set to 1.

## 3 EXPERIMENTS

We evaluate the performance of Diffsurv on censored survival data across semi-synthetic and real- world datasets. In each experiment, we train a neural network using Diffsurv and Cox’s partial likelihood loss, then compare their respective results. Cox’s partial likelihood and the closely related ranking loss are used in popular baselines; Deepsurv (Katzman et al., 2018), Cox-MLP (Kvamme et al., 2019) and DeepHit Lee et al. (2018).

We present a new semi-synthetic dataset, _survSVHN_, to evaluate survival models. Based on the Street View House Numbers (SVHN) dataset Petersen et al. (2021), we simulate survival times akin to survMNIST Pölsterl (2019). The increased complexity of SVHN offers a testbed which is better able to discern the performance differences between methods. Each house number parameterizes an<tbc>

