Then, we enlarge the DP table _q_\[-_L_<sub>_j_-1</sub>_...L_<sub>_j_-1</sub>\] to _q_\[-_L<sub>j</sub>...L<sub>j</sub>_\] by padding dummy entries \(-\infty\), and define a HintedKnapsackExtend<sup>+</sup> instance on functions _Q<sub>w</sub>_ and DP table _q_\[-_L<sub>j</sub>...L<sub>j</sub>_\] with hints \(S[-L_j\dots L_j]:=S^+[-L_j\dots L_j]\) (recall \(S^+[i]\subseteq\mathcal{W}_1\) and \(|S^+[i]|\le b_j\)). We run the algorithm from Theorem 3.11 to solve this instance in _O(L<sub>j</sub>b<sub>j</sub>_log<sup>2</sup>(_L<sub>j</sub>b<sub>j</sub>_)) time, and obtain solution vectors \(x[i]\in\mathbb{Z}_{\ge 0}^{\mathcal{W}_1}\) for all \(-L_j\le i\le L_j\). Recall from Eqs. (15) and (16) that solution vector **_x_**\[_i_\] achieves total profit

\(r[i]:=q\big[z[i]\big]+\sum_{w\in\mathcal{W}_1}Q_w(x[i]_w),\)

where \(z[i]+\sum_{w\in\mathcal{W}_1}w\cdot x[i]_w=i\).

In the following, we will first show that _r_\[-_L<sub>j</sub>...L<sub>j</sub>_\] satisfies Item 1 of Definition 3.8 (and thus is an \((J_{\le j}^+\cup J_{\le j-1}^-)\)-optimal DP table). Then we will compute new hints \(T^+[-L_j\dots L_j],T^-[-L_j\dots L_j]\) to satisfy Item 2 of Definition 3.8, making \(r[-L_j\dots L_j]\) a hinted-\((J_{\le j}^+\cup J_{\le j-1}^-)\)-optimal DP table.

## Optimality.

Since _q_\[\] is a hinted-\((J_{\le j-1}^+\cup J_{\le j-1}^-)\)-optimal DP table by assumption, by Definition 3.8 (Item 1) there exists an _I_<sub>W<sub>1</sub></sub>-optimal partial solution \((A',B')\) such that _q_\[\] contains partial solution \((A'',B'')\) where \(A'':=A'\cap J_{\le j-1}^+,B'':=B'\cap J_{\le j-1}^-\), that is, we have \(q[z'']=P(A'')-P(B'')\) for \(z'':=W(A'')-W(B'')\). Now consider the partial solution \((\widehat{A}'',B'')\) where \(\widehat{A}'':=A'\cap J_{\le j}^+\), and denote their difference by \(Y:=\widehat{A}''\backslash A''=A'\cap J_j^+\). Encode the items in _Y_ by a vector \(y\in\mathbb{Z}_{\ge 0}^{\mathcal{W}_1}\) where \(y_w=|I_{\{w\}}\cap Y|\), and by the prefix property (Lemma 2.4) we must have \(P(Y)=\sum_{w\in\mathcal{W}_1}Q_w(y_w)\), so \(q[z'']+\sum_{w\in\mathcal{W}_1}Q_w(y_w)=P(\widehat{A}'')-P(B'')\). Now the goal is to show that \((\widehat{A}'',B'')\) indeed survives in the solution of the HintedKnapsackExtend<sup>+</sup> instance, i.e., for \(\hat{i}:=W(\widehat{A}'')-W(B'')\) we want to show \(r[\hat{i}]=q[z'']+\sum_{w\in\mathcal{W}_1}Q_w(y_w)\).

First we verify that \(\hat{i}\) is contained in the index range \[-_L<sub>j</sub>...L<sub>j</sub>_\] of the returned table: by Lemma 3.7 (Item 2) we have \(W(\widehat{A}'')\le|A'\cap J_{\le j}^+|\cdot w_{max}\le m_jw_{max}=L_j\), and similarly \(W(B'')\le L_{j-1}\), so \(|\hat{i}|=|W(\widehat{A}'')-W(B'')|\le L_j\) as desired. Now, if \(r[\hat{i}]\neq q[z'']+\sum_{w\in\mathcal{W}_1}Q_w(y_w)\), then by the definition of Problem 1 there are only two possibilities:

• Case 1: \((y,z'')\) is not a maximizer for \(r[\hat{i}]\).<tbc>

<tbc>This means there is a solution (**_x_**_<sup>⋆</sup>,z<sup>⋆</sup>_) with strictly better total profit \(q[z^\star]+\sum_{w\in\mathcal{W}_1}Q_w(x_w^\star)>q[z'']+\sum_{w\in\mathcal{W}_1}Q_w(y_w)\). Let \(X^\star\subseteq J_j^+\) be the item set encoded by **_x_**_<sup>⋆</sup>_, and let _q_\[_z<sup>⋆</sup>_\] correspond to the partial solution (_A<sup>⋆</sup>,B<sup>⋆</sup>_) supported on \((J_{\le j-1}^+\cup J_{\le j-1}^-)\). Then the partial solution \((A^\star\cup X^\star,B^\star)\) has the same weight as \((\widehat{A}'',B'')\) but achieves strictly higher profit (both of them are supported on \(J_{\le j}^+\cup J_{\le j-1}^-)\). This contradicts the _I_<sub>W<sub>1</sub></sub>-optimality of \((A',B')\) by an exchange argument.<tbc>

• Case 2: \((y,z'')\) is a maximizer for \(r[\hat{i}]\), but there is also another maximizer (**_x_**_<sup>⋆</sup>,z<sup>⋆</sup>_) for \(r[\hat{i}]\) that violates the support containment condition \(\text{supp}(x^\star)\subseteq S[z^\star]=S^+[z^\star]\) (Eq. (17)).<tbc>

<tbc>Let \(X^\star\subseteq J_j^+\) and (_A<sup>⋆</sup>,B<sup>⋆</sup>_) be defined in the same way as in Case 1. Similarly to the discussion in Case 1, here we know that there is an alternative _I_<sub>W<sub>1</sub></sub>-optimal partial solution \((\widetilde{A}',\widetilde{B}'):=\big((A'\backslash\widehat{A}'')\cup(A^\star\cup X^\star)\), \((B'\backslash B'')\cup B^\star\big)\) that achieves the same weight and profit as \((A',B')\).<tbc>

<tbc>By the violation of Eq. (17) we have \(\text{supp}(\text{weights}(X^\star))=\text{supp}(x^\star)\unknown S^+[z^\star]\), that is, \(X^\star\unknown\subseteq I_{S^+[z^\star]}\). Since \(\widetilde{A}'\backslash(J_{\le j-1}^+\cup J_{\le j-1}^-)\supseteq X^\star\), this means \(\widetilde{A}'\backslash(J_{\le j-1}^+\cup J_{\le j-1}^-)\unknown\subseteq I_{S^+[z^\star]}\). This violates<tbc>

