The quantity \(\rho_j|U|\) is the average over \(v\in U\) of the number of \(u\in U\) with \(2^j\le M(u,v)<2^{j+1}\). Thus some \(v\in U\) has at least \(\rho_j|U|\) vertices \(u\in U\) with \(M(u,v)\ge 2^j\). For every such vertex,

\(\nu(u,v)=(1+M(u,v))\nu(u)\nu(v)\ge(1+2^j)\nu(u)\nu(v).\)

The first step follows from the definition of _M_, and the second step uses \(M(u,v)\ge 2^j\). Together with the lower bound on \(\rho_j\), this proves Eq. (12).

## 4.2 Cost per bit

The following inequality bounds the logarithmic loss in set size in terms of the logarithmic increase in the marginal threshold. The bound is uniform over all dyadic correlation scales.

**Lemma 4.2** (Cost per bit)**.** _Let_ \(\ell\ge 1\) _be an integer and_ \(\Lambda\ge 0\) _a real number. For every integer_ \(j\ge-1\),<tbc>

\((j+1)\ell+\Lambda\le(2\ell+2\Lambda)log(1+2^j).\)

<tbc>_Proof._ If _j_=-1, the left-hand side is \(\Lambda\), while \(log(3/2)\ge 1/2\) implies that the right-hand side is at least \(\ell+\Lambda\). If _j_=0, the left-hand and right-hand sides are \(\ell+\Lambda\) and \(2\ell+2\Lambda\), respectively. If \(j\ge 1\), then \(log(1+2^j)\ge j\), and

\((j+1)\ell+\Lambda\le 2j\ell+j\Lambda\le j(2\ell+2\Lambda)\le(2\ell+2\Lambda)log(1+2^j).\)

The first step uses \(j+1\le 2j\) and \(\Lambda\le j\Lambda\). The second step uses \(\Lambda\ge 0\), and the third step uses \(log(1+2^j)\ge j\).

## 4.3 Iterated conditioning

Repeated conditioning raises the marginal threshold until the retained set becomes sparse. The next lemma bounds the number of conditioned vertices and the cumulative loss in set size.

**Lemma 4.3** (Iterated conditioning)**.** _Let_ \(t,h\ge 1\) _be integers. Let_ \(\ell\) _be the smallest odd integer with_ \(\ell\ge h+2\)_, and define_<tbc>

\(\Lambda:=h+log\frac{16}{3},K:=2(\ell+1)+2\Lambda.\)

<tbc>_Let_ \(r\ge 2t+3\)_, and let_ \(\mu\) _be a level-r pseudo-distribution satisfying_ \(\sum_{u\in V}\mu(u)\ge 2^{-t}N\)_. Assume_ \(N\ge 2^{(2K+1)(t+1)}\)_. Then there are a set_ \(S\subseteq V\) _with_ \(|S|\le 2t+1\) _and_ \(\mu(S)>0\)_, and a number_ \(\tau\in[2^{-(t+1)},1]\)_, such that_

\(U:=\{u\in V\backslash S:\mu_S(u)\ge\tau\}\)

_satisfies_ \(|U|\ge 2^{-(K+1)(t+1)}N\) _and_ \(d(U)\le 2^{-h}\).

_Proof._ Let \(\delta:=2^{-h}\) and \(\tau_0:=2^{-(t+1)}\). The choice of \(\ell\) gives \(2^{-\ell}\le\delta/4\). We construct sets \(\emptyset=S_0\subseteq S_1\subseteq\cdots\) , thresholds \(\tau_0,\tau_1,\dots\) , and integers \(j_0,j_1,\dots\ge-1\). Write

\(U_i:=\{u\in V\backslash S_i:\mu_{S_i}(u)\ge\tau_i\},c_k:=(j_k+1)(\ell+1)+\Lambda.\)

At each index _i_ reached by the construction, we maintain the following invariants, with empty sums equal to 0 and empty products equal to 1:

(a) |_S<sub>i</sub>_|=_i_ and \(\mu(S_i)>0\).<tbc>

(b) \(\tau_i=\tau_0\prod_{k=0}^{i-1}(1+2^{j_k})\) and \(\tau_i\le 1\).<tbc>

