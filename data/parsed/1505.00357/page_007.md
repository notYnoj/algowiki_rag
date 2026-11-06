<tbc>_Proof. (Thm. 6)_ Consider any equality-testing node \(N=\langle v=K_a\rangle\) and any key \(K_z\in\mathcal{Q}_N\). Since \(K_z\in\mathcal{Q}_N\), node _N_ has descendant leaf \(\langle K_z\rangle\). Without loss of generality (by Proposition 1), leaf \(\langle K_z\rangle\)’s parent is \(\langle v=K_z\rangle\). That parent is a descendant of \(\langle v=K_a\rangle\), so \(\omega(K_a)\ge\omega(K_z)\) by Lemma 1. \(\square\)

## 3 Proofs of Thm. 1 (algorithm for 2WCST) and Thm. 3

First we prove Thm. 1. Fix an instance \(\mathcal{I}=(\mathcal{K},\mathcal{Q},\mathcal{C},\alpha,\beta)\). Assume for now that all probabilities in \(\beta\) are distinct. For any query subset \(\mathcal{S}\subseteq\mathcal{Q}\), let opt(S) denote the minimum cost of any 2wcst that correctly determines all queries in subset S (using keys in K, comparisons in C, and weights from the appropriate restriction of \(\alpha\) and \(\beta\) to S). Let \(\omega(\mathcal{S})\) be the probability that a random query _v_ is in S. The cost of any tree for S is the weight of the root \((=\omega(\mathcal{S}))\) plus the cost of its two subtrees, yielding the following dynamic-programming recurrence:

**Lemma 5.** _For any query set_ \(\mathcal{S}\subseteq\mathcal{Q}\) _not handled by a single-node tree,_

\(\mathsf{opt}(\mathcal{S})=\omega(\mathcal{S})+\mathrm{min}\left\{\begin{array}{ c c }
\mathrm{min}_k\mathsf{opt}(\mathcal{S}\backslash\{k\}) & \text{\textit{(if "=" is in}}\mathcal{C}\text{\textit{, else}}\infty\text{\textit{)}} \\
\mathrm{min}_{k,\prec}\mathsf{opt}(\mathcal{S}_k^\prec)+\mathsf{opt}(\mathcal{S}\backslash\mathcal{S}_k^\prec), & \text{\textit{(ii)}}
\end{array}\right.\)

_where k ranges over_ K_, and_ \(\prec\) _ranges over the allowed inequality operators (if any), and_ \(\mathcal{S}_k^\prec=\{v\in\mathcal{S}:v\prec k\}\).

Using the recurrence naively to compute opt(Q) yields exponentially many query subsets S, because of line (i). But, by Thm. 6, we can restrict _k_ in line (i) to be the maximum-likelihood key in S. With this restriction, the only subsets S that arise are intervals within Q, minus some most-likely keys. Formally, for each of _O(n_<sup>2</sup>) key pairs \(\{k_1,k_2\}\subseteq\mathcal{K}\cup\{-\infty,\infty\}\) with _k_<sub>1</sub>_\<k_<sub>2</sub>, define four _key intervals_

\(\begin{array}{ c c }
(k_1,k_2)=\{v\in\mathcal{Q}:k_1<v<k_2\}, & [k_1,k_2]=\{v\in\mathcal{Q}:k_1\le v\le k_2\}, \\
(k_1,k_2]=\{v\in\mathcal{Q}:k_1<v\le k_2\}, & [k_1,k_2)=\{v\in\mathcal{Q}:k_1\le v<k_2\}.
\end{array}\)

For each of these _O(n_<sup>2</sup>) key intervals _I_, and each integer \(h\le n\), define top(_I,h_) to contain the _h_ keys in _I_ with the _h_ largest \(\beta_i\)’s. Define S(_I,h_)=_I_\\top(_I,h_). Applying the restricted recurrence to S(_I,h_) gives a simpler recurrence:

**Lemma 6.** _If_ S(_I,h_) _is not handled by a one-node tree, then_ opt(S(_I,h_)) _equals_

\(\omega(\mathcal{S}(I,h))+\mathrm{min}\left\{\begin{array}{ c c }
\mathsf{opt}(\mathcal{S}(I,h+1)) & \text{\textit{(if equality is in}}\mathcal{C}\text{\textit{, else}}\infty\text{\textit{)}} \\
\mathrm{min}_{k,\prec}\mathsf{opt}(\mathcal{S}(I_k^\prec,h_k^\prec))+\mathsf{opt}(\mathcal{S}(I\backslash I_k^\prec,h-h_k^\prec)), & \text{\textit{(ii)}}
\end{array}\right.\)

_where key interval_ \(I_k^\prec=\{v\in I:v\prec k\}\)_, and_ \(h_k^\prec=|\mathsf{top}(I,h)\cap I_k^\prec|\).

Now, to compute opt(Q), each query subset that arises is of the form S(_I,h_) where _I_ is a key interval and \(0\le h\le n\). With care, each of these _O(n_<sup>3</sup>) subproblems can be solved in _O(n_) time, giving an _O(n_<sup>4</sup>)-time algorithm. In

