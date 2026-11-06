## A APPENDIX

### A.1 COX’S PARTIAL LIKELIHOOD AND RANKING LOSSES

Cox (1972) introduced the most popular method for addressing censoring for survival analysis. The original work and many subsequent extensions seek to maximize the partial likelihood, the general form is described as

\(\mathcal{L}(\theta)=\prod_{i:\delta=1}\frac{f_\theta(\mathbf{x}_i)}{\sum_{j:T_j>T_i}f_\theta(\mathbf{x}_j)},\) (4)

where \(f_\theta\) is the hazard function, a real valued score prediction function estimating the probability of an event at particular time, given input features **_x_**_<sub>i</sub>_. The product is taken over the set of uncensored patients, while the denominator term considers only comparable pairs and includes censored patients with _T<sub>j</sub>\>T<sub>i</sub>_.

The classic Cox proportional hazards model used \(f_\theta=\mathrm{exp}(\theta\cdot\mathbf{x}_i)\). Multiple extensions of this basic loss relax the linear covariate interaction and proportional hazards assumptions by altering \(f_\theta\). For example, (Katzman et al., 2018) parameterized with a neural network \(h_\theta\), such that \(f_\theta=\mathrm{exp}(h_\theta(\mathbf{x}_i))\), to model non-linear interactions between covariates on the hazard. (Kvamme et al., 2019) further show that this can be extended to non-proportional hazards by introducing temporal covariates, \(f_\theta=\mathrm{exp}(h_\theta(\mathbf{x}_i,T_i))\).

Kvamme et al. (2019) also make a few adjustments to the original partial likelihood loss. First, they consider that the risk set R={_j:T<sub>j</sub>\>T<sub>i</sub>_} is intractable for deep learning applications as it considers all comparable patients. Instead, it is possible take a fixed size sample risk set \(|\tilde{\mathcal{R}}|=n<N\) and further, it is reasonable to take a constant sample size of 1 and include the individual _i_ in the risk set (such that n=2). This leads to the simplified loss of the form

\(\mathcal{L}(\theta)=\prod_{i:\delta=1}\frac{f_\theta(\mathbf{x}_i)}{f_\theta(\mathbf{x}_i)+f_\theta(\mathbf{x}_j)},j\in\mathcal{R}\backslash\{i\}.\) (5)

Further, we can take the mean log partial likelihood to be

\(\mathrm{loss}=\frac{1}{n_e}\sum_{i:\delta=1}\mathrm{log}(1+\mathrm{exp}[h_\theta(\mathbf{x}_j)-h_\theta(\mathbf{x}_i)]),j\in\mathcal{R}\backslash\{i\},\) (6)

where _n<sub>e</sub>_ is the number of non-censored events. From this simplified form, it can be seen that the partial likelihood only considers the relative ordering or ranking of survival times.

The concordance index or c-index Harrell et al. (1982) is a commonly used as an evaluation for survival analysis methods and is a generalization of the Area Under the Receiver Operating Characteristic Curve (AUROC) that handles right-censored data.

\(\text{c-index}=\frac{1}{n}\sum_{i:\delta=1}\unknown(f(\mathbf{x}_i)<f(\mathbf{x}_j)),j\in\mathcal{R}\backslash\{i\}.\) (7)

Raykar et al. (2007) showed that the Cox’s partial likelihood is approximately equivalent to maximizing the concordance index or C-index and that closer bounds can be found by maximizing the general ranking loss

\(\text{ranking-loss}=\frac{1}{|\mathcal{A}|}\sum_{(\mathbf{x}_i,\mathbf{x}_j)\in\mathcal{A}}\phi(f_\theta(\mathbf{x}_i)-f_\theta(\mathbf{x}_j)),\) (8)

where \(\phi\) is a function that relaxes the non-differentiable \(\unknown\) of the C-index. We have also introduced A as the graph of acceptable pairs, where each node is a patient that can only be linked to another with an edge if we are sure that the first event occurs before the second. This is another way of describing the risk sets introduced earlier. From Equation 6 is can be seen that \(\phi:x\rightarrow-\mathrm{log}(1+\mathrm{exp}(-x))=\)<tbc>

