We now argue \(L(s,\ell)=\hat{L}(s,\ell)\). In our above argument, in the iteration where we set \(\widehat{\mathfrak{d}}(s,v)\) we also add _v_ to \(\hat{L}(s,\ell)\), so \(L(s,\ell)\subseteq\hat{L}(s,\ell)\). Again, this follows as \(\text{level}(s)=\ell-1\) and we add _v_ to \(\hat{L}(s,\text{level}(s)+1)\).

To argue the reverse inclusion, let _v_ be some vertex where \(\widehat{\mathfrak{d}}(s,v)=\ell\) in some iteration of the while loop where \(s\in S'\) and \(\text{level}(s)=\ell-1\). By Lemma 5.2, we have \(\text{dist}(s,v)\unknown\ell\). If \(v\unknown\in L(s,\ell)\), we have \(\text{dist}(s,v)<\ell\). Then, since \(\text{level}(s)=\ell-1\), the inductive hypothesis states that \(\widehat{\mathfrak{d}}(s,v)=\text{dist}(s,v)\unknown\ell-1\), a contradiction.

Finally, we again observe that in any future iterations where \(\text{level}(s)\unknown\ell\), only \(\hat{L}(s,\text{level}(s)+1)\) is modified so \(L(s,\ell)=\hat{L}(s,\ell)\) for all future iterations of the while loop, as desired.

Next, we argue that the while loop does not terminate until all distances are computed.

**Lemma 5.4.** _If there exists_ \(\widehat{\mathfrak{d}}(s,v)>\text{dist}(s,v)\) _at the end of an iteration, then the while loop will not terminate._

_Proof of Lemma 5.4._ We claim \(\mathcal{A}(s)\neq\emptyset\) for all \(s\in S\). If \(\mathcal{A}(s)=\emptyset\) at the end of the iteration, then it is empty at the if statement right before the end of the iteration. If A(_s_) is still empty after the if statement, \(\hat{L}(s,\text{level}(s))=\emptyset\). By Lemma 5.3 and _G_ being connected, we have ecc(_s)\<_level(_s_). Consider the first iteration where level(_s_)=eccc(_s_) (which must be a previous iteration of the while loop). By Lemma 5.3, during that iteration _s_ is already removed from _S_ as

\(\bigcup_{r=0}^{\text{level}(s)}\hat{L}(s,r)=\bigcup_{r=0}^{\text{level}(s)}L(s,r)=\bigcup_{r=0}^{\text{eccc}(s)}L(s,r)=V.\)

Thus, \(s\unknown\in S\), a contradiction.

Applying our claim above, we argue that \(\sum_i\text{score}(i)\unknown|S|\) since<tbc>

\(\sum_{i\in[k]}\text{score}(i)=\sum_{i\in[k]}|\{s\in S\text{s.t.}\mathcal{A}(s)\cap V_i\neq\emptyset\}|=\sum_{s\in S}|\{i\in[k]\text{s.t.}\mathcal{A}(s)\cap V_i\neq\emptyset\}|\unknown|S|.\)

<tbc>If all \(\text{score}(i)\unknown\frac{|S||N(V_i)|}{2\phi n}\) , then since C is a \((d,\phi)\)-LDSND,

\(\sum_i\text{score}(i)\unknown|S|\sum_i\frac{|N(V_i)|}{2\phi n}\unknown\frac{|S|}{2}.\)

Thus, there is some _i_ with \(\text{score}(i)>\frac{|S||N(V_i)|}{2\phi n}\) and the while loop does not terminate.

Thus, if the while loop terminates, then we return \(\widehat{\mathfrak{d}}(s,v)=\text{dist}(s,v)\) for all \(s\in S_\text{in},v\in V\) .

## Running Time.

We now bound the running time of our algorithm. This will also complete the correctness argument as we will show that the while loop terminates. Initializing _S_, \(\hat{L}(s,0)\), A(_s_), \(\widehat{\mathfrak{d}}(s,s)\), level(_s_), and \(\widehat{\mathfrak{d}}(s,v)\) for all _v_ requires _O_(|_S_<sub>in</sub>|_n_) time. Initializing score(_i_) requires _O(n_) time by enumerating all _V<sub>i</sub>_. Overall, we have used time linear in the output so far.

It now remains to analyze the running time of the while loop. Fix a cluster _V<sub>i</sub>_. We bound the running time of all iterations of the while loop where _i_ is chosen as the cluster with \(\text{score}(i)>\frac{|S||N(V_i)|}{2\phi n}\) . Let _T(i_) denote the iterations where _V<sub>i</sub>_ is the chosen cluster. We now argue that (1) for all \(s\in S_\text{in}\), there are few (roughly _d_) iterations \(t\in T(i)\) where \(V_i\cap\mathcal{A}(s)\neq\emptyset\), and (2) |_T(i_)| is not too large (roughly \(\frac{n}{|V_i|}\)). We begin with the first claim.

**Lemma 5.5.** _For any_ \(s\in S_\text{in}\) _and V<sub>i</sub>,_ \(V_i\cap\mathcal{A}(s)\neq\emptyset\) _(equivalently_ \(s\in S'\)_) for at most d_+1 _distinct_ \(t\in T(i)\).

_Proof of Lemma 5.5._ Let \(V_i\cap\mathcal{A}(s)\neq\emptyset\) (equivalently \(s\in S'\)) for _k_:=_k(s,i_) distinct iterations of the while loop where _V<sub>i</sub>_ is the chosen cluster (i.e. distinct \(t\in T(i)\)).

First, observe that for all \(s\in S_\text{in}\), \(\mathcal{A}(s)\subseteq\hat{L}(s,\text{level}(s))\) at every iteration, since every time level(_s_) increases, we set \(\mathcal{A}(s)\leftarrow\hat{L}(s,\text{level}(s))\). In later iterations, we only remove vertices from A(_s_) and leave<tbc>

