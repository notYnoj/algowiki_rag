<tbc>scoring rules circumvents both the utilitarian and egalitarian criteria. Their optimization on combinatorial domains have been studied in several settings (often under the name of _Ordered Weighted Averages_): assignment problems \[Lesca _et al._, 2018\], proportional representation \[Elkind and Ismaili, 2015\], resource allocation \[Heinen _et al._, 2015\]. To the best of our knowledge, the problem of determining a GGI optimal stable marriage has not been studied yet. This is precisely the purpose of the present work.

The paper is organized as follows. In Section 2, we introduce notations and we formally define the GGI stable marriage problem studied here. Then, in Section 3, we prove that it is NP-hard to determine an optimal stable marriage according to a GGI criterion applied to agents’ disutilities. In Section 4, we provide a polynomial time 2-approximation algorithm. Finally, in Section 5, we establish a parametrized complexity result with respect to a GGI- specific parameter.

## 2 The GGI Stable Marriage Problem

Let M={_m_<sub>1</sub>_,...,m<sub>n</sub>_} denote the set of men, and W={_w_<sub>1</sub>_,...,w<sub>n</sub>_} the set of women. As in Example 1, for each _m<sub>k</sub>_ (resp. _w<sub>k</sub>_), a preference relation \(\succ_k^m\) (resp. \(\succ_k^w\)) is defined on W (resp. M), where \(i\succ_k^mj\) (resp. \(i\succ_k^wj\)) means that _m<sub>k</sub>_ (resp. _w<sub>k</sub>_) prefers _w<sub>i</sub>_ to _w<sub>j</sub>_ (resp. _m<sub>i</sub>_ to _m<sub>j</sub>_). We denote by `rk`(_m<sub>i</sub>,w<sub>j</sub>_) the rank of woman _w<sub>j</sub>_ in the preference order of man _m<sub>i</sub>_, and similarly for `rk`(_w<sub>j</sub>,m<sub>i</sub>_).

A solution of a stable marriage problem is a matching represented by a binary matrix **x**, where _x<sub>ij</sub>_=1 means that _m<sub>i</sub>_ is matched with _w<sub>j</sub>_. A matching **x** induces a matching function \(\mu_\mathbf{x}\) defined by \(w_j=\mu_\mathbf{x}(m_i)\) and \(m_i=\mu_\mathbf{x}(w_j)\) if _x<sub>ij</sub>_=1. In a perfect matching (called indifferently matching or marriage from now on), every man (resp. woman) is matched with a different woman (resp. man). More formally, a matching is defined by:

\(\sum_{i=1}^nx_{ij}=1\forall j\in\{1,\dots,n\}\) (1)

\(\sum_{j=1}^nx_{ij}=1\forall i\in\{1,\dots,n\}\) (2)

A matching is said to be _stable_ if there exists no man and woman who prefer each other to their current partner. More formally, a perfect matching is stable if the following constraints hold \[Vande Vate, 1989\]:

\(x_{ij}+\sum_{j^\prime\succ_i^mj}x_{ij^\prime}+\sum_{i^\prime\succ_j^wi}x_{i^\prime j}\ge 1\forall(i,j)\in\{1,\dots,n\}^2\) (3)

The set of stable marriages, i.e. binary matrices **x** such that constraints 1, 2 and 3 hold, is denoted by X. In their seminal paper, Gale and Shapley \[1962\] states that there always exists at least one stable marriage, which can be computed in _O(n_<sup>2</sup>).<br>
The Gale-Shapley algorithm is based on a sequence of proposals from men to women. Each man proposes to the women following his preference order, pausing when a women agrees to be matched with him but continuing if his proposal is rejected. When a woman receives a proposal, she rejects it if she already has a better proposal according to her preferences. Otherwise, she agrees to hold it for consideration and rejects any former proposal that she might had. Such a sequence of proposals always leads to a stable marriage called man- optimal stable marriage and denoted by **x**_<sup>m</sup>_ (if the role of men and women is reversed, we obtain the woman-optimal stable marriage denoted by **x**_<sup>w</sup>_). In the man-optimal stable marriage, each man has the best partner, and each woman has the worst partner, that is possible in any stable marriage. Contrarily, in the woman-optimal stable marriage, each

