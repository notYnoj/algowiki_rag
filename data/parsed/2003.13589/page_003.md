Then, our goal is to compute \(dp_{|\sigma|}[n][n]\).

All \(|\sigma|\cdot n^2\) entries in _dp_ can be calculated in O(1) time each using the following recurrence:

\(dp_{v+1}[i][j]=\left\{\begin{array}{ c c }
\mathrm{max}\{dp_v[i][j],dp_v[i-1][j-1]+1\}, & \text{if}A[i]=B[j]=\sigma[v+1], \\
\mathrm{max}\{dp_v[i][j],dp_{v+1}[i-1][j],dp_{v+1}[i][j-1]\}, & \text{otherwise.}
\end{array}\right.\)

In order to decrease the time we will speed up calculating _dp_<sub>_v_+1</sub> from _dp<sub>v</sub>_. Because calculating _dp_<sub>_v_+1</sub> only requires the knowledge of _dp<sub>v</sub>_, we will only keep the current _dp<sub>v</sub>_ and update all of its entries to obtain _dp_<sub>_v_+1</sub>.

**Lemma 3.1.** \(0\le dp_v[i][j]-dp_v[i][j-1]\le 1\) _and_ \(0\le dp_v[i][j]-dp_v[i-1][j]\le 1\).

_Proof._ A subsequence of _B_\[1..(_j_-1)\] is still a subsequence of _B_\[1.._j_\], so \(dp_v[i][j-1]\le dp_v[i][j]\). Consider a sequence _C_ corresponding to _dp<sub>v</sub>_\[_i_\]\[_j_\], and let \(C'\) be _C_ without the last element. Because _C_ is a subsequence of _B_\[1.._j_\], \(C'\) is a subsequence of _B_\[1..(_j_-1)\]. So, \(C'\) is an increasing subsequence of _A_\[1.._i_\] and _B_\[1..(_j_-1)\], hence \(|C'|\le dp_v[i][j-1]\). As \(|C|=|C'|+1\), we conclude that \(dp_v[i][j]\le dp_v[i][j-1]+1\). The second part of the lemma follows by a symmetrical reasoning.

Instead of maintaining _dp<sub>v</sub>_, we keep another table \(dp'_v[i][j]=dp_v[i][j]-dp_v[i][j-1]\) (where _dp<sub>v</sub>_\[_i_\]\[_j_\]=0 for _j\<_1). Due to Lemma 3.1, each entry of \(dp'_v\) is either 0 or 1. This allows us to store each row of \(dp'_v\) by partitioning it into O(_n/B_) blocks of length _B_, with every block represented by a bitmask of size _B_ saved in a single machine word, where \(B=\alpha\mathrm{log}n\) for some constant \(\alpha\) to be fixed later. By definition, \(dp_v[i][j]=\sum_{k=1}^jdp'_v[i][k]\). In addition to \(dp'_v\), we store the value of _dp<sub>v</sub>_\[_i_\]\[_j_\] for every block boundary, so O(_n_<sup>2</sup>_/B_) values overall. This will allow us later to recover any _dp<sub>v</sub>_\[_i_\]\[_j_\] in constant time by retrieving the value at the appropriate block boundary and adding the number of 1s in a prefix of some bitmask. We preprocess such prefix sums for every possible bitmask in \(\mathcal{O}(2^B\cdot B)\) time and space.

**Lemma 3.2.** \(0\le dp_{v+1}[i][j]-dp_v[i][j]\le 1\).

_Proof._ Because allowing using more elements cannot decrease the length, \(dp_v[i][j]\le dp_{v+1}[i][j]\). Let _C_ be a sequence corresponding to _dp_<sub>_v_+1</sub>\[_i_\]\[_j_\], and let \(C'\) be _C_ without the last element. Because _C_ is strictly increasing and \(\sigma\) consists of all distinct elements, the elements of \(C'\) are not larger than \(\sigma(v)\), so \(|C'|\le dp_v[i][j]\). Then, using \(|C'|+1=|C|\) we obtain that \(dp_{v+1}[i][j]-1\le dp_v[i][j]\).

We now describe how to calculate \(dp'_{v+1}\). We start with describing an approach that works in O(_n_<sup>2</sup>) time and then explain how to accelerate it to O(_n_<sup>2</sup>/log_n_). We use the recursion for _dp_<sub>_v_+1</sub>\[_i_\]\[_j_\] to update the rows of \(dp'_{v+1}\) one-by-one. While updating the entries in a row going from left to right we are no longer guaranteed that \(dp_{v+1}[i][j]\le dp_{v+1}[i][j+1]\), so \(dp'_{v+1}[i][j]\) can become negative. To overcome this issue, we immediately propagate each value to the right: after increasing _dp_<sub>_v_+1</sub>\[_i_\]\[_j_\] (by one due to Lemma 3.2) we also increase every _dp_<sub>_v_+1</sub>\[_i_\]\[_k_\] equal to the original value of _dp_<sub>_v_+1</sub>\[_i_\]\[_j_\], for all _k\>j_. This translates into setting \(dp'_{v+1}[i][j]\) to 1 and setting \(dp'_{v+1}[i][k]\) to 0, for the smallest _k\>j_ such that \(dp'_{v+1}[i][k]=1\). To implement this efficiently, we maintain _k_ while considering _j_=1,2_,...,n_ in O(_n_) overall time. The details of this procedure are shown in Algorithm 1.

