**Corollary 3.9.** _Given a straight-line program_ **G**_<sub>X</sub> of size n generating a string X of length N\>_0_, a straight-line program_ **G**_<sub>Y</sub> of size m generating a string Y of length M\>_0_, and an integer_ \(\tau\in[1..N+M]\)_, one can in_ \(\widetilde{O}(\frac{N+M}{\tau}+nm\tau)\) _time construct a box decomposition_ \(\mathbf{B}=(B_{i,j})_{i\in[1..p_X],j\in[1..p_Y]}\) _of G<sub>X,Y</sub> with_ \(p_X=O(\lceil\frac{N}{\tau}\rceil)\) _and_ \(p_Y=O(\lceil\frac{M}{\tau}\rceil)\)_, along with an oracle providing_ \(\widetilde{O}(1)\)_-time random access to the DIST<sub>B<sub>i,j</sub></sub> matrices._

_Proof._ First, we use Lemma 3.7 to obtain grammars \(\mathbf{G}_X^+\) and \(\mathbf{G}_X^P\). The string _P<sub>X</sub>_ represented by \(\mathbf{G}_X^P\) satisfies \(X=\mathrm{exp}_{\mathbf{G}_X^+}(P_X)\), so it can be interpreted as a decomposition of _X_ into _p<sub>X</sub>_:=|_P<sub>X</sub>_| phrases, with the _i_th phrase _X<sub>i</sub>_ being an occurrence of \(\mathrm{exp}_{\mathbf{G}_X^+}(P_X[i])\). The decomposition of _Y_ is obtained in the same way based on grammars \(\mathbf{G}_Y^+\) and \(\mathbf{G}_Y^P\) constructed for _Y_ .

The box decomposition **B** is based on these decompositions of _X_ and _Y_ . Note that each box _B<sub>i,j</sub>_ satisfies

\(DIST_{B_{i,j}}=DIST_{\mathrm{exp}_{\mathbf{G}_X^+}(P_X[i]),\mathrm{exp}_{\mathbf{G}_Y^+}(P_Y[j])}.\)

Due to \(|P_X[i]|\le\tau\) and \(|P_Y[j]|\le\tau\), Lemma 3.8 applied to \(\mathbf{G}_X^+\) and \(\mathbf{G}_Y^+\) provides \(\widetilde{O}(1)\)-time oracle access to all these matrices. Storing _P<sub>X</sub>_ and _P<sub>Y</sub>_, we can point to _DIST<sub>B<sub>i,j</sub></sub>_ in _O_(1) time given _i,j_.

## 3.3 Algorithm

**Proposition 3.10.** _Given a straight-line program_ **G**_<sub>X</sub> of size n generating a string X of length N\>_0_, a straight-line program_ **G**_<sub>Y</sub> of size m generating a string Y of length M\>_0_, and a parameter_ \(\epsilon\in(0,1]\)_, a_ \((1+\epsilon)\)_-approximation of_ \(\delta_D(X,Y)\) _can be computed in_ \(\widetilde{O}\left((nm(N+M))^{2/3}\epsilon^{-1/3}\right)\) _time._

_Proof._ The algorithm uses Corollary 3.9 and Lemma 3.5 with the set of portals **P** defined as in Lemma 3.6, where \(\alpha=\Omega(\frac{\epsilon}{p_X+p_Y-2})=\Omega(\frac{\epsilon\tau}{N+M})\) is chosen so that \((1+2\alpha)^{p_X+p_Y-2}=1+\epsilon\). Lemma 3.6 guar antes that the resulting value is a \((1+\epsilon)\)-approximation of \(\delta_D(X,Y)\). The number of portals is \(O\left(\frac{NM}{\tau^2}+\frac{N}{\tau}\mathrm{log}_{1+\alpha} M+\frac{M}{\tau}\mathrm{log}_{1+\alpha} N\right)=\widetilde{O}\left(\frac{(N+M)^2}{\epsilon\tau^2}\right)\), so the overall running time is \(\widetilde{O}\left(nm\tau+\frac{(N+M)^2}{\epsilon\tau^2}\right)\). Optimizing \(\tau\in[1..N+M]\), we get \(\widetilde{O}(nm+\epsilon^{-1}+(nm(N+M))^{2/3}\epsilon^{-1/3})\) time. If the first term dominates, then \(nm\ge(nm(N+M))^{2/3}\epsilon^{-1/3}\ge(N+M)^2\epsilon^{-1}\). However, \(O(NM)=O((N+M)^2\epsilon^{-1})\) time is enough to compute \(\delta_D(X,Y)\) exactly without compression. If the second term dominates, then \(\epsilon^{-1}\ge(nm(N+M))^{2/3}\epsilon^{-1/3}\ge nm(N+M)\). However, \(\widetilde{O}(\sqrt{nm}(N+M))=\widetilde{O}(nm(N+M))\) time is enough to compute \(\delta_D(X,Y)\) exactly using Proposition 3.13 with _D=N+M_.

Theorem 3.1 follows through the reduction from \(\delta_E\) to \(\delta_D\).

## 3.4 Exact Output-Sensitive Algorithm

In this section we prove Theorem 3.11:

**Theorem 3.11.** _Given a straight-line program_ **G**_<sub>X</sub> of size n generating a string X of length N\>_0 _and a straight-line program_ **G**_<sub>Y</sub> of size m generating a string Y of length M\>_0_, the edit distance_ \(\delta_E(X,Y)\) _can be computed in_ \(\widetilde{O}\left(\sqrt{(1+\delta_E(X,Y))nm(N+M)}\right)\) _time._

The algorithm behind Theorem 3.11 reduces the problem to a decision version (asking whether \(\delta_E(X,Y)\le D\) for a threshold _D_) and then uses the same scheme with all boundary vertices (_x,y_) satisfying \(|x-y|\le D\) selected as portals.

**Lemma 3.12.** _Let_ **B** _be a box decomposition of the graph G<sub>X,Y</sub> for_ \(X,Y\in\Sigma^+\) _and let_ \(D\ge 0\) _be an integer. Suppose that_ **P** _consists of all the boundary vertices v<sub>x,y</sub> of_ **B** _satisfying_ \(|x-y|\le D\)_. Then, every vertex_ \(v_{x,y}\in B_{i,j}\) _with_ \(d_{x,y}\le D\) _satisfies_ \(D_{x,y}^{i,j}=d_{x,y}\).

_Proof._ We proceed by induction on _i+j_. The base case is trivially satisfied due to \(D_{x,y}^{1,1}=d_{x,y}\) for \(v_{x,y}\in B_{1,1}\). We henceforth fix \(v_{x,y}\in B_{i,j}\) with \((i,j)\neq(1,1)\) and \(d_{x,y}\le D\). By Observation 3.3, there is a shortest path from _v_<sub>0,0</sub> to _v<sub>x,y</sub>_ contained within _G_<sub>_X_\[1_..x_\]_,Y_\[1_..y_\]</sub>. Let \(v_{x^\prime,y^\prime}\) be the first vertex on this path that belongs to _B<sub>i,j</sub>_. Observe that \(v_{x^\prime,y^\prime}\in\mathrm{in}^{B_{i,j}}\) and \(d_{x,y}=d_{x^\prime,y^\prime}+d(v_{x^\prime,y^\prime},v_{x,y})\). Consequently, \(|x'-y'|\le d_{x^\prime,y^\prime}\le d_{x,y}\le D\), so \(v_{x^\prime,y^\prime}\in\mathbf{P}_{i-1,j}\cup\mathbf{P}_{i,j-1}\). By symmetry, we may assume without loss of generality that \(v_{x^\prime,y^\prime}\in\mathbf{P}_{i-1,j}\).

Let us construct a portal-respecting (_i,j_)-walk to _v<sub>x,y</sub>_ by concatenating a shortest portal-respecting (_i_-1_,j_)-walk to \(v_{x^\prime,y^\prime}\) and a shortest path from \(v_{x^\prime,y^\prime}\) to _v<sub>x,y</sub>_ (by Observation 3.3 applied to \(G_{X(x^\prime..x],Y(y^\prime..y]}\),<tbc>

