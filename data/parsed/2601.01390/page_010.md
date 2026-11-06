4. Return \((A+\Sigma(X_L))\cap[t]\), which can be computed by applying Lemma 3.3 with _k=r_<sup>6</sup>log_<sup>c</sup>t_ in \(\widetilde{O}(r^{O(1)}|\Sigma(X)\cap[t]|\sqrt{n})\) deterministic time (this is because \(\Sigma(X_L)\cap[t]=\Sigma_{\le r^6\mathrm{log}^c t}(X_L)\cap[t]\) when \(X_L\subseteq(t/(r^6\mathrm{log}^ct),\infty)\)).<tbc>

<tbc>Bringmann, Fischer, and Nakos \[BFN25\] proved that

\(|(\Sigma(X_1)\cap[t/r(1+1/r)])+\cdots+(\Sigma(X_r)\cap[t/r(1+1/r)])|\le|\Sigma(X_1\cup\cdots\cup X_r)\cap[t]|^{1+1/(r-1)}\)

by using a "submultiplicativity" property for sumsets due to Gyarmati, Matolcsi, and Ruzsa \[GMR10\]. Thus, \(|A|=|A_1+\cdots+A_r|\le|\Sigma(X)\cap[t]|^{1+1/(r-1)}\). Bringmann, Fischer, and Nakos further noted that \(|A_1|+\cdots+|A_r|\le|A_1+\cdots+A_r|+r-1\).

Thus, the running time for \(\mu=|\Sigma(X)\cap[t]|\) satisfies the recurrence

\(T(n,t,\mu)\le\mathrm{max}_{n_1,\dots,n_r,\mu_1,\dots,\mu_r:n_1+\cdots+n_r\le n,\mu_1+\cdots+\mu_r\le\mu^{1+1/(r-1)}+r-1}\big(T(n_1,t/r+t/r^2,\mu_1)+\cdots+T(n_r,t/r+t/r^2,\mu_r)+\widetilde{O}(r^{O(1)}\cdot(\mu^{1+1/(r-1)}+\mu\sqrt{n}))\big).\)

By choosing _r_=log<sup>2</sup>_t_+1, we have \(\mu^{1/(r-1)}\le 2^{\mathrm{log}\mu/\mathrm{log}^2t}\le 2^{1/\mathrm{log}t}=1+O(1/\mathrm{log}t)\), and the recurrence solves to \(T(n,t,\mu)=\widetilde{O}(\mu\sqrt{n})\).

To close, we mention that another output-sensitive subset sum algorithm by Bringmann and Nakos \[BN20\] can be similarly derandomized. They described a (more complicated) alternative to Lemma 3.2 on output- sensitive construction of clipped sumsets, running in \(\widetilde{O}(|C|^{4/3})\) time (their construction is deterministic, if a deterministic version of Lemma 3.1 is used). By replacing Lemma 3.2, keeping the rest of the algorithm the same, and straightforwardly modifying the above analysis, we immediately obtain:

**Theorem 3.11.** _Given a set X of n integers in_ \[_t_\]_, we can compute_ \(\Sigma(X)\cap[t]\) _in_ \(\widetilde{O}(|\Sigma(X)\cap[t]|^{4/3})\) _deterministic time._

## 4 Remarks

In the \(\widetilde{O}(t)\)-time algorithm in Section 2, we have not tried to optimize (and thus have not written out) the number of log_t_ factors. It is larger than the previous randomized algorithms (Bringmann’s algorithm \[Bri17\] had 4 log factors, and Jin and Wu’s algorithm \[JW19\] had 2), but is not gigantic (probably below 20).

In the output-sensitive algorithms in Section 3, we reiterate that the hidden extra factors are polylogarithmic in _n_ and _t_. The previous randomized algorithms by Bringmann, Fischer, and Nakos \[BFN25\] actually got factors that are polylogarithmic in the output size \(|\Sigma(X)\cap[t]|\) rather than in _t_; this seems harder to do from the derandomization perspective (but would not make a big difference except in some extreme cases).

Like previous work, our algorithms easily adapt to the setting when _X_ is a multiset--a subset of _X_ cannot use an element more times than its original multiplicity. (Note that _n_ could be larger than _t_ here, and to avoid an _O(n_) term in the running time, we may need to assume that _X_ is represented as a list of distinct elements with given multiplicities.)

In the \(\widetilde{O}(t)\)-time algorithm in Section 2, we generate canonical subsets by adapting Koiliaris and Xu’s algorithm \[KX19\], but in Section 3, we have realized that Koiliaris and Xu’s algorithm is not essential to our technique (though it is convenient, since it already incorporates dyadic intervals). This realization may potentially help in future applications.

