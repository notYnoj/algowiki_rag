<tbc>and the worst-case space exponent, defined analogously, can be expressed as

\(max\left\{max_{\ell^\prime\in(0,1/2]\cup(\gamma_1,1]}\frac{H(\ell')+\ell'}{4},max_{\ell^\prime\in(1/2,\gamma_1]}\sigma_\text{rrb}\left(\ell',max\{0,\ell'-\alpha_1\}\right)\right\}.\)

Both are maximized at \(\ell'=\gamma_1\). At this point, the time exponent is upper-bounded by \(\frac{H(\gamma_1)+\gamma_1}{2}=\tau_\text{rrb}\left(\gamma_1,\gamma_1-\alpha_1\right)\le 0.76502\), and the space exponent is upper-bounded by \(\sigma_\text{rrb}\left(\gamma_1,\gamma_1-\alpha_1\right)=\alpha_1\le 0.64738\). Therefore, the worst-case time complexity is \(O^*(2^{0.76502n})\le O^*(1.6994^n)\), and the worst- case space complexity is \(O^*(2^{0.64738n})\le O^*(1.5664^n)\).

## 4 Faster Polynomial-Space Algorithm

For algorithms restricted to poly(_n_) space, we can employ the low-space element distinctness algorithm. This algorithm was introduced in \[7\], generalized in \[5\], and later freed from non-standard assumptions in \[11, 23\]. Lemma 4.1 can be inferred from \[11, Section 4.2, proof of Theorem 1.1\]. The same extracted lemma is also stated in \[22, Theorem 12\].

**Lemma 4.1** (\[11\])**.** _Given random access to an array of N nonnegative integers a_<sub>1</sub>_,...,a<sub>N</sub>, with_ \(a_i\le poly(N)\) _for all_ \(i\in[N]\)_, suppose that the array contains at least one colliding pair, that is, a pair_ (_i,j_) _with_ \(i\neq j\) _and a<sub>i</sub>=a<sub>j</sub>. Then there is a Monte Carlo algorithm that reports such a pair using only_ polylog(_N_) _space and_

\(O\left(\frac{N\sqrt{F_2}}{F_2-N}polog(N)\right)\)

_time, where_ \(F_2=\sum_{i=1}^N\sum_{j=1}^N\mathbf{1}[a_i=a_j]\) _is the second frequency moment. In particular, under the above assumption,_ \(F_2\in[N+2,N^2]\).

Although the statement in \[11\] is phrased for positive integers, the same bound applies to nonnegative integers by adding 1 to every array entry, which preserves all collisions. We apply Lemma 4.1 to the 2_<sup>n</sup>_ subset sums of _S_ to obtain Theorem 4.2.

**Theorem 4.2.** _Let_ \(\ell'\) _be the minimum solution ratio. Then there is a Monte Carlo algorithm for ESS that runs in_ \(O^*(2^{(\ell^\prime+1/2)n})\) _time using polynomial space._

_Proof._ We provide random access to the list _L_ of all subset sums of _S_={_w_<sub>1</sub>_,...,w<sub>n</sub>_} by computing each element on the fly. Specifically, for each index \(i\in[N]\), where _N_=2_<sup>n</sup>_, let

\(X_i=\{j\in[n]|\text{the}j\text{-th least significant bit of the binary representation of}i-1\text{is}1\}.\)

Then the _i_-th element of _L_ is computed as \(L_i=\sum_{j\in X_i}w_j\). This gives random access to _L_ using polylog(_N_) time and space. We apply Lemma 4.1 to _L_. A colliding pair in _L_ corresponds exactly to two distinct subsets of _S_ with equal sum, and hence yields an ESS solution.

It remains to bound the running time. Let \(A,B\subseteq S\) be a minimum solution, so that \(|A\cup B|=\ell'n\). Let \(Z=S\backslash(A\cup B)\); then \(|Z|=(1-\ell')n\). For every subset \(Z'\subseteq Z\), the two subsets \(A\cup Z'\) and \(B\cup Z'\) have equal sum. Therefore, these pairs contribute at least \(2^{|Z|}=2^{(1-\ell^\prime)n}\) nontrivial terms to _F_<sub>2</sub>, and hence \(F_2\ge N+2^{(1-\ell^\prime)n}\). Since the function \(\sqrt{x}/(x-N)\) is monotonically decreasing for \(x\in[N+2,N^2]\), we can upper-bound the running time by setting \(F_2=N+2^{(1-\ell^\prime)n}\). Thus,

\(O\left(\frac{N\sqrt{F_2}}{F_2-N}polog(N)\right)\le O\left(\frac{2^n\sqrt{2^n+2^{(1-\ell^\prime)n}}}{2^{(1-\ell^\prime)n}}poly(n)\right)\le O^*(2^{(\ell^\prime+1/2)n}).\)

Hence, the algorithm runs in \(O^*(2^{(\ell^\prime+1/2)n})\) time and uses polynomial space.

