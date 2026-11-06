### 2.3 Putting everything together

Finally, we use halvers to obtain a deterministic divide-and-conquer algorithm for subset sum (which may be viewed as a variant of Bringmann’s randomized algorithm \[Bri17\]):

**Lemma 2.6.** _Given a set X of integers in_ \[_u_\] _and a number k, we can compute a set_ \(\mathrm{OUT}\subseteq[ku]\) _such that_ \(\Sigma_{\le k}(X)\subseteq\mathrm{OUT}\subseteq\Sigma(X)\)_, in_ \(\widetilde{O}(ku)\) _deterministic time._

_Proof._ The algorithm proceeds as follows:

1. Compute a (_k,k/_log_k_)-halver \((X',X'')\) of _X_ in \(\widetilde{O}(u)\) time, by applying Lemma 2.5 with _b_=log_<sup>c</sup>(ku_) for a sufficiently large constant _c_ (assuming _k\>b_).<tbc>

2. Recursively solve the problem for the input set \(X'\) and number _k/_2+_k/_log_k_; let \(\mathrm{OUT}'\subseteq[ku]\) be the output set. Recursively solve the problem for the input set \(X''\) and number _k/_2+_k/_log_k_; let \(\mathrm{OUT}''\subseteq[ku]\) be the output set.<tbc>

3. Return the clipped sumset \(\mathrm{OUT}=(\mathrm{OUT}'+\mathrm{OUT}'')\cap[ku]\), which can be computed by a convolution two Boolean vectors of length _O(ku_) in \(\widetilde{O}(ku)\) time.

The running time satisfies the recurrence:

\(T(k,u)=2T(k/2+k/\mathrm{log}k,u)+\widetilde{O}(ku).\)

For the base case \(k\le b\) (which implies \(k\le\mathrm{log}^{O(1)}u\)), we can use Lemma 2.1 to compute \(\Sigma_{\le k}(X)\) in \(\widetilde{O}(u)\) time and thus get \(T(k,u)=\widetilde{O}(u)\). The recurrence solves to \(T(k,u)=\widetilde{O}(ku)\).

To prove correctness, consider a subset \(S\subseteq X\) with \(|S|\le k\) and \(\sigma(S)=y\). By definition of halver, there exists a subset \(\hat{S}\subseteq X\) with \(|\hat{S}|\le k\), \(\sigma(\hat{S})=y\), and \(|\hat{S}\cap X'|,|\hat{S}\cap X''|\le k/2+k/\mathrm{log}k\). Then \(\sigma(\hat{S}\cap X')\in\mathrm{OUT}'\) and \(\sigma(\hat{S}\cap X'')\in\mathrm{OUT}''\) by induction, and so \(y=\sigma(\hat{S}\cap X')+\sigma(\hat{S}\cap X'')\in\mathrm{OUT}\).

**Theorem 2.7.** _Given a set X of n integers in_ \[_t_\]_, we can compute_ \(\Sigma(X)\cap[t]\) _in_ \(\widetilde{O}(t)\) _deterministic time._

_Proof._ For each \(i\in[\lceil\mathrm{log}t\rceil]\), let \(X_i=X\cap(t/2^i,t/2^{i-1}]\). Compute \(\Sigma(X_i)\cap[t]\) by applying Lemma 2.6 with _u=t/_2<sup>_i_-1</sup> and _k_=2_<sup>i</sup>_ in \(\widetilde{O}(2^i\cdot t/2^{i-1})=\widetilde{O}(t)\) time (this is because \(\Sigma(X_i)\cap[t]=\Sigma_{\le 2^i}(X_i)\cap[t]\) when \(X_i\subseteq(t/2^i,\infty)\)). We return the clipped sumset \(((\Sigma(X_0)\cap[t])+(\Sigma(X_1)\cap[t])+\cdots)\cap[t]\), which can be computed by _O_(log_t_) convolutions of Boolean vectors of length _O(t_) in \(\widetilde{O}(t)\) time.

## 3 Output-Sensitive Algorithms

In this section, we describe another application of our technique: the derandomization of a recent output- sensitive algorithm for all-targets subset sum by Bringmann, Fischer, and Nakos \[BFN25\], which runs in \(\widetilde{O}(|\Sigma(X)\cap[t]|\sqrt{n})\) time. An earlier output-sensitive algorithm by Bringmann and Nakos \[BN20\], which runs in \(\widetilde{O}(|\Sigma(X)\cap[t]|^{4/3})\) time, can also be derandomized in a similar way, as we will briefly mention at the end.

