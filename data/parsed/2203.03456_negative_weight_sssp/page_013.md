**Lemma 4.3.** _For every i and every_ \(u,v\in V_i\), \(\mathrm{dist}_G(u,v)\le dB\).

_Proof._ For every \(u,v\in V_i\), we have \(\mathrm{dist}_G(u,v)\le\mathrm{dist}_{G_{\ge 0}^B}(u,v)\le dB\) where the first inequality is because \(w(e)\le w_{\ge 0}^B(e)\) for every edge \(e\in E\) and the second inequality is by the output guarantee of LowDiamDecomposition (Lemma 1.2).

Another crucial property from the decomposition is this: Recall from Definition 2.4 that _P<sub>G<sup>B</sup></sub>(v_) is the shortest _sv_-path in \(G_s^B\) with \(\eta_{G^B}(v)\) negative-weight edges. We show below that in expectation _P<sub>G<sup>B</sup></sub>(v_) contains only _O_(log<sup>2</sup>_n_) edges from _E<sup>rem</sup>_. This will be used in Phase 3.

**Lemma 4.4.** _If_ \(\eta(G^B)\le\Delta\)_, then for every_ \(v\in V\) , \(E\left[|P_{G^B}(v)\cap E^{rem}|\right]=O(\mathrm{log}^2m)\).

_Proof._ Consider any \(v\in V\) . The crux of the proof is the following bound on the weight of _P<sub>G<sup>B</sup></sub>(v_) in \(G_{\ge 0}^B\):

\(w_{\ge 0}^B(P_{G^B}(v))\le\eta_{G^B}(v)\cdot B\) (2)

where we define \(w_{\ge 0}^B(s,u)=0\) for every \(u\in V\) . Recall the definition of of \(w_s^B\) from Definition 2.3 and note that \(w_s^B(P_{G^B}(v))\le 0\) because there is an edge of weight 0 from _s_ to every \(v\in V\) . We thus have Equation (2) because

\(w_{\ge 0}^B(P_{G^B}(v))\le w_s^B(P_{G^B}(v))+|P_{G^B}(v)\cap E^{neg}(G^B)|\cdot B\text{since}w^B(e)\ge-B\text{for all}e\in E\)<br>
\(\le|P_{G^B}(v)\cap E^{neg}(G^B)|\cdot B\text{since}w_s^B(P_{G^B}(v))\le 0\)<br>
\(=\eta_{G^B}(v)\cdot B\text{by definition of}P_{G^B}(v)\)

Recall from the output guarantee of LowDiamDecomposition (Lemma 1.2) that \(\mathrm{Pr}[e\in E^{rem}]=O(w_{\ge 0}^B(e)\cdot(\mathrm{log}n)^2/D+n^{-10})\), where in our case \(D=dB=B\Delta/2\). This, the linearity of expectation, and (2) imply that

\(E[P_{G^B}(v)\cap E^{rem}]=O\left(\frac{w_{\ge 0}^B(P_{G^B}(v))\cdot(\mathrm{log}n)^2}{B\Delta/2}+|(P_{G^B}(v))|\cdot n^{-10}\right)\)<br>
\(=^\text{(2)}O\left(\frac{2\eta_{G^B}(v)\cdot(\mathrm{log}n)^2}{\Delta}+n^{-9}\right)\)

which is _O_(log<sup>2</sup>_n_) when \(\eta(G^B)\le\Delta\).

**Phase 1: Make edges inside the SCCs** _G<sup>B</sup>_\[_V<sub>i</sub>_\] **non-negative.** We argue that \(\mathrm{ScaleDown}(H,\Delta/2,B)\) is called with an input that satisfies its input requirements (Theorem 3.5). The most important requirement is \(\eta(H^B)\le\Delta/2\) (Item 1b) which we prove below (other requirements are trivially satisfied). Recall that we set \(d:=\Delta/2\) in Line 3.

**Lemma 4.5.** _If G has no negative-weight cycle, then_ \(\eta(H^B)\le d=\Delta/2\).

_Proof._ Consider any vertex \(v\in V\) . Let _P_:=_P<sub>H<sup>B</sup></sub>(v_)\\_s_; i.e. _P_ is obtained by removing _s_ from a shortest _sv_-path in \(H_s^B\) that contains \(\eta_{H^B}(v)\) negative weights in \(H_s^B\). Let _u_ be the first vertex in _P_. Note three easy facts:

(a) _w<sub>H<sup>B</sup></sub>(e_)=_w<sub>H</sub>(e_)+_B_ for all \(e\in E^{neg}(H^B)\),<tbc>

(b) \(|E^{neg}(H^B)\cap P|=|E^{neg}(H^B)\cap P_{H^B}(v)|=\eta_{H^B}(v)\), and<tbc>

(c) \(w_{H^B}(P)=w_{H_s^B}(P_{H^B}(v))\le w_{H_s^B}(s,v)=0\),<tbc>

