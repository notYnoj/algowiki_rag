## 3 Effect of Composition on Wilber’s bounds

We prove Theorem 1 in this section. Namely, we show that Wilber’s bounds act nicely under composition, allowing us to boost the separation between them in Section 4. We divide the proofs into the following two theorems.

\(\blacktriangleright\) **Theorem 19 (subadditivity of Alt).** _Let_ \(X:=\widetilde{X}(X^{(1)},\dots,X^{(l)})\) _be a composed sequence with_ \(|X^{(1)}|=\cdots=|X^{(l)}|\).<sup>7</sup> _Then_

\(\mathsf{Alt}(X)\le\mathsf{Alt}\big(\widetilde{X}\big)+\sum_j\mathsf{Alt}\big(X^{(j)}\big)+O(m).\)

We prove Theorem 19 in Section 3.1.

\(\blacktriangleright\) **Theorem 20 (superadditivity of Funnel).** _Let_ \(X:=\widetilde{X}(X^{(1)},\dots,X^{(l)})\) _be a composed sequence. Then_

\(\mathsf{Funnel}(X)\ge\mathsf{Funnel}\big(\widetilde{X}\big)+\sum_j\mathsf{Funnel}\big(X^{(j)}\big)-O(m).\)

We prove Theorem 20 in Section 5.

### 3.1 Subadditivity of the alternation bound

We prove Theorem 19 in this section.

### Proof plan

We will show that for any binary search tree T over \(S_1\cup\cdots\cup S_l\),

\(\mathsf{Alt}_\mathcal{T}(X)\le\mathsf{Alt}\big(\widetilde{X}\big)+\sum_j\mathsf{Alt}\big(X^{(j)}\big)+O(m).\)

We will do this by

decomposing T into the corresponding binary trees \(\widetilde{\mathcal{T}}\) over [_l_] and T_<sub>j</sub>_ over _S<sub>j</sub>_ for all _j_; \(\blacksquare\) classifying preferred child alternations in T into 4 types, which correspond to either \(\blacksquare\) alternations in \(\widetilde{\mathcal{T}}\), \(\blacksquare\) alternations in T_<sub>j</sub>_ for some _j_, \(\blacksquare\) or to some other events that happen at most _O(m_) times in aggregate. That is, we will show that

\(\mathsf{Alt}_\mathcal{T}(X)\le\mathsf{Alt}_\widetilde{\mathcal{T}}\big(\widetilde{X}\big)+\sum_j\mathsf{Alt}_{\mathcal{T}_j}\big(X^{(j)}\big)+O(m).\)

#### 3.1.1 Decomposing the tree

For a tree T , we write \(x\prec_\mathcal{T}b\) if _x_ is a descendent of _b_ in T , and we write \(S\prec_\mathcal{T}b\) if \(x\prec_\mathcal{T}b\) for all \(x\in S\).

\(\blacktriangleright\) **Definition 21.** _Let_ T_<sub>j</sub> be the unique binary search tree over S<sub>j</sub> such that if_ \(b,x\in S_j\) _and_ \(x\prec_\mathcal{T}b\) _then_ \(x\prec_{\mathcal{T}_j}b\).

<sup>7</sup> We make this assumption so that the proof is simpler.

