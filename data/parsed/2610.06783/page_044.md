than _P_<sub>0</sub>, and replace its _P_<sub>0</sub> by a star at every lower level of _Q_ (or at every level of _Q_, if _t_=0). The result is a box of _w_, and each box of _w_ arises exactly once in this way. This means that _w_ has exactly \(\alpha_t\) boxes.

## Every leaf of order at least _t_ lies in exactly one box.

A leaf contributing to _w_ that chooses _P_<sub>0</sub> at the set _Z_ of levels is a leaf of a box of B_<sub>V</sub>_ if and only if it chooses _P_<sub>0</sub> at every level of _V_\\_F<sub>V</sub>_ and at no level of _Q_\\_V_ , that is,

\(V\backslash F_V\subseteq Z\subseteq V.\)

Furthermore, it is a leaf of exactly one of these boxes, namely, the one with its terms at the levels of _Q_\\_V_ . We will see in the following lemma that, for \(|Z|\le m-t\), exactly one _V_ satisfies this condition, namely _Z_ padded from the bottom. Thus every leaf of order at least _t_ lands in exactly one box.

**Lemma 27.** _Let Q be a set of m levels, and let_ \(0\le t\le m\)_. For every_ \(Z\subseteq Q\) _with_ \(|Z|\le m-t\)_, there is exactly one set_ \(V\subseteq Q\) _with_ |_V_|=_m-t and_

\(V\backslash F_V\subseteq Z\subseteq V,\)

_namely Z together with the m-t_-|_Z_| _lowest levels of Q_\\_Z._

_Proof._ Let \(V\subseteq Q\) with |_V_|=_m-t_ and \(Z\subseteq V\) . We show that \(V\backslash F_V\subseteq Z\) holds if and only if _V_\\_Z_ consists of the |_V_\\_Z_|=_m-t_-|_Z_| lowest levels of _Q_\\_Z_, which determines _V_ . If _V=Q_, then both conditions hold: _F<sub>V</sub>=Q_, so \(V\backslash F_V=\emptyset\subseteq Z\), and _V_\\_Z_ is all of _Q_\\_Z_. Otherwise, let \(\ell\) be the lowest level of _Q_\\_V_ . Then _F<sub>V</sub>_ consists of the levels of _Q_ below \(\ell\), so \(V\backslash F_V\subseteq Z\) says that every level of _V_\\_Z_ is below \(\ell\). Since _Q_\\_Z_ is the disjoint union of _V_\\_Z_ and _Q_\\_V_ , and every level of _Q_\\_V_ is at least \(\ell\), this holds if and only if _V_\\_Z_ consists of the lowest levels of _Q_\\_Z_.

**Lemma 28.** _Let w be an output string, with inner set Q. The leaves of order at least t contributing to w are exactly the leaves of the boxes in_ \(\bigcup_V\mathcal{B}_V\)_, the union over all_ \(V\subseteq Q\) _with_ |_V_|=_m-t, and each of them is a leaf of exactly one of these boxes. Hence_

\((X_QY_Q)[w]=\sum_{\tau\text{\textit{contributing to}}w\text{\textit{of order}}<t}\Phi_\tau(a)\Psi_\tau(b)+\sum_{V\subseteq Q|V|=m-t}\sum_{\pi\in\mathcal{B}_V}val(\pi),\)

_a sum of_ \(\sum_{d=0}^{t-1}\alpha_d\) _products and_ \(\alpha_t\) _values of boxes._

_Proof._ Every leaf of a box of B_<sub>V</sub>_ agrees with the private leaf of _w_ outside _Q_, so it contributes to _w_, and it chooses _P_<sub>0</sub> at most |_V_|=_m-t_ times, so its order is at least _t_. Conversely, a leaf \(\tau\) contributing to _w_, of order at least _t_, chooses _P_<sub>0</sub> at a set \(Z\subseteq Q\) of at most _m-t_ levels, and as we saw above, it is a leaf of a box of B_<sub>V</sub>_ if and only if \(V\backslash F_V\subseteq Z\subseteq V\) , and then of exactly one such box. By Lemma 27, exactly one _V_ satisfies this condition. The desired equation follows, since (_X<sub>Q</sub>Y<sub>Q</sub>_)\[_w_\] is the sum of the products at the leaves contributing to _w_. Finally, \(\alpha_d\) leaves of order _d_ contribute to _w_, and there are \(\genfrac(){pt}{2}{m}{m-t}\) sets _V_ with 9_<sup>t</sup>_ boxes each, i.e., \(\genfrac(){pt}{2}{m}{m-t}9^t=\genfrac(){pt}{2}{m}{t}9^t=\alpha_t\) boxes in all (as many as the leaves of order exactly _t_ contributing to _w_, although they cover its leaves of every order from _t_ to _m_).

