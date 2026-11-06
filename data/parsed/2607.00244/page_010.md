triangles. Therefore, at most \(\lceil log(3n)\rceil\) of these vertices can be part of the same independent set. Similarly to the mere subdivision, there is a largest independent set of _G_ that for every \(uv\in E(J)\) contains at most one original vertex among _u,v_. Indeed, if both \(u,v\in V(G)\) are in an independent set _I_ of _G_, only \(\lceil log(3n)\rceil-1\) vertices of _T<sub>uv</sub>_ can be part of _I_. This is because _T<sub>uv</sub>_\\_N<sub>G</sub>_({_u,v_}) can be vertex-partitioned into \(\lceil log(3n)\rceil-1\) triangles. One can thus remove, say, _v_ from _I_, and have \(\lceil log(3n)\rceil\) vertices of _T<sub>uv</sub>_ in _I_. We conclude that

\(\alpha(G)\le\alpha(J)+|E(J)|\lceil log(3n)\rceil=\alpha(J)+(3n+3m)\lceil log(3n)\rceil.\)

Actually the equality holds.

We then claim that \(\alpha(J)\le max\{|X|:X\subseteq V(H),H[X]\text{is}3\text{-colorable}\}\) (again, the equality holds). Let _I_ be an independent set of _J_. Because of the triangles (_u,_1)(_u,_2)(_u,_3), _I_ contains at most one vertex of the form (_u,i_) for every \(u\in V(H)\). Furthermore, for every edge \(uv\in E(H)\), it cannot be that both (_u,i_) and (_v,i_) are in _I_ for some \(i\in[3]\). Thus, the partial 3-coloring obtained by giving color _i_ to vertex _u_ for every \((u,i)\in I\) is well-defined, proper, and colors |_I_| vertices of _H_. Therefore if no induced subgraph of _H_ on at least _p_ vertices is 3-colorable, then

\(\alpha(G)\le p+(3n+3m)\cdot\lceil log(3n)\rceil.\blacktriangleleft\)

Using these ingredients, we can now prove the main result of this section. The omitted proof is similar to the one of Theorem 1.

\(\blacktriangleright\) **Theorem 2.** _Unless the ETH fails, there is a constant_ \(\gamma>0\) _such that Min Coloring does not admit a polynomial-time_ \(n^{\gamma/(loglogn)^2}\)_-approximation algorithm on n-vertex graphs of twin-width at most 4, even when a 4-sequence is given as part of the input._

**Proof.** Fix the constants \(\beta<1,\Delta,c\) satisfying Theorem 12. Every promised _N_-vertex instance _H_ of Theorem 12 is mapped to the graph _G_<sup>[_k_]</sup> with _G_:=_G<sub>H</sub>_, as defined in Theorem 13, and \(k:=\lceil N/log^{c+2}N\rceil\). We assume, without loss of generality, that \(N\ge 2\) is large enough. In particular, the following inequalities hold:

