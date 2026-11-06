_Proof._ Recall that, by definition, an edge (_u,v_) _kills_ a witness (_S,T,Y_) if \(z_u\neq z_v\)--i.e., _u_ and _v_ lie on opposite sides of the cut--and \((u,v)\notin Y\) . Under this characterization, the LHS quantity becomes:<tbc>

\(Pr_{Z\sim\mathcal{Z}}(z_u\neq z_v)\cdot Pr_{(Z,Y)\sim(\mathcal{Z},\mathcal{Y}|z_u\neq z_v)}\left[(u,v)\text{kills}(Z,Y)|z_u\neq z_v\right].\)

<tbc>By Claim 5.3, we have \(Pr_{Z\sim\mathcal{Z}}(z_u\neq z_v)\ge|\hat{z}_u-\hat{z}_v|\). Moreover, we can bound the second term by:

\(Pr_{(Z,Y)\sim(\mathcal{Z},\mathcal{Y}|z_u\neq z_v)}\left[(u,v)\text{kills}(Z,Y)|z_u\neq z_v\right]\)<br>
\(=\sum_{Z\in supp(\mathcal{Z}|z_u\neq z_v)}Pr\left(\mathcal{Z}=Z|z_u\neq z_v\right)\cdot Pr_{Y\sim\mathcal{Y}|Z}\left[(u,v)\notin Y\backslash E_H(S,T)|Z\right])\)<br>
\(\ge\sum_{Z\in supp(\mathcal{Z}|z_u\neq z_v)}Pr\left(\mathcal{Z}=Z|z_u\neq z_v\right)\cdot\frac{k'+1}{k}\) (Claim 5.4)

\(=\frac{k'+1}{k}\cdot\sum_{Z\in supp(\mathcal{Z}|z_u\neq z_v)}Pr\left(\mathcal{Z}=Z|z_u\neq z_v\right)\)<br>
\(=\frac{k'+1}{k}.\)

Multiplying the two bounds completes the proof.

We emphasize that Claim 5.5 is vastly useful in our analysis, as it applies to every edge \((u,v)\in G\backslash H\). Recall that the distribution (Z,Y) is a uniform among all remaining witnesses. Hence, the claim then implies that any edge \((u,v)\in G\backslash H\) kills an \(\Omega\left(|\hat{z}_u-\hat{z}_v|\right)\) fraction of the current witnesses. Furthermore, given the current subgraph _H_, the values \(\hat{z}_v\) for all \(v\in V\) can be computed locally with no extra costs. As a result, our task is significantly simplified: it suffices to identify an edge \((u,v)\in G\backslash H\) such that \(|\hat{z}_u-\hat{z}_v|\ge\gamma\) for some suitable threshold \(\gamma>0\). The following claim ensures the existence of such an edge, with \(\gamma=\Omega\left(\frac{\sqrt{k}}{n}\right)\).

**Claim 5.6.** _There exists an edge_ \((u,v)\in G\backslash H\) _such that_ \(|\hat{z}_u-\hat{z}_v|\ge\alpha\cdot\frac{k'}{n\sqrt{k}}\)_, for some universal constant_ \(\alpha>0\).

_Proof._ For any support \(Z\in supp(\mathcal{Z})\) (meaning that _Z_=(_S,T_) appears in some witness), we have \(\sum_{(u,v)\in H}|z_u-z_v|\le f-k'-1\) following the equivalent definition of witness in (3). Taking expectation over _Z_∼Z, we have:

\(f-k'-1\ge\mathbb{E}_{Z\sim\mathcal{Z}}\sum_{(u,v)\in H}|z_u-z_v|\)<br>
\(=\sum_{(u,v)\in H}\mathbb{E}_{Z\sim\mathcal{Z}}|z_u-z_v|\) (linearity of expectation)<br>
\(\ge\sum_{(u,v)\in H}\left|\mathbb{E}_{Z\sim\mathcal{Z}}z_u-\mathbb{E}_{Z\sim\mathcal{Z}}z_v\right|\) (triangle inequality)<br>
\(=\sum_{(u,v)\in H}|\hat{z}_u-\hat{z}_v|.\)

On the other hand, let \(Q\subseteq G\backslash H\) be such that \(|Q|=O(n\sqrt{k})\) and \(\nu(H\cup Q)=f\). The existence of _Q_ is guaranteed via construction. Let \(F\unknown H\) be a flow subgraph of _H_ with \(\nu(F)=\nu(H)\ge f-k\).

