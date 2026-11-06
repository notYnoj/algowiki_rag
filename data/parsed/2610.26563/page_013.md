**Definition 11** (Weight vector)**.** _Define_ \(w\in\mathbb{C}^{n+2}\) _by_

\(w_i=\left\{\begin{array}{ c c }
1 & \text{\textit{if}}0\le i\le n \\
-(n+1)^{1/3} & \text{\textit{if}}i=n+1
\end{array}\right..\) (55)

The efficacy of the weighting follows from the following claim.

**Claim 1.** _The weight vector w and padded centering embedding_ \(\nu\circ\mu\) _satisfy the following properties. For any_ \(x,y\in\mathbb{C}^n\),

1. _metric preservation:_ \(\sum_iw_i\nu(\mu(x))_i\nu(\mu(y))_i=x^Ty\),<tbc>

_2._ _linear reducibility annihilation:_ \(\sum_iw_i^2\nu(\mu(x))_i=0\),<tbc>

_3._ _replication annihilation:_ \(\sum_iw_i^3=0\).

_Proof._ Since _w<sub>i</sub>_=1 for \(0\le i\le n\) and \(\nu(\mu(x))_{n+1}=0\),

\(\sum_{i=0}^{n+1}w_i\nu(\mu(x))_i\nu(\mu(y))_i=\sum_{i=0}^n(Qx)_i(Qy)_i=x^TQ^TQy=x^Ty.\) (56)

Since _Q_ maps into \(1_{n+1}^\perp\),

\(\sum_{i=0}^{n+1}w_i^2\nu(\mu(x))_i=\sum_{i=0}^n(Qx)_i=0.\) (57)

Finally,

\(\sum_{i=0}^{n+1}w_i^3=\sum_{i=0}^n1-(n+1)=0.\) (58)

Hence, to eliminate both linearly reducible and replicated terms, we aggregate weighted, padded, and centered tensors.

**Definition 12** (Weighting and the combined embedding)**.** _Let w be the weight vector from Definition 11. For finite coordinate sets_ \(S\subseteq F\)_, define_<tbc>

\(\Omega_{S,F}:(\mathbb{C}^{n+2})^{\otimes|F\backslash S|}\longrightarrow(\mathbb{C}^{n+2})^{\otimes|F|}\)

<tbc>_by_

\(\Omega_{S,F}(T)_\mathbf{i}=T_{\mathbf{i}_{|F\backslash S}}\prod_{r\in S}w_{i_r},\mathbf{i}\in\unknown 0,n+1\unknown^F.\) (59)

_The input modes are indexed by F_\\_S, and the output modes by F, both in increasing order. The map inserts the coordinates in S with the corresponding weights. Define the combined embedding by_

\(\Phi_{S,F}=\Omega_{S,F}\circ(\nu\circ\mu)^{\otimes|F\backslash S|}.\) (60)

_It centers and pads the retained modes, then inserts the weighted coordinates. For its transpose, write_ \(k=|F\backslash S|\) _and_ \(F\backslash S=\{r_0<\cdots<r_{k-1}\}\)_. With respect to the algebraic pairing,_

\(\left(\Phi_{S,F}^\star(A)\right)_\unknown=\sum_{\mathbf{i}\in\unknown 0,n+1\unknown^F}A_\mathbf{i}\left(\prod_{r\in S}w_{i_r}\right)\left(\prod_{j=0}^{k-1}\nu(\mu(e_{\alpha_j}))_{i_{r_j}}\right),\unknown\in\unknown 0,n-1\unknown^k.\) (61)

_Here e_<sub>0</sub>_,...,e_<sub>_n_-1</sub> _are the standard basis vectors of_ C_<sup>n</sup>._

