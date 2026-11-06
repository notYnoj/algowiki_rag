Note that it is straightforward to verify whether any vertex _v_ of _T_ is a leaf in the \(\alpha\)-separating tree of _T_ and hence we obtain the following.

**Observation 6.3.** _Given a tree T with no long chain and_ \(\alpha\)_, a minimal_ \(\alpha\)_-separating tree of T can be computed in polynomial-time._

Using Lemma 6.2 and choosing appropriately the value of \(\alpha\), one can obtain an \(\alpha\)-separating tree of _T_ having at most \(t=2^{O(\sqrt{logn})}\) vertices.

**Lemma 6.4.** _Let T be any tree and let_ \(\alpha\) _be selected arbitrarily. If T_<sup>∗</sup> _is a minimal_ \(\alpha\)_-separating tree of T, then_ \(\xi(T^*)\) _has at most_ \(4\left\lceil\frac{n}{\alpha}\right\rceil\) _vertices._

_Proof._ By definition, for each leaf _v_ of _T_<sup>∗</sup>, the subtree _T<sub>v</sub>_ has more than \(\alpha\) nodes. Since these trees are node-disjoint, we obtain that there are at most \(\left\lceil\frac{n}{\alpha}\right\rceil\) leaves in _T_<sup>∗</sup>. We denote the leaves of _T_<sup>∗</sup> by _v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>l</sub>_, \(l\le\left\lceil\frac{n}{\alpha}\right\rceil\); note that \(\xi(T^*)\) has the same leaves as _T_<sup>∗</sup>.

Let \(V(\xi(T^*))\) be the vertex set of \(\xi(T^*)\). Then, we claim that \(|V(\xi(T^*))|=O(\left\lceil\frac{n}{\alpha}\right\rceil)\) by count ing the number of nodes with different degrees in \(\xi(T^*)\). Clearly, we have \(\left|\{v\in V(\xi(T^*))\big|deg(v)>2\}\right|\le\left\lceil\frac{n}{\alpha}\right\rceil\). Since the tree \(\xi(T^*)\) contains no long chains, the parent (if exists) of every node with degree exactly 2 must have degree at least 3. Thus,

\(\left|\{v\in V(\xi(T^*))\big|deg(v)=2\}\right|\le\left|\{v\in V(\xi(T^*))\big|deg(v)>2\}\right|+1\le\left\lceil\frac{n}{\alpha}\right\rceil+1.\)

Hence we get \(|V(\xi(T^*))|\le 4\left\lceil\frac{n}{\alpha}\right\rceil\).

With Lemmas 6.2, 6.4 and Observation 6.3 we are now ready to obtain the efficient recursive decomposition of the problem:

**Lemma 6.5.** _If there is a O_(1)_-approximation algorithm running in n_<sup>_O_(log_n_)</sup> _time for any input tree, then one can obtain a_ \(O(\sqrt{logn})\)_-approximation algorithm with polynomial running time for any input tree._

_Proof._ Suppose Solve is a given constant-factor approximation algorithm running in time _n_<sup>_O_(log_n_)</sup> that, for any input tree _T_, outputs a search strategy for _T_. We then design a polynomial- time procedure Rec as shown in Algorithm 6.1, which outputs a search strategy R for an input tree _T_.

**Algorithm 6.1** \(O(\sqrt{logn})\)-approximation procedure Rec based on _n_<sup>_O_(log_n_)</sup>-time constant approximation algorithm Solve

procedure Rec(tree T=(V,E,w))<br>   \(n\leftarrow|V|\)<br>   if \(n\le 2^{\sqrt{logn}}\) then<br>
   return Solve(T)<br>
   else<br>
   \(\alpha\leftarrow n/2^{\sqrt{logn}}\)<br>
   \(T^*\leftarrow\) a minimal \(\alpha\)-separating tree of T with vertex set V<sup>∗</sup><br>
   \(\mathcal{A}^*\leftarrow\) Solve(\xi(T^*))<br>
   \(\mathcal{A}_{T^*}\leftarrow\) search strategy for T<sup>∗</sup> obtained from A<sup>∗</sup> as described in proof of Lemma 6.2<br>
   for each \(T'\) in C(T\\V<sup>∗</sup>) do<br>
   \(\mathcal{R}_{r(T^\prime)}\leftarrow\) Rec(\(T'\));<br>
   return \((\mathcal{A}_{T^*},\{\mathcal{R}_{r(T^\prime)}\big|T'\in\mathcal{C}(T\backslash V^*)\})\)-strategy for T

