ii. Remove _V<sub>i</sub>_ from A(_s_) and decrement score\((i)\leftarrow^-1\).<tbc>

iii. If \(\mathcal{A}(s)=\emptyset\):<br>
A. Update level\((s)\leftarrow^\pm 1\), \(\hat{L}(s,\text{level}(s)+1)\leftarrow\emptyset\).<br>
B. If \(\bigcup_{r=0}^{\text{level}(s)}\hat{L}(s,r)=V\) : then remove _s_ from _S_. Else, set \(\mathcal{A}(s)\leftarrow\hat{L}(s,\text{level}(s))\).<br>
C. For all \(V_i\cap\mathcal{A}(s)\neq\emptyset\), increment score(_i_).<br>
**Output:** \(\widehat{\text{d}}(s,v)\) for all \(s\in S_\text{in}\) and \(v\in V\) .

_Proof of Theorem 5.1._ We prove the correctness and running time of our algorithm.

## Correctness.

Beginning with correctness, we argue that our algorithm terminates and upon termination of our algorithm, all distances are correct i.e. \(\widehat{\text{d}}(s,v)=\text{dist}(s,v)\) for all \(s\in S_\text{in},v\in V\) .

First, we claim that in every iteration of the while loop \(\widehat{\text{d}}(s,v)\ge\text{dist}(s,v)\) for all \(s\in S_\text{in},v\in V\) .

**Lemma 5.2.** _In every iteration of the while loop_ \(\widehat{\text{d}}(s,v)\ge\text{dist}(s,v)\) _for all_ \(s\in S_\text{in},v\in V\) .

_Proof of Lemma 5.2._ Suppose for contradiction that there is some \(s\in S_\text{in}\) where \(\widehat{\text{d}}(s,v)<\text{dist}(s,v)\) in some iteration of the while loop. Consider the first iteration of the while loop where a violation \(\widehat{\text{d}}(s,v)<\text{dist}(s,v)\) occurs and let _v_ be the violating vertex. In particular, at the start of this iteration, we have \(\widehat{\text{d}}(s,v)\ge\text{dist}(s,v)\). During this iteration, we update \(\widehat{\text{d}}(s,v)\leftarrow\text{level}(s)+1<\text{dist}(s,v)\). By our two update rules, there exists \(u\in\mathcal{A}(s)\cap V_i\) with \((u,v)\in E\). Observe that \(\mathcal{A}(s)\subseteq\hat{L}(s,\text{level}(s))\) so \(u\in\hat{L}(s,\text{level}(s))\). Since \(u\in\hat{L}(s,\text{level}(s))\), we have at the start of this iteration that \(\text{dist}(s,u)\le\widehat{\text{d}}(s,u)\le\text{level}(s)\). By the triangle inequality, for \((u,v)\in E\) we have \(\text{dist}(s,v)\le\text{dist}(s,u)+1\le\text{level}(s)+1\), a contradiction.

Now, we argue that \(L(s,r)=\hat{L}(s,r)\) for all \(s\in S_\text{in}\) and \(r\le\text{level}(s)\) at the end of each iteration of the while loop.

**Lemma 5.3.** _At the end of each iteration of the while loop,_ \(\widehat{\text{d}}(s,v)=\text{dist}(s,v)\) _for all v with_ \(\text{dist}(s,v)\le\text{level}(s)\)_. In particular, for all_ \(r\le\text{level}(s)\), \(L(s,r)=\hat{L}(s,r)\).

_Proof of Lemma 5.3._ We proceed by induction on level(_s_). In the base case, _L(s,_0)={_s_} and we initialize \(\widehat{\text{d}}(s,s)=0\) and \(\hat{L}(s,0)=\{s\}\). In any future iteration of the while loop, we do not modify \(\hat{L}(s,0)\) or \(\widehat{\text{d}}(s,0)\) since level(_s_)+1_\>_0.

Now, consider \(\ell:=\text{level}(s)>0\). Consider the iteration of the while loop where level(_s_) is incremented to \(\ell\) for the first time. At the end of the previous iteration, we have \(\text{level}(s)=\ell-1\). Induction then implies that \(\widehat{\text{d}}(s,u)=\text{dist}(s,u)\) for all \(\text{dist}(s,u)<\ell\) and \(L(s,r)=\hat{L}(s,r)\) for all \(r<\ell\).

Fix _v_ with \(\text{dist}(s,v)=\ell\) and let \(s=w_0,\dots,w_{\ell-1},w_\ell=v\) denote a shortest path. By induction, \(w_{\ell-1}\in L(s,\ell-1)=\hat{L}(s,\ell-1)\) holds at the iteration where level(_s_) is incremented to \(\ell-1\) for the first time. At this iteration, the algorithm sets \(\mathcal{A}(s)\leftarrow\hat{L}(s,\ell-1)=L(s,\ell-1)\) so that \(w_{\ell-1}\in\mathcal{A}(s)\).

Since we only increment level(_s_) when A(_s_) is empty, there was an iteration of the while loop (possibly the current one) \(w_{\ell-1}\) must have been removed from A(_s_). In particular, there was an iteration where \(w_{\ell-1}\in V_i\cap\mathcal{A}(s)\) and therefore \(s\in S'\). For this iteration, we consider two cases.

**Case 1:** \(|N(V_i)|\le\frac{\phi n\mathrm{log}n}{|S_\text{in}|}\)**.** Since \(w_{\ell-1}\in V_i\cap\mathcal{A}(s)\) and \((w_{\ell-1},v)\in E\), so we set \(\widehat{\text{d}}(s,v)\le\ell\) since at this time \(\text{level}(s)=\ell-1\) (i.e. we have inserted \(w_{\ell-1}\) into A(_s_) so \(\text{level}(s)\ge\ell-1\) but we have yet to increment level(_s_) to \(\ell\)).

**Case 2:** \(|N(V_i)|>\frac{\phi n\mathrm{log}n}{|S_\text{in}|}\)**.** Since \(w_{\ell-1}\in V_i\cap\mathcal{A}(s)\) and \((w_{\ell-1},v)\in E\), we have \(X[s,w_{\ell-1}]=Y[w_{\ell-1},v]=1\) so that (_XY_)\[_s,v_\]=1 and we set \(\widehat{\text{d}}(s,v)\le\ell\) (where \(\text{level}(s)=\ell-1\) as observed in Case 1).

By Lemma 5.2, we have in both cases that \(\widehat{\text{d}}(s,v)\ge\text{dist}(s,v)=\ell\) so \(\widehat{\text{d}}(s,v)=\ell\). In any future iterations, the estimated distance does not change, as \(\text{level}(s)+1\ge\ell+1\) is increasing.

