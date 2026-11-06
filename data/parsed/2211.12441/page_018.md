## 4.3 Lipschitz continuity

Average-case notions typically do not change much under small changes to the input. This is indeed the case for the average sensitivity when "small" is interpreted as affecting few of the subtrees. The following lemma quantifies the property and can be viewed as a form of Lipschitz continuity.

**Lemma 28.** _Given a tree T, if a subtree T_<sub>_v_<sup>∗</sup></sub> _with_ \(\ell\) _leaves is replaced with a tree_ \(T'_{v^*}\) _with the same number of leaves, resulting in the tree_ \(T'\)_, then_

\(|s(\Pi_T)-s(\Pi_{T^\prime})|\le\frac{\ell(\ell-1)}{n}.\)

_Proof._ We think of the leaf sets of _T_ and \(T'\) as being the same set \(X=\mathrm{L}(T)=\mathrm{L}(T')\), and fix a ranking \(\rho\) of _X_. Consider an ordering of _T_ and the ranking \(\sigma\) of _X_ that it induces. Outside of \(T'_{v^*}\) we can order \(T'\) in the same way as _T_. Irrespective of how we order \(T'\) inside \(T'_{v^*}\), the induced ranking \(\sigma'\) of _X_ agrees with \(\sigma\) on all leaves in _X_ except possibly those in \(Y\doteq\mathrm{L}(T_{v^*})=\mathrm{L}(T'_{v^*})\). Moreover, under both \(\sigma\) and \(\sigma'\), the set _Y_ gets mapped to the same contiguous interval. It follows that for all pairs \((\ell_1,\ell_2)\) of distinct leaves of which at least one lies outside of _Y_, \((\ell_1,\ell_2)\) constitutes an inversion of \(\sigma\) with respect to \(\rho\) if and only if \((\ell_1,\ell_2)\) constitutes an inversion of \(\sigma'\) with respect to \(\rho\). For any node _v_ outside of _T_<sub>_v_<sup>∗</sup></sub>, root inversions in _T<sub>v</sub>_ cannot involve leaves that are both in \(Y\doteq\mathrm{L}(T_{v^*})\). See Figure 8 for an illustration. Thus, for such nodes _v_, \(\mathrm{RInv}(T_v,\rho,\sigma)=\mathrm{RInv}(T'_v,\rho,\sigma')\). By taking the minimum over all orderings, we conclude:

**Claim 29.** \(\mathrm{MinRInv}(T_v,\rho)=\mathrm{MinRInv}(T'_v,\rho)\) _holds for every node v outside of T_<sub>_v_<sup>∗</sup></sub> _(or equivalently, outside of_ \(T'_{v^*}\)_)._

Consider a ranking \(\rho\) and an adjacent-rank transposition \(\tau=(r,r+1)\). We claim that, unless \((\ell_1,\ell_2)\doteq(\rho^{-1}(r),\rho^{-1}(r+1))\in Y\times Y\) , \(\Pi_T\) is sensitive to \(\tau\) at \(\rho\) if and only if \(\Pi_{T^\prime}\) is sensitive to \(\tau\) at \(\rho\). This is because by Proposition 27 the only term in the decomposition (5) of \(\mathrm{MinInv}(T,\rho)\) that can be affected by \(\tau\) is the contribution \(\mathrm{MinRInv}(T_v,\rho)\) for \(v=\mathrm{LCA}(\ell_1,\ell_2)\). If at least one of \(\ell_1\) or \(\ell_2\) is not inside _T_<sub>_v_<sup>∗</sup></sub>, then _v_ is not inside _T_<sub>_v_<sup>∗</sup></sub> either, so by Claim 29, \(\mathrm{MinRInv}(T_v,\rho)=\mathrm{MinRInv}(T'_v,\rho)\). By the same token, \(\mathrm{MinRInv}(T_v,\tau\rho)=\mathrm{MinRInv}(T'_v,\tau\rho)\). It follows that \(\mathrm{MinInv}(T,\rho)\neq\mathrm{MinInv}(T,\tau\rho)\) if and only if \(\mathrm{MinInv}(T',\rho)\neq\mathrm{MinInv}(T',\tau\rho)\).

We bound the expected number of values of _r_ for which \((\rho^{-1}(r),\rho^{-1}(r+1))\in Y\times Y\) with \(Y\doteq\mathrm{L}(T_v)\) when \(\rho\) is chosen uniformly at random. For \(r\in[n-1]\), the probability that \(\rho^{-1}(r)\in Y\) is \(\frac{\ell}{n}\), and the probability that \(\rho^{-1}(r+1)\in Y\) given that \(\rho^{-1}(r)\in Y\) is \(\frac{\ell-1}{n-1}\). Using linearity of expectation on the indicators, the expected number of said _r_ is

\((n-1)\left(\frac{\ell(\ell-1)}{n(n-1)}\right)=\frac{\ell(\ell-1)}{n}.\)

v
v*
l1
l2
Y
X

Figure 8: Effects of changing _T_<sub>_v_<sup>∗</sup></sub>

