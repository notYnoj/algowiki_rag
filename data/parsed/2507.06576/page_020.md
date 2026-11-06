To see why (11) holds, suppose not. Then there exists \(F''\in\mathcal{F}_{2w}(H_j)\backslash\mathcal{F}_{2w}^w(H_j,r)\) with \(x(H_j)_{F^{\prime\prime}}>0\). By definition of projection, this implies that there exists \(F'\in\mathcal{F}_{2w}(G^{S(L^\prime)})\) with \(x_{F^\prime}>0\) and \(F'\cap E(H_j)=F''\). Now, \(F''\notin\mathcal{F}_{2w}^w(H_j,r)\) means that in \(H_j\backslash F''\) there exists some vertex \(v\in V(H_j)\) with \(d_{H_j}(r,v)\ge w\). As mentioned earlier<tbc>

\(d_{G^{S(L^\prime)}}(r,v)=d_{H_j}(r,v)\ge w.\)

<tbc>Thus, _r_ and _v_ lie in the same connected component of \(G^{S(L^\prime)}\backslash F'\), and so \(F'\notin\mathcal{F}_{2w}^w(G^{S(L^\prime)},r)\). This contradicts (10), since \(x_{F^\prime}>0\). Hence, (11) must hold, and therefore _x(H<sub>j</sub>_) is an _SDD(H<sub>j</sub>,_2_w,p,r_). It remains to show that<tbc>

\(\sum_{F^{\prime\prime}\in\mathcal{F}_{2w}^k(H_j,r)}x(H_j)_{F^{\prime\prime}}\ge R_{(\mathcal{G},2w,p)}^k.\)

<tbc>Indeed, for any \(F'\in\mathcal{F}_{2w}^w(G^{S(L^\prime)},r)\) we have \(F''=F'\cap E(H_j)\in\mathcal{F}_{2w}^k(H_j,r)\) whenever \(F'\in\mathcal{F}_{2w}^k(G^{S(L^\prime)},r)\). Therefore,

\(\sum_{F^{\prime\prime}\in\mathcal{F}_{2w}^k(H_j,r)}x(H_j)_{F^{\prime\prime}}=\sum_{F^{\prime\prime}\in\mathcal{F}_{2w}^k(H_j,r)}\sum_{F^\prime\in\mathcal{F}_{2w}(G^{S(L^\prime)})F^{\prime\prime}=F^\prime\cap E(H_j)}x_{F^\prime}\)<br>
\(\ge\sum_{F^\prime\in\mathcal{F}_{2w}^k(G^{S(L^\prime)},r)}x_{F^\prime}\)<br>
\(\ge R_{(\mathcal{G},2w,p)}^k,\)

where the last inequality follows from the defining property of _x_. \(\blacktriangle\)

For each \(j\in\{1,\dots,m\}\) and \(i\in\{1,\dots,l\}\), let \(\mathcal{F}_i^j\) denote the copy of F_<sub>i</sub>_ inside _H<sub>j</sub>_. Also, let \(\mathcal{F}^j=\cap_{i=1}^l\mathcal{F}_i^j\) be the copy of F in _H<sub>j</sub>_. Since _x(H<sub>j</sub>_) is a feasible solution to LP (9), we obtain<tbc>

\(\sum_{F_j\in\mathcal{F}_{2w}^w(H_j)\backslash\mathcal{F}^j}x(H_j)_{F_j}\ge z.\)

<tbc>Hence, for each \(j\in\{1,\dots,m\}\) there exists an index \(i_j\in\{1,\dots,l\}\) such that

\(\sum_{F_j\in\mathcal{F}_{2w}^w(H_j)\backslash\mathcal{F}_{i_j}^j}x(H_j)_{F_j}\ge\frac{z}{l}.\) (12)

The indices _i<sub>j</sub>_ play a crucial role. By the Pigeonhole Principle, for at least<tbc>

\(t=\left\lceil\frac{m}{l}\right\rceil\)

<tbc>values of _j_, the same index _i<sub>j</sub>_ is chosen. Without loss of generality, assume \(i_1=\cdots=i_t=1\). Summing (12) over _j_=1_,...,t_ gives<tbc>

\(\sum_{j=1}^t\sum_{F_j\in\mathcal{F}_{2w}^w(H_j)\backslash\mathcal{F}_1^j}x(H_j)_{F_j}\ge\sum_{j=1}^t\frac{z}{l}=\frac{tz}{l}\ge\frac{m}{l}\cdot\frac{z}{l}>1.\) (13)

<tbc>The left-hand side of (13) can be rewritten as<tbc>

\(\sum_{j=1}^t\sum_{F_j\in\mathcal{F}_{2w}^w(H_j)\backslash\mathcal{F}_1^j}\sum_{F^\prime\in\mathcal{F}_{2w}(G^{S(L^\prime)})F_j=F^\prime\cap E(H_j)}x_{F^\prime}.\) (14)

