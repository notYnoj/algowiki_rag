<tbc>Since \(2^m=\sqrt{D}\) and 2<sup>-_m/_9</sup>=_D_<sup>-1/18</sup>, the second inequality of Lemma 11 says that

\(|\text{Leaves}(U)|\le D^{-1/18}\big(\sqrt{D}|U|+2M\big).\)

Consider a tile in which \(|U|=M/\sqrt{D}\) entries are wanted. (This is the density of Theorem 5, which allows \(N^2/\sqrt{D}\) wanted entries out of _N_<sup>2</sup>.) Then \(\sqrt{D}|U|=M\), and the bound says that only _O(M/D_<sup>1/18</sup>) leaves contribute to the wanted entries of the tile. This is a factor _D_<sup>1/18</sup> below the number _M_ of output entries of the tile, and far below the \(|U|\cdot D=M\sqrt{D}\) multiplications that computing each wanted entry directly, as an inner product, would take. Next in Section 2.4.4 we sum the number of leaves over all the tiles, and we will use the fact that the bound is linear in |_U_|, meaning the total is the same no matter how the wanted entries are spread over the tiles.

## 2.4.4 Proof of Theorem 5

We finally put everything together to state and analyze our algorithm. As before, set _D_=4_<sup>m</sup>_ and _L_=19_m_.

_Two consequences of_ \(N\ge D^{18}\). We use the assumption \(N\ge D^{18}\) twice, each time to check that _N_ is large enough compared with a quantity that grows exponentially in _m_. Since _D_<sup>18</sup>=4<sup>18_m_</sup>, we compare _m_-th powers by comparing their bases.

First, the tiling of Section 2.3.4 requires that \(N\ge K_0N_0\) so that it does not lose too much when padding, since it pads _N_ to a multiple of _K_<sub>0</sub>_N_<sub>0</sub>. This holds: using the general bound \(\genfrac(){pt}{2}{L}{m}\le(eL/m)^m\), we have \(K=\genfrac(){pt}{2}{19m}{m}\le(19e)^m\), so \(KN_0\le(19e\cdot 3^{18})^m\le 4^{18m}\), as \(19e\cdot 3^{18}<4^{18}\), and hence \(K_0N_0\le KN_0\le D^{18}\le N\). This means the padding at most doubles _N_, and we continue to write _N_ for the padded size.

Second, the encoding phase of the algorithm (Section 2.4.1) has a cost that does not depend on _W_ at all, and we need to ensure it is not too large. Recall that we perform 2_N/K_<sub>0</sub>_N_<sub>0</sub> encodings, which use _O_(10_<sup>L</sup>_) operations each. To afford them within our budget of _O_(2<sup>-_m/_9</sup>_N_<sup>2</sup>)<tbc>

number of leaves (log scale)
M
|U| ad
|U|
small order: charge each output string
large order: take all the leaves
βd 2-dM
order d
m/9
m

Figure 7: The count of Lemma 11, schematically. The leaves of order _d_ in Leaves(_U_) number at most \(min\{|U|\alpha_d\), \(\beta_d\}\): the bound \(|U|\alpha_d\) grows with _d_ up to _d_≈0.9_m_ (more leaves of higher order contribute to each output string), and the bound \(\beta_d\) shrinks geometrically (there are fewer leaves of higher order). The proof splits at _d=m/_9, which is not necessarily where the two bounds cross, and it bounds the total by the shaded area.

