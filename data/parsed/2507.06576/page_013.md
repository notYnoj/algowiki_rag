3. the distance of _u_ and _v_ from _r_ is at least _w_.

But then, the diameter of \(F'\) is at least 2_w_, which contradicts the fact that \(F'\in\mathcal{F}'_{2w}\). This implies that _z_=0, and completes the proof of the theorem.

We say that a graph _G_ together with a vertex \(r\in V(G)\) has an _SDD(G,_2_w,p,r_) if there exists an _SDD(G,_2_w,p_) distribution \(y=\{y_F\}_{F\in\mathcal{F}_{2w}(G)}\) such that

\(\sum_{F\in\mathcal{F}_{2w}^w(G,r)}y_F=1.\)

In this case, every sampled 2_w_-diameter decomposition _F_ from _y_ satisfies \(\mathrm{rad}_F(r)\le w-1\). We say that a graph class G is strongly _SDD_(2_w,p_)-acceptable if for every \(G\in\mathcal{G}\) and every \(r\in V(G)\), there exists an _SDD(G,_2_w,p,r_).

In Theorem 4, we proved that if a graph class G, closed under the 1-sum operation, is _SDD_(2_w,p_)-acceptable, then it is also strongly _SDD(w,p_)-acceptable. In Theorem 5, we extend this result to arbitrary radii. For the proof, we additionally assume that G contains _K_<sub>2</sub>, the complete graph on two vertices (i.e., a single edge).

**Theorem 5.** _Suppose that_ G _is closed under the_ 1_-sum operation, contains K_<sub>2</sub>_, and is strongly SDD_(2_w,p)-acceptable. Let_ \(G\in\mathcal{G}\), \(r\in V(G)\)_, and_ \(k\in\{1,\dots,w\}\)_. Then there exists an SDD(G,_2_w,p,r_) _distribution_ \(y=\{y_F|F\in\mathcal{F}_{2w}(G)\}\) _such that_

\(\sum_{F\in\mathcal{F}_{2w}^k(G,r)}y_F\ge 1-p(w-k).\)

_Proof._ Let \(\mathcal{F}_{2w}=\mathcal{F}_{2w}(G),\mathcal{F}_{2w}^w(r)=\mathcal{F}_{2w}^w(G,r)\) and \(\mathcal{F}_{2w}^k(r)=\mathcal{F}_{2w}^k(G,r)\) for simplicity. It is sufficient to show that the following LP (7) is feasible and has optimal value 0.

\(\mathrm{min}\sum_{F\in\mathcal{F}_{2w}\backslash\mathcal{F}_{2w}^w(r)}y_F\)<br>
\(\sum_{F\in\mathcal{F}_{2w}^k(r)}y_F\ge 1-p(w-k)\)<br>
\(\sum_{F\in\mathcal{F}_{2w}^{e\in F}}y_F\le p\forall e\in E(G)\) (7)

\(\sum_{F\in\mathcal{F}_{2w}}y_F=1\)<br>
\(y_F\ge 0\forall F\in\mathcal{F}_{2w}\)

For now, assume that the LP (7) is feasible and its optimal value is _z\>_0. The proof that LP (7) is feasible will also follow from the discussion below. Let \(m>\frac{1}{z}\) and _G_<sub>1</sub>_,...,G<sub>m</sub>_ be _m_ disjoint copies of _G_. Let _r<sub>i</sub>_ be the vertex of _G<sub>i</sub>_ which corresponds to _r_ and \(G'\) be formed by taking 1-sum of _G_<sub>1</sub>_,...,G<sub>m</sub>_ at _r_<sub>1</sub>_,...,r<sub>m</sub>_. We construct _H_ by adding a path of length _w-k_ to \(G'\) at _r_. Let _P_={_e_<sub>1</sub>_,e_<sub>2</sub>_,...,e_<sub>_w-k_</sub>} be the set of edges on this path, where _e_<sub>1</sub>=(_r,v_<sub>1</sub>)_,e_<sub>2</sub>=(_v_<sub>1</sub>_,v_<sub>2</sub>)_,...,e_<sub>_w-k_</sub>=(_v_<sub>_w-k_-1</sub>_,v_). See the following Figure 3 for an illustration:

