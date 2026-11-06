This approach works as in the recursive calls performed by A<sub>DISED</sub> we compute \(\text{sim}(\text{sub}(v),\text{sub}(v'))\) for all \((v,v')\in\mathbf{S}\times\mathbf{S}'\). Indeed, fix \((v,v')\in\mathbf{S}\times\mathbf{S}'\). We have the invariant that we always recurse on an instance where both _v_ and \(v'\) are contained, until we reach an \((u,u',w,w')\)-DISED instance such that either \(u\le v<w\) and \(u'\) immediately precedes \(w'\), or _u_ immediately precedes _w_ and \(u'\le v'<w'\). In either case \(\text{sim}(\text{sub}(v),\text{sub}(v'))\) is among the output of the \((u,u',w,w')\)-DISED instance.

To conclude the proof, we must also explain where we get the inputs from. We rewrite the indices for Input (i) as

\(\{(x,x',y,y'):x\in\mathsf{B}_\mathsf{I}^\top(s,s',q,q'),(y,y')\in\mathsf{B}_\mathsf{r}^\top(s,s',q,q')\}=\)<br> \(\{(x,x',y,y'):(x,x')\in[\mathsf{I}(s)..\mathsf{I}(q)]\times\mathsf{I}(q'),(y,y')\in[\mathsf{r}(q)..\mathsf{r}(s)]\times\mathsf{r}(q')\}\) (7)

\(\cup\{(x,x',y,y'):(x,x')\in[\mathsf{I}(s)..\mathsf{I}(q)]\times\mathsf{I}(q'),(y,y')\in\mathsf{r}(q)\times[\mathsf{r}(q')..\mathsf{r}(s')]\}\) (8)

\(\cup\{(x,x',y,y'):(x,x')\in\mathsf{I}(q)\times[\mathsf{I}(s')..\mathsf{I}(q')],(y,y')\in[\mathsf{r}(q)..\mathsf{r}(s)]\times\mathsf{r}(q')\}\) (9)

\(\cup\{(x,x',y,y'):(x,x')\in\mathsf{I}(q)\times[\mathsf{I}(s')..\mathsf{I}(q')],(y,y')\in\mathsf{r}(q)\times[\mathsf{r}(q')..\mathsf{r}(s')]\}.\) (10)

We can compute the similarity for the various subsets of indices (7), (8), (9) and (10) as follows.

For (7), note that \(\mathbf{F}'[x'..y')=\mathbf{F}'[\mathsf{I}(q')..\mathsf{r}(q'))=\text{sub}(q')\) contains a single node, namely \(q'\), because \(q'\) is the last node appearing in \(\mathbf{S}'\). Consequently, the similarity to be computed corresponds to

\(max\left\{0,max_{v\in\mathbf{F}[x..y)}\{\eta(v,q')\}\right\}.\)

By using clever bottom-up dynamic programming we can compute these similarities for all \(x\in[\mathsf{I}(s)..\mathsf{I}(q)]\) and \(y\in[\mathsf{r}(q)..\mathsf{r}(s)]\) in time O(_m_<sup>2</sup>).

For (8), note that \(\mathbf{S}\cap\mathbf{F}[\mathsf{I}(s)..\mathsf{r}(q))=\{q\}\) and \(\mathbf{S}'\cap\mathbf{F}'[\mathsf{I}(q')..\mathsf{r}(s'))=\{q'\}\). Furthermore, since sub(_q_)=_q_ and \(\text{sub}(q')=q'\), it follows that \(\text{sim}(\text{sub}(q),\text{sub}(q'))=max\{0,\eta(q,q')\}\). This last similarity, combined with the input provided to SED, gives us \(\text{sim}(\text{sub}(v),\text{sub}(v'))\) for all pairs \((v,v')\in\mathbf{F}[\mathsf{I}(s)..\mathsf{r}(q))\times\mathbf{F}'[\mathsf{I}(q')..\mathsf{r}(s'))\). Thus, we can apply Main Theorem 4 on **F**[I(_s).._r(_q_)) and \(\mathbf{F}'[\mathsf{I}(q')..\mathsf{r}(s'))\) to obtain the suffix-prefix similarities between these intervals, which is exactly what we need to compute.

For (9), as (9) equals to (8) under reverse symmetry, it suffices to apply symmetric computations.

For (10), as (7) equals to (8) under swap symmetry, it suffices to apply symmetric computations.

Finally, Inputs (ii), (iii), (iv), and (v) can all be computed using similar computations as in (7).

The overall complexity can be bounded by O(T<sub>MUL</sub>(_n_)+_n_<sup>2+_o_(1)</sup>) since the bottlenecks are applying the DISED algorithm and Main Theorem 4. In the unweighted setting, we note that global tree size is at most _n_, thus obtaining a running time of O(T<sub>MonMUL</sub>(_n_)+_n_<sup>2+_o_(1)</sup>_g(n_)) where T<sub>MonMUL</sub>(_n,n,n,_D)=O(_f(n)g_(D)). Furthermore, we can use Theorem 4.1 instead of Main Theorem 4.

## 5.3 Patching together subproblems

This section is dedicated to proving Lemma 5.3. Given the numerous cases involved, we first prove Lemma 5.7, Lemma 5.8, and Lemma 5.9, which allow us to break down the proof of Lemma 5.3 into three more "digestible" steps.

**Lemma 5.7.** _Suppose we are provided with the input of an_ \((s,s',q,q')\)_-DISED instance of size m. Further, let_ \(r\in\mathbf{S}\) _such that s\<r\<q. Then, we can compute_ \(\text{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\) _for all_ \((x,x')\in(\mathsf{I}(r)\times[\mathsf{r}(q')..\mathsf{r}(s')])\cup([\mathsf{I}(r)..\mathsf{I}(q)]\times\mathsf{r}(q'))\) _and_ \((y,y')\in(\mathsf{r}(r)\times[\mathsf{r}(q')..\mathsf{r}(s')])\cup([\mathsf{r}(q)..\mathsf{r}(r)]\times\mathsf{r}(s'))\) _in time_ O(T<sub>_MUL_</sub>(_m_)+_m_<sup>2+_o_(1)</sup>).

_Furthermore, if the DISED instance is unweighted and has global tree size_ D_, then the algorithm requires time_ O(T<sub>_MonMUL_</sub>(_m,m,m,D_)+_m_<sup>2+_o_(1)</sup>_g_(D)) _where_ T<sub>_MonMUL_</sub>(_m,m,m,_D)=O(_f(m)g_(D)).

