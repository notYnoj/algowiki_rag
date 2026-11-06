Each value \(\mu_S(u)=\mu(S\cup\{u\})/\mu(S)\) is available because \(|S\cup\{u\}|\le 2t+4\le 2r\). The first step uses \(|S|\le 2t+3\), and the second step uses _r_=2_t_+5. There are at most (_N_+1)<sup>2_t_+4</sup> pairs, and each requires poly(_N_) arithmetic operations on rationals of bit length _N_<sup>_O(t_)</sup>.

To implement the size tests exactly, use \(2^{K^\prime}=2^{2\ell+2h+10}/9\), which is rational, as are both powers of 2 used in the size tests. No approximation of a logarithm is required. To handle arbitrarily large values of _h_ given in binary, first check whether \(h\ge\lceil\mathrm{log}N\rceil\). In that case \((2K'+1)(t+2)>\mathrm{log}N\), so a singleton already satisfies Eq. (16). Otherwise \(h<\lceil\mathrm{log}N\rceil\), and all powers needed in the tests have bit length polynomial in _t_ and log_N_. Together with Lemma 4.4, this proves the running-time bound. Finally, \(\ell\le h+3\) and log(16/3)_\<_5/2 give \(K'\le 4h+13\), so the exponent in Eq. (16) is _O(th_) for \(t,h\ge 1\).

## 4.6 Completing the proof of the main theorem

We now combine the sparse-set bound with the greedy algorithm to prove the main theorem.

**Theorem 4.6** (Formal version of Theorem 1.1)**.** _Let G be a graph on N vertices, and let t be an integer with_ \(1\le t\le\sqrt{\mathrm{log}N}/12\)_. If_ \(\alpha(G)\ge 2^{-t}N\)_, then a deterministic algorithm finds an independent set of size at least_ 2_<sup>t</sup> in time N_<sup>_O(t_)</sup>_. Consequently, a deterministic algorithm running in time_ \(N^{O(\sqrt{\mathrm{log}N})}\) _outputs an independent set of size at least_ \(\alpha(G)2^T/N\)_, where_ \(T:=\lfloor\sqrt{\mathrm{log}N}/12\rfloor\).

_Proof._ Apply Lemma 4.5 with _h_:=_t_+1. Then \(\ell\le h+3=t+4\). Since log(16/3)_\<_5/2,<tbc>

\(\Lambda'=h+\mathrm{log}\frac{16}{3}\le t+\frac{7}{2}.\)

<tbc>The first step uses the definition of \(\Lambda'\), and the second step uses _h=t_+1 and the preceding logarithm bound. Therefore<tbc>

\(K'=2(\ell+1)+2\Lambda'\le 4t+17.\)

<tbc>The first step uses the definition of \(K'\), and the second step substitutes the bounds on \(\ell\) and \(\Lambda'\). It follows that

\((2K'+1)(t+2)\le(8t+35)(t+2)\le 43t\cdot 3t=129t^2.\)

The first step uses \(K'\le 4t+17\). The second step uses \(8t+35\le 43t\) and \(t+2\le 3t\), which follow from \(t\ge 1\). The third step multiplies the constants. By Eq. (16), the output _U_ therefore satisfies \(|U|\ge 2^{-129t^2}N\) and \(d(U)\le 2^{-(t+1)}\).

The restriction on _t_ gives \(144t^2\le\mathrm{log}N\). Also \(t+1\le 2t^2\) for integers \(t\ge 1\), so

\(129t^2+t+1\le 131t^2\le\mathrm{log}N.\)

The first step uses \(t+1\le 2t^2\), and the second step uses \(131\le 144\) and \(144t^2\le\mathrm{log}N\). Consequently \(|U|\ge 2^{t+1}\).

Run the greedy algorithm of Lemma 3.5 on _G_\[_U_\]. Since 2|_E(G_\[_U_\])|/|_U_|=_d(U_)|_U_|, it returns an independent set of _G_ with size at least

\(\frac{|U|}{1+d(U)|U|}=\frac{1}{|U|^{-1}+d(U)}\ge\frac{1}{2^{-(t+1)}+2^{-(t+1)}}=2^t.\)

The first step divides numerator and denominator by |_U_|. The second step uses \(|U|\ge 2^{t+1}\) and \(d(U)\le 2^{-(t+1)}\), and the third step simplifies the denominator. The running time is _N_<sup>_O(t_)</sup>.

For the approximation guarantee, if _T_=0, output any vertex; its size is at least \(\alpha(G)/N\). Otherwise, run the algorithm above with _t_:=_T_. If it returns an independent set of size at least<tbc>

