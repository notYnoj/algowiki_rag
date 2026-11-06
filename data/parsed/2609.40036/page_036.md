_Proof._ The selected representatives are closed under deleting nonzero coordinates. Indeed, replacing a nonzero coordinate by zero increases the weight disadvantage of any competing representative, unless the competing word agrees on that coordinate. In the latter case the lexicographic comparison is unchanged. The stronger set of words whose one-coordinate neighbors are all selected is also closed under deletion: a change on a different coordinate commutes with deletion, and a change on the deleted coordinate is already a neighbor of the original word.

To couple _P<sub>k</sub>_ and _P_<sub>_k_+1</sub>, first draw independent nonzero symbols from the \(\theta_i\), choose a uniform ordering of the coordinates, and retain the first _k_ or _k_+1 symbols. Deletion closure gives \(R_k\le R_{k+1}\). Conditioning the independent channel on _K_ gives \(R(p')=\unknown R_K\ge R_\ell Pr(K\ge\ell)\).

## A.3 Planting a small matching early in a round

The converse needs a lower probability bound. Throughout this section, _H_ is an arbitrary (_D_-1)- regular graph of girth at least _g_. Choose an even integer

\(m=n^{(1+c)/2+o(1)},T=(n-m)/2,\) (157)

and let _M<sub>T</sub>_ be the matching selected in the first _T_ steps of the final round. A degree-_D_ graph has at most _C<sub>D</sub>(D_-1)_<sup>g</sup>=O<sub>D</sub>(n<sup>c</sup>_) vertices in a ball of radius _g_-2. Since \(m\gg n^c\), the process cannot freeze before _T_.

**Lemma 8** (Early matching probabilities)**.** _Uniformly over H and specified matchings F with_ \(s=|F|\le K_0logn\),

\(Pr(F\subseteq M_T|H)\le(1+o(1))n^{-s}.\) (158)

_If in addition H+F is simple and has girth at least g, then_

\(Pr(F\subseteq M_T|H)=(1+o(1))n^{-s}.\) (159)

_Here K_<sub>0</sub> _is any fixed constant._

_Proof._ The upper bound follows from the potential in Lemma 2, using the state-dependent missing- degree bound _C<sub>D</sub>n<sup>c</sup>_. Stop at _T_, then complete the residual matching uniformly without a girth constraint for this calculation only. The cumulative multiplicative error is

\(exp\left(O_D\left(sn^c\sum_{v\ge m}v^{-2}\right)\right)=exp(O_D(sn^c/m))=1+o(1).\) (160)

Together with \(\Phi_s(n)=(1+o(1))n^{-s}\) this proves (158).

For the lower bound, we use a planted process. Choose a uniform injection from the _s_ labelled edges of _F_ to the first _T_ selection times. Insert each prescribed edge at its assigned time. At every other step select a uniform available pair avoiding all endpoints of still-pending edges of _F_. For purposes of defining a probability measure, insert a forced edge even when it is unavailable; call such a trajectory _invalid_. Forced endpoints are either protected or already matched, so no unforced edge ever touches _V(F_). Even on invalid trajectories the graph is simple and has maximum degree _D_, and the unforced choices exist because at least \(m-2s\gg n^c\) outside vertices remain free.

