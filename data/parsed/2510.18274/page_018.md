2. \(\nu(\mathcal{G})=\nu(\mathcal{P})\).<tbc>

_3._ (_S,T_) _is a minimum s-t cut of_ G _if and only if it is a minimum s-t cut of_ P.

_Proof._ The average degree (1) is clear due to Lemma 4.2. We will now show (2). Observe that \(\mathcal{P}\unknown\mathcal{G}\) immediately gives \(\nu(\mathcal{P})\le\nu(\mathcal{G})\). Let (_S,T_) be an arbitrary minimum _s-t_ cut of P with value<tbc>

\(|E_{P_A}(S,T)|+|E_{P_B}(S,T)|+w_F(S,T)=w_\mathcal{P}(S,T)=\nu(\mathcal{P})\le\nu(\mathcal{G})\le k-1\) (1)

<tbc>We claim that \(|E_{G_A}(S,T)|\le k\). To see this, assume for CTD that \(|E_{G_A}(S,T)|\ge k+1\). By Lemma 4.2, we then have \(|E_{P_A}(S,T)|\ge k\) which immediately contradicts (1). Thus, we must have \(|E_{G_A}(S,T)|\le k\) and analogously \(|E_{G_B}(S,T)|\le k\). Then, by Lemma 4.2, we have _E<sub>G<sub>A</sub></sub>(S,T_)=_E<sub>P<sub>A</sub></sub>(S,T_) and _E<sub>G<sub>B</sub></sub>(S,T_)=_E<sub>P<sub>B</sub></sub>(S,T_). This then implies

\(\nu(\mathcal{G})\le w_\mathcal{G}(S,T)=|E_{G_A}(S,T)|+|E_{G_B}(S,T)|+w_F(S,T)\)<br>
\(=|E_{P_A}(S,T)|+|E_{P_B}(S,T)|+w_F(S,T)\)<br>
\(=w_\mathcal{P}(S,T)\)<br>
\(=\nu(\mathcal{P})((S,T)\text{be a min cut of}\mathcal{P}.)\)

Combining this with an earlier inequality \(\nu(\mathcal{P})\le\nu(\mathcal{G})\), we have \(\nu(\mathcal{G})=\nu(\mathcal{P})\).

Last but not lease, we prove (3). We will first prove (\(\Leftarrow\)) by showing that no cuts (_S,T_) of G with value \(w_\mathcal{G}(S,T)\ge\nu(G)+1\) becomes a min-cut of P. Assume for contradiction that it occurred. Then, we have<tbc>

\(\nu(\mathcal{G})+1\le w_\mathcal{G}(S,T)=|E_{G_A}(S,T)|+|E_{G_B}(S,T)|+w_F(S,T)\)

<tbc>and

\(\nu(\mathcal{G})=\nu(\mathcal{P})=|E_{P_A}(S,T)|+|E_{P_B}(S,T)|+w_F(S,T)\) (2)

This implies that either |_E<sub>P<sub>A</sub></sub>(S,T_)|_\<|E<sub>G<sub>A</sub></sub>(S,T_)| or |_E<sub>P<sub>B</sub></sub>(S,T_)|_\<|E<sub>G<sub>B</sub></sub>(S,T_)|. Assume WLOG that it is the earlier case. Then, if we had \(|E_{G_A}(S,T)|\le k\), we would have _E<sub>G<sub>A</sub></sub>(S,T_)=_E<sub>P<sub>A</sub></sub>(S,T_) via Lemma 4.2 which is a contradiction. Thus, we must have \(|E_{G_A}(S,T)|\ge k+1\). Via Lemma 4.2, we then have \(|E_{P_A}(S,T)|\ge k\). Continuing (2), we then have \(\nu(\mathcal{G})\ge|E_{P_A}(S,T)|\ge k\). This contradicts the premise that \(k\ge\nu(\mathcal{G})+1\). Hence, the (\(\Leftarrow\)) direction is proved.

Finally, we prove the (\(\Rightarrow\)) direction. Let (_S,T_) be an arbitrary minimum _s-t_ cut of G. Then, we have<tbc>

\(|E_{G_A}(S,T)|+|E_{G_B}(S,T)|+w_F(S,T)=w_\mathcal{G}(S,T)=\nu(\mathcal{G})\le k-1.\)

<tbc>This implies \(|E_{G_A}(S,T)|\le k-1\). Then, via Lemma 4.2, we have _E<sub>P<sub>A</sub></sub>(S,T_)=_E<sub>G<sub>A</sub></sub>(S,T_) and analogously _E<sub>P<sub>B</sub></sub>(S,T_)|=_E<sub>G<sub>B</sub></sub>(S,T_). We then have

\(\nu(\mathcal{P})=\nu(\mathcal{G})=w_\mathcal{G}(S,T)=|E_{G_A}(S,T)|+|E_{G_B}(S,T)|+w_F(S,T)\)<br>
\(=|E_{P_A}(S,T)|+|E_{P_B}(S,T)|+w_F(S,T)\)<br>
\(=w_\mathcal{P}(S,T)\)

In other words, the cut (_S,T_) attains a minimum cut value in P; thus is a min cut of P.

This lemma proves to be extremely useful. It implies that, in order to determine a minimum _s-t_ cut of the graph \(\mathcal{G}=(G_A\cup G_B,F)\), it suffices to determine a minimum _s-t_ cut of its _k_-forest packing analogue \(\mathcal{P}=(P_A\cup P_B,F)\), if we set _k_ such that \(k\ge\nu(\mathcal{G})+1\). Furthermore, Alice can locally compute _P<sub>A</sub>_ from her subgraph _G<sub>A</sub>_ without communicating with Bob, and vice versa. We put these advantages into action by giving a communication-efficient protocol for Lemma 3.3.

