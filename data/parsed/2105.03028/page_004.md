## 23:4 Improved Approximation for Longest Common Subsequence over Small Alphabets

Now, let us describe our algorithm. Given _A_ and _B_, we consider all subsets of the alphabet consisting of precisely \(\ell\) symbols (one of these subsets will be _x_.) For each such collection _y_, consider the sub-instance of the LCS instance restricted to the symbols of _y_. Let OPT(_y_) be the optimal LCS for this instance.

We know that \(|\mathrm{OPT}(x)|\ge|C_x|\ge(\ell/s)|C|\). So when we consider _y=x_, if we can efficiently obtain an \(1/(\ell-\epsilon)\) approximation for OPT(_x_), we will get a common subsequence of _A_ and _B_ of length at least

\(\frac{|\mathrm{OPT}(x)|}{\ell-\epsilon}\ge\frac{|C|}{s(1-\epsilon/\ell)},\)

and thus yields the desired approximation for the LCS of _A_ and _B_. The running time is multiplied by \(\genfrac(){pt}{2}{s}{\ell}\) which is a constant, as long as _s_ is. \(\blacktriangleleft\)

By setting \(\epsilon=\ell\delta s/(1+\delta s)\) in the above Theorem statement, we obtain a linear time reduction from obtaining a \(1/s+\delta\)-approximation for _s_-ary strings to a \(1/\ell+(\delta s)/\ell\)-approximation for \(\ell\)-ary strings. We obtain Theorem 1 as a corollary:

\(\blacktriangleright\) **Corollary 5.** _Fix an integer_ \(s\ge 3\) _and a constant_ \(\delta>0\)_. The problem of obtaining a_ \(1/s+\delta\) _approximation for the LCS of two strings from an alphabet of size s can be reduced in linear time to the problem of obtaining a_ \(1/2+(\delta s)/2\) _approximation for the LCS of two strings binary strings (i.e. strings from an alphabet of size two)._

**Proof.** This follows from Theorem 4 by taking \(\ell=2\). The reduction has _O(s_<sup>2</sup>) overhead. \(\blacktriangleleft\)

The reason we cannot prove Theorem 2 by combining Corollary 5 with the result of [21] is that the latter gives a better than 1/2 approximation for strings from an alphabet of size 2 only when the input strings have _equal length_. Note that in the reduction from the proof of Theorem 4, the subsequences obtained from restrictions to subalphabets may be of different lengths even if the original strings have equal lengths.

Although at first it may seem that extending the Rubinstein-Song result to strings of differing length should not be too hard, generalizing the result does not appear straightforward. In the following we will discuss why this not simple. The main hurdles come from the lemma and algorithm used in [21] stated below.

\(\blacktriangleright\) **Lemma 6** (LCS and Edit Distance Connection)**.** _For any strings X and Y of length n and m respectively, we have_

\(2\cdot\mathrm{LCS}(X,Y)+\mathrm{ED}(X,Y)=n+m.\)

For the sake of completeness, we include a proof of the above lemma.

**Proof.** Consider an optimal alignment between _X_ and _Y_ , which matches the maximum possible number of characters of _X_ with identical characters of _Y_ while respecting the order in which the characters appear in each string. The characters that are matched in _X_ and _Y_ correspond to a longest common subsequence. This is because if there were a longer common subsequence, we could get a larger alignment by matching the characters of the subsequence in _X_ and _Y_ , but this would contradict the optimality of _X_ and _Y_ .

Similarly, the unmatched characters correspond to a minimum set of symbols that need to be deleted from _X_ and inserted from _Y_ to turn _X_ into _Y_ . If there were a smaller edit distance computation, then all the characters which were not deleted or inserted could be paired up to form a larger alignment, again contradicting optimality.

