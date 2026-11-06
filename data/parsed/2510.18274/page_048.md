with _C_. This implies that the number of (_S,T_) pairs whose cut is precisely _C_ is at most _n<sup>f</sup>_. As we have already argued that there are _n_<sup>_O(f_)</sup> possibilities for _C_ and _X_, the total number of witnesses to _H<sub>F</sub>_ is at most _n_<sup>_O(f_)</sup>. This concludes the proof of Claim C.8.

## C.4 Putting All Together: Proof of Claim C.1

Finally, we conclude by proving Claim C.1.

**Claim C.1.** _Let_ \(f,k,k'\) _be known parameters such that_ \(k'<k\le f\) _with a promise that_ \(\nu(G)\ge f\)_, and also given explicitly is a subgraph_ \(H\unknown G\) _with_ \(\nu(H)\ge f-k\)_. Then, there is a deterministic protocol which communicates_ \(\widetilde{O}\left(nf\cdot\frac{\sqrt{k}}{k'}\right)\) _bits and outputs_ \(H^\mathrm{after}\unknown G\) _with_ \(\nu(H^\mathrm{after})\ge f-k'\).

_Proof._ Let \(\beta>0\) be a suitably small hidden constant following the statement of Claim C.7. We propose the following protocol.

1. Players pre-process _H_ so that every vertex \(v\in H\) is reachable from _s_.<tbc>

2. Players locally determine \(F\unknown H\), consisting of exactly _f-k_ edge-disjoint _s-t_ paths.<tbc>

3. If \(\mathcal{W}_F(H)=\emptyset\), output the current _H_ and terminate. Otherwise, proceed.<tbc>

4a. Alice declares her private edge _e_<sup>Alice</sup>, if any, such that \(|\mathcal{W}_F(H\cup e^\mathrm{Alice})|\le\left(1-\frac{\beta k'}{n\sqrt{k}}\right)\cdot|\mathcal{W}_F(H)|\).<tbc>

4b. Bob declares his private edge _e_<sup>Bob</sup>, if any, such that \(|\mathcal{W}_F(H\cup e^\mathrm{Bob})|\le\left(1-\frac{\beta k'}{n\sqrt{k}}\right)\cdot|\mathcal{W}_F(H)|\).<tbc>

5. Both players update \(H\leftarrow H\cup\{e^\mathrm{Alice},e^\mathrm{Bob}\}\) and go back to Step 3.

If our algorithm ever terminates, its correctness follows from Invariant C.5 that \(\mathcal{W}_F(H)=\emptyset\) implies \(\nu(H)\ge f-k'\). Thus, it suffice to justify the termination and communication costs.

Assume that at the start of an iteration at Line 3, we have \(\mathcal{W}_F(H)\neq\emptyset\). Applying Claim C.7, it is guaranteed that either Alice must have found _e_<sup>Alice</sup> or Bob must have found _e_<sup>Bob</sup>. Without loss of generality, suppose that Alice has found _e_<sup>Alice</sup>. Then, upon the insertion of _e_<sup>Alice</sup> and _e_<sup>Bob</sup>, the number of remaining residual witnesses is reduced to:

\(|\mathcal{W}_F(H\cup\{e^\mathrm{Alice},e^\mathrm{Bob}\})|\le|\mathcal{W}_F(H\cup\{e^\mathrm{Alice}\}|\text{(adding}e^\mathrm{Bob}\text{only reduces witnesses)}\)<br>
\(\le\left(1-\frac{\beta k'}{n\sqrt{k}}\right)\cdot|\mathcal{W}_F(H)|\text{(Alice finds}e^\mathrm{Alice}\text{satisfying Line 4a)}\)

Claim C.8 asserts that the number of starting residual witnesses is bounded by _n_<sup>_O(f_)</sup>. Therefore, we only need

\(\left(\frac{n\sqrt{k}}{\beta k'}\right)\cdot\mathrm{log}\left(n^{O(f)}\right)=\widetilde{O}\left(nf\cdot\frac{\sqrt{k}}{k'}\right)\)

iterations before all residual witnesses are killed. Then, in the next iteration, the protocol will surely terminate.

Finally, in each iteration, the players only communicate at most two edges which costs _O_(log_n_) bits. Thus, the total communication cost of our protocol is, up to a polylogarithmic factor, bounded by the number of iterations which is \(\widetilde{O}\left(nf\cdot\frac{\sqrt{k}}{k'}\right)\). This concludes our proof.

