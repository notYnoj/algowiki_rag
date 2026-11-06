## 4 Proof of Thm. 2 (additive-3 approximation algorithm)

Fix any instance \(\mathcal{I}=(\mathcal{K},\mathcal{Q},\mathcal{C},\alpha,\beta)\). If C is {=} then the optimal tree can be found in _O(n_log_n_) time, so assume otherwise. In particular, \< and/or \(\le\) are in C. Assume that \< is in C (the other case is symmetric).

The entropy \(H_\mathcal{I}=-\sum_i\beta_ilog_2\beta_i-\sum_i\alpha_ilog_2\alpha_i\) is a lower bound on opt(I). For the case K=Q and C={\<}, Yeung’s _O(n_)-time algorithm \[19\] constructs a 2wcst that uses only \<-comparisons whose cost is at most \(H_\mathcal{I}+2-\beta_1-\beta_n\). We reduce the general case to that one, adding roughly one extra comparison.

Construct \(\mathcal{I}'=(\mathcal{K}'=\mathcal{K},\mathcal{Q}'=\mathcal{K},\mathcal{C}'=\{<\},\alpha',\beta')\) where each \(\alpha'_i=0\) and each \(\beta'_i=\beta_i+\alpha_i\) (except \(\beta'_1=\alpha_0+\beta_1+\alpha_1\)). Use Yeung’s algorithm \[19\] to construct tree \(T'\) for \(\mathcal{I}'\). Tree \(T'\) uses only the \< operator, so any query \(v\in\mathcal{Q}\) that reaches a leaf \(\langle K_i\rangle\) in \(T'\) must satisfy \(K_i\le v<K_{i+1}\) (or _v\<K_<sub>2</sub> if _i_=1). To distinguish _K<sub>i</sub>=v_ from _K<sub>i</sub>\<v\<K_<sub>_i_+1</sub>, we need only add one additional comparison at each leaf (except, if _i_=1, we need two).<sup>8</sup> By Yeung’s guarantee, \(T'\) costs at most \(H_{\mathcal{I}^\prime}+2-\beta'_1-\beta'_n\). The modifications can be done so as to increase the cost by at most \(1+\alpha_0+\alpha_1\), so the final tree costs at most \(H_{\mathcal{I}^\prime}+3\). By standard properties of entropy, \(H_{\mathcal{I}^\prime}\le H_\mathcal{I}\le\mathsf{opt}(\mathcal{I})\), proving Thm. 2.

## 5 Proof of Thm. 4 (errors in work on binary split trees)

A _generalized binary split tree_ (gbst) is a rooted binary tree where each node _N_ has an _equality_ key _e<sub>N</sub>_ and a _split_ key _s<sub>N</sub>_. A search for query \(v\in\mathcal{Q}\) starts at the root _r_. If _v=e<sub>r</sub>_, the search halts. Otherwise, the search recurses on the left subtree (if _v\<s<sub>r</sub>_) or the right subtree (if \(v\ge s_r\)). The _cost_ of the tree

<sup>8</sup> If it is possible to distinguish _v=K<sub>i</sub>_ from _K<sub>i</sub>\<v\<K_<sub>_i_+1</sub>, then C must have at least one operator other than \<, so we can add either \(\langle v=K_i\rangle\) or \(\langle v\le K_i\rangle\).

