## 3.10 Complete Split Distributions

Motivated by the leveled partition of tensor powers of CW_<sub>q</sub>_, we define the notion of complete split distributions to characterize the level-1 variable blocks contained in level-\(\ell\) variable blocks.

**Definition 3.4** (Complete Split Distribution)**.** A _complete split distribution_ for a level-\(\ell\) constituent tensor _T<sub>i,j,k</sub>_ with \(i+j+k=2^\ell\) is a distribution on all length \(2^{\ell-1}\) sequences \((\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^{\ell-1}})\in\{0,1,2\}^{2^{\ell-1}}\).

For a level-1 index sequence \(\hat{I}\in\{0,1,2\}^{2^{\ell-1}\cdot n}\), we say that it is _consistent_ with a complete split distribution \(\beta\) if the proportion of any index sequence \((\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^{\ell-1}})\) in<tbc>

\(\big\{\big(\hat{I}_{(t-1)\cdot 2^{\ell-1}+p}\big)_{p=1}^{2^{\ell-1}}\big|t\in[n]\big\}\)

<tbc>equals \(\beta(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^{\ell-1}})\). Namely, for every \((\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})\in\{0,1,2\}^{2^{\ell-1}}\), we have

\(\big|\big\{t\in[n]\big|\big(\hat{I}_{(t-1)\cdot 2^{\ell-1}+p}\big)_{p=1}^{2^{\ell-1}}=(\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})\big\}\big|=\beta(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^{\ell-1}})\cdot n.\)

Notice that any level-1 index sequence \(\hat{I}\in\{0,1,2\}^{2^{\ell-1}\cdot n}\) defines a complete split distribution by computing the proportions of each type of length-\(2^{\ell-1}\) consecutive chunks present in \(\hat{I}\). More specifically, we have the following definition.

**Definition 3.5.** Given a level-1 index sequence \(\hat{I}\in\{0,1,2\}^{2^{\ell-1}\cdot n}\), its complete split distribution over \((\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})\in\{0,1,2\}^{2^{\ell-1}}\) is defined as<tbc>

\(\text{split}\big(\hat{I}\big)\big(\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}}\big)=\frac{1}{n}\cdot\big|\big\{t\in[n]\big|\big(\hat{I}_{(t-1)\cdot 2^{\ell-1}+p}\big)_{p=1}^{2^{\ell-1}}=\big(\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}}\big)\big\}\big|.\)

<tbc>Given a subset \(S\subseteq[n]\), we can define the complete split distribution over \((\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})\in\{0,1,2\}^{2^{\ell-1}}\) given by \(\hat{I}\) restricted to the subset _S_ as<tbc>

\(\text{split}\big(\hat{I},S\big)\big(\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}}\big)=\frac{1}{|S|}\cdot\big|\big\{t\in S\big|\big(\hat{I}_{(t-1)\cdot 2^{\ell-1}+p}\big)_{p=1}^{2^{\ell-1}}=\big(\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}}\big)\big\}\big|.\)

<tbc>Given two complete split distributions \(\beta_1\) and \(\beta_2\) over the length-\(2^{\ell-1}\) index sequences \(\{0,1,2\}^{2^{\ell-1}}\), the \(L_\infty\) distances between \(\beta_1\) and \(\beta_2\) is defined to be

\(\|\beta_1-\beta_2\|_\infty=max_{\sigma\in\{0,1,2\}^{2^{\ell-1}}}|\beta_1(\sigma)-\beta_2(\sigma)|.\)

For any constant \(\varepsilon>0\) and a fixed complete split distribution \(\beta\), we say that a level-1 index sequence \(\hat{I}\in\{0,1,2\}^{2^{\ell-1}\cdot n}\) is consistent with \(\beta\) up to \(\varepsilon\) error if \(\|\text{split}(\hat{I})-\beta\|_\infty\le\varepsilon\). When the \(\varepsilon\) is clear from context, we say that \(\hat{I}\) is approximately consistent with \(\beta\) if it is consistent with \(\beta\) up to \(\varepsilon\) error.

**Definition 3.6.** For a level-\(\ell\) constituent tensor _T<sub>i,j,k</sub>_, an integer exponent _N_, a constant \(\varepsilon\ge 0\), and three complete split distributions \(\beta_X,\beta_Y,\beta_Z\) for the _X_-, _Y_ -, _Z_-variables respectively, we define

\(T_{i,j,k}^{\otimes N}[\beta_X,\beta_Y,\beta_Z,\varepsilon]:=\sum_\text{level-1 triple}X_\hat{I}Y_\hat{J}Z_\hat{K}\text{in}T_{i,j,k}^{\otimes N}X_\hat{I}Y_\hat{J}Z_\hat{K}.\)

It is a subtensor of \(T_{i,j,k}^{\otimes N}\) over all level-1 _X_-, _Y_ -, _Z_-variable blocks that are approximately consistent with \(\beta_X\), \(\beta_Y\), \(\beta_Z\), respectively. When \(\varepsilon=0\), we will simplify the notation to \(T_{i,j,k}^{\otimes N}[\beta_X,\beta_Y,\beta_Z]\).

