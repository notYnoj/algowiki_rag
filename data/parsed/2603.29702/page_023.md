bf\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\]. If _s_=0, we calculate bf\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] using brute force. Suppose that _s\>_0. For \(0\le i\le M\) we say that the _i_-th _anchor_ is \(m_i:=l+i\cdot\frac{r-l}{M}\) . Every sequence \(\widehat{Y}=(y_l=\widehat{y}_0,\widehat{y}_1,\dots,\widehat{y}_M=y_r)\) where for \(1\le i\le M\), \(|\widehat{y}_i-\widehat{y}_{i-1}|\le\frac{r-l}{M}\) defines an _anchor path_ visiting vertices \((\langle m_i,\widehat{y}_i\rangle)_i\). bf\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] can be found via minimizing over the anchor paths:

\(\mathrm{bf}[l,y_l,r,y_r]=\mathrm{min}_{\widehat{Y}\in\text{\textbf{Fig.}}}\sum_{i=1}^M\mathrm{bf}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i].\)

The idea towards improving the efficiency of the brute force idea above is to only consider a small subset of the possible anchor paths, at the cost of some error. If we incur an additive error of \(I_s/\phi\) for every recursion interval where length-relative factor \(\phi=\omega(\mathrm{log}(n))\), we should only incur an additive error of \(n/\omega(\mathrm{log}n)\) per scale and the total additive error across _S=O_(log(_n_)) scales is \(n/\omega(1)\). Consider the following "hierarchically-sparsified" grid graph:

**Definition 5.6** (Sparsified Edit Distance Grid Graph)**.** The Sparsified Edit Distance Grid Graph is defined given the following parameters:

• Rounding threshold for columns: \(\mathcal{B}_x:=n/M^S=\widetilde{\Theta}(n^{0.99})\);<tbc>

• Length-relative rounding factor for rows: \(\phi_y:=2^{\lfloor\mathrm{log}^{0.009}(n)\rfloor}\).

**Vertices** We only consider vertices \(\langle x,y\rangle\) such that

• B_<sub>x</sub>|x_;<tbc>

• Let \(s\in[S]\cup\{0\}\) be the largest scale such that _I<sub>s</sub>|x_. Then \((I_s/\phi_y)|y\).

**Edges** There is an edge from \(\langle x,y\rangle\) to \(\langle x+\mathcal{B}_x,y'\rangle\) such that \(|y'-y|\le\mathcal{B}_x\) with weight \(\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\) equal to the shortest \(\langle x,y\rangle\)-\(\langle x+\mathcal{B}_x,y'\rangle\) path<sup>18</sup> in the Rotated Edit Distance Grid Graph.

**Objective** Find the shortest path from \(\langle 0,n_X\rangle\) to \(\langle n_X+n_Y,n_Y\rangle\).

We can identically define the Sparsified Grid Graph for LCS:

**Definition 5.7** (Sparsified LCS Grid Graph)**.** The Sparsified LCS Grid Graph is defined given the following parameters:

• Rounding threshold for columns: \(\mathcal{B}_x:=n/M^S=\widetilde{\Theta}(n^{0.99})\);<tbc>

• Length-relative rounding factor for rows: \(\phi_y:=2^{\lfloor\mathrm{log}^{0.009}(n)\rfloor}\).

**Vertices** We only consider vertices \(\langle x,y\rangle\) such that

• B_<sub>x</sub>|x_;<tbc>

• Let \(s\in[S]\cup\{0\}\) be the largest scale such that _I<sub>s</sub>|x_. Then \((I_s/\phi_y)|y\).

**Edges** There is an edge from \(\langle x,y\rangle\) to \(\langle x+\mathcal{B}_x,y'\rangle\) such that \(|y'-y|\le\mathcal{B}_x\) with weight \(\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\) equal to the longest \(\langle x,y\rangle\)-\(\langle x+\mathcal{B}_x,y'\rangle\) path in the Rotated LCS Grid Graph.

<sup>18</sup>Note that both coordinates (and in fact all coordinates involved in our algorithm) are always even, meaning that these vertices are never created from splitting diagonal edges in the original grid.

