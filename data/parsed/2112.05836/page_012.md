Effectively, Lemma 4.3 says that there is a near-optimal alignment that aligns the windows of _X_<sub>1</sub> to substrings of the other strings that are not more than \(1/\epsilon^2\) times larger.

_Proof._ We partition _X_<sub>1</sub> into substrings of length \(\tau\), \(\{X_{1,j}\}_{j\in[J]}\). _X_<sup>∗</sup> can be partitioned into substrings \(\{\tilde{X}_j^*\}_{j\in[J]}\) such that \(\delta_E(X_1,X^*)=\sum_{j\in[J]}\delta_E(X_{1,j},\tilde{X}_j^*)\).

First, we will "realign" _X_<sub>1</sub> and _X_<sup>∗</sup> to ensure no \(\tilde{X}_j^*\) is much larger than _X_<sub>1_,j_</sub>. Call a contiguous subsequence of \[_J_\], \([j..j']:=\{j,j+1,\dots j'\}\), "skewed" if \(\sum_{m\in[j..j^\prime]}|X_{1,m}|<\frac{\epsilon}{2}\sum_{m\in[j..j^\prime]}|\tilde{X}_m^*|\). Let us take a "maximal" set _S_ of disjoint skewed contiguous subsequences, i.e. a set _S_ such that (i) all the subsequences in _S_ are disjoint (ii) for every contiguous subsequence _s_ in _S_, there is no skewed contiguous subsequence \(s'\) such that \(s\subset s'\) and (iii) there is no skewed contiguous subsequence that is not in _S_ but also is completely disjoint from every element of _S_.

For each skewed contiguous subsequence \([j..j']\) in _S_, note that \(j'+1\) does not appear in any element of _S_ (otherwise, \([j..j']\) and this element can be combined to form a longer skewed contiguous subsequence, violating (ii)), and \([j..j'+1]\) is not skewed (again, \([j..j'+1]\) being skewed would violate (ii) since \([j..j']\subset[j..j'+1]\)). Take _S_ and replace each \([j..j']\) with \([j..j'+1]\) to get \(S'\). For each \([j..j'+1]\in S'\), we have:<tbc>

\(\frac{\epsilon}{2}\sum_{m\in[j..j^\prime+1]}|\tilde{X}_m^*|\le\sum_{m\in[j..j^\prime+1]}|X_{1,m}|\le 2\sum_{m\in[j..j^\prime]}|X_{1,m}|<\epsilon\sum_{m\in[j..j^\prime+1]}|\tilde{X}_m^*|.\) (1)

<tbc>The right-hand side of (1) implies:<tbc>

\(\delta_E(\circlearrowleft_{m\in[j..j^\prime+1]}X_{1,m},\circlearrowleft_{m\in[j..j^\prime+1]}\tilde{X}_m^*)\ge(1-\epsilon)|\circlearrowleft_{m\in[j..j^\prime+1]}\tilde{X}_m^*|.\)

<tbc>It also implies that for any partition of \(\circlearrowleft_{m\in[j..j^\prime+1]}\tilde{X}_m^*\) into substrings \(\{X_m^*\}_{m\in[j..j^\prime+1]}\), we have:<tbc>

\(\sum_{m\in[j..j^\prime+1]}\delta_E(X_{1,m},X_m^*)\le(1+\epsilon)|\circlearrowleft_{m\in[j..j^\prime+1]}\tilde{X}_m^*|.\)

<tbc>And so if \(\epsilon\) is sufficiently small:

\(\sum_{m\in\cup_{e\in S^\prime} e}\delta_E(X_{1,m},X_m^*)\le\frac{1+\epsilon}{1-\epsilon}\sum_{m\in\cup_{e\in S^\prime} e}\delta_E(X_{1,m},\tilde{X}_m^*)\le(1+3\epsilon)\sum_{m\in\cup_{e\in S^\prime} e}\delta_E(X_{1,m},\tilde{X}_m^*)\)

In particular, because of the left-hand side of (1), we can choose the partition of \(\circlearrowleft_{m\in[j..j^\prime+1]}\tilde{X}_m^*\) that splits it into substrings \(\{X_m^*\}_{m\in[j..j^\prime+1]}\), each of length at most \(2\tau/\epsilon\).

Now if we set \(X_m^*=\tilde{X}_m^*\) for any _m_ not in a subsequence in \(S'\), we trivially have:<tbc>

\(\sum_{m\notin\cup_{e\in S^\prime} e}\delta_E(X_{1,m},X_m^*)\le\sum_{m\notin\cup_{e\in S^\prime} e}\delta_E(X_{1,m},\tilde{X}_m^*)\)

<tbc>And also \(X_m^*\le 2\tau/\epsilon\) for all such _m_ (otherwise, _m_ should appear in some subsequence in \(S'\) by condition (iii)). So we’ve found a partition of _X_<sup>∗</sup> into substrings \(\{X_j^*\}_{j\in[J]}\) such that \(|X_j^*|\le\frac{1}{\epsilon}|X_{1,j}|\) for all _j_, and:<tbc>

\(\sum_{j\in[J]}\delta_E(X_{1,j},X_j^*)\le(1+3\epsilon)\sum_{j\in[J]}\delta_E(X_{1,j},\tilde{X}_j^*).\)

<tbc>Now, we will use this partition to determine \(\{X_{i,j}\}_{i>1,j\in[J]}\). For each _i_, _X<sub>i</sub>_ can be partitioned into substrings \(X'_{i,j}\) such that \(\delta_E(X_i,X^*)=\sum_{j\in[J]}\delta_E(X'_{i,j},X_j^*)\). If \(|X'_{i,j}|\le 2\tau/\epsilon^2\), we set \(X_{i,j}=X'_{i,j}\). If any \(X'_{i,j}\) has length larger than \(2\tau/\epsilon^2>|X_j^*|/\epsilon\), then \(\delta_E(X'_{i,j},X_j^*)\ge(1-\epsilon)|X'_{i,j}|\). On the other hand:

\(\delta_E(\gamma,X_j^*)+|X'_{i,j}|\le(1+\epsilon)|X'_{i,j}|\le\frac{1+\epsilon}{1-\epsilon}\delta_E(X'_{i,j},X_j^*)\le(1+3\epsilon)\delta_E(X'_{i,j},X_j^*)\)

for the empty string \(\gamma\). So we can now choose _X<sub>i,j</sub>_ to be any empty substring of \(X'_{i,j}\). These choices of _X<sub>i,j</sub>_ give the properties of the lemma, completing the proof.

Let W<sub>1</sub> be the set of all windows we partition _X_<sub>1</sub> into, and W_<sub>i</sub>_ be the set of windows we define for _X<sub>i</sub>_. Let `s`(_W_) denote the index of the first character in _W_, and `e`(_W_) denote the index of the last character. For _k_ strings, we define a window-respecting alignment as follows:

