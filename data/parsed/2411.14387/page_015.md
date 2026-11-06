_X_<sup>(_j<sub>x</sub>_)</sup> caused it. So the total number of alternations of this type is bounded by

\(\underbrace{l}_{\text{which}j_b\text{?}}\underbrace{max_{j_x}\big|X^{(j_x)}\big|}_{\text{which access within}X^{(j_x)\text{?}}}=l\frac{m}{l}=m,\)

where the first equality uses our assumption that \(|X^{(1)}|=\cdots=|X^{(l)}|\).

Overall, we have shown that

\(\text{Alt}_\mathcal{T}(X)\le\underbrace{\text{Alt}_\widetilde{\mathcal{T}}\big(\widetilde{X}\big)}_{\text{type 4}}+\sum_j\underbrace{\text{Alt}_{\mathcal{T}_j}\big(X^{(j)}\big)}_{\text{type 1}}+\underbrace{O(m)}_{\text{type 2 (charge to}t_x\text{or}t_y)}+\underbrace{O(m)}_{\text{type 3 (charge to}j_b)},\)

so we can now take the maximum over T to conclude

\(\text{Alt}(X):=max_\mathcal{T}\text{Alt}_\mathcal{T}(X)\)<br> \(\le max_\mathcal{T}\big(\text{Alt}_\widetilde{\mathcal{T}}\big(\widetilde{X}\big)+\sum_j\text{Alt}_{\mathcal{T}_j}\big(X^{(j)}\big)+O(m)\big)\)<br> \(\le max_\widetilde{\mathcal{T}}\text{Alt}_\widetilde{\mathcal{T}}\big(\widetilde{X}\big)+\sum_jmax_{\mathcal{T}_j}\text{Alt}_{\mathcal{T}_j}\big(X^{(j)}\big)+O(m)\)<br> \(=\text{Alt}\big(\widetilde{X}\big)+\sum_j\text{Alt}\big(X^{(j)}\big)+O(m).\blacktriangleleft\)

## 4 Boosting the separation between Wilber’s bounds

We prove Theorem 2 in this section. We now use the composition properties of Alt and Funnel we proved in Section 3 to show that Tango tree makes an optimal trade-off between fixed costs and variable costs that depend on the alternation bound.

### 4.1 What boosting can we get?

Lecomte and Weinstein [27] show an \(\Omega(loglogn)\) separation between Alt and Funnel.

\(\blacktriangleright\) **Theorem 24** (Theorem 2 in [27])**.** _For any n of the form_ 2<sup>2_k_</sup>_, there is a sequence_ \(Y_n\in[n]^m\) _where_ \(m\le poly(n)\)_, each element appears O(m/n_) _times, and_

\(\overline{\text{Alt}}(Y_n)\le O(1)\)<br> \(\overline{\text{Funnel}}(Y_n)\ge\Omega(loglogn).\)

We can use the tight composition results from Section 3 to show the following boosted separation. We emphasize that the approximate subadditivity of the Alternation bound [6] is insufficient to boost the separation.

\(\blacktriangleright\) **Theorem 25** (Hardness Amplification, Restatement of Theorem 2)**.** _There is a constant K\>_0 _such that for any n of the form_ 2<sup>2_k_</sup> _and any power-of-two_ \(R\le\frac{logn}{K}\) _, there is a sequence_ \(Y_n^{\circ R}\in[n]^{m^\prime}\) _with_ \(m'\le poly(n)\) _such that_

\(\overline{\text{Alt}}\big(Y_n^{\circ R}\big)\le O(R)\)<br> \(\overline{\text{Funnel}}\big(Y_n^{\circ R}\big)\ge\Omega\big(Rlog\big(\frac{logn}{R}\big)\big).\)

