<tbc>_Proof._ For _s_=1_,...,n_-1, the probability that \(\rho^{-1}(s)\in\mathrm{L}(T_v)\) is \(\frac{\ell}{n}\), and the probability that \(\rho^{-1}(s+1)\unknown\in\mathrm{L}(T_v)\) given that \(\rho^{-1}(s)\in\mathrm{L}(T_v)\) is \(\frac{n-\ell}{n-1}\). Using linearity of expectation on the indicator random variables for \(\rho^{-1}(s)\in\mathrm{L}(T_v)\) and \(\rho^{-1}(s+1)\unknown\in\mathrm{L}(T_v)\), the expected number of _s_ satisfying this property is

\((n-1)\left(\frac{\ell(n-\ell)}{n(n-1)}\right)=\frac{\ell(n-\ell)}{n}.\)

Combining Claim 22, Claim 23, and Claim 24, we can conclude with Lemma 21.

## Bounded degree.

We apply our analysis to the case of trees of degree _k_. Observe that for fixed _n_, Lemma 21 is strongest when \(\ell=n/2\). Not every tree _T_ has a subtree with exactly _n/_2 leaves, but Lemma 21 still gives a useful bound for subtrees that do not contain too few or too many leaves. In the case of trees of bounded degree, there always exists a subtree _T<sub>v</sub>_ that contains a fairly balanced fraction of the leaves. The following quantification is folklore, but we include a proof for completeness.

**Fact 25.** _If T is a tree of degree k with n leaves, there exists a node v in T such that_ \(\ell\doteq|\mathrm{L}(T_v)|=\alpha\cdot n\)_, where_ \(\frac{1}{k+1}\le\alpha\le\frac{k}{k+1}\).

_Proof._ Let _r_ be the root of _T_ and construct a sequence _v_<sub>1</sub>=_r,v_<sub>2</sub>_,v_<sub>3</sub>_,..._ such that _v<sub>i</sub>_ is a child of _v_<sub>_i_-1</sub> that maximizes \(\ell_i\doteq|\mathrm{L}(T_{v_i})|\), with ties broken arbitrarily. Notice that \(\{\ell_i\}\) is a decreasing sequence, and since _T_ has degree _k_, \(\ell_i\le k\ell_{i+1}\) for all _i_. We claim that some _v<sub>i</sub>_ in this sequence satisfies the conditions of the claim. If not, then for some _i_, \(\ell_i>\frac{k}{k+1}\cdot n\) and \(\ell_{i+1}<\frac{1}{k+1}\cdot n\), which contradicts the fact that \(\ell_i\le k\ell_{i+1}\).

By choosing a subtree satisfying Fact 25, we can apply Lemma 21 and conclude that \(s(\Pi_T)\ge\frac{k}{(k+1)^2}\cdot n-1\). The Sensitivity Lemma then gives the "in particular" part of Theorem 5.

v
2
7
3
9
8
1
5
4
6

σ
9
8
7
6
5
L(Tv)
4
3
2
1
1
2
3
4
5
6
7
8
9
r1
r2
p
S1
S1
S2
S2

(a) Leaves in \(\sigma\)-order, labeled with \(\rho\)-ranks

(b) Corresponding plot of \(\rho,\sigma\) for each leaf

Figure 7: \(\sigma\) maps leaves of L(_T<sub>v</sub>_) in a contiguous range.

