### Preprocessing Algorithm

The preprocessing algorithm (Algorithm 1) constructs log(_n_)+1 hash tables just like in Section 2. The \(\ell\)-th hash table corresponds to window size \(2^\ell\); we use a rolling hash function (e.g. Rabin fingerprint) to construct a hash table of all contiguous substrings of _X_ of length \(2^\ell\) in time _O(n_). Since there are log_n_+1 levels, the overall preprocessing time is _O(n_log_n_). Let \(H_A[\ell]\) store all the hashes for windows of length \(2^\ell\) of _A_ and similarly \(H_B[\ell]\) stores all the hashes for windows of length \(2^\ell\) of _B_.

### Answering Equal(_i,d_) in _O_(log_n_) time

_Equal(i,d_) queries can be implemented by doing a simple binary search over the presorted hashes in _O_(log_n_) time. The pseudocode is given below. Suppose _Equal(i,d_)=_q_. The first While loop (line 5-8) identifies the smallest \(\ell\ge 0\) such that \(q<2^\ell\). The next While loop does a binary search for _q_ between \(i+2^{\ell-1}\) to \(i+2^\ell\).

\(n\leftarrow\text{length}(A)\)<br>
\(\text{ASStart}\leftarrow i\text{,}\text{BStart}\leftarrow i+d\)<br>
\(\ell\leftarrow 0\)<br>
while \(\ell<\text{log}(n)\) do<br>
   if \(H_A[\ell][\text{ASStart}]\neq H_B[\ell][\text{BStart}]\) then<br>
break<br>
   \(\ell\leftarrow\ell+1\)<br>
  \(\text{ASStart}\leftarrow i+2^{\ell-1}\), \(\text{BStart}\leftarrow i+d+2^{\ell-1}\)<br>
  \(\text{AEEnd}\leftarrow i+2^\ell-1\), \(\text{BEEnd}\leftarrow i+d+2^\ell-1\)<br>
  \(\text{Mid}\leftarrow\frac{(\text{AEEnd-ASStart+1})}{2}\)<br>
while \(\text{Mid}\ge 1\) do<br>
   if H<sub>A</sub>\[Mid\]\[ASstart\] == H<sub>B</sub>\[Mid\]\[BStart\] then<br>
  \(\text{ASStart}\leftarrow\text{ASStart}+\text{Mid}\), \(\text{BStart}\leftarrow\text{BStart}+\text{Mid}\)<br>
   else<br>
  \(\text{AEEnd}\leftarrow\text{AEEnd-Mid-1}\), \(\text{BEEnd}\leftarrow\text{BEEnd}-\text{Mid-1}\)<br>
  \(\text{Mid}\leftarrow\frac{(\text{AEEnd-ASStart+1})}{2}\)<br>
return AEEnd

Implementing _Equal(i,d_) query in _O_(log_n_) time together with the correctness proof of _O(n+k_<sup>2</sup>) algorithm leads to Theorem 3.

## 4 Preprocessing a Single String: Answering Gap Edit Distance in Sublinear Time

In this section, we design an algorithm that given two strings _A_ and _B_, preprocess only one string, say _B_. During the query phase, the string _A_ is provided, and a query algorithm must answer whether \(\text{ED}(A,B)\le k\) or \(\text{ED}(A,B)\ge 2k^2\). We give an algorithm for this quadratic gap-edit distance problem that runs in \(\tilde{O}(\frac{n}{k}+k^2)\) time. Therefore, the algorithm achieves a sublinear query time whenever \(k\le n^{1/2}\) and \(k\ge\text{polylogn}n\). Note that this problem was recently studied in \[GKS19\] without any preprocessing. They achieve a running time bound of \(\tilde{O}(\frac{n}{k}+k^3)\).

**Algorithm 4:** Equal(_i,d,A,H<sub>A</sub>,B,H<sub>B</sub>_)

