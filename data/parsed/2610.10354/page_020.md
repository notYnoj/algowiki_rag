and

\(|A\cap H|\ge\frac{|A|}{K},\) (6)

for some<tbc>

\(K\le O_{\epsilon,c}\big(\alpha^{-O_\epsilon(1)}\big(1+\frac{|P_D|}{|A|}\big)^{\epsilon/(4c)}\big).\)

<tbc>From the previous bounds on _K_ and |_P<sub>D</sub>|/|A_|, we can bound

\(K\le O_{\epsilon,c}(|A|^{O_{\epsilon,c}(\delta)+\epsilon/4+o(1)}).\)

Recall that \(\delta=2c/k\). Choose \(k=k(c,\epsilon)\) sufficiently large so that this bound becomes \(K\le O_{\epsilon,c}(|A|^{\epsilon/2})\). Then the right-hand side of (5) can be bounded by \(O_{\epsilon,c}(|A|^\epsilon)\cdot|A|^{1+c}\). Hence, the set _H_ is as claimed by Equations (4) to (6).

## 3.3 Efficient Algorithm

We finally revisit the previous proof to demonstrate that all steps can be implemented efficiently, leading to the following algorithmic theorem:

**Theorem 3.5.** _For every c\>_0 _and_ \(\epsilon>0\)_, there is some_ \(k=k(c,\epsilon)\) _such that the following holds. There is a randomized algorithm that, given_ \(A\subseteq\mathbb{Z}\) _and some parameter_ \(p=\Omega(|A|^{k-1-c})\)_, either certifies that_ \(\mathrm{Pop}^k(A;p)=\emptyset\)_, or otherwise computes a set_ \(H\subseteq\mathbb{Z}\) _such that the following properties hold for some_ \(K\le O(|A|^\epsilon)\):

• \(|H|\le K|A|^{1+c}\),<tbc>

• \(|H+H|\le K|H|\),<tbc>

• \(|A\cap H|\ge|A|/K\).

_The algorithm runs in time_ \(\widetilde{O}(|A|^{1+c+\epsilon})\).

The following lemma is analogous to Lemma 3.4.

**Lemma 3.6.** _For every_ \(\epsilon,c>0\)_, there is some_ \(k=k(c,\epsilon)\) _such that the following holds. There is a randomized algorithm that, given_ \(A\subseteq\mathbb{Z}\) _such that_ \(T_k(A)\ge\Omega(|A|^{2k-1-c})\) _computes a set_ \(H\subseteq\mathbb{Z}\) _such that the following properties hold for some_ \(K\le O(|A|^\epsilon)\):

• \(|H|\le K|A|^{1+c}\),<tbc>

• \(|H+H|\le K|H|\),<tbc>

• \(|A\cap H|\ge|A|/K\).

_The algorithm runs in time_ \(\widetilde{O}(|A|^{1+c+\epsilon})\).

