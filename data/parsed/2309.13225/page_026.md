\(\hat{\delta}(w^*,v)\le\delta(w,v)+1\)

<tbc>Since \(D_{\ell(w)}\subset D_2\) and \(z^*\in D_5\), and \(2+5+6\le 13\), the path \((v,w^*,z^*,z)\circ P_{z,u}\) exists in _G_<sub>6_,v_</sub> and **Dijkstra** computes a +4 approximation.

\(\hat{\delta}(v,u)\le\hat{\delta}(v,w^*)+\hat{\delta}(w^*,z^*)+1+\delta(z,u)=\delta(v,u)+4\)

To analyze the running time, it suffices to observe that for each _i_, \(|D_i|=\tilde{O}(n^{i/6})\) while _G<sub>i,w</sub>_ has _O(n_<sup>2-(_i_-1)/6</sup>) edges so that the computation of **Dijkstra** requires \(\tilde{O}(n^{13/6})\). Finally, computing **BK2APASP** on _G_<sub>3</sub>=(_V,E_<sub>3</sub>) requires \(\tilde{O}(m\sqrt{n})=\tilde{O}(n^{13/6})\).

## Correctness

Finally, we prove Theorem 4.1 for general \(k\ge 6\).

_Proof._ First, we note that \(\delta(u,v)\le\hat{\delta}(u,v)\) since **BK2APASP** is correct and every edge weight in _G<sub>j,w</sub>_ is a distance estimate computed by some path in the original graph _G_.

Suppose \(P\subset E_{l_0+1}\). By the correctness of **BK2APASP**, \(\hat{\delta}(u,v)\le 2\delta(u,v)\).

Then, suppose \(P\unknown\subset E_{l_0+1}\). Suppose \(\ell(v)\le\ell(u)\). Recall from Lemma A.2 the blocking vertices _B(P_)={_x_<sub>0</sub>_,x_<sub>1</sub>_,...,x<sub>t</sub>_} and levels _L<sub>B</sub>(P_) of path _P_.

Let \(a=min_{\ell(x_i)\le l-\frac{l_0}{2}+1}i\) be the minimum index of an element in the blocking set such that \(\ell(x_i)\le l-\frac{l_0}{2}+1\). Since _P_ is not contained in _E_<sub>_l_<sub>0</sub>+1</sub>, we can assume _a_ exists and \(a\ge 1\). Otherwise, every edge is in \(E_{l-\frac{l_0}{2}+2}=E_{(3k+2)/2}\subset E_{k-1}=E_{l_0+1}\). Since \(l\ge\ell(x_1)>\ell(x_2)>\dots>\ell(x_t)\ge 1\) (Lemma A.1), we can upper bound,

\(a\le l-\left(l-\frac{l_0}{2}+1\right)=\frac{l_0}{2}-1=\frac{k}{2}-2\)

Let \(x_a\in B(P)\) be the corresponding vertex in _B(P_). Since _P_ has an edge not in _E_<sub>_l_<sub>0</sub>+1</sub>, the last blocking vertex of minimum level must have \(\ell(x_t)\le l_0\). Recall that we denote \(v^*=r\left(v,D_{\ell(v)}\right)\) for any vertex _v_. Since \(P\subset E_{\ell(x_t)}\), we again have \(\hat{\delta}_{\ell(x_t)}(x_t^*,x_a^*)\le\delta(x_t,x_a)+2\) and \(\hat{\delta}_{\ell(x_t)}(x_t^*,x_{a+1}^*)\le\delta(x_t,x_{a+1})+2\).

Consider the \(\ell(x_a)\)-th iteration. The edges \(D_{\ell(x_t)}\times D_{\ell(x_{a+1})}\) are in \(G_{\ell(x_a),x_a}\) as,<tbc>

\(\ell(z)+\ell(x_{a+1})+\ell(x_a)\le l_0+\left(l-\frac{l_0}{2}\right)+\left(l-\frac{l_0}{2}+1\right)=2l+1\)

<tbc>Next observe that \(x_t\in P_{x_a,x_{a+1}}\) (Lemma A.1), as each blocking vertex _x_<sub>_i_+1</sub>=_b(x<sub>i</sub>,P_<sub>_x<sub>i</sub>,x_<sub>_i_-1</sub></sub>) is by definition in the sub-path _P_<sub>_x<sub>i</sub>,x_<sub>_i_-1</sub></sub>. Therefore we have the path \((x_a^*,x_t^*,x_{a+1}^*,x_{a+1})\circ P_{x_{a+1},x_{a-1}}\) so **Dijkstra** computes an estimate at most,

\(\hat{\delta}_{\ell(x_a)}(x_a^*,x_{a-1})\le\hat{\delta}_{\ell(x_t)}(x_a^*,x_t^*)+\hat{\delta}_{\ell(x_t)}(x_t^*,x_{a+1}^*)+1+\delta(x_{a+1},x_{a-1})\)<br>
\(\le\delta(x_a,x_t)+\delta(x_t,x_{a+1})+\delta(x_{a+1},x_{a-1})+5\)<br>
\(\le\delta(x_a,x_{a-1})+5\)

Then, following a similar argument to the inductive step of Lemma A.2, we claim the following for all \(1\le j\le a\).

\(\hat{\delta}_{\ell(x_j)}(x_j^*,x_{j-1})\le\delta(x_j,x_{j-1})+2(2+(a-j))+1\)

where we have established the base case _j=a_ above. We now proceed by induction for _j\<a_. Consider an execution of **Dijkstra** from \(x_j^*\) in \(G_{\ell(x_j),x_j^*}\). Let _x_<sub>_j_+1</sub> be the blocking vertex from the<tbc>

