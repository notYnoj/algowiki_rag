of this decomposition gives \(\widetilde{\mathsf{R}}(\mathsf{GT}_q(G))\le q^{|E(G)|}\). Taking base-two logarithms and combining with the lower bound proves the claimed equality. If _G_ has no edges, then GT_<sub>q</sub>(G_)=l_<sub>k</sub>_(1) for _k_=|_V(G_)|, so the same equality holds with all three quantities equal to zero.

A cut of _K<sub>n</sub>_ with _s_ vertices on one side has _s(n-s_) crossing edges. Since _s(n-s_)=_n_<sup>2</sup>/4-(_s-n/_2)<sup>2</sup>, its maximum over integers \(1\le s\le n-1\) is \(\lfloor n^2/4\rfloor\).

We next state the triangle version of the covering argument in \[CVZ19, Proposition 1.1.25\], allowing a graph to be covered with unequal multiplicities. A triangle cover may use the same triangle more than once. The symbolic bound in terms of \(\omega\) is the covering argument; the numerical value 3/4 per edge specifically uses \(\omega\le 9/4\) from OpenAI \[Ope26a\].

**Theorem A.5** (triangle-cover upper bound)**.** _Let G_=(_V,E_) _be a finite simple undirected graph with_ \(|V|\ge 3\) _and_ \(E\neq\varnothing\)_. Let M,r be positive integers, and let_ \(\Delta_1,\dots,\Delta_M\) _be triangles of G such that every edge of G belongs to at least r of them, counting repetitions. Then_<tbc>

\(log_2\widetilde{\mathsf{R}}(\mathsf{GT}_2(G))\le\frac{M\omega}{r}.\)

<tbc>_In particular, for every integer_ \(n\ge 3\),

\(log_2\widetilde{\mathsf{R}}(\mathsf{GT}_2(K_n))\le\frac{\omega}{3}\genfrac(){pt}{2}{n}{2}\le\frac{3}{4}\genfrac(){pt}{2}{n}{2},\tau(K_n)\le\frac{3}{4}.\)

_The last inequalities use OpenAI’s bound_ \(\omega\le 9/4\) _\[Ope26a\]._

_Proof._ Write _k_=|_V_| and label _V_ by {1_,...,k_}. For each \(1\le h\le M\), let _T<sub>h</sub>_ be the _k_-th order graph tensor supported on the three edges of \(\Delta_h\), with dimension 1 at every vertex outside that triangle. Appending legs of dimension 1 does not change rank: a decomposition extends by appending the scalar 1 on those legs, and conversely contracting those legs removes them from any decomposition. The same observation applies to every Kronecker power. Hence \(\widetilde{\mathsf{R}}(T_h)=\widetilde{\mathsf{R}}(\mathsf{GT}_2(K_3))=2^\omega\) for \(1\le h\le M\).

For every edge \(e\in E\), let \(r_e=|\{h|1\le h\le M,e\in E(\Delta_h)\}|\). Rearranging the edge factors in \(B=\otimes_{Kh=1}^MT_h\) gives _r<sub>e</sub>_ copies of the edge tensor on _e_. For each _e_, choose the same _r_ occurrences to retain at both endpoints. Project the coordinates in the other _r<sub>e</sub>-r_ occurrences onto the coordinate with label 0 at both endpoints. Each removed copy then contributes the scalar 1, and exactly _r_ copies remain on every edge. These projections act separately at each vertex and give \(\mathsf{GT}_2(G)^{\otimes_Kr}\unknown B\). Asymptotic rank is monotone under restriction and submultiplicative under Kronecker product. Both facts follow by taking ordinary rank inequalities for the _N_-th powers, then _N_-th roots and limits. Also, its definition gives \(\widetilde{\mathsf{R}}(T^{\otimes_Kr})=\widetilde{\mathsf{R}}(T)^r\), by taking the subsequence of powers divisible by _r_. Therefore

\(\widetilde{\mathsf{R}}(\mathsf{GT}_2(G))^r\le\widetilde{\mathsf{R}}(B)\le\prod_{h=1}^M\widetilde{\mathsf{R}}(T_h)=2^{M\omega}.\)

Taking base-2 logarithms and dividing by _r_ proves the general bound.

For _K<sub>n</sub>_, use every triangle once. There are \(M=\genfrac(){pt}{2}{n}{3}\) triangles, and an edge belongs to exactly _r=n_-2 of them, one for each choice of a third vertex. Thus \(M/r=\genfrac(){pt}{2}{n}{2}/3\). Substituting \(\omega\le 9/4\) and dividing by \(\genfrac(){pt}{2}{n}{2}\) gives the stated bounds.

