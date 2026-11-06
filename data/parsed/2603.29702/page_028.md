**Edges** There is an edge from \(\langle x,y\rangle\) to \(\langle x+\mathcal{B}_x,y'\rangle\) such that \(|y'-y|\le\mathcal{B}_x\) with weight \(\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\) equal to the shortest \(\langle x,y\rangle\)-\(\langle x+\mathcal{B}_x,y'\rangle\) path<sup>22</sup> in the Rotated Edit Distance Grid Graph.

**Objective** Find the shortest path from \(\langle 0,n_X\rangle\) to \(\langle n_X+n_Y,n_Y\rangle\).

**Lemma 5.12** (Restated)**.** _Suppose that for every edge from_ \(\langle x,y\rangle\) _to_ \(\langle x+\mathcal{B}_x,y'\rangle\)_, we are given ("for free") a constant-factor approximation_ \(\mathrm{apprew}[x,y,x+\mathcal{B}_x,y']\) _of the edge weight_ \(\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\) _(i.e.,_ \(\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\le\mathrm{apprew}[x,y,x+\mathcal{B}_x,y']\le 4\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\)_). To know the exact edge weight requires an edge-weight query. Then we can approximate the problem in Definition 5.6 in o(n_<sup>0.1</sup>) _time with high prob ability using_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01(n)}\right)}\) _edge-weight queries, up to a multiplicative factor of_ (1+_o_(1))_, assuming that the answer is at least n/_2<sup>_o_(log<sup>0.009</sup>(_n_)</sup>)</sup>.

We first revisit the naïve recursion scheme we briefly talked about in Section 5.2, but in the context of the sparsified grid graph. Let \(M:=2^{\left\lfloor\mathrm{log}(\mathrm{log}^{0.109}(n))\right\rfloor}=\Theta(\mathrm{log}^{0.109}(n))\) and \(S:=3\cdot\left\lfloor\mathrm{log}_M(n^{0.01})\right\rfloor\). For each _scale_ \(s\in[S]\cup\{0\}\), we consider the partition of \[_n_\] into disjoint intervals of length _I<sub>s</sub>_:=_n/M_<sup>_S-s_</sup>, and we say that each interval in this partition is a scale-_s_ interval. Suppose we want to compute the length of the shortest \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path where (_l,r_\] is a scale-_s_ interval, denoted by ans\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\]. If _s_=0, we obtain ans\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] by querying the edge weight \(\mathrm{ew}[l,y_l,r,y_r]\).

If _s\>_0, for \(0\le i\le M\), let \(m_i:=l+i\cdot\frac{r-l}{M}\) be the _i_-th anchor. Then ans\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] can be found via minimizing over every anchor path defined by some sequence <o>_Y_</o>=(<o>_y_</o><sub>i</sub>) that satisfies

• <o>_y_</o><sub>0</sub>=_y<sub>l</sub>_ and <o>_y_</o><sub>M</sub>=_y<sub>r</sub>_;<tbc>

• For \(1\le i\le M\), \(\left|\overline{y_i}-\overline{y_{i-1}}\right|\le\frac{r-l}{M}\) ;<tbc>

• For \(0\le i\le M\), \(\langle m_i,\overline{y_i}\rangle\) exists in the Sparsified Grid Graph.

The recursion is as follows:

\(\mathrm{ans}[l,y_l,r,y_r]:=\left\{\begin{array}{ c c }
\mathrm{ew}[l,y_l,r,y_r], & \text{if}s=0 \\
\mathrm{min}_{\widehat{Y}\in\text{\unknown}}\sum_{i=1}^M\mathrm{ans}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i], & \text{otherwise}
\end{array}\right..\)

Unfortunately, the naïve recursion scheme will eventually visit every possible (_l,y<sub>l</sub>,r,y<sub>r</sub>_), and it will query every edge weight. Thus the total number of edge-weight queries is \(O(n^2\phi_y^2/\mathcal{B}_x^2)\). Our final algorithm will shave a \(2^{\mathrm{log}^{\Omega(1)}(n)}\) factor off this query count.

## 6.1 Regular Paths

We first review the high-level idea for estimating the shortest path on a sparsified grid graph. The bound on tree total deviation roughly tells us that a path should resemble a "straight line" on an average interval on an average scale. Thus if we sample a small fraction of scales to be _active_, and force the path to be a straight line on these active scales, we should not lose too much precision.

Let \(\widetilde{S}\subset[S]\) be a subset of active scales (other scales are _passive_), we define the notion of \(\widetilde{S}\)-regularity:<tbc>

<sup>22</sup>Note that both coordinates (and in fact all coordinates involved in our algorithm) are always even, meaning that these vertices are never created from splitting diagonal edges in the original grid.

