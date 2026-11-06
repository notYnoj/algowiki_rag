**Lemma 3.3** (Modified RSW via communication)**.** _Let_ G=(_G,F_) _be an input mixed graph where G is undirected and unweighted and is partitioned among two players, and F be a directed bounded- weighted that is known explicitly. Then, there exists an_ \(\widetilde{O}(n\cdot\nu(\mathcal{G})^{2/3})\)_-bit deterministic protocol that Alice and Bob jointly outputs a minimum s-t cut of_ G.

_Proof._ We assert the following pre-processing step.

(i) Players compute _f_ be such that of \(2\nu(\mathcal{G})\le f\le 100\nu(\mathcal{G})\) using \(\widetilde{O}(n)\) communications.<sup>7</sup><tbc>

(ii) Alice locally computes \(P_A\leftarrow f\)-forest packing of _G<sub>A</sub>_, and Bob locally computes \(P_B\leftarrow f\)-forest packing of _G<sub>B</sub>_,

According to Lemma 4.3, both _P<sub>A</sub>_ and _P<sub>B</sub>_ have average degree _O(f_). Moreover, it suffices to determine a minimum _s-t_ cut of \(\mathcal{P}=(P_A\cup P_B,F)\). We shall do this by implementing Algorithm 2 with respect to \(\mathcal{G}\leftarrow\mathcal{P}\).<sup>8</sup> We specify such implementation as follows.

• In Step 2, the players proceed as follows. Alice locally construct \(P'_A\) which is an \(\varepsilon\)-cut sparsifier with \(\widetilde{O}(n/\varepsilon^2)\) edges and maximum weight \(\widetilde{O}(\varepsilon^2f)\), and then sends it to Bob. To do that, Alice can employ a brute-force search for \(P'_A\), as its existence is guaranteed due to Theorem 2.6. Bob also construct \(P'_B\) analogously, and then sends it to Alice. The players then set \(P'=P'_A\cup P'_B\) to be an \(\varepsilon\)-cut sparsifier of _P_.<tbc>

• Once obtained \(P'\), each player can do Step 3,4,5,6 locally.<tbc>

• Step 7 can be done by having each player sends over all edges crossing the partition (_V_<sub>1</sub>_,...,V<sub>z</sub>_).<tbc>

• Once Step 7 is completed, each player can do Step 8 locally.

It remains to bound the amount of communication. Following our implementation, Step 2 consumes \(\widetilde{O}(n/\varepsilon^2)\) bits. The communication cost of Step 7 is, up to polylogarithmic factor, bounded by \(|P\langle V_1,\dots,V_z\rangle|\) which is also bounded by \((1+\varepsilon)\cdot|P'\langle V_1,\dots,V_z\rangle|\) as \(P'\) is a \(\varepsilon\)-cut sparsifier of _P_. Since \(P'\unknown K\cup\mathcal{F}\), we then have

\(|P'\langle V_1,\dots,V_z\rangle|\le|K\langle V_1,\dots,V_z\rangle|+|\mathcal{F}|\)<br>
\(\le 3\varepsilon n\cdot\nu(H)+n\cdot\sqrt{\nu(H)\cdot\widetilde{O}(\varepsilon^2f)}\text{(Lemma 2.5 and Lemma 2.2)}\)<br>
\(\le\widetilde{O}\left(\varepsilon nf\right)\text{(}\nu(H)\approx\nu(\mathcal{P})=\nu(\mathcal{G})\le f\text{)}\)

Therefore, the total communication is bounded by \(\widetilde{O}\left(\frac{n}{\varepsilon^2}+\varepsilon nf\right)\). By setting \(\varepsilon=f^{-1/3}=\Theta\left(\nu(\mathcal{G})^{-1/3}\right)\), the communication cost becomes \(\widetilde{O}\left(n\cdot\nu(\mathcal{G})^{2/3}\right)\) as wished.

## 5 Finding a Large Flow via Cut-Query

The goal of this section is to prove Lemma 3.4, thereby concluding our minimum _s-t_ cut algorithm in the cut-query model. We first state our main claim.

<sup>7</sup>Alice computes an \(G_A^*\) to be a \(\frac{1}{100}\)-cut sparsifier of _G<sub>A</sub>_ using Corollary 2.13, and Bob does the same for \(G_B^*\). Players exchange these sparsifiers and set \(f:=99\cdot\nu(G_A^*\cup G_B^*\cup F)\). <sup>8</sup>Notationally, \(G_A,G_B,G,G'\) are replaced by \(P_A,P_B,P,P'\) respectively.

