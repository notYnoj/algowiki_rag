_Proof._ As before, let \(\mathrm{deg}(P)=\mathrm{max}_{v\in P}\mathrm{deg}(v)\) be the maximum degree of any vertex in _P_ and \(\ell(P)=\mathrm{min}_{v\in P}\ell(v)\) the minimum level of any vertex in _P_. In the following, we will frequently use (some variant of) the following equality,

\(k-k_0=\left(\frac{3}{2}\beta+1\right)-(\beta-2)=\frac{\beta}{2}+3\) (1)

Let us begin by assuming _P_ has length exactly \(\beta+1\) so that we can label the vertices \(P=(u,u_2,\dots,u_{\beta/2+1},v_{\beta/2+1},\dots,v_2,v)\).

If \(P\subset E_{k_0+3}\), then \(L(P,k)\subset\{k_0+3,\dots,k-1\}\) is a set of size at most \(k-k_0-3=\frac{\beta}{2}\) , so we may apply Lemma A.3 and obtain a \(+\beta\)-approximation. Thus, in the following, assume _P_ has an edge in _E_<sub>_k_<sub>0</sub>+1</sub>\\_E_<sub>_k_<sub>0</sub>+3</sub>. In particular, there are at least two vertices \(x\in P\) with deg(_x)\>s_<sub>_k_<sub>0</sub>+2</sub>.

Suppose \(|L_B(P,k)|\le\frac{\beta}{2}\) . In the _k_-th iteration, as _D<sub>k</sub>=V_ , we have by A.2, \(\hat{\delta}_k(u,v)\le\delta(u,v)+\beta\). Thus, we can assume \(|L_B(P,k)|>\frac{\beta}{2}\) .

By assumption, the levels of vertices _u<sub>r<sub>i</sub></sub>,v<sub>r<sub>i</sub></sub>_ are restricted. Recall that \(r_i=\frac{\beta}{2}-(i-(k_0+1))\) so that,

\(r_{k_0+1}=\frac{\beta}{2}-((k_0+1)-(k_0+1))=\frac{\beta}{2}\)<br>
\(r_{k_0+\frac{\beta}{2}-1}=\frac{\beta}{2}-((k_0+\frac{\beta}{2}-1)-(k_0+1))=2\)

In particular, other than the two middle vertices, \(u_{\frac{\beta}{2}+1},v_{\frac{\beta}{2}+1}\), the remaining vertices have level at least \(i+2\ge k_0+3\), so that we can assume both central vertices have degree at least _s_<sub>_k_<sub>0</sub>+2</sub>. Furthermore, at most one of these vertices can be a blocking vertex. Suppose for contradiction that both are, so that one, for example \(u_{\frac{\beta}{2}+1}\), has level _k_<sub>0</sub>+1 and the other level _k_<sub>0</sub>+2. However, in this case \(P\subset E_{k_0+2}\) so that \(u_{\frac{\beta}{2}+1}\) cannot be a blocking vertex. In particular, if _L(P,k_) does not contain all levels {_k_<sub>0</sub>+3_,...,k_-1} then we can already obtain a \(\beta\) approximation by Lemma A.3.

Therefore, let _L<sub>B</sub>(P_) denote the blocking vertices of _P_. Since \(k_0+3\in L_B(P)\), we have either \(u_{\beta/2},v_{\beta/2}\in B(P)\). Without loss of generality, suppose \(u_{\beta/2}\in B(P)\).

In Line 209, since \(\mathrm{deg}(u_{\beta/2})<s_{k_0+2}\) and \(P\subset E_{k_0+1}\), we compute \(\hat{\delta}(u_{\beta/2},v_{\beta/2+1})=2\). Then, if \(u_{\beta/2}^*=r(u_{\beta/2},D_{k_0+3})\), in Line 215, we have \(\hat{\delta}(u_{\beta/2}^*,v_{\beta/2+1})\le 3\). We claim that,

\(\hat{\delta}_{k_0+3}(u_{\beta/2}^*,x)\le\delta(u_{\beta/2},x)+1\)

for all \(x\in P\). We have shown this already for \(x\in\{u_{\beta/2+1},v_{\beta/2+1}\}\). For \(x\in\{u,u_2,\dots,u_{\beta/2}\}\), this follows simply from the assumption that all these vertices have level at least _k_<sub>0</sub>+3 so that \(P_{w,x}\subset E_{k_0+3}\). For \(x\in\{v_{\beta/2},\dots,v_2,v\}\), when executing **Dijkstra** we take the edge \((u_{\beta/2}^*,v_{\beta/2+1})\) and the remaining edges of _P_ in _E_<sub>_k_<sub>0</sub>+3</sub>.

This allows us to make the following claim stronger than Lemma A.2. For any \(w,x\in P\) where \(\ell(w)\ge k_0+3\),

\(\hat{\delta}_{\ell(w)}(w^*,x)\le\delta(w,x)+2|L_B(P_{w,x})|-1\) (2)

where we have shown the base case for \(\ell(u_{\beta/2})=k_0+3\). The inductive step will follow similarly. Let \(j\ge k_0+3\) and \(\ell(w)=j\). Let _y=b(w,P<sub>w,x</sub>_) be the blocking vertex so that \(\ell(y)<\ell(w)\). Then,

\(\hat{\delta}_{\ell(w)}(w^*,x)\le\hat{\delta}_{\ell(y)}(w^*,y^*)+1+\delta(y,x)\)<br>
\(\le\delta(w,y)+2|L_B(P_{y,w})|+1+\delta(y,x)\)<br>
\(\le\delta(w,x)+2|L_B(P_{w,x})|-1\)

