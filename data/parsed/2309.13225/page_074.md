good additive approximation from Lemma A.2 as there are at most 2 blocking levels. On the other hand, suppose \(\{5,6\}\subset L_B(P)\). Note \(\ell(u_3),\ell(v_3)<5\), otherwise we obtain a +4 approximation as _L<sub>B</sub>(P_)={5,6}. Assume without loss of generality that \(\ell(v)\le\ell(u)\) as in Definition 3.4. If \(\ell(v)=5\), then since \(P\subset E_{\ell(u_3)}\), \(\hat{\delta}(u_3^*,v)\le\delta(u_3,v)\). Since the remaining edges are in _E_<sub>5</sub>, _G_<sub>5_,v_<sup>∗</sup></sub>

Otherwise, \(\ell(v)\ge 6\). If \(\ell(v)=7\), then \(\ell(u)=\ell(v)=7\) and we obtain a +4 approximation following the same argument as Theorem 3.3. Therefore, assume \(\ell(v)=6\). If \(\ell(u_2)\ge 6\), then the blocking vertex _b(v,P_)=_u_<sub>3</sub> and we obtain a +4 approximation as _B(P_)={_u,v,u_<sub>3</sub>}.

We can therefore assume \(\ell(u_2)=5\). However, since this vertex has degree at most _s_<sub>4</sub>, we use a depth 2 **BFS** in Line 209 to bypass the middle edge entirely, therefore obtaining a +4 approximation, as illustrated in Figure 9. The depth 2 **BFS** requires time \(s_2s_4=\tilde{O}(n^{8/7})\).

**Algorithm** In Phase 0, we initialize the distance estimates to the adjacency matrix, set parameters _k,k_<sub>0</sub> and decompose the graph _G_ into _k_ degree thresholds. To compute the dominating sets, we use<tbc>

\(\includegraphics{}\text{Figure 8: Imposing the degree restriction}\ell(v_2)\ge 5\includegraphics{}\text{Figure 9: Using depth 2 \textbf{BFS} to bypass the central edge.}\ell(v_2)\ge 5\)

