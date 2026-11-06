Since G is closed under the 1-sum operation and \(K_2\in\mathcal{G}\), we conclude that \(H\in\mathcal{G}\). By the assumption that G is strongly _SDD_(2_w,p_)-acceptable, there exists an _SDD(H,_2_w,p,r_) distribution<tbc>

\(x=\{x_{F^\prime}|F'\in\mathcal{F}_{2w}(H)\},\)

<tbc>with properties<tbc>

\(\sum_{F^\prime\in\mathcal{F}_{2w}^w(H,r)}x_{F^\prime}=1\text{and}\sum_{F^\prime\in\mathcal{F}_{2w}(H)e\in F^\prime} x_{F^\prime}\le p\text{for all}e\in E(H).\)

<tbc>Let \(A=\{F'\in\mathcal{F}_{2w}^w(H,v)|F'\cap E(P)\neq\emptyset\}\) and \(B=\{F'\in\mathcal{F}_{2w}^w(H,v)|F'\cap E(P)=\emptyset\}\). Let \(A_i=\{F'\in A|e_i\in F'\}\) for _i_=1_,...,w-k_. Note that \(\sum_{F^\prime\in A}x_{F^\prime}+\sum_{F^\prime\in B}x_{F^\prime}=1\). Since \(\sum_{F^\prime\in A_i}x_{F^\prime}\le p\), and \(A=\cup_{i=1}^{w-k}A_i\), it follows that:

\(\sum_{F^\prime\in A}x_{F^\prime}\le(w-k)p\Rightarrow\sum_{F^\prime\in B}x_{F^\prime}\ge 1-(w-k)p.\)

Let _G<sub>i</sub>_=(_V<sub>i</sub>,E<sub>i</sub>_) and F<sub>2_w_</sub>(_G<sub>i</sub>_) be the set of all 2_w_-diameter decompositions of _G<sub>i</sub>_ for _i_=1,2_,...,m_. Recall that \(\mathcal{F}_{2w}^w(G_i,r),\mathcal{F}_{2w}^k(G_i,r)\) is the set of 2_w_-diameter decompositions of _G<sub>i</sub>_ in which the distance of every vertex in the connected component containing _r_ is at most _w_-1 and _k_-1 from it, respectively. The next claim shows that the projection of the distribution _x_ onto _G<sub>i</sub>_, denoted _y<sup>i</sup>=x(G<sub>i</sub>_), yields a feasible solution to the LP (7).

**Claim 2.** _The distribution y<sup>i</sup> is a feasible solution to the LP_ (7).

_Proof of Claim._ Lemma 2 implies _y<sup>i</sup>_ is a _SDD(G<sub>i</sub>,_2_w,p_) for _G<sub>i</sub>_. Let \(B_i=\{F'\cap E_i|F'\in B\}\). Observe that \(B_i\in\mathcal{F}_{2w}(G_i)\). Let \(F\in B_i\). Then there exists \(F'\in B\) such that \(F=F'\cap E_i\). Furthermore, for any \(F'\in B\), we have \(F'\in\mathcal{F}_{2w}^w(H,v)\) and \(F'\cap E(P)=\emptyset\). Hence we can conclude that \(F\in\mathcal{F}_{2w}^k(G_i,r)\). Thus,<tbc>

\(\sum_{F\in\mathcal{F}_{2w}^k(G_i,r)}y_F^i\ge\sum_{F\in B_i}y_F^i=\sum_{F\in B_i}\sum_{F^\prime\in BF^\prime\cap E_i=F}x_{F^\prime}=\sum_{F^\prime\in B}x_{F^\prime}\ge 1-(w-k)\cdot p.\)

<tbc>Since _G<sub>i</sub>_ is an identical copy of _G_ and F<sub>2_w_</sub>(_G<sub>i</sub>_) is also an identical copy of F<sub>2_w_</sub>=F<sub>2_w_</sub>(_G_), Claim 2 shows that _y<sup>i</sup>_ is a feasible solutions for LP (7) for _G<sub>i</sub>_, it follows that LP (7) is feasible. Since _z_ is the optimal solution of LP (7), for each _y<sup>i</sup>_, we have:<tbc>

\(\sum_{F\in\mathcal{F}_{2w}(G_i)\backslash\mathcal{F}_{2w}^w(G_i,r)}y_F^i\ge z.\)

V
r = r1 = r2 = = rm
G1
Gm
G2
H

Figure 3: Illustration of the construction of _H_

