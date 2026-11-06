Then, during this iteration, \(\widehat{\mathrm{d}}(s,v)\) was updated, i.e. we update \(\widehat{\mathrm{d}}(s,v)\leftarrow\widehat{\mathrm{d}}(s,u)+\mathrm{wt}(u,v)<\mathrm{dist}(s,v)\) for some \(u\in\mathcal{A}(s,b)\cap V_i^{(b)}\) with \(\widehat{\mathrm{d}}(s,v)=\widehat{\mathrm{d}}(s,u)+\mathrm{wt}(u,v)\). Note that \(\widehat{\mathrm{d}}(s,u)\) was computed in some previous iteration. Thus, there is a path from _s_ to _u_ with length \(\widehat{\mathrm{d}}(s,u)\), which we may extend to _v_ via the edge (_u,v_) with weight wt(_u,v_). This is a contradiction.

The remainder of the proof is dedicated to showing that our algorithm produces exact shortest distances. We begin with some useful claims about level(_s,b_), level(_s_), whose proofs are deferred.

**Claim 5.11.** _In any iteration of the while loop,_ level(_s_) _increases by at most one for all_ \(s\in S_\mathrm{in}\).

**Claim 5.12.** _Let_ \(s\in S_\mathrm{in}\) _and_ \(\ell\le\mathrm{ccc}(s)\)_. Then, for every b such that_ \(\ell\) _is a multiple of b, there exists an iteration where_ \(\mathrm{level}(s)=\mathrm{level}(s,b)=\ell\) _at the beginning of the iteration._

Next, we prove that our algorithm iteratively computes correct distances, analogously to Lemma 5.3.

**Lemma 5.13.** _At the end of each iteration of the while loop,_ \(\widehat{\mathrm{d}}(s,v)=\mathrm{dist}(s,v)\) _for all_ \(\mathrm{dist}(s,v)\le\mathrm{level}(s)\)_. In particular, for all_ \(r\le\mathrm{level}(s)\), \(L(s,r)=\hat{L}(s,r)\).

_Proof._ We proceed by induction, where the base case follows identically as Lemma 5.3. Now, let \(\ell>0\). Consider the first iteration of the while loop where \(\mathrm{level}(s)=\ell\). In this iteration, we incremented level(_s_). By Claim 5.11, level(_s_) increments by at most 1, so that at the end of the previous iteration, we have \(\mathrm{level}(s)=\ell-1\).

By induction, we have \(\widehat{\mathrm{d}}(s,u)=\mathrm{dist}(s,u)\) for all \(\mathrm{dist}(s,u)<\ell\). Consider a vertex with \(\mathrm{dist}(s,v)=\ell\) and a shortest path _s=w_<sub>0</sub>_,...,w_<sub>_p_-1</sub>_,w<sub>p</sub>=v_ where \(\mathrm{dist}(s,w_{p-1})<\ell\). Suppose \((w_{p-1},v)\in E_b\) and \(w_{p-1}\in V_i^{(b)}\). By induction, \(\widehat{\mathrm{d}}(s,w_{p-1})=\mathrm{dist}(s,w_{p-1})\) and \(w_{p-1}\in\hat{L}(s,r)\) for \(r=\mathrm{dist}(s,w_{p-1})\ge\ell-2b+1\) since edge weights in _E<sub>b</sub>_ are less than 2_b_. Let \(\ell_0\) be the multiple of _b_ such that \(\ell_0-b<\mathrm{dist}(s,w_{p-1})\le\ell_0\). Note that we have \(\ell_0<\ell\le\mathrm{ccc}(s)\) since \(\mathrm{wt}(u,v)\ge b\).

Consider the first iteration where \(\mathrm{level}(s,b)=\mathrm{level}(s)=\ell_0\), which exists by Claim 5.12. In this iteration, we set \(\mathcal{A}(s,b)\leftarrow\bigcup_{r=\ell_0-b+1}^{\ell_0}\hat{L}(s,r)=\bigcup_{r=\ell_0-b+1}^{\ell_0}L(s,r)\) so that \(w_{p-1}\in\mathcal{A}(s,b)\). Now, in the current iteration, we have \(\mathrm{level}(s,b)\ge\mathrm{level}(s)=\ell\), which implies that `updateScores` or `increaseLevel` was triggered i.e. \(\mathcal{A}(s,b)=\emptyset\). Thus, there was an intermediate iteration where _w_<sub>_p_-1</sub> was removed from A(_s,b_) i.e. \(V_i^{(b)}\) was chosen. We argue that at the start of this intermediate iteration, \(\widehat{\mathrm{d}}(s,w_{p-1})=\mathrm{dist}(s,w_{p-1})\). This follows via induction, as above we showed \(\mathrm{level}(s)\ge\ell_0\ge\mathrm{dist}(s,w_{p-1})\) (in fact this was already true in the iteration where A(_s,b_) was set).

We now consider two cases.

**Case 1:** \(|N(V_i^{(b)})|\le\frac{n}{|S_\mathrm{in}|}\)**.** Since \(w_{p-1}\in V_i^{(b)}\cap\mathcal{A}(s,b)\) and \((w_{p-1},v)\in E_b\), so we set \(\widehat{\mathrm{d}}(s,v)\le\widehat{\mathrm{d}}(s,w_{p-1})+\mathrm{wt}(w_{p-1},v)\le\mathrm{dist}(s,w_{p-1})+\mathrm{wt}(w_{p-1},v)=\mathrm{dist}(s,v)\).

**Case 2:** \(|N(V_i^{(b)})|>\frac{n}{|S_\mathrm{in}|}\)**.** Since \(w_{p-1}\in V_i^{(b)}\cap\mathcal{A}(s,b)\) and \((w_{p-1},v)\in E_b\), we have \(X[s,w_{p-1}]=\mathrm{dist}(s,u)\), _Y_\[_w_<sub>_p_-1</sub>_,v_\]=wt(_u,v_) so that \((X\star Y)[s,v]\le\mathrm{dist}(s,u)+\mathrm{wt}(u,v)\) and we set \(\widehat{\mathrm{d}}(s,v)\le\mathrm{dist}(s,u)+\mathrm{wt}(u,v)=\mathrm{dist}(s,v)\).

Thus, we have \(\widehat{\mathrm{d}}(s,v)=\mathrm{dist}(s,v)\) in this intermediate iteration. Note that we already have \(\widehat{\mathrm{d}}(s,v)=\mathrm{dist}(s,v)\) in an iteration where level(_s_)=\(\mathrm{level}(s,b)=\ell_0\). The distance equality holds also in any subsequent iteration since \(\widehat{\mathrm{d}}\) does not increase, and does not decrease below dist(_s,v_) Lemma 5.10.

Finally, we argue that \(\hat{L}(s,\ell)=L(s,\ell)\). Suppose \(v\in\hat{L}(s,\ell)\), so that \(\widehat{\mathrm{d}}(s,v)\le\ell\). We can in fact conclude \(\widehat{\mathrm{d}}(s,v)=\ell\) since if \(\widehat{\mathrm{d}}(s,v)=\mathrm{dist}(s,v)<\ell\) then \(v\notin\hat{L}(s,\ell)\) by induction.

Conversely, if \(v\in L(s,\ell)\), consider the iteration where \(\mathrm{level}(s)=\ell\) for the first time. We increment level(_s_) either in `updateScores` or `increaseLevel`. Recall from our previous discussion that we have \(\widehat{\mathrm{d}}(s,v)=\mathrm{dist}(s,v)\) in some iteration where \(\mathrm{level}(s)=\ell_0<\ell\), where \(\ell_0\) is the multiple of _b_ satisfying \(\ell_0-b<\mathrm{dist}(s,w_{p-1})\le\ell_0\) above. We consider two cases.

