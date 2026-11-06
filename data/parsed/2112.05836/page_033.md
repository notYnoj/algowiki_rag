By Lemma 6.14 we have that the total size of the compression of these strings is _O(kd(n+n<sup>b</sup>_)). Because we have _n<sup>b</sup>_ distinct copies of _v<sub>i</sub>_ we are generating the _IVG_ strings with, so the _x_ of the lemma is _n<sup>a</sup>_ in our case. Note that _kd=n_<sup>_o_(1)</sup>. So the total size of these compressions is _O(n_<sup>1+_o_(1)</sup>+_n_<sup>_b+o_(1)</sup>)

Next, we need to analyze the size of the compression of the entire string. We use the compression of the interleave gadgets and the coordinate gadgets. In addition to this we are wrapping our interleave gadgets in an alignment gadget (from Lemma 6.12). This adds an additional _O_(lg(_n_)+_n<sup>b</sup>_) variables to the SLP.

This gives an SLP of total size of _O(n_<sup>_b+o_(1)</sup>+_n_<sup>1+_o_(1)</sup>).

Now we will now combine the previous lemmas to give the hardness of _k_-LCS with compression.

**Reminder of Theorem 1.1.** _If the_ \(k'\)_-OV hypothesis is true for all constants_ \(k'\)_, then for any constant_ \(\epsilon\in(0,1]\) _grammar-compressed k-LCS requires_ \(\left(M^{k-1}m\right)^{1-o(1)}\) _time when the alphabet size is_ \(|\Sigma|=\Theta(k)\) _and_ \(m=M^{\epsilon\pm o(1)}\)_. Here, M denotes the total length of the k input strings and m is their total compressed size._

_Proof._ Use the gadgets from Lemma 6.15. Call the strings _S_<sub>1</sub>_,...,S<sub>k</sub>_ Consider positive integers _a_ and _b_.

These have an alphabet of size _O(k_) and length _M=O(n_<sup>_a+b+o_(1)</sup>) by Lemma 6.15. These have a compression of total size _m=O(n_<sup>_b+o_(1)</sup>+_n_<sup>1+_o_(1)</sup>) by Lemma 6.16.

The size of the alphabet of the reduction is _O(k_), so if the alphabet is allowed to be size \(\Theta(k)\), then this lower bound applies.

So _M_<sup>_k_-1</sup>_m=O(n_<sup>(_k_-1)_a+kb+o_(1)</sup>). If (_bk+a(k_-1))-OV requires _n_<sup>_bk+a(k_-1)-_o_(1)</sup> time, then this corresponds to a lower bound of \(\left(M^{k-1}m\right)^{1-o(1)}\) for SLP compressed _k_-LCS.

Consider a contradiction to our theorem statement. There would be an algorithm running in \((M^{k-1}m)^{1-\gamma}\) time to solve grammar compressed _k_-LCS when \(m=M^{\epsilon\pm o(1)}\) and \(\epsilon\in(0,1]\). In the easiest case we can pick an _a,b_ such that \(b/(a+b)=\epsilon\), in this case we are done. For irrational \(\epsilon\) we need to approximate and then pad the strings. Choose an _a_ and _b_ such that \(\epsilon\le b/(a+b)<\epsilon(1+\gamma/2)\). Such _a,b_ exist that are in \(O(\frac{1}{\epsilon\gamma})\). We add a new character 3. Let \(S'_i=S_i3^x\), where we will set \(x\in[M,M^2]\) later. Note that \(\text{LCS}(S'_1,\dots,S'_k)=\text{LCS}(S_1,\dots,S_k)+x\). Note that the compression of these strings is \(m'=m+lg(x)=\Theta(m)\) where as the length is \(M'=M+x=\Theta(x)\). Choose \(x=m^{1/\epsilon\pm o(1)}=M^{b/(a+b)\cdot 1/\epsilon}\). So now \(m'=M^{1/\epsilon\pm o(1)}\). Note that \(1\le b/(a+b)\cdot 1/\epsilon\le(1+\gamma/2)\). Now consider running the claimed fast algorithm on our new \(S'_1,\dots,S'_k\) instance. The running time is

\((M^{\prime(k-1)}m')^{1-\gamma}=O((M^{(1+\gamma/2)(k-1)}m)^{1-\gamma-o(1)}).\)

This running time can be simplified to \(O(M^{(k-1)}m)^{(1+\gamma/2)(1-\gamma-o(1))}\). Note that \((1+\gamma/2)(1-\gamma-o(1))\) is less than 1-_o_(1). This algorithm violates the lower bound for the original _S_<sub>1</sub>_,...,S<sub>k</sub>_ instance. This is a contradiction.

So any algorithm running in \((M^{k-1}m)^{1-\gamma}\) time to solve grammar compressed _k_-LCS when \(m=M^{\epsilon\pm o(1)}\) and \(\epsilon\in(0,1]\) violates \(k'\)-OV for some \(k'\) that depends on \(\epsilon,\gamma\). This implies our theorem statement.

## 6.6 Easy Edit Distance Lower Bounds from LCS

In this section we will prove that _k_-median edit distance is hard from \(k'\)-LCS. We take a \(k'\)-LCS instance and add various numbers of empty strings. This pushes the _k_-median edit distance problem towards deletions. So, we increase the number of strings, but we don’t increase the total uncompressed or compressed length of the input.

Nicolas and Rivals show NP-hardness for _k_-edit distance through \(k'\)-LCS for large _k_ and \(k'\) \[NR05\]. We take inspiration from their reduction to build our own, removing some of their restrictions, and making it fine-grained efficient. We then use the hardness results we have for \(k'\)-LCS to get lower bounds for _k_-edit distance. We will be focusing on a version of edit distance where the strings are allowed to be of very different sizes. We will give an explicit definition now.

**Definition 6.17.** Given _k_ strings _S_<sub>1</sub>_,...,S<sub>k</sub>_ of lengths _M_<sub>1</sub>_,M_<sub>2</sub>_,...,M<sub>k</sub>_ the _k_-edit distance (or _k_-median edit distance) of those strings is the minimum sum across all strings of edits needed to make all strings equal some new string \(S'\). The allowed edits are deleting a character, adding a character and replacing a character (Levenshtein distance).

