That is,

\(\mathsf{OPT}(X)\ge\mathsf{OPT}\big(\widetilde{X}\big)+\sum_j\mathsf{OPT}\big(X^{(j)}\big).\) (1)

The superadditivity of optimal cost finds an application in designing a new _O_(loglog_n_)- competitive online BST algorithm based on purely geometric formulation [6].

However, the direct sum results for Wilber’s bounds are poorly understood despite their importance to the pursuit of dynamic optimality. The only published work that we are aware of is the approximate subadditivity of the Alternation bound [6]. That is, they proved that

\(\mathsf{Alt}(X)\le 4\cdot\mathsf{Alt}\big(\widetilde{X}\big)+8\cdot\sum_j\mathsf{Alt}\big(X^{(j)}\big)+O(|X|).\) (2)

Their proof is quite involved, and it is based on geometric arguments and the probabilistic method. This finds applications in proving the separation between the Alternation and Funnel bounds. In [6], they used approximate subadditivity of the Alternation bound (Equation (2)) to prove a near-optimal separation between the Alternation and Funnel bounds. That is, they constructed a sequence _Y_ such that the gap between Alt(_Y_) and Funnel(_Y_) is as large as \(\Omega(\frac{loglogn}{logloglogn})\). This gap is nearly optimal because the upper bound of Tango tree [16] implies that the gap must be _O_(loglog_n_). This gap has been closed by an independent work by Lecomte and Weinstein [27], proving the optimal separation between the Alternation and Funnel bounds. That is, they constructed an instance _Y_ such that the gap between Alt(_Y_) and Funnel(_Y_) is as large as \(\Omega(loglogn)\).

Furthermore, [6] also used the approximate subadditivity of the Alternation bound (Equation (2)) to prove the \(\Omega(\frac{loglogn}{logloglogn})\) gap between Alt(_Y_) and cGB(_Y_) where cGB(_Y_) denotes the _Consistent Guillotine Bound_ (cGB), a lower bound measure that is an extension of Alt(_Y_).

### 1.1 Our Results

We prove that the Alternation bound is subadditive whereas the Funnel bound is superadditive for composed sequences. More precisely, we prove the following theorem.

\(\blacktriangleright\) **Theorem 1** (Direct-Sum Theorem for Wilber’s Bounds)**.** _Let_ \(X:=\widetilde{X}(X^{(1)},\dots,X^{(l)})\) _be a composed sequence. Then_

\(\mathsf{Alt}(X)\le\mathsf{Alt}\big(\widetilde{X}\big)+\sum_j\mathsf{Alt}\big(X^{(j)}\big)+O(|X|)\)_, and_

\(\mathsf{Funnel}(X)\ge\mathsf{Funnel}\big(\widetilde{X}\big)+\sum_j\mathsf{Funnel}\big(X^{(j)}\big)-O(|X|).\)

Our proof of the subadditivity of the Alternation bound is simpler and yields stronger bounds than the proof in [6] (Theorem 3.6 in their arXiv version). Direct sum theorems are a natural black-box tool for hardness amplification, as they effectively reduce complex lower bounds to a simpler "one-dimensional" problem. Indeed, as a showcase application, we use the base-case separation proved in [27] along with Theorem 1 to amplify both Wilber’s bounds. Let <o>Alt</o>(_X_):=Alt(_X)/|X_|, and <o>Funnel</o>(_X_):=Funnel(_X)/|X_|. They proved that there is a sequence _Y_ such that

\(\overline{\mathsf{Alt}}(Y)\le O(1),\text{but}\)<br> \(\overline{\mathsf{Funnel}}(Y)\ge\Omega(loglogn).\)

