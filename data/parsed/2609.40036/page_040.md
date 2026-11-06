For each simple cycle, fix an orientation using its labeled edges and assign the circulation **f** with coefficients \(\pm a\). We call the cycle favorable when its likelihood ratio satisfies

\(L_C(\mathbf{E})=\prod_{e\in C}\frac{\nu(E_e-f_e)}{\nu(E_e)}\ge 1.\) (181)

The denominators are positive almost surely; a zero numerator sets the ratio to zero. Evenness of \(\nu\) makes the score distributions for coefficients _a_ and -_a_ identical. Thus the probability _p<sub>L</sub>_ of favorability depends only on the cycle length _L_.

**Lemma 10** (Single-cycle and joint score bounds)**.** _For some fixed C_<sub>0</sub>_\>_0 _and all sufficiently large even L,_

\(Z^LL^{-C_0}\le p_L\le Z^L.\) (182)

_For two distinct length-L cycles sharing j edges,_

\(\mathrm{Pr}\{L_{C_1}(\mathbf{E})\ge 1,L_{C_2}(\mathbf{E})\ge 1\}\le Z^{2(L-j)}.\) (183)

_Proof._ For \(b\neq 0\), let \(S_b(z)=\mathrm{log}[\nu(z-b)/\nu(z)]\) on the support of \(\nu\), allowing the value \(-\infty\). Then

\(\mathbb{E}e^{S_a(E_e)/2}=Z,\mathbb{E}e^{S_b(E_e)}=\sum_{z:\nu(z)>0}\nu(z-b)\le 1.\) (184)

The first identity and Markov’s inequality give the upper bound in (182). For the lower bound, use the tilted distribution

\(\pi_a(z)=Z^{-1}\sqrt{\nu(z)\nu(z-a)}.\) (185)

The involution \(z\mapsto a-z\) preserves \(\pi_a\) and reverses _S<sub>a</sub>_. Choose symbol counts within _O(q_) of \(L\pi_a(z)\), equal on paired orbits. Such counts summing to _L_ exist: round the counts on each pair down equally, round fixed-point counts down to even integers, and allocate the even remainder to an orbit with positive \(\pi_a\)-mass. The resulting type has total score zero. Stirling’s formula bounds its tilted probability below by a reciprocal polynomial in _L_. Undoing the tilt multiplies this probability by _Z<sup>L</sup>_, proving (182), including when \(\nu\) has zero entries.

On a shared edge, Cauchy-Schwarz and (184) give

\(\mathbb{E}e^{[S_b(E_e)+S_{b^\prime}(E_e)]/2}\le\sqrt{\mathbb{E}e^{S_b(E_e)\mathbb{E}e^{S_{b^\prime}(E_e)}}}\le 1.\) (186)

Each unshared edge contributes _Z_. Markov’s inequality applied to \(\sqrt{L_{C_1}L_{C_2}}\) proves (183).

Let _X_ count favorable candidate cycles already present in \(G_n^T\), and put

\(Y=\mathbf{1}_{\mathcal{B}_n}X,\mu_L=\frac{(D-1)^L}{2L}p_L.\) (187)

The channel can be sampled independently on all potential edges before generating the graph. Since the candidate length in (172) is even, Lemmas 9 and 10 give

\(\mathbb{E}Y=(1+o(1))\mu_L,\mu_L\ge\frac{R^L}{2L^{C_0+1}}\rightarrow\infty.\) (188)

The cycle count is uniform over the graph before the last round, so the preceding-round event B_<sub>n</sub>_ costs only its probability 1-_o_(1).

