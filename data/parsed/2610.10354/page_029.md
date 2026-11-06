**Proof of Lemma 4.3.** We start from a 3SUM instance (_A,B,C_) where _C_ has rank at most \(n^{1-\rho}\). Let \(\epsilon_1=\frac{\epsilon}{4}\) and \(\epsilon_2=\frac{3\epsilon}{4}\). Lemma 4.5 reduces this instance to \(O(n^{\epsilon_1})\) subinstances \((A'\subseteq A,B,C)\), each provided with a \((K=O(n^{\epsilon_1}),N=O(n^{2-2\rho}))\)-container _H_ of \(A'\). We pass each such instance to Lemma 4.8, obtaining \(O(n^{\epsilon_2})\) subinstances \((A',B'\subseteq B,C'\subseteq C)\) where \(B'\) is covered by a translate of _H_ and \(C'\) is covered by a translate of _H+H_. Pick<tbc>

\(H'=H\cup B'\cup C';\)

<tbc>we claim that this is a (_O(K_<sup>4</sup>)_,O(N_))-container of \(A'\cup B'\cup C'\). The containment condition is clear, and the size of \(H'\) is bounded by \(|H|+|B|+|C|\le N+2n\le O(N)\). Regarding the doubling of \(H'\), observe that \(H'+H'\) can be covered by _O_(1) translates of _H+H+H+H_. Thus, by the Plünnecke-Ruzsa inequality (Lemma 2.1),

\(|H'+H'|\le O(|H+H+H+H|)\le O(K^4)|H|\le O(K^4)|H'|.\)

In summary, it follows that \(H'\) is indeed a \((O(n^{4\epsilon_1})=O(n^\epsilon),O(n^{2-2\rho}))\)-container of \(A'\cup B'\cup C'\). Moreover, the total number of instances is \(O(n^{\epsilon_1+\epsilon_2})=O(n^\epsilon)\).

Let us finally analyze the running time. The reduction in Lemma 4.5 takes time \(O(n^{2-\delta_1})\) for some constant \(\delta_1=\delta_1(\rho,\epsilon_1)>0\). Each of the \(O(n^{\epsilon_1})\) calls to Lemma 4.8 takes time \(\widetilde{O}(KNn^{\epsilon_2}+Kn^{2-\epsilon_2})\), amounting to a total time of

\(\widetilde{O}(n^{\epsilon_1}\cdot(KNn^{\epsilon_2}+Kn^{2-\epsilon_2}))=\widetilde{O}(n^{2-2\rho+2\epsilon_1+\epsilon_2}+n^{2+2\epsilon_1-\epsilon_2})=\widetilde{O}(n^{2-2\rho+5\epsilon/4}+n^{2-\epsilon/4}).\)

If necessary, decrease \(\epsilon\) to \(4\rho/5\) so that the first term becomes \(O(n^{2-\rho})\). Then the running time is as claimed for any constant \(0<\delta<min(\delta_1,\rho,\frac{\epsilon}{4})\).

## 5 Universe Reductions for Min-Plus Convolution

In this section we design our universe reductions for Min-Plus Convolution. These work somewhat differently in two regimes, and thus we design a "small-universe reduction" from \[_n_\] to \([n^\gamma]\), for \(\gamma<1\), and a separate "large-universe reduction" from \[_n<sup>c</sup>_\] to \[_n_\], for _c\>_1. We start with the simpler small- universe reduction in Section 5.1. Then, to prepare the more involved large-universe reduction, in Section 5.2 we first design a "doubling reduction", proving that the index sets of the given sequences can be assumed to have low-doubling containers. In Section 5.3 we then design a universe reduction for the _Monotone_ Min-Plus Convolution problem. Finally, in Section 5.4 we put these two pieces together to obtain the large-universe reduction, conditioned on Hypothesis 1.7.

### 5.1 Small-Universe Reduction

The small-universe reduction can be stated as follows:

**Lemma 5.1** (Small-Universe Reduction)**.** _For any_ \(0\le\gamma\le 1\) _and_ \(\epsilon>0\),

\(\text{MPConv}(n|u\le n)=\widetilde{O}\big(n^\epsilon\cdot\text{MPonvList}(n,n^{1-\gamma}|u\le n^\gamma)+3\text{SUM}(n|r\le n^{1-\epsilon/2})\big).\) (7)

**Proof.** Let (_A,B_) be the given Min-Plus Convolution instance with universe \[0_,n_\]. Let \(q=\lceil n^{1-\gamma}\rceil\), and rewrite these sequences as

\(A=A_1\cdot q+A_0,\)<br>
\(B=B_1\cdot q+B_0,\)

