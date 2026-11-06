<tbc>be simulated in _M_ words, with a constant number of physical transfers per logical transfer. For input and output of total size _L_ words, layout conversion costs _O_(1+_L/B_) transfers. Polynomial disk space is preserved. Moreover,

\(log(\widehat{M}/\widehat{B})=\Theta(log(M/B)),log\widehat{M}=\Theta(logM).\)

The hidden constants depend only on the fixed simulation parameters.

_Proof._ Choose \(K\ge 4R_0\) and then _C_<sub>∗</sub> large enough that \(\widehat{M}\ge M/8\ge max\{R_0,C_0\}\). If \(B\ge K\), then \(\widehat{M}/\widehat{B}\ge KM/(8B)\ge K/4\ge R_0\); if _B\<K_, then \(\widehat{B}=1\) and the conclusion again follows. Also \(B/(2K)\le\widehat{B}\le B\), so block size changes by only a fixed factor.

Store each logical block in the first \(\widehat{B}\) words of its own physical block. The algorithm state uses at most _M/_4 words, transfers use one buffer of \(B\le M/2\) words, and the remaining memory stores control information. After reading a physical block, copy its valid portion into working memory; reuse the same transfer buffer for writes. Each logical transfer therefore takes a constant number of physical transfers.

For initial layout conversion, extract logical blocks one at a time. Their words span at most two original physical blocks, which are read sequentially into working memory before reusing the transfer buffer to write the logical block. To restore packed output, read, modify, and write boundary blocks. Both conversions take a constant number of transfers per logical block, for \(O(1+L/\widehat{B})=O(1+L/B)\) in total. Space expands by at most 2_K_, and addresses still occupy _O_(log_N_) bits.

Finally, \(M/(8B)\le\widehat{M}/\widehat{B}\le KM/(2B)\), both memory-to-block ratios are at least two, and \(\widehat{M}=\Theta(M)\). These give the logarithmic relations.

We now apply the simulation lemma to the complexity expressions in the main text. This checks the effect of parameter substitution rather than proving the algorithms again.

**Corollary A.3** (Parameter transfer)**.** Suppose the address-field interchange, local sorting, and large-input sorting bounds in the main text hold for sufficiently large _M_ and _M/B_. The simulation of Lemma A.2 preserves these bounds and yields the main bound (2) in the original parameters. Address-field interchange only requires increasing its absolute memory threshold; each sorting bound applies to every \(2B\le M\) under its original input-size condition.

_Proof._ For a _V_ -bit array, layout conversion costs _O_(1+_V/(Bw_)) transfers. Apply the address- field interchange bound at \(\widehat{M},\widehat{B}\). Since \(1/\widehat{B}=O(1/B)\) and the logarithms are comparable, this gives (14); it suffices to increase _C_<sub>abs</sub> to at least _C_<sub>∗</sub>.

First assume \(M\ge C_*\), and write _a_=log(_M/B_), _h_=log_M_, and _p_=log(_N/M_). The adjusted parameters satisfy \(\widehat{a}=\Theta(a)\), \(\widehat{h}=\Theta(h)\), \(\widehat{p}=p+O(1)\), and \(1/\widehat{B}=O(1/B)\).

For local sorting, if \(1\le n\le\widehat{M}^2\), apply (19) directly. If \(\widehat{M}^2<n\le M^2\), use \(\widehat{M}\ge M/8\) to divide the input into at most 64 subarrays, each of size at most \(\widehat{M}^2\). Sort them individually and perform a constant number of two-way merge rounds. Subarrays fitting in memory are sorted directly. Logical memory holds the fixed number of merge buffers, and each round costs \(O(1+n/\widehat{B})\) transfers. Since the number of subarrays is fixed, the total cost, including startup, merging, and layout conversion, is

\(O\big(1+\frac{n}{B}[1+(h/a)^\tau]\big),\)

which is (19) in the original parameters. This transfer uses only local sorting and merging, without depending on general sorting.

