(1) For each assignment \(A=((p_1,q_1),\dots,(p_\ell,q_\ell))\in\mathcal{A}\), we do:<tbc>

(1a) Partition _V_ into 6 sets. Namely, for each \((r,s)\in\{1,2,3\}\times\{1,2\}\), we denote:<tbc>

<tbc>\(V_{r,s}:=\{v\in V|\phi(v)\in I_j\wedge(r,s)=(p_j,q_j)\}.\)<tbc>

<tbc>In words, for each \(v\in V\) , we first identify the block _I<sub>j</sub>_ that contains \(\phi(v)\). Then we look up the _j<sup>th</sup>_ pair of the assignment, namely (_p<sub>j</sub>,q<sub>j</sub>_), and that becomes the index of the partition which _v_ belongs to.<tbc>

(1b) Make three find-edge queries: FindEdge(_V_<sub>1,1</sub>_,V_<sub>1,2</sub>),FindEdge(_V_<sub>2,1</sub>_,V_<sub>2,2</sub>), and FindEdge(_V_<sub>3,1</sub>_,V_<sub>3,2</sub>).<tbc>

(1c) If any of the three find-edge queries ever return an edge (_u,v_), output it and terminate immediately. Otherwise, proceed to the next assignment.<tbc>

(2) If all find-edge queries never return an edge, output "FAIL".

We now justify the correctness of our algorithm, which follows from these two miniclaims.

1. If \(\delta\le\delta_\mathrm{max}\), then the algorithm never outputs "FAIL", i.e. it must output some edge (_u,v_).<tbc>

<tbc>Let \((u^*,v^*)\in E\) be such that \(|\phi(u^*)-\phi(v^*)|=\delta_\mathrm{max}\). Let \(\phi(u^*)\in I_a\) and \(\phi(v^*)\in I_b\) for some \(a,b\in[\ell]\). WLOG, assume that \(\phi(u^*)\ge\phi(v^*)\) so that \(\phi(u^*)-\phi(v^*)=\delta_\mathrm{max}\). Then, we have<tbc>

<tbc>\(\delta\le\delta_\mathrm{max}=\phi(u^*)-\phi(v^*)<\frac{\delta}{2}\cdot(a+1)-\frac{\delta}{2}\cdot b.\)<tbc>

<tbc>This then implies that \(a-b\ge 2\). By the construction of our assignments as guaranteed by Claim 5.7, (_a,b_) must be matched by some assignment \(((p_1,q_1),\dots,(p_\ell,q_\ell))\in\mathcal{A}\). Within this assignment, we must have _p<sub>a</sub>=p<sub>b</sub>_:=_p_ and \(q_a\neq q_b\). When we make the query FindEdge(_V_<sub>_p,_1</sub>_,V_<sub>_p,_2</sub>) in (1b), the vertices _u_<sup>∗</sup> and _v_<sup>∗</sup> belong to the different side of the query. As a result, the find-edge query must return some edge \((u,v)\in V_{p,1}\times V_{p,2}\) which may or may not be the same edges as (_u_<sup>∗</sup>_,v_<sup>∗</sup>). Thus, the algorithm never outputs "FAIL".<tbc>

2. If the algorithm outputs some edge (_u,v_), then we have \(|\phi(u)-\phi(v)|\ge\frac{\delta}{2}\) .<tbc>

<tbc>To see this, assume that (_u,v_) is found upon a find-edge query FindEdge(_V_<sub>_i,_1</sub>_,V_<sub>_i,_2</sub>) of an assignment \(A\in\mathcal{A}\). This implies \(u\in V_{i,1}\) and \(v\in V_{i,2}\). Let \(a,b\in[\ell]\) such that \(\phi(u)\in I_a\) and \(\phi(v)\in I_b\). By definition, we have (_p<sub>a</sub>,q<sub>a</sub>_)=(_i,_1) and (_p<sub>b</sub>,q<sub>b</sub>_)=(_i,_2) which implies \(a\neq b\). Moreover, since adjacent interval cannot have the same _p_ values, we must have \(|a-b|\ge 2\). WLOG we assume that \(a-b\ge 2\). As a result we have<tbc>

<tbc>\(\phi(u)-\phi(v)\ge\frac{\delta}{2}\cdot(a-1)-\frac{\delta}{2}\cdot b\ge\frac{\delta}{2}\)<tbc>

<tbc>as wished.

Finally, we analyze the query complexity of our algorithm. We make up to \(O(\mathrm{log}\ell)=O(\mathrm{log}(1/\delta))\) find-edge queries, out of which up to one query outputs an edge. Since all find-edge queries that answer "NONE" spends _O_(1) cut queries, and the one that actually outputs an edge spends _O_(log_n_) cut queries, in total our algorithm only makes \(O(\mathrm{log}\left(n/\delta\right))\) cut queries to _G_.

