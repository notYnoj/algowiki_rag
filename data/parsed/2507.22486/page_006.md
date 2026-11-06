## 6 Deterministic Longest Common Subsequence Approximation in Near-Linear Time

At every iteration, the algorithm uses _D_LIS to obtain \(\pi'\) which is a 2-approximation of LDS(_x_) in \(O(|\pi'|)\) time. The algorithm uses \(D_\text{Occ}^y\) to find all indices in _y_ in which symbols of \(\pi'\) occur in \(O(|\sum_{\sigma\in\pi^\prime}\#_\sigma(y)|)=\tilde{O}(|\text{Project}(y,\pi')|)\) time. The algorithm iterates these indices and concatenates the corresponding symbols from _y_ to obtain \(\text{Project}(y,\pi')\) in \(\tilde{O}(|\text{Project}(y,\pi')|)\) time. Then, the algorithm applies a near linear time LIS algorithm to compute \(\text{LIS}_{\pi^\prime}(\text{Project}(y,\pi'))\). Next, the algorithm finds all indices in _x_ containing a symbol of \(\pi'\) in \(\tilde{O}(|\sum_{\sigma\in\pi^\prime}\#_\sigma(x)|)\) time. The algorithm then updates both _D_LIS and \(D_\text{Occ}^x\) to delete all indices in _x_ that contain occurrences of symbols from \(\pi'\). This implements \(x\leftarrow\text{Exclude}(x,\pi')\). The symbols of \(\pi'\) in each iteration are disjoint from the symbols of \(\pi'\) in every previous iteration. Therefore, the total running time for implementing Lines 5-7 is bounded by \(\tilde{O}(\sum_{\sigma\in\Sigma}\#_\sigma(x)+\#_\sigma(y))=\tilde{O}(|x|+|y|)=\tilde{O}(n)\).

### Correctness.

We show that each candidate for _L_ is a common subsequence of _x_ and _y_. For _L_=BestMatch(_x,y_) this is trivial. The rest of the candidates are created by taking \(\eta\), a repetition-free subsequence of _x_, and finding an increasing subsequence of _y_ with respect to \(\eta\). Clearly, the result is a subsequence of _y_, and it is also a subsequence of _x_ as a subsequence of \(\eta\).

### Approximation ratio.

Clearly, if |LCS(_x,y_)|=0 the algorithm would not find any common subsequence, which is a satisfactory answer. If \(|\text{LCS}(x,y)|\ge 1\), in particular there is a common symbol occurring both in _x_ and in _y_. It immediately follows that BestMatch(_x,y_) returns a common subsequence of length at least 1, which is an _n_<sup>4/5</sup>-approximation if \(|\text{LCS}(x,y)|\le n^{4/5}\). Let us assume from now on that |LCS(_x,y_)|_\>n_<sup>4/5</sup>. In particular, let \(0<t\le 1/5\) be the number such that |LCS(_x,y_)|=_n_<sup>4/5+_t_.

If \(|\text{BestMatch}(x,y)|\ge n^t\), we have found a candidate which is an _n_<sup>4/5</sup>-approximation for LCS(_x,y_). Let us assume from now on that |BestMatch(_x,y_)|_\<n<sup>t</sup>_. This means that no symbol occurs in both _x_ and _y_ more than _n<sup>t</sup>_ times. Let _L_ be some longest common subsequence of _x_ and _y_. In particular, no letter occurs in _L_ more than _n<sup>t</sup>_ times. Consider the subsequence RF(_L_) of _L_ in which an arbitrary occurrence of each symbol is taken and everything else is deleted. Since every symbol occurs in _L_ less than _n<sup>t</sup>_ times and |_L_|=_n_<sup>4/5+_t_</sup>, we have that |RF(_L_)|_\>n_<sup>4/5</sup>.

Assume that \(|\text{LIS}_\pi(\text{RF}(L))|\ge n^t\). Since RF(_L_) is a subsequence of _y_, we have in particular that \(|\text{LIS}_\pi(y)|\ge|\text{RF}(L)|\ge n^t\). In this case, Line 3 returns a candidate of length at least _n<sup>t</sup>_, which is an _n_<sup>4/5</sup>-approximation for every possible length of LCS(_x,y_).

Assume from now on that \(|\text{LIS}_\pi(\text{RF}(L))|<n^t\). By Erdős-Szekeres theorem (Lemma 5), it holds that \(|\text{LDS}_\pi(\text{RF}(L))|\ge|\text{RF}(L)|/n^t\ge n^{4/5-t}\).

Before proceeding to analyze the while loop in Line 4, we provide an intuitive explanation for why it should work. Let \(D=\text{LDS}_\pi(\text{RF}(L))\) be the longest decreasing subsequence of the repetition-free reduction of the LCS according to \(\pi\). As a common subsequence, _D_ appears in both _x_ and _y_.

At each iteration of the while loop, the algorithm finds an approximate longest decreasing subsequence \(\pi'\) of _x_ with respect to \(\pi\), and removes from _x_ all symbols participating in \(\pi'\). Initially, _D_ is a valid candidate for the longest decreasing subsequence of _x_ with respect to \(\pi\).

Notice that the symbols of \(\pi'\) appear in the same order in \(\pi'\) and in _D_ (i.e., decreasing in \(\pi\)), which is a subsequence of _y_. We therefore say that an iteration in which \(\pi'\) contains many symbols of _D_ is _good_ - such an iteration would yield a large candidate \(\text{LIS}_{\pi^\prime}(y)\) for the LCS.

If an iteration is not _good_, it removes only a small fraction of _D_, so in the next iteration, _D_ remains fairly large, and the same argument can be applied again. By repeatedly applying

