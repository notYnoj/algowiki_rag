\(\blacktriangleright\) **Lemma 33** (time of one access)**.** _The time to search for X<sub>i</sub> is_

\(O\big((a^{(X_i)}+\frac{logn}{k})\cdot(logk+1)\big).\)

**Proof.** We first compute the time that the algorithm spends within a subtree \(\mathcal{T}_\ell^{(X_i)}\) for any \(\ell\in[\lceil h_{X_i}/k\rceil]\). Since \(\mathcal{T}_\ell^{(X_i)}\) has height _k_, the cost of each operation of an auxiliary tree is _O_(log_k_+1). The algorithm needs to make at least one search operation in one auxiliary tree, and apart from this, the algorithm also needs to make _O_(1) operations whenever a preferred child is changed, so the search time of _X<sub>i</sub>_ within the subtree \(\mathcal{T}_\ell^{(X_i)}\) is

\(O\big((a_\ell^{(X_i)}+1)(1+logk)\big).\)

Thus the total search time of _X<sub>i</sub>_ is

\(\sum_{\ell=1}^{\lceil h_{X_i}/k\rceil} O\big((a_\ell^{(X_i)}+1)(1+logk)\big)=O\big((a^{(X_i)}+\frac{logn}{k})\cdot(logk+1)\big),\)

where we used the fact that \(h_{X_i}\le logn\) and \(a^{(X_i)}=\sum_{\ell=1}^{\lceil h_{X_i}/k\rceil} a_\ell^{(X_i)}\). \(\blacktriangleleft\)

Since \(\mathsf{Alt}_\mathcal{T}(X)=\sum_{i=1}^ma^{(X_i)}\), we can easily compute the total access time.

\(\blacktriangleright\) **Lemma 34** (total time)**.** _The total access time of the sequence_ \(X=(X_1,\cdots,X_m)\) _is_

\(O\big((\mathsf{Alt}_\mathcal{T}(X)+m\cdot\frac{logn}{k})\cdot(logk+1)\big).\)

