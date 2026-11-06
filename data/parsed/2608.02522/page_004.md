a recent breakthrough by OpenAI [Ope26] for the case _p_=1 (i.e., for the multicolor Ramsey number of the triangle), we prove the following result.

**Theorem 1.7.** _Let_ \(p\in\mathbb{N}\) _be fixed. Then for all sufficiently large integers k we have_

\(R_k(\mathcal{O}_p)\ge(log^{(p-1)}k)^{k/3-o(k)}.\)

_In particular, since_ \(C_{2p+1}\in\mathcal{O}_p\)_, we have_ \(R_k(C_{2p+1})\ge R_k(\mathcal{O}_p)\ge(log^{(p-1)}k)^{k/3-o(k)}.\)

Here, for a non-negative integer _i_ we denote by \(log^{(i)}(\cdot)\) the _i_-fold iterated natural logarithm, defined as log<sup>(0)</sup>(_x_):=_x_ and log<sup>(_i_)</sup>(_x_):=log(log<sup>(_i_-1)</sup>(_x_)) for \(i\ge 1\).

In the following we give some context for Theorem 1.7 and place it within related work. The study of the asymptotic growth of Ramsey numbers is one of the oldest and yet still most active branches of combinatorics and graph theory. We refer the interested reader to [CFS15, Mor26] for surveys on the rich subject. The particular case of estimating the growth of multicolor Ramsey numbers _R<sub>k</sub>(F_) of fixed graphs _F_, as the number _k_ of colors grows, has also received a lot of attention. In the following, we discuss specifically the problem of estimating the multicolor Ramsey number \(R_k(C_\ell)\) where \(\ell\ge 3\) is a fixed odd number and _k_ tends to infinity, which has been the subject of a significant body of prior work.

Until recently, the best asymptotic upper and lower bounds in this setting that hold for arbitrary odd \(\ell\ge 3\) were

\((2+\delta_\ell)^k\le R_k(C_\ell)\le k^\frac{2k}{\ell-1}+o(k),\)

for all sufficiently large _k_ and some constant \(\delta_\ell>0\) depending solely on \(\ell\). The lower bound is due to Day and Johnson [DJ17] and the upper bound as stated was first proved by Axenovich et al. [ABJ<sup>+</sup>26], and subsequently improved further by Miyazaki et al. [MMPZ26] and Huang et al. [HYC26], however the bounds proved by the latter groups are still of the form \(k^\frac{2k}{\ell-1}+o(k)\). See also [BE73, EG75, Li09, LC19, JS21, Chu73, Rad11] for several earlier asymptotic bounds, bounds for different parameter regimes, and related work.

The case \(\ell=3\) has probably received the most attention, and it was a well-known open problem to determine whether or not _R<sub>k</sub>(C_<sub>3</sub>) grows exponentially or super- exponentially in _k_. Until recently, the best lower bound for this case was \(R_k(C_3)\ge 380^{k/5-O(1)}\) due to Ageron et al. [ACP<sup>+</sup>22]. In a recent breakthrough, OpenAI broke this exponential barrier by proving the lower bound

\(R_k(C_3)\ge\left(\frac{ck^{1/3}}{logk}\right)^k\)

for an absolute constant _c\>_0 [Ope26, Chapter 9, Theorem 1.1]. Together with the classic factorial upper bound for _R<sub>k</sub>(C_<sub>3</sub>) [GG55] this determines _R<sub>k</sub>(C_<sub>3</sub>) as \(k^{\Theta(k)}\). Our Theorem 1.7 generalizes this result and obtains a superexponential lower bound for arbitrary odd cycles. Our proof builds on and modifies the construction introduced by OpenAI [Ope26].

