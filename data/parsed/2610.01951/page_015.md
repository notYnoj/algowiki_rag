covered by that theorem, in particular their uniform tie-breaking convention. We do not claim that this result applies to the fixed deterministic tie-breaking convention in Algorithm 1. It is not used in the unconditional high-probability analysis or in the guarded expected result.

### Results established in this paper.

Starting from the concentration event above, we prove the discrete penalized allocation-benchmark approximation, the simultaneous empirical-to-population pairwise-GLR transfer, linear challenger growth in the stabilized regime, the uniform evidence lower bound, a high-probability bound on the time to reach that regime, and the inversion of the stopping-threshold inequality. We also prove that the exploration guard gives deterministic sufficient exploration with sublinear pull overhead. The one-step comparison limitation concerns only the stated index-domination proof route; it is not an impossibility theorem for the algorithm.

#### Connection to the main theorems.

The deterministic allocation-benchmark analysis and time- uniform concentration yield Theorem 5.2 and the challenger-growth results. The high-probability stabilization bound then gives Corollary 6.3 and almost-sure termination of the unguarded rule under a unique best arm. If the stabilization time also admits a summable upper-quantile bound, integrating that bound yields Theorem 6.4. For pairwise-distinct means, the theorem of Jourdan et al. \[9\] verifies this additional premise for the tie-breaking variant in Corollary 6.5. For the guarded rule, Proposition 6.6 verifies sufficient exploration directly and leads to Theorem 6.7. Finally, whenever our analysis establishes almost-sure termination, combining it with the stopping-rule error guarantee above gives \(\delta\)-correctness.

The distinction is important: error control at stopping does not imply termination, and a high- probability bound on a random time need not have finite expectation.

## B Error Control and \(\delta\)-Correctness

### B.1 Bernoulli specialization of the transportation cost

We first justify the Bernoulli specialization of the transportation cost used in the main text. In the general bounded-reward framework of Jourdan et al. \[9\], for a model class F one defines

\(K_\mathrm{inf}^+(F,u):=\mathrm{inf}\left\{\mathrm{KL}(F,G):G\in\mathcal{F},\mathbb{E}_G[X]>u\right\},\)<br>
\(K_\mathrm{inf}^-(F,u):=\mathrm{inf}\left\{\mathrm{KL}(F,G):G\in\mathcal{F},\mathbb{E}_G[X]<u\right\},\)

and the one-sided transportation cost

\(W_t^\mathrm{gen}(i,j):=\mathrm{inf}_{x\in(0,1)}\left\{N_{t,i}K_\mathrm{inf}^-(F_{t,i},x)+N_{t,j}K_\mathrm{inf}^+(F_{t,j},x)\right\},\)

where _F<sub>t,i</sub>_ is the empirical distribution of arm _i_ at time _t_.

In our Bernoulli setting, \(F_{t,i}=\mathrm{Ber}(\widehat{\mu}_{t,i})\), and the optimization over \(G\in\mathcal{F}\) reduces to an optimization over the Bernoulli mean parameter.

**Proposition B.1** (Bernoulli specialization of the transportation cost)**.** _For any_ \(p,u\in(0,1)\),<tbc>

\(K_\mathrm{inf}^+(\mathrm{Ber}(p),u)=\left\{\begin{array}{ c c }
0, & u<p, \\
d(p,u), & u\ge p,
\end{array}\right.K_\mathrm{inf}^-(\mathrm{Ber}(p),u)=\left\{\begin{array}{ c c }
d(p,u), & u\le p, \\
0, & u>p.
\end{array}\right.\)

<tbc>_Consequently, for any_ \(p_i\ge p_j\) _and any_ \(N_i,N_j\ge 0\),<tbc>

\(\mathrm{inf}_{x\in(0,1)}\left\{N_iK_\mathrm{inf}^-(\mathrm{Ber}(p_i),x)+N_jK_\mathrm{inf}^+(\mathrm{Ber}(p_j),x)\right\}=\mathrm{inf}_{x\in(0,1)}\left\{N_id(p_i,x)+N_jd(p_j,x)\right\}.\)

<tbc>_Proof of Proposition B.1._ Since every \(G\in\mathcal{F}\) has the form _G_=Ber(_q_) for some \(q\in(0,1)\),<tbc>

\(K_\mathrm{inf}^+(\mathrm{Ber}(p),u)=\mathrm{inf}_{q>u}d(p,q),K_\mathrm{inf}^-(\mathrm{Ber}(p),u)=\mathrm{inf}_{q<u}d(p,q).\)

<tbc>For \(q\in(0,1)\),<tbc>

\(\frac{\partial}{\partial q}d(p,q)=-\frac{p}{q}+\frac{1-p}{1-q}=\frac{q-p}{q(1-q)}.\)

