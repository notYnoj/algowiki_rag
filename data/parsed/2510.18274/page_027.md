### 5.4 Putting All Together: Proof of Claim 5.1

We now combine all the pieces to prove our main claim of this section.

**Claim 5.1.** _Let f,k be known parameters with a promise that_ \(\nu(G)\ge f\)_, and also given explicitly is a subgraph_ \(H\unknown G\) _with_ \(\nu(H)\ge f-k\)_. Set_ \(k'=\frac{k}{2}\)_. Then, there is a deterministic algorithm which makes_ \(\widetilde{O}\left(\frac{n^2}{\sqrt{k}}\right)\) _cut queries to G and outputs_ \(H^\mathrm{after}\unknown G\) _with_ \(\nu(H^\mathrm{after})\ge f-k'=f-\frac{k}{2}\).

_Proof._ We do as follows.

1. If \(\mathcal{W}(H)=\emptyset\), output the current _H_ and terminate. Otherwise, proceed.<tbc>

2. Compute \(\hat{z}_v\) for all \(v\in V\) w.r.t. _H_.<tbc>

3. Use the algorithm of Lemma 5.8 to compute `FindLongEdge` with respect to the graph _G_\\_H_, potential \(\phi(v):=\hat{z}_v\) and \(\delta:=\frac{\alpha}{2}\cdot\frac{\sqrt{k}}{n}\). Let \((u,v)\in G\backslash H\) be the edge that is outputted.<tbc>

4. Set \(H\leftarrow H\cup(u,v)\) and go back to Step 1.

If our algorithm ever terminates, its correctness follows from Invariant 3.7 that \(\mathcal{W}(H)=\emptyset\) implies \(\nu(H)\ge f-k'\). Thus, it suffice to justify the termination and query complexity.

Assume that at the start of an iteration, we have \(\mathcal{W}(H)\neq\emptyset\). Claim 5.6 tells us that some \((u^*,v^*)\in G\backslash H\) has \(|\hat{z}_{u^*}-\hat{z}_{v^*}|\ge\frac{\alpha}{2}\cdot\frac{\sqrt{k}}{n}\) ; i.e. the graph _G_\\_H_ has \(\delta_\mathrm{max}\ge\frac{\alpha}{2}\cdot\frac{\sqrt{k}}{n}=\delta\). This means Step 2 successfully finds \((u,v)\in G\backslash H\) such that \(|\hat{z}_u-\hat{z}_v|\ge\frac{\delta}{2}=\frac{\alpha}{4}\cdot\frac{\sqrt{k}}{n}\) per the guarantee of Lemma 5.8. Thus, via Claim 5.5, the fraction of W(_H_) that (_u,v_) kills is at least \(\frac{k'+1}{k}\cdot|\hat{z}_u-\hat{z}_v|\ge\frac{\alpha}{8}\cdot\frac{\sqrt{k}}{n}\) . As a result, upon inserting (_u,v_) to _H_, the number of remaining witnesses is reduced to

\(\mathcal{W}(H\cup(u,v))\le\left(1-\frac{\alpha}{8}\cdot\frac{\sqrt{k}}{n}\right)\cdot\mathcal{W}(H)\le\mathrm{exp}\left(-\frac{\alpha}{8}\cdot\frac{\sqrt{k}}{n}\right)\cdot\mathcal{W}(H).\)

A trivial bound shows that in the beginning, we have at most _n_<sup>_O(n_)</sup> witnesses. Therefore, we only need

\(\left(\frac{8}{\alpha}\cdot\frac{n}{\sqrt{k}}\right)\cdot\mathrm{log}\left(n^{O(n)}\right)=\widetilde{O}\left(\frac{n^2}{\sqrt{k}}\right)\)

iterations before all witnesses are killed. Then, in the next iteration, the algorithm will surely terminate.

Finally, we need to bound the number of cut queries made to _G_. Consider an arbitrary iteration which _H_ has been given explicitly. Only Line 3 requires us to make _O_(log_n_) cut queries to _G_\\_H_. Each of which can be simulated by a single query to _G_, along with an explicit description of _H_. Since the algorithm only needs \(\widetilde{O}\left(\frac{n^2}{\sqrt{k}}\right)\) iterations, we only make \(\widetilde{O}\left(\frac{n^2}{\sqrt{k}}\right)\) cut queries to _G_.

## 6 Open Problems

We conclude with a brief discussion of open problems and future directions motivated by our results.

