The first step uses \(f(y^0)\ge 0\) and \(f(y^1)\ge\mathrm{OPT}-\eta\). The second step discards the nonnegative term \(\theta\eta\), and the third step uses \(\eta\le 1/4\), \(\theta\le 1/(4N)\), and \(\mathrm{OPT}\le N\). If \(\alpha(G)\ge 2^{-t}N\), then

\(f(y)\ge 2^{-t}N-\frac{1}{2}\ge 2^{-(t+1)}N.\)

The first step combines Claim 3 with the preceding objective guarantee, and the second step uses \(N\ge 2^t\).

For the running time, \(D\le(N+1)^{2r}\), and \(\mathrm{log}(1/\rho_0)\), \(\mathrm{log}(1/\eta)\), and \(\mathrm{log}(1/\epsilon)\) are all _O(r_log_N_). Computing _y_<sup>0</sup> requires only enumeration of I_<sub>r</sub>_ and its subsets. All rational operations above have bit complexity polynomial in these parameters. The total running time is therefore _N_<sup>_O(r_)</sup>.

## 4.5 Finding a large sparse set

The following lemma converts the conditioning result into a deterministic algorithm by enumerating small conditioning sets and marginal thresholds. The algorithm produces a sparse induced subgraph of the required size.

**Lemma 4.5** (Finding a large sparse set)**.** _Let_ \(t,h\ge 1\) _be integers. Let_ \(\ell\) _be the smallest odd integer with_ \(\ell\ge h+2\)_, and define_<tbc>

\(\Lambda':=h+\mathrm{log}\frac{16}{3},K':=2(\ell+1)+2\Lambda'.\)

<tbc>_If_ \(\alpha(G)\ge 2^{-t}N\)_, then a deterministic algorithm running in time N_<sup>_O(t_)</sup>+_O_(log(_h_+1)) _finds a nonempty_ \(U\subseteq V\) _such that_

\(|U|\ge 2^{-(2K^\prime+1)(t+2)}N,d(U)\le 2^{-h}.\) (16)

_In particular,_ \(|U|\ge 2^{-O(th)}N\)_. The additive term accounts for reading the binary parameter h; when h=O(t_) _it is absorbed in N_<sup>_O(t_)</sup>.

_Proof._ If \(N<2^{(2K^\prime+1)(t+2)}\), output a single vertex. Its density is zero, and its size satisfies Eq. (16).

Otherwise, \(N\ge 2^t\). Let _r_:=2_t_+5, and compute \(\mu\) using Lemma 4.4. The hypothesis on \(\alpha(G)\) gives \(\sum_{u\in V}\mu(u)\ge 2^{-(t+1)}N\). Apply Lemma 4.3 with _t_+1 in place of _t_. Its constants are \(\Lambda'\) and \(K'\), and its hypotheses hold because _r_=2(_t_+1)+3 and \(N\ge 2^{(2K^\prime+1)(t+2)}\). It gives _S_ with \(|S|\le 2t+3\) and \(\mu(S)>0\), and \(\tau\in[2^{-(t+2)},1]\), for which

\(U_*:=\{u\in V\backslash S:\mu_S(u)\ge\tau\}\)

satisfies \(|U_*|\ge 2^{-(K^\prime+1)(t+2)}N\) and \(d(U_*)\le 2^{-h}\).

To find _S_ and \(\tau\), the algorithm enumerates every \(S\subseteq V\) with \(|S|\le 2t+3\) and \(\mu(S)>0\), and every \(w\in V\backslash S\). For each pair, it computes

\(U_{S,w}:=\{u\in V\backslash S:\mu_S(u)\ge\mu_S(w)\}.\)

It outputs the first candidate with \(|U_{S,w}|\ge 2^{-(K^\prime+1)(t+2)}N\) and \(d(U_{S,w})\le 2^{-h}\); if there is no such candidate, it reports failure. Under the lemma’s hypothesis, a suitable candidate exists: take _S_ from Lemma 4.3 and choose _w_ minimizing \(\mu_S\) over the nonempty set _U_<sub>∗</sub>. Every \(u\in U_*\) has \(\mu_S(u)\ge\mu_S(w)\). Conversely, if \(u\in V\backslash S\) has \(\mu_S(u)\ge\mu_S(w)\), then \(\mu_S(u)\ge\tau\), because \(w\in U_*\). Thus _U<sub>S,w</sub>=U_<sub>∗</sub>. Its size bound implies the weaker bound in Eq. (16).

