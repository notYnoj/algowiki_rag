which is trivially satisfied at _s_=0 since there are \(O(N^3/B^{(\ell)})\) triples \((i,j,K^{(\ell)})\). Given \(\mathcal{P}_s^{(\ell)}\), we describe how to choose _p_<sub>_s_+1</sub> to obtain \(\mathcal{P}_{s+1}^{(\ell)}\). At a high level, our goal is to choose _p_ so that \(\Phi_{s+1}^{(\ell)}\) is minimized. However, since it is not clear how to compute \(\Phi_s^{(\ell)}\) efficiently directly, we must take an alternative approach.

Define<tbc>

\(C(i,j,K^{(\ell)},p)=\left|\left\{k\in K^{(\ell)}|\Delta_{ikj}\equiv 0\mathrm{mod}p\right\}\right|\)<br>
\(Z(i,j,K^{(\ell)})=\left|\left\{k\in K^{(\ell)}|\Delta_{ikj}=0\right\}\right|\)

<tbc>so that<tbc>

\(F(i,j,K^{(\ell)},p)=C(i,j,K^{(\ell)},p)-Z(i,j,K^{(\ell)}).\)

<tbc>For any fixed \(p'\in\mathcal{P}\backslash\mathcal{P}_s^{(\ell)}\), let \(\mathcal{P}_{s+1}^{(\ell)}=\mathcal{P}_s^{(\ell)}\cup\{p'\}\) and define

\(Z_{s+1}(p'):=\sum_{q\in\mathcal{Q}}\sum_{i,j,K^{(\ell)}}\prod_{p\in\mathcal{P}_{s+1}^{(\ell)}}\left(C(i,j,K^{(\ell)},p)-C(i,j,K^{(\ell)},pq)\right).\)

Here \(\mathcal{P}_{s+1}^{(\ell)}\), and hence \(\Phi_{s+1}^{(\ell)}\), depends on \(p'\). We first show that \(Z_{s+1}(p')\) approximates \(\Phi_{s+1}^{(\ell)}\), and then describe how to compute it.

**Lemma 3.8.** _Let_ \(\mathcal{P}_s^{(\ell)}\) _be a set of s distinct primes. Then, for any prime_ \(p'\in\mathcal{P}\backslash\mathcal{P}_s^{(\ell)}\),

\(\frac{|\mathcal{Q}|}{2}\Phi_{s+1}^{(\ell)}\unknown Z_{s+1}(p')\unknown|\mathcal{Q}|\Phi_{s+1}^{(\ell)}.\)

_Proof of Lemma 3.8._ Fix a triple \((i,j,K^{(\ell)})\). We begin by examining \(\Phi_{s+1}^{(\ell)}\). The product \(\prod_{p\in\mathcal{P}_{s+1}^{(\ell)}}F(i,j,K^{(\ell)},p)\) counts tuples \((k_1,\dots,k_{s+1})\in K^{(\ell)}\) such that \(\Delta_{ik_uj}\neq 0\) and \(\Delta_{ik_uj}\equiv 0\mathrm{mod}p_u\) for \(1\unknown u\unknown s+1\). We say such a tuple \((i,j,K^{(\ell)},k_1,\dots,k_{s+1})\) is _bad_, so that \(\Phi_{s+1}^{(\ell)}\) counts exactly the number of bad tuples.

Now, let us examine \(Z_{s+1}(p')\). Observe

\(C(i,j,K^{(\ell)},p)-C(i,j,K^{(\ell)},pq)=\left|\left\{k\in K^{(\ell)}|\Delta_{ikj}\equiv 0\mathrm{mod}p\wedge\Delta_{ikj}\neq 0\mathrm{mod}q\right\}\right|\)

Since \(p\neq q\), no triple \(\Delta_{ikj}=0\) contributes to the difference. Furthermore, \(\prod_p\left(C(i,j,K^{(\ell)},p)-C(i,j,K^{(\ell)},pq)\right)\) counts tuples (_k_<sub>1</sub>_,...,k_<sub>_s_+1</sub>) such \(\Delta_{ik_uj}\neq 0\mathrm{mod}q\) but \(\Delta_{ik_uj}\equiv 0\mathrm{mod}p_u\) for \(u\in[s+1]\). We say a tuple \((i,j,K^{(\ell)},k_1,\dots,k_{s+1})\) is counted by _q_ if it satisfies the above condition.

By definition, for any \(q\in\mathcal{Q}\), every tuple that is counted by _q_ is bad, yielding the upper bound. To argue the lower bound, it suffices to show that any bad tuple is counted by at least 1/2 fraction of Q. To see this, observe that each \(|\Delta_{ik_uj}|\unknown 4U\) and therefore has at most _H=O_(log_U_) distinct prime factors. Combined, there are at most _tH_ distinct primes that factor at least one of \(\Delta_{ik_1j},\dots,\Delta_{ik_{s+1}j}\). Since \(|\mathcal{Q}|\unknown 2tH\), there are at least _tH_ primes \(q\in\mathcal{Q}\) that do not divide any of \(\Delta_{ik_uj}\), so that any bad tuple is counted by at least _tH_ of the primes in Q.

Next, we describe how to estimate \(Z_{s+1}(p')\).

**Lemma 3.9.** _For every constant_ \(s\unknown 0\)_, there is a deterministic algorithm that computes_ \(Z_{s+1}(p')\) _for all_ \(p'\in\mathcal{P}\backslash\mathcal{P}_s^{(\ell)}\) _in time_

\(\tilde{O}(P^{s+2}\mathrm{log}^{s+2}U)\mathsf{T}_{MUL}\left(N,N(B^{(\ell)})^s,N\right).\)

_Proof of Lemma 3.9._ We compute \(Z_{s+1}(p')\) separately for each \(p'\in\mathcal{P}\backslash\mathcal{P}_s^{(\ell)}\). Fix such a \(p'\), write \(\mathcal{P}_s^{(\ell)}=\{p_1,\dots,p_s\}\), and let \(p_{s+1}=p'\).

