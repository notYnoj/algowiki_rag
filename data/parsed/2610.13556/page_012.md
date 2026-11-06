<tbc>_for every_ \(f\in\mathcal{R}_k(G,\unknown)\) _and_ \(g\in\mathcal{R}_k(H,\unknown)\) _whose summed source profile belongs to_ M_<sub>k</sub>(G_)+M_<sub>k</sub>(H). In particular, for L=B(G_)+_B(H), equality_ \(B(G\sqcup H)=B(G)+B(H)\) _holds if and only if this condition holds for every such pair at budget L, and fails for at least one such pair at budget L_-1.

_Proof._ For a fixed pair of responses, \((f\star g)(\mathbf{m})\le L\) means that **m**=**p**+**q** for profiles satisfying \(f(\mathbf{p})+g(\mathbf{q})\le L\). Since costs are integers, this is equivalent to \(\mathbf{m}\in\mathcal{K}_L(f,g)\). Theorem 4.9 and (4.13) now give the asserted upper-bound criterion. Failure at _L_-1, together with the bound at _L_, is equivalent to equality. The argument does not require equal chromatic numbers for the summands. □

This is an exact compositional criterion in local profile data, rather than an elementary structural classification of the graph pairs. It distinguishes two effects: target multiplicities may transfer between summands during repair, and a globally feasible disturbance may have locally infeasible profiles.

## 4.4. The growth of ordinary villainy under repetition.

The response composition law also determines the asymptotic behavior of ordinary villainy. Fix a graph _G_ with \(\chi(G)=k\), and let W and P be, respectively, all words and all proper colorings of _G_ on \[_k_\]. Both sets are finite. A vector \(\mathbf{x}=(x_w)_{w\in\mathcal{W}}\) describes proportions of source words on many copies of _G_. Its average profile must belong to the convex hull of the proper profiles. Accordingly, put<tbc>

\(\mathcal{X}_G=\left\{\mathbf{x}\ge\mathbf{0}:\sum_wx_w=1,\sum_wx_w\mathbf{m}(w)\in conv\mathcal{M}_k(G)\right\}.\)

<tbc>For \(\mathbf{x}\in\mathcal{X}_G\), define the fractional repair cost

\(\Phi_G(\mathbf{x})=min_{\mathbf{z}\ge\mathbf{0}}\sum_{w\in\mathcal{W},y\in\mathcal{P}}d_\mathrm{H}(w,y)z_{wy},\text{subject to}\sum_yz_{wy}=x_w(w\in\mathcal{W}),\sum_{w,y}z_{wy}(\mathbf{m}(y)-\mathbf{m}(w))=\mathbf{0}.\text{(4.15)}\)

The variable _z<sub>wy</sub>_ assigns a proportion of copies with source _w_ to the proper target _y_. Thus the second constraint preserves the total color counts. The program is feasible precisely for \(\mathbf{x}\in\mathcal{X}_G\). Set<tbc>

\(\Lambda(G)=max_{\mathbf{x}\in\mathcal{X}_G}\Phi_G(\mathbf{x}).\) (4.16)

<tbc>**Theorem 4.11** (Ordinary repetition)**.** _For every fixed graph G with_ \(k=\chi(G)\)_, the number_ \(\Lambda(G)\) _is rational and effectively computable. The maximum in_ (4.16) _is attained by a distribution supported on at most k source words, meaning that at most k coordinates x<sub>w</sub> are positive. Moreover,_

\(B(mG)=m\Lambda(G)+O_G(1),\Lambda(G)\ge F_k(G).\) (4.17)

_The error term is bounded by a constant depending only on G. There are effectively computable integers_ \(h\ge 1\), \(a\ge 0\)_, and_ \(M\ge 1\) _such that_ \(a=h\Lambda(G)\) _and_

\(B((m+h)G)=B(mG)+a(m\ge M).\) (4.18)

_Proof._ Write the constraints in (4.15) as _A_**z**=(**x**,**0**), where _A_ is a fixed integer matrix, and write **c** for the nonnegative integer cost vector. When \(\mathbf{x}\in\mathbb{Z}_{\ge 0}^\mathcal{W}\) counts actual source copies, its sum is their number. The source is feasible if and only if the same system has a nonnegative integer solution. In that case the minimum over integer solutions, denoted _C<sub>G</sub>_(**x**), is its ordinary repair cost. This is the repeated form of Theorem 4.9. For unnormalized vectors, we define \(\Phi_G\) by the same program; scaling all source proportions by a nonnegative factor scales its optimum by that factor.

