_Proof._ We follow the framework of Algorithm 1 with \(\Delta=n^{4/5}\). In addition, we use Lemma 3.2 for Step 1 and Lemma 3.4 for Step 2. Assume that all steps succeed which occurs w.h.p. Note that given _H_ from Step 1, we can locally compute _F_ at no extra costs. Plus, we have \(\nu(G_F)=\nu(G)-\nu(F)\le\Delta\) via Proposition 2.3. The total number of queries then becomes

\(\widetilde{O}\left(\frac{n^2}{\sqrt{\Delta}}+\frac{n^3}{\Delta^2}+n^{4/3}\Delta^{1/3}\right)=\widetilde{O}\left(n^{8/5}\right)\)

as \(\Delta=n^{4/5}\).

**Theorem 1.2** (Main result #2)**.** _There is a deterministic two-player communication protocol that computes a minimum s-t cut of an undirected unweighted graph G. The protocol uses_ \(\widetilde{O}(n\nu^{4/7})\) _bits of communication where_ \(\nu\) _denotes the value of G’s minimum s-t cut, and always succeeds._

_Proof._ We first compute \(\hat{\nu}\) which is a constant approximation of \(\nu\) using \(\widetilde{O}(n)\) communication via Corollary 2.13. Then, we follow the framework of Algorithm 1 using \(\Delta=\hat{\nu}^{6/7}\). In addition, we use Lemma 3.5 for Step 1 and Lemma 3.3 for Step 2, both of which are deterministic. Note that given _H_ from Step 1, both players can locally compute _F_ at no extra costs. Plus, we have \(\nu(G_F)=\nu(G)-\nu(F)\le\Delta\) via Proposition 2.3. The total number of queries then becomes

\(\widetilde{O}\left(n+\frac{n\cdot\nu(G)}{\sqrt{\Delta}}+\frac{n\cdot\nu(G)^2}{\Delta^2}+n\Delta^{2/3}\right)=\widetilde{O}\left(n\nu^{4/7}\right)\)

as \(\Delta=\hat{\nu}^{6/7}=\Theta\left(\nu^{6/7}\right)\).

## 4 Modifications to RSW Algorithm

In this section, we discuss Step 2 of our meta algorithm. To this end, we propose a baseline procedure--independent of the computational model--that is adapted from the work of \[RSW18\] to handle a mixed input graph G=(_G,F_). As a reminder, in our setting the directed weighted graph _F_ is provided explicitly and at no cost; hence, the "true" input is an undirected, unweighted graph _G_.

