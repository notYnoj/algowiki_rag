zeros and \(0.01\cdot 2^k\) ones. Passing to only these subintervals, we conclude that _x_ contains a subsequence of the form \(x'=x_1x_2\cdots x_{0.2\cdot 2^{K-k}}\) where each _x<sub>i</sub>_ contains \(0.01\cdot 2^k\) zeros and \(0.01\cdot 2^k\) ones. A string of the form \((1^\ell 0^\ell)^a\) can be found as a subsequence of \(x'\) by taking ones from the first \([100\ell/2^k]x_i\)’s, then zeros from the next \([100\ell/2^k]\), and so on. Since \(\ell\ge 2^{k-6}\), we can pick

\(a\ge\frac{0.2\cdot 2^{K-k}}{2[100\ell/2^k]}\ge 10^{-4}w/\ell,\)

as desired.

Combining the above two claims proves that if case 1 of the lemma does not hold, then case 2 does for \(\ell=2^{max(0,k_0-5)}\).

