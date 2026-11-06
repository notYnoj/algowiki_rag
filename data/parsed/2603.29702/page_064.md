## 7.3.4 Our Can be computed Efficiently

Finally we show that our algorithm is efficient:

**Lemma 7.12** (Restated)**.** _With probability_ 1-_o_(1)_, to compute_ est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>_\]_, the running time is at most o(n_<sup>0.09</sup>)_, and the total number of edge weight queries is at most_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\).

_Proof._ For the running time, the total number of (_l,y<sub>l</sub>,r,y<sub>r</sub>_) is

\(\underbrace{(n/\mathcal{B}_x)}_l\cdot\underbrace{(n/\mathcal{B}_x)}_r\cdot\underbrace{(n\phi_y/\mathcal{B}_x)}_{y_l}\cdot\underbrace{(n\phi_y/\mathcal{B}_x)}_{y_r}=n^4\cdot\phi_y^2/\mathcal{B}_x^4=o(n^{0.045}).\)

For each (_l,y<sub>l</sub>,r,y<sub>r</sub>_) with (_l,r_\] on scale _s_, the bottleneck for computing est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] is to compute the longest path in the Scale-(_s_-1) Sparsified Grid Graph, which takes linear time in the number of edges. This number of edges is no more than the total number of (_l,y<sub>l</sub>,r,y<sub>r</sub>_)’s which is _o(n_<sup>0.045</sup>). The overall running time is therefore at most _o(n_<sup>0.09</sup>).

For query complexity, for each edge from \(\langle x,y\rangle\) to \(\langle x+\mathcal{B}_x,y'\rangle\), the edge is queried if every interval \((l,r]\supset(x,x+\mathcal{B}_x]\) on an active scale is sub-sampled, which happens with probability 1/2 per active scale independently. Thus the probability that an edge "survives" sub-sampling is \(2^{-\left|\widetilde{S}\right|}\). With probability 1-_o_(1), \(\left|\widetilde{S}\right|=\Omega(S^{0.02})\), and the number of queries is at most \(2^{-\Omega(S^{0.02})}<2^{-\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) times the total number of edges. The total number of edges is (notice that \(|y-y'|\le\mathcal{B}_x\))

\(\underbrace{(n/\mathcal{B}_x)}_x\cdot\underbrace{(n\phi_y/\mathcal{B}_x)}_y\cdot\underbrace{\phi_y}_{y^\prime}=\frac{n^2\phi_y^2}{\mathcal{B}_x^2}\)

And the total number of queries is \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\).

## 7.3.5 Proof of Claim 7.8

Finally, we give the missing proof of Claim 7.8.

**Claim 7.8** (Restated)**.** _Let A_=(_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>M</sub>_) _be a sequence of non-negative numbers. Suppose that we only know A<sub>I</sub>, that is, the sub-sequence_ \((a_i)_{i\in I}\) _for a uniformly randomly chosen subset_ \(I\subset[M]\) _of M/_2 _indices._

_We obtain a non-negative estimate EstSum(A<sub>I</sub>_) _for the sum_ \(\sum_{i=1}^Ma_i\) _in the following way:_

1. _Estimate the mean of A using_ \(\widetilde{A}:=\sum_{i\in I}a_i/\left(\frac{M}{2}\right)\);<tbc>

_2._ _Estimate the sum of A by clipping outliers down:_ \(EstSum(A_I):=2\sum_{i\in I}\mathrm{min}\left(a_i,2\mathrm{log}^{0.02}(n)\widetilde{A}\right)\).

_The pseudocode for computing EstSum(A<sub>I</sub>_) _is shown in Algorithm 2._

_Then with probability_ \(1-\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\)_, the estimate we obtain satisfies_

**Upper bound** \(EstSum(A_I)\le\left(1+O\left(1/\mathrm{log}^{0.02}(n)\right)\right)\sum_{i=1}^Ma_i\);

