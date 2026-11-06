## 4.2.2 Proving the constant-fraction guarantee

It remains to prove the second statement of Theorem 3, namely that

\(\sum_{A_t\times B_t\in\Gamma}|A_t||B_t|\ge 0.4|S\cap I|.\) (7)

We begin with a single subproblem \(T(m',n')\) discussed above. Let \(S'\) denote the set of all point pairs between \(A'\) and \(B'\) whose distances lie in _I_.

For each leaf cell \(\sigma\) of \(\Xi\), the pairs recorded in the biclique \(\hat{A}'_\sigma\times B'(\sigma)\) are considered _uncertain pairs_. All other pairs of \(S'\) are called _certified pairs_. Since \(|\hat{A}'_\sigma|\le m'/r'\) and \(\sum_{\sigma\in\Xi_k}B'(\sigma)=n'\), the total number of uncertain pairs in the subproblem is \(O(m'n'/r')\).

The following lemma is the key ingredient. Its proof relies crucially on the capture condition.

**Lemma 5.** _The number of pairs recorded in the bicliques of_ C _is at least one half of all certified pairs of_ \(S'\).

_Proof._ Consider a certified pair \((a,b)\in S'\). Let \(\sigma_b\) be the leaf cell of \(\Xi\) containing _b_. Since (_a,b_) is certified, the annulus _D<sub>a</sub>_ contains \(\sigma_b\).

Assume that (_a,b_) is not recorded by any biclique of C. Then \(\sigma_b\) cannot itself be a capture cell. By Lemma 2, there is a unique capture cell \(\sigma\) on the root-to-leaf path from the root to \(\sigma_b\). Since \(\sigma_b\) is not a capture cell, \(\sigma\) must be a Type-I capture cell. Because \(b\in\sigma_b\subseteq\sigma\), we have \(b\in B'(\sigma)\).

Because (_a,b_) is not recorded by the biclique \(\mathcal{A}'(\sigma)\times B'(\sigma)\), the annulus _D<sub>a</sub>_ does not contain \(\sigma\). Since _D<sub>a</sub>_ contains \(\sigma_b\subseteq\sigma\), the boundary of _D<sub>a</sub>_ must cross \(\sigma\). Hence \(a\in\hat{A}'_\sigma\).

We charge (_a,b_) to the Type-I capture cell \(\sigma\).

The number of charged pairs associated with \(\sigma\) is at most \(|\hat{A}'_\sigma|\cdot|B'(\sigma)|\). On the other hand, the number of pairs recorded by the biclique \(\mathcal{A}'(\sigma)\times B'(\sigma)\) is \(|\mathcal{A}'(\sigma)|\cdot|B'(\sigma)|\). Since \(\sigma\) is a Type-I capture cell, \(|\mathcal{A}'(\sigma)|\ge|\hat{A}'_\sigma|\). Therefore, \(|\mathcal{A}'(\sigma)|\cdot|B'(\sigma)|\ge|\hat{A}'_\sigma|\cdot|B'(\sigma)|\). Thus every charged pair associated with \(\sigma\) can be injectively assigned to a pair recorded by \(\mathcal{A}'(\sigma)\times B'(\sigma)\).

Summing over all Type-I capture cells, the total number of recorded pairs in C is at least the total number of charged pairs. Consequently, the recorded pairs in C account for at least one half of all certified pairs of \(S'\).

We now prove (7).

Let _N_ denote the total number of uncertain pairs produced by the algorithm. As shown above, the number of uncertain pairs for a subproblem \(T(m',n')\) is \(O(m'n'/r')\), which is _O_(_q_<sup>2/3</sup>_g_<sup>8</sup>) because \(r'=m'/g^6\) and \(n'\le q^{2/3}g^2\). It follows that the number of uncertain pairs associated with a subproblem _T(q,q_) in Recurrence (6) is _O(q_<sup>4/3</sup>_g_<sup>4</sup>). Since _g_=log<sup>(_i_-2)</sup>_q_ and _q_=log<sup>6</sup>log_n_, the total number of uncertain pairs in the entire algorithm is _N=O(n_<sup>4/3</sup>(log<sup>(_i_)</sup>_n_)<sup>4</sup>). Hence, for some constant _c\>_0, \(N\le c\cdot n^{4/3}(log^{(i)}n)^4\). By the assumption of Theorem 3, \(|S\cap I|\ge c_1\cdot n^{4/3}(log^{(i)}n)^4\). Therefore,

\(N\le\frac{c}{c_1}|S\cap I|.\)

Let _M_ denote the number of pairs recorded in \(\Gamma\), i.e., \(M=\sum_{A_t\times B_t\in\Gamma}|A_t||B_t|\).

Partition _M_ into two parts:

• _M_<sub>1</sub>: the number of pairs recorded by bicliques produced before the subproblems \(T(m',n')\);<tbc>

• _M_<sub>2</sub>: the number of pairs recorded by the capture-cell bicliques produced inside the subproblems \(T(m',n')\).

Hence _M=M_<sub>1</sub>+_M_<sub>2</sub>.

Every pair of \(S\cap I\) belongs to exactly one of the following categories:

