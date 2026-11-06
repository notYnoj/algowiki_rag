## 3. \(\frac{(e(\varphi)+3m)\cdot\lceil log(3m)\rceil}{(1-\beta)m}>2\).

Building _H_ takes O(_m_log_m_)+(_m_log_m_)<sup>O(_k_)</sup> time. Indeed, note that \(e(\varphi)\le B^2N\le 3B^2m\). So the first term in the running time corresponds to building \(G_\varphi\), and the second term, to building its _k_-th lexicographic power _H_. By Theorem 8 and Lemma 10, _H_ indeed has twin-width at most 4, and a 4-sequence of _H_ can be computed in time polynomial in \(\|H\|\).

Suppose there is an _n_<sup>O(1)</sup>-time _r_-approximation algorithm A for Max Independent Set on _n_-vertex graphs of twin-width at most 4. Our proof will work even if A has access to a 4-sequence of _H_.

Let \(\delta\le\Delta:=6(B^2+1)\) be such that

\((e(\varphi)+3m)\cdot\lceil log(3m)\rceil=\delta mlog(3m).\)

We set the constant

\(\gamma:=\frac{0.8(1-\beta)}{8(\beta+\Delta)}.\)

To conclude the proof, we assume that \(r=n^{\gamma/(loglogn)^2}\) with \(n:=|V(G_\varphi)|^k\), and proceed to refute the ETH.

When run on _H_, A returns an independent set _I<sub>H</sub>_ of _H_ of size at least \(\alpha(H)/r\). By Lemma 9, we find in time O((_m_log_m_)<sup>2_k_</sup>) an independent set _I_ of \(G_\varphi\) of size at least

\(\left(\frac{\alpha(H)}{r}\right)^{1/k}=\frac{\alpha(G_\varphi)}{r^{1/k}}.\)

We report that \(\varphi\) is satisfiable if \(|I|>\beta m+\delta mlog(3m)\), and that at most \(\beta m\) clauses of \(\varphi\) are satisfiable, otherwise.

**Running time.** Let us first verify that the overall process takes 2<sup>_o(N/_log<sup>_c_</sup>_N_)</sup>. Building _H_, optionally computing a 4-sequence of _H_, running A on _H_, finding _I_, and concluding whether \(\varphi\) is satisfiable takes time

\((mlogm)^{\mathcal{O}(k)}+n^{\mathcal{O}(1)}+\mathcal{O}((mlogm)^{2k})=m^{\mathcal{O}(m/log^{c+2}m)}=2^{\mathcal{O}(m/log^{c+1}m)}\)

and, since \(m\le BN\) and \(m\ge N/3\),

\(2^{\mathcal{O}(m/log^{c+1}m)}=2^{\mathcal{O}(BN/log^{c+1}(N/3))}=2^{o(N/log^cN)}.\)

**Correctness.** We now check that we are correct on the satisfiability of \(\varphi\), and thus conclude by Theorem 7. The crux of the argument is the following claim.

\(\vartriangleright\) Claim 11. \((m+\delta mlog(3m))\cdot\frac{1}{r^{1/k}}>\beta m+\delta mlog(3m)\).

Proof. We first recall that

\(n=|V(G_\varphi)|^k=(3m+(e(\varphi)+3m)\cdot 2\lceil log(3m)\rceil)^k\le\left(4(3B^2+6)mlog(3m)\right)^k.\)

So,

\(logn\le klogm+klog\left(4(3B^2+6)log(3m)\right)<2klog(3m),\) (1)

where the last inequality holds by Item 1. And

\(loglogn\ge logk\ge logm-loglog^{c+2}m>\frac{1}{2}log(3m),\)

