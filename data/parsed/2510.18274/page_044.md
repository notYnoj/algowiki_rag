_Proof._ First, suppose that \(\nu(\mathcal{G})\ge f-k'\). Assume for the sake of contradiction that a residual witness exists and let (_S,T_) be a cut with respect to that witness. By definition of a witness, the cut (_S,T_) has value \(w_{\mathcal{G}_F}(S,T)\le k-k'-1\). Via Claim 3.1, we have \(|E_\mathcal{G}(S,T)|=\nu(F)+w_{\mathcal{G}_F}(S,T)\). Thus, we derive:

\(f-k'\le\nu(\mathcal{G})\le|E_\mathcal{G}(S,T)|=\nu(F)+w_{\mathcal{G}_F}(S,T)\le(f-k)+(k-k'-1)=f-k'-1\)

yielding a contradiction. This concludes \(\mathcal{W}_F(\mathcal{G})=\emptyset\).

Conversely, suppose that \(\nu(\mathcal{G})\le f-k'-1\). Let (_S,T_) be a minimum _s-t_ cut of G with value \(|E_\mathcal{G}(S,T)|=\nu(G)\le f-k'-1\). Again, following Claim 3.1, we have

\(w_{\mathcal{G}_F}(S,T)=|E_\mathcal{G}(S,T)|-\nu(F)\le(f-k'-1)-(f-k)=k-k'-1.\)

Then by taking \(X=\emptyset\), (_S,T,E_<sub>G<sub>_F_</sub></sub>(_S,T_)) is a residual witness of G, implying \(\mathcal{W}_F(\mathcal{G})\neq\emptyset\).

We now define the process of eliminating a witness. This is analogous to Definition 3.8.

**Definition C.6** (Killing a residual witness)**.** _Let_ G=(_V,E_) _be an unweighted and undirected graph with terminals s and t. Let F be its flow subgraph. Let_ W=(_S,T,Y_) _be a residual witness of_ G_. We say that a pair of vertices_ \((a,b)\notin E\) kills W _iff_ W _is_ not _a residual witness of_ \(\mathcal{G}\cup(a,b)\)_. Equivalently, this occurs if and only if_ \(a\in S\), \(b\in T\)_, and_ \((a,b)\notin Y\) .

Recall the brief description of our protocol that Alice and Bob begin with _H_<sub>1</sub>:=_H_ and iteratively add private edge(s) that eliminate a \(\gamma\) fraction of remaining residual witnessed. The next claim shows that when \(\gamma=\Omega\left(\frac{k'}{n\sqrt{k}}\right)\), at least one player is in possession of such edge; thus, by having each player exhaustively search for that edge, it is surely found.

**Claim C.7.** _For any iteration i where_ \(\mathcal{W}_F(H_i)\neq\emptyset\)_, there exists an edge_ \(e_i\in G\backslash H_i\) _such that_<tbc>

\(|\mathcal{W}_F(H_i\cup e_i)|\le\left(1-\Omega\left(\frac{k'}{n\sqrt{k}}\right)\right)\cdot|\mathcal{W}_F(H_i)|.\)

<tbc>_Proof._ Recall that _F_ is a flow graph of size _f-k_, and _G<sub>F</sub>_ is the residual graph of _G_ with respect to _F_. By Proposition 2.3, _G<sub>F</sub>_ has a maximum flow of at value least _k_ since

\(MaxFlow(G_F)=MaxFlow(G)-MaxFlow(F)\ge f-(f-k)=k.\)

Let _Q_ be a flow subgraph of _G<sub>F</sub>_ that consists of _k_ non-circular flows. By Lemma 2.2, _Q_ contains \(O(n\sqrt{k})\) edges. Let \(Q^*\subseteq Q\) denote the set of edges in _Q_ that does not appear in (_H<sub>i</sub>)<sub>F</sub>_. Then, we have \(Q\unknown(H_i)_F\cup Q^*\), implying that \((H_i)_F\cup Q^*\) has a maximum flow, i.e., a minimum cut, of value at least _k_.

Let \(\mathsf{W}=(S,T,E_{(H_i)_F}(S,T)\cup X)\) be an arbitrary residual witness of _H<sub>i</sub>_. We know that \(w_{(H_i)_F\cup Q^*}(S,T)\ge k\) while \(w_{(H_i)_F\cup X}(S,T)=w_{(H_i)_F}(S,T)+|X|\le k-k'-1\).<sup>11</sup> Thus, we ob tain \(w_{Q^*\backslash X}(S,T)\ge k'+1\). In addition, we have \(Q^*\backslash X\subseteq Q\subseteq G\backslash H_i\) only consists of private undirected edge with weight 1. Hence, the set _Q_<sup>∗</sup>\\_X_ represents (at least) \(k'+1\) edges among _Q_<sup>∗</sup> that kills W .

Finally, by the averaging argument over all residual witnesses, there must exist a private edge in _Q_<sup>∗</sup> that kills at least a fraction of

\(\frac{k'+1}{|Q^*|}\ge\frac{k'+1}{|Q|}=\Omega\left(\frac{k'}{n\sqrt{k}}\right)\)

of W_<sub>F</sub>(H<sub>i</sub>_). This completes the proof.

<sup>11</sup>Here, we slightly abuse the notation by treating _X_ as a set of undirected unit-capacitated edges in (_H<sub>i</sub>)<sub>F</sub>_, even though they do not actually exist in (_H<sub>i</sub>)<sub>F</sub>_.

