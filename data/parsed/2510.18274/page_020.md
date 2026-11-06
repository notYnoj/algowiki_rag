**Claim 5.1.** _Let f,k be known parameters with a promise that_ \(\nu(G)\ge f\)_, and also given explicitly is a subgraph_ \(H\unknown G\) _with_ \(\nu(H)\ge f-k\)_. Set_ \(k'=\frac{k}{2}\)_. Then, there is a deterministic algorithm which makes_ \(\widetilde{O}\left(\frac{n^2}{\sqrt{k}}\right)\) _cut queries to G and outputs_ \(H^\mathrm{after}\unknown G\) _with_ \(\nu(H^\mathrm{after})\ge f-k'=f-\frac{k}{2}\) .

Such task, in fact, can be accomplished trivially with \(\widetilde{O}\left(n\cdot(k-k')\right)=\widetilde{O}(nk)\) queries via \(k-k'\) iterations of the augmenting path method. Thus, our claim yields substantial savings compared to the augmenting path approach when \(k=\omega(n^{2/3})\). In addition, by recursively applying the claim, we can obtain a "promise" version of Lemma 3.4.

**Corollary 5.2.** _Let f and_ \(\Delta\le f\) _be parameters with a promise that_ \(\nu(G)\ge f\)_. Then, there is a deterministic algorithm which makes_ \(\widetilde{O}\left(\frac{n^2}{\sqrt{\Delta}}\right)\) _cut queries to G and outputs_ \(H\unknown G\) _with_ \(\nu(H)\ge f-\Delta\).

_Proof._ We use Claim 5.1 recursively with \((k,k')=(f,f/2),\dots,(2\Delta,\Delta)\) with _H_ being _H_<sup>after</sup> from the previous iteration (for the first iteration, set \(H=\emptyset\)). Inductively, each iteration is successful to obtain \(\nu(H^\mathrm{after})\ge f-k'\). Thus, upon the completion we obtain _H_ with \(\nu(H)\ge f-\Delta\). In total, the number of cut-queries made to _G_ is \(\widetilde{O}\left(\frac{n^2}{\sqrt{\Delta}}\right)\) due to the geometric sum.

Let us now to use Corollary 5.2 to recover Lemma 3.4.

**Lemma 3.4** (Finding a large flow via cut query)**.** _Let G be an input graph, and let_ \(\Delta\le n\) _be an additive error parameter. Then, there is a randomized algorithm that computes_ \(H\unknown G\) _with_ \(\nu(H)\ge\nu(G)-\Delta\)_. The algorithm makes_ \(\widetilde{O}\left(\frac{n^2}{\sqrt{\Delta}}+\frac{n^3}{\Delta^2}\right)\) _cut queries to G and succeeds w.h.p._

_Proof._ Set \(\lambda=\frac{\Delta}{10n}\le\frac{1}{10}\). Consider the following algorithm.

1. Compute _f_ such that \((1-\lambda)\nu(G)\le f\le(1+\lambda)\nu(G)\).<tbc>

2a. If \(f\le(1-\lambda)\Delta\), output \(H:=\emptyset\).<tbc>

2b. If \(f\ge(1-\lambda)\Delta\), apply Corollary 5.2 with \((f,\Delta)\leftarrow\left(\frac{f}{1+\lambda},\frac{\Delta}{10}\right)\) and output the resulting _H_.

Assume that Step 1 computes _f_ correctly which occurs w.h.p. We will argue that the output _H_ following step 2 is correct. If \(f\le(1-\lambda)\Delta\), we then have \(\nu(G)\le\Delta\). Hence, outputting \(H:=\emptyset\) with \(\nu(H)=0\ge\nu(G)-\Delta\) is correct.

Otherwise, we have \(f\ge(1-\lambda)\Delta\). In this case, we see that \(\frac{f}{1+\lambda}\ge\frac{1-\lambda}{1+\lambda}\cdot\Delta>\frac{\Delta}{10}\). Therefore, the premises of Corollary 5.2 in line 2b are met. As a result, the output _H_ must satisfy:

\(\nu(H)\ge\frac{f}{1+\lambda}-\frac{\Delta}{10}=\nu(G)-\left[\nu(G)-\left(\frac{f}{1+\lambda}-\frac{\Delta}{10}\right)\right]\)<br>
\(\ge\nu(G)-\left(\frac{1}{1-\lambda}-\frac{1}{1+\lambda}\right)\cdot f-\frac{\Delta}{10}(\nu(G)\le\frac{f}{1-\lambda})\)<br>
\(\ge\nu(G)-4\lambda f-\frac{\Delta}{10}(\lambda\le\frac{1}{10})\)<br>
\(\ge\nu(G)-\Delta(\lambda f\le\lambda n=\frac{\Delta}{10}.)\)

Thus, the algorithm computes _H_ with a guarantee that \(\nu(H)\ge\nu(G)-\Delta\).

Finally, the algorithm makes \(\widetilde{O}\left(\frac{n}{\lambda^2}\right)\) cut queries from step 1 and \(\widetilde{O}\left(\frac{n^2}{\sqrt{\Delta}}\right)\) cut queries from step 2b. In total, these simplify to \(\widetilde{O}\left(\frac{n^2}{\sqrt{\Delta}}+\frac{n^3}{\Delta^2}\right)\) queries.

