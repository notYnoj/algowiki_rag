trary approximation algorithms.

### 1.1 Our result

We state our main result as follows.

**Theorem 1.1** (Informal version of Theorem 4.6)**.** _Let t be an integer with_ \(1\le t\le\sqrt{\mathrm{log}N}/12\)_. If_ \(\alpha(G)\ge 2^{-t}N\)_, then a deterministic algorithm finds an independent set of size at least_ 2_<sup>t</sup> in time N_<sup>_O(t_)</sup>_. Consequently,_ \(\alpha(G)\) _can be approximated within a factor_ \(N/2^{\Omega(\sqrt{\mathrm{log}N})}\) _in deterministic time_ \(N^{O(\sqrt{\mathrm{log}N})}\).

We make quantitative progress on the first open problem posed by Lovett \[Lov26, Section 1.3\], concerning the gap between approximation algorithms and hardness for maximum independent set. We improve the approximation ratio achievable in deterministic quasi-polynomial time from \(N/2^{\Omega((\mathrm{log}N)^{1/3})}\) to \(N/2^{\Omega(\sqrt{\mathrm{log}N})}\).

As a consequence of Tulsiani’s integrality gaps, Proposition 4.8 shows that the range \(t=O(\sqrt{\mathrm{log}N})\) is optimal, up to a factor \(\sqrt{\mathrm{loglog}N}\), for universal implications from the value of the Lasserre relaxation to the existence of an independent set of size 2_<sup>t</sup>_. This limitation applies to implications of the form specified there, at \(2^{o(\sqrt{\mathrm{log}N}\mathrm{loglog}N)}\) levels.

## 2 Technique Overview

### 2.1 Lovett’s Method

For integers \(t,h\ge 1\), we describe Lovett’s argument \[Lov26\] in five steps. Here _d(U_) denotes edge density, and averages over _U_ are taken over independently and uniformly chosen vertices.

#### Step 1: Initialize.

For the structural argument, assume that we are given a pseudo-distribution \(\mu\) with \(\sum_u\mu(u)\ge 2^{-t}N\) and sufficiently many levels. Set the initial threshold and vertex set as follows:

\(\tau_0:=2^{-(t+1)},U_0:=\{u:\mu(u)\ge\tau_0\},|U_0|\ge\tau_0N.\) (1)

The size bound follows from the objective bound and \(\mu(u)\le 1\).

#### Step 2: Increase the marginals.

Let \(\nu\) be the current conditioned pseudo-distribution. Suppose \(\nu(u)\ge\tau\) on _U_ and \(d(U)\ge\delta:=2^{-h}\). Set \(M(u,v):=\nu(u,v)/(\nu(u)\nu(v))-1\) and \(\rho:=\mathrm{Pr}_{u,v\in U}[M(u,v)\ge 1/2]\). Choose the smallest odd \(\ell\ge h+1\), so \(2^{-\ell}\le\delta/2\). Then

\(0\le\mathbb{E}_{u,v\in U}[M(u,v)^\ell]\le-d(U)+2^{-\ell}+\rho\tau^{-\ell}\le-\delta/2+\rho\tau^{-\ell}.\) (2)

\begin{tabular}{ccccc}
Year & Authors & Reference & Approximation ratio & Time \\
1992 & Boppana and Halldórsson & \[BH92\] & \(O(\frac{N}{(\mathrm{log}N)^2})\) & _N_<sup>_O_(1)</sup> \\
2004 & Feige & \[Fei04\] & \(O(\frac{N(\mathrm{loglog}N)^2}{(\mathrm{log}N)^3})\) & _N_<sup>_O_(1)</sup> \\
2026 & Lovett & \[Lov26\] & \(N/2^{\Omega((\mathrm{log}N)^{1/3})}\) & _N_<sup>_O_(log_N_)<sup>1/3</sup></sup> \\
2026 & This work & Theorem 1.1 & \(N/2^{\Omega(\sqrt{\mathrm{log}N})}\) & \(N^{O(\sqrt{\mathrm{log}N})}\) \\
\end{tabular}

1: Approximation guarantees for maximum independent set in general graphs.

