<tbc>graph _G<sub>i,p(u,D<sub>i</sub>_)</sub>. Thus, the shortest path of length _r<sub>i</sub>_ between _p(u,D<sub>i</sub>),u_ is available in the _i_-th iteration.

Consider now the a path \(P'\) from _p(u,D<sub>i</sub>_) to _v_ of length at most |_P_|+_r<sub>i</sub>_. By our arguments above and \(P\subset E_{k_0+1}\), the path \(P'\) is also in _E_<sub>_k_<sub>0</sub>+1</sub>. From Lemma A.3, \(L(P')\subset\{k_0+1,\dots,i-1\}\) has size at most _i_-(_k_<sub>0</sub>+1), so we can conclude the total error is at most,<tbc>

\(\hat{\delta}_i(p(u,D_i),v)\le\delta(u,v)+r_i+2(i-(k_0+1))\)

<tbc>Then,

\(\hat{\delta}(u,v)\le r_i+\hat{\delta}(p(u,D_i),v)\)<br>
\(\le\delta(u,v)+2r_i+2(i-(k_0+1))\)<br>
\(=\delta(u,v)+2\left(r_i+(i-(k_0+1))\right)\)<br>
\(\le\delta(u,v)+\beta\)

Next, we prove correctness under the assumption that _B(u_) is false. In particular, assume the set \(|C(u,i)|=|N(u,r_i)\cap D_{i+1}|\le 12s_{k-1}\mathrm{log}n\) is small.

**Lemma E.7.** _Suppose that the error event E does not occur._

_Let_ \(k_0+1\le i\le k_0+\frac{\beta}{2}-1\)_. Let u,v be a pair of vertices with a shortest path P_=(_u,u_<sub>2</sub>_,u_<sub>3</sub>_,...,v_<sub>3</sub>_,v_<sub>2</sub>_,v_) _with all edges in E_<sub>_k_<sub>0</sub>+1</sub>_. Suppose_ \(|N(u,r_i)\cap D_{i+1}|\le 12s_{k-1}\mathrm{log}n\)_. If_ \(\ell(u_{r_i})\le i+1\) _then, after Line 220 we have,_

\(\hat{\delta}(u,v)\le\hat{\delta}(u,v)+\beta\)

_Proof._ Since \(\ell(u_{r_i})\le i+1\), there is some vertex \(z\in N(u,r_i)\cap D_{i+1}\) such that _z=r(u<sub>r<sub>i</sub></sub>,D_<sub>_i_+1</sub>) as \(u_{r_i}\in N(u,r_i-1)\). Since \(P\subset E_{k_0+1}\), then after the (_i_+1)-th iteration,

\(\hat{\delta}(z,v)\le\delta(u_{r_i},v)+2(i-k_0)+1\)

where we apply Lemma A.3 with \(L(P)\subset\{k_0+1,\dots,i\}\) has size at most _i-k_<sub>0</sub>.

Then, after Line 220, since \(z\in N(u,r_i)\cap D_{i+1}=C(u,i)\),<tbc>

\(\hat{\delta}(u,v)\le r_i+\hat{\delta}(z,v)\le\delta(u_{r_i},v)+r_i+2(i-k_0)+1\)

<tbc>Now, \(\delta(u_{r_i},v)=\delta(u,v)-r_i+1\) so that,

\(\hat{\delta}(u,v)\le\delta(u,v)+2(i-k_0+1)\le\delta(u,v)+\beta\)

as \(i+1\le k_0+\frac{\beta}{2}\) .

From Lemmas E.6 and E.7 we can place an upper bound on the levels of many vertices of the shortest path. The following lemma shows that we obtain a good additive approximation when these bounds hold.

**Lemma E.8.** _Let P_=(_u,u_<sub>2</sub>_,...,v_<sub>2</sub>_,v_) _be a shortest path of length at most_ \(\beta+1\) _such that_ \(P\subset E_{k_0+1}\)_. Suppose the degrees_ \(\ell(u_{r_i}),\ell(v_{r_i})>i+1\) _for all_ \(k_0+1\le i\le k_0+\frac{\beta}{2}-1\).

_Then, Algorithm 15 obtains an approximation such that_ \(\hat{\delta}(u,v)\le\delta(u,v)+\beta\).

