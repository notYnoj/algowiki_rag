If _r_=1, the list contains only _r_<sub>1</sub>=1 and the intermediate layers below are empty.

Partition _V(G_) into

\(V(G)\backslash U(P^{r_1}),U(P^{r_\ell})\backslash U(P^{r_{\ell+1}})(1\le\ell<j),U(P^r).\)

First color _U(P<sup>r</sup>_), assigning to each vertex a witness color of degree at most _D<sub>r</sub>_. Since \(|U(P^r)|\le n\), counting all possible neighbors gives at most _nD<sub>r</sub>_ monochromatic edges inside this part.

Next add the remaining layers in reverse order. For a vertex in \(U(P^{r_\ell})\backslash U(P^{r_{\ell+1}})\), use a witness color in \(P^{r_\ell}\) of degree at most \(D_{r_\ell}\). Every already colored vertex uses a color belonging to its palette at time \(r_\ell\), by nestedness. Hence this vertex creates at most \(D_{r_\ell}\) new monochromatic edges to previously colored vertices. Finally color _V(G_)\\_U(P_<sup>1</sup>) arbitrarily, charging at most _n_ edges per vertex.

Using (4), the total number of monochromatic edges is at most

\(nD_r+\sum_{t=1}^ra_tE_{t-1}.\) (5)

With _B_<sub>0</sub>=0, summation by parts gives

\(\sum_{t=1}^ra_tE_{t-1}=B_rE_{r-1}+\sum_{t=1}^{r-1}B_t(E_{t-1}-E_t)\)<br>
\(\le\alpha n\left(rE_{r-1}+\sum_{t=1}^{r-1}t(E_{t-1}-E_t)\right)\)<br>
\(=\alpha n\sum_{t=0}^{r-1}E_t\)<br>
\(=\alpha n\left(E_0+\sum_{t=1}^{r-1}E_t\right)\)<br>
\(\le\alpha n\left(n+kn\right)\)<br>
\(\le\alpha(k+1)n^2.\)

Together with \(nD_r\le kn^2/T\), we have reached the conclusion that there is a way to color the graph as required.

## 5 The trial coloring process

The trial coloring process calculates palettes _Q_<sup>0</sup>_,P_<sup>1</sup>_,Q_<sup>1</sup>_,P_<sup>2</sup>_,Q_<sup>2</sup>_,..._ and chooses pivots _f_<sub>1</sub>_,...,f<sub>T</sub>_ using colors _i_<sub>1</sub>_,...,i<sub>T</sub>_. Two features of this process are crucial. First, it only removes colors from palettes and never adds any. Second, it is dynamic: each operation is based on the current palette system, rather than on the initial graph alone.

Fix a total order on _V(G_) for tie-breaking. Given \(A\subseteq V(G)\) and prescribed colors \(i_1,i_2,\dots\in[k]\), the trial coloring process is defined as follows.

**Trial coloring process.**<br>
**Input:** A graph _G_=(_V,E_), an integer \(k\ge 1\), a set \(A\subseteq V\) , a round limit _T_, a prescribed color sequence \((i_t)_{t\ge 1}\), and a fixed total order on _V_ for tie-breaking.<br>
**Output:** The pivots, thresholds, cap palettes, and palette systems generated before the process stops or completes _T_ rounds.

