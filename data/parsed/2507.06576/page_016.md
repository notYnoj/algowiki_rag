also closed under the 1-sum operation, Theorem 4 ensures that G is strongly _SDD_(2_w,p_)- acceptable. In Theorem 6, we show that if G is strongly _SDD_(2_w,p_)-acceptable, then \(w\cdot p\ge\frac{10}{9}\). This implies

\(w\cdot p=w\cdot\frac{\alpha}{2w}\ge\frac{10}{9},\)

and hence \(\alpha\ge\frac{20}{9}\).

**Theorem 6.** _Let_ G _be the family of cactus graphs. If_ G _is strongly SDD_(2_w,p)-acceptable, then_ \(w\cdot p\ge\frac{10}{9}\).

_Proof._ Let _H_ be a cycle of length 2_w_. Let _r_, _u_, \(r'\), and _v_ be four vertices of the cycle in anti-clockwise order, such that \(d(r,u)=d(u,r')=d(r',v)=d(v,r)=\frac{w}{2}\). We construct _G_ from _H_ by attaching paths \(u-u'\) and \(v-v'\) of length \(\frac{w}{2}\) from _u_ and _v_, respectively. We denote the path of length \(\frac{w}{2}\) from _r_ to _u_ by _P<sub>u</sub>_, from _u_ to \(r'\) by _P<sub>a</sub>_, from \(r'\) to _v_ by _P<sub>b</sub>_, and from _v_ to _r_ by _P<sub>v</sub>_. We denote the path from _u_ to \(u'\) by _P<sub>c</sub>_ and the path from _v_ to \(v'\) by _P<sub>d</sub>_. See the Figure 6 for an illustration. Note that \(G\in\mathcal{G}\).

For the sake of contradiction, assume that \(w\cdot p<\frac{10}{9}\) . Let \(k=\frac{w}{2}\) , \(\mathcal{F}=\mathcal{F}_{2w}^w(G,r)\) and \(A=\mathcal{F}_{2w}^k(G,r)\). Since \(K_2\in\mathcal{G}\) and G is closed under 1-sum, we can use Theorem 4 and Theorem 5 to conclude that there exists _SDD(G,_2_w,p,r_) \(y=\{y_F|F\in\mathcal{F}_{2w}^w(G,r)\}\) such that,

\(\sum_{F\in A}y_F=\sum_{F\in\mathcal{F}_{2w}^k(r)}y_F\ge 1-(w-k)\cdot p=1-\frac{w}{2}\cdot p=1-\frac{w\cdot p}{2}.\)

Suppose that \(F\in A\). Since \(d(u,r)=k=\frac{w}{2}\) and \(d(v,r)=k=\frac{w}{2}\) , we have that \(F\cap E(P_v)\neq\varnothing\) and \(F\cap E(P_u)\neq\varnothing\). The next claim shows that under the assumption that \(w\cdot p<\frac{10}{9}\) , there exists \(F\in A\) which does not pick any edges from _P<sub>a</sub>,P<sub>b</sub>,P<sub>c</sub>,P<sub>d</sub>_. This will lead to a contradiction, as \(u'\) and \(v'\) are 2_w_ distance apart, and since _F_ is a 2_w_-diameter decomposition, they should have been separated by _F_. This implies that \(w\cdot p\ge\frac{10}{9}\) and completes the proof of the theorem.

**Claim 3.** _There exists_ \(F\in A\) _such that_ \(F\cap E(P_a),F\cap E(P_b),F\cap E(P_c),F\cap E(P_d)=\varnothing\).

_Proof of Claim._ Let \(P'_a,P'_b\) be the two paths between \(r,r'\) containing _P<sub>a</sub>,P<sub>b</sub>_ respectively. Also, let \(P'_u,P'_v\) be the unique shortest paths starting at _r_ and ending at \(u',v'\), respectively. Let \(A_a=\{F\in A|F\cap E(P_a)\neq\varnothing\}\) and \(F\in A_a\). This implies that \(|F\cap E(P'_a)|\ge 2\). Since \(P'_a\) is a shortest path with length _w_ from _r_, using Lemma 3, we have,<tbc>

\(\sum_{F\in\mathcal{F},|F\cap E(P'_a)|\ge 2}y_F\le(w\cdot p)-1\Rightarrow\sum_{F\in A_a}y_F\le(w\cdot p)-1.\)

<tbc>Similarly, we define,<tbc>

\(A_b=\{F\in A|F\cap E(P_b)\neq\varnothing\},A_c=\{F\in A|F\cap E(P_c)\neq\varnothing\},A_d=\{F\in A|F\cap E(P_d)\neq\varnothing\},\)

r
Pu
Pv
u'
u
v
Pc
Pd
Pa
Pb
r'
G

