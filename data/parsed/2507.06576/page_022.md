Recall that \(k=\frac{w}{2}\) . By Theorem 7, there exists an _SDD(G,_2_w,p,r_) distribution \(y=\{y_F|F\in\mathcal{F}_{2w}^w(G,r)\}\) such that

\(\sum_{F\in\mathcal{F}_{2w}^k(G,r)}y_F\ge R_{(\mathcal{G},2w,p)}^k\ge 1-(w-k)p=1-\frac{w\cdot p}{2},\) (16)

and moreover, for each _i_=1,2, the projection \(y(H'_i)\) is an \(SDD(H'_i,2w,p,r'_i)\).<br>
For the sake of contradiction, assume that \(w\cdot p<\frac{8}{7}-\frac{4\epsilon}{7}\) . Let \(\mathcal{F}=\mathcal{F}_{2w}^w(G,r)\) and \(A=\mathcal{F}_{2w}^k(G,r)\). For _i_=1,2, let \(\mathcal{F}_i=\mathcal{F}_{2w}^w(H'_i,r'_i)\) and \(\mathcal{F}_i^k=\mathcal{F}_{2w}^k(H'_i,r'_i)\). From (16) we have

\(\sum_{F\in A}y_F\ge R_{(\mathcal{G},2w,p)}^k.\) (17)

In the following we are going to show that under the assumption \(w\cdot p<\frac{8}{7}-\frac{4\epsilon}{7}\) there exists \(F\in A\) with _y<sub>F</sub>\>_0 which (i) does not pick any edges from _P<sub>a</sub>_ or _P<sub>b</sub>_, and (ii) fails the radius-_k_ condition inside both attachments: \(F\cap E(H'_i)\notin\mathcal{F}_i^k\) for _i_=1,2. This leads to a contradiction, since _d(u_<sub>1</sub>_,u_<sub>2</sub>)=_w_ and for each _i_ there exists \(v_i\in V(H'_i)\) with \(d(u_i,v_i)\ge k=\frac{w}{2}\) . Thus \(d(v_1,v_2)\ge 2w\), and all _v_<sub>1</sub>_,v_<sub>2</sub>_,u_<sub>1</sub>_,u_<sub>2</sub> lie in the same connected component of _G_\\_F_, contradicting that _F_ is a 2_w_-diameter decomposition. Hence \(w\cdot p\ge\frac{8}{7}-\frac{4\epsilon}{7}\) .

Suppose \(F\in A\). Since _d(r,u_<sub>1</sub>)=_d(r,u_<sub>2</sub>)=\(k=\frac{w}{2}\) , we must have \(F\cap E(P_{u_1})\neq\varnothing\) and \(F\cap E(P_{u_2})\neq\varnothing\). Let \(P'_a,P'_b\) be the two _r_-\(\tilde{r}\) paths on the cycle containing _P<sub>a</sub>,P<sub>b</sub>_, respectively. Define \(A_a=\{F\in A|F\cap E(P_a)\neq\varnothing\}\). If \(F\in A_a\), then \(|F\cap E(P'_a)|\ge 2\). Since \(P'_a\) is a shortest path of length _w_ from _r_, by Lemma 3,

\(\sum_{F\in\mathcal{F}|F\cap E(P'_a)|\ge 2}y_F\le(w\cdot p)-1\Longrightarrow\sum_{F\in A_a}y_F\le(w\cdot p)-1.\) (18)

Similarly, with \(A_b=\{F\in A|F\cap E(P_b)\neq\varnothing\}\) and the path \(P'_b\),

\(\sum_{F\in A_b}y_F\le(w\cdot p)-1.\) (19)

Next, set

\(A_c=\{F\in A|F\cap E(H'_1)\in\mathcal{F}_1^k\},A_d=\{F\in A|F\cap E(H'_2)\in\mathcal{F}_2^k\}.\)

**Claim 5.**

\(\sum_{F\in A_c}y_F<R_{(\mathcal{G},2w,p)}^k+\epsilon-\left(1-\frac{w\cdot p}{2}\right),\sum_{F\in A_d}y_F<R_{(\mathcal{G},2w,p)}^k+\epsilon-\left(1-\frac{w\cdot p}{2}\right).\) (20)

_Proof of Claim._ We prove the inequality for _A<sub>c</sub>_; the case of _A<sub>d</sub>_ follows by the same reasoning. Since \(y(H'_1)\) is an \(SDD(H'_1,2w,p,r'_1)\) and \(H'_1\) is a copy of \(H'\), the choice of \((H',r')\) in (15) implies

\(\sum_{F^\prime\in\mathcal{F}_1^k}y(H'_1)_{F^\prime}<R_{(\mathcal{G},2w,p)}^k+\epsilon.\)

