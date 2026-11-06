The first step follows from Schur positivity; the second step partitions correlations by sign and magnitude; the third step uses \(d(U)\ge\delta\) and \(2^{-\ell}\le\delta/2\). Averaging gives a vertex _v_ and a set _W_ with

\(|W|\ge\frac{\delta}{2}\tau^\ell|U|,\nu_v(u)\ge\frac{3}{2}\nu(u)(u\in W).\) (3)

The size bound follows by rearranging Eq. (2) and averaging. The marginal bound follows from \(\nu_v(u)=\nu(u,v)/\nu(v)\) and \(M(u,v)\ge 1/2\).

### Step 3: Iterate.

The choice of \(\ell\) gives \(\ell\le h+2\). Put _A_:=(_t_+2)(_h_+2). When \(N\ge 2^{3(t+2)^2(h+2)}\), deleting _v_ after each conditioning step yields

\(\tau_i=(3/2)^i\tau_0,|U_i|\ge 2^{-(t+1)-Ai}N.\) (4)

The threshold formula follows by iterating the gain 3/2; the size bound uses Eq. (3), \(\tau_i\ge\tau_0\), and a factor of two to account for deleting _v_. Since \(\tau_i\le 1\), fewer than 2(_t_+1) steps suffice, yielding \(|U|\ge 2^{-O(t^2h)}N\) and \(d(U)\le 2^{-h}\).

### Step 4: Enumerate.

For \(\mu(S)>0\), the candidates are

\(U_S:=\{u\in V\backslash S:\mu_S(u)\ge(3/2)^{|S|}2^{-(t+1)}\},|S|=O(t).\) (5)

An SDP supplies feasible pseudo-marginals whose objective value is at least half the target. This slack is accounted for by replacing _t_ by _t_+1. Enumerating _S_ takes _N_<sup>_O(t_)</sup> time. For small _N_, a singleton suffices for the sparse-set bound.

### Step 5: Extract an independent set.

Set _h=t_+1. For \(t\le c(logN)^{1/3}\), choosing _c_ sufficiently small ensures \(|U|\ge 2^{t+1}\). Greedy extraction gives

\(|I|\ge\frac{|U|}{1+d(U)|U|}=\frac{1}{|U|^{-1}+d(U)}\ge 2^t.\) (6)

The first step is the greedy bound; the second step divides by |_U_|; the third step uses the size and density bounds.

## 2.2 Our Techniques

The main changes to the argument in Section 2.1 occur in Steps 2 and 3: selecting a dyadic correlation scale and charging vertex loss to marginal gain improve the sparse-set exponent from _O(t_<sup>2</sup>_h_) to _O(th_). Step 4 adapts the enumeration to variable thresholds; Steps 1 and 5 are unchanged.

### Step 1: Reuse the initialization.

This step is unchanged: Eq. (1) supplies the initial threshold and set. The same normalized covariance matrix and Schur positivity remain available. Taking high entrywise powers requires no additional SDP levels; only conditioning consumes levels.

### Step 2: Select a dyadic scale using geometric weights.

Instead of the uniform bound \(M(u,v)^\ell\le\tau^{-\ell}\) in Eq. (2), keep track of the contributions from individual dyadic scales. Let \(\rho_j:=Pr_{u,v\in U}[2^j\le M(u,v)<2^{j+1}]\), where \(-1\le j\le\lceil log(1/\tau)\rceil-1\). Choose the smallest odd \(\ell\ge h+2\), so \(2^{-\ell}\le\delta/4\). Then<tbc>

\(\sum_j\rho_j2^{(j+1)\ell}\ge d(U)-2^{-\ell}\ge 3\delta/4.\)

