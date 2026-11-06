_Proof._ For the running time, the total number of (_l,y<sub>l</sub>,r,y<sub>r</sub>_) is

\(\underbrace{(n/\mathcal{B}_x)}_l\cdot\underbrace{(n/\mathcal{B}_x)}_r\cdot\underbrace{(n\phi_y/\mathcal{B}_x)}_{y_l}\cdot\underbrace{(n\phi_y/\mathcal{B}_x)}_{y_r}=n^4\cdot\phi_y^2/\mathcal{B}_x^4=o(n^{0.045}).\)

For each (_l,y<sub>l</sub>,r,y<sub>r</sub>_) with (_l,r_\] on scale _s_, the bottleneck for computing est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] is to compute the shortest path in the Scale-(_s_-1) Sparsified Grid Graph, which takes linear time in the number of edges. This number of edges is no more than the total number of (_l,y<sub>l</sub>,r,y<sub>r</sub>_)’s which is _o(n_<sup>0.045</sup>). The overall running time is therefore at most _o(n_<sup>0.09</sup>). We can do a similar analysis on the computation of the appr values and also obtain a running time of _o(n_<sup>0.09</sup>).

For query complexity, for each edge from \(\langle x,y\rangle\) to \(\langle x+\mathcal{B}_x,y'\rangle\), the edge is queried if every interval \((l,r]\supset(x,x+\mathcal{B}_x]\) on an active scale is sub-sampled, which happens with probability 1/2 per active scale independently. Thus the probability that an edge "survives" sub-sampling is \(2^{-\left|\widetilde{S}\right|}\). With probability 1-_o_(1), \(\left|\widetilde{S}\right|=\Omega(S^{0.02})\), and the number of queries is at most \(2^{-\Omega(S^{0.02})}<2^{-\Omega\left(log^{0.01}(n)\right)}\) times the total number of edges. The total number of edges is (notice that \(|y-y'|\le\mathcal{B}_x\))

\(\underbrace{(n/\mathcal{B}_x)}_x\cdot\underbrace{(n\phi_y/\mathcal{B}_x)}_y\cdot\underbrace{\phi_y}_{y^\prime}=\frac{n^2\phi_y^2}{\mathcal{B}_x^2}\)

And the total number of queries is \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(log^{0.01}(n)\right)}\).

## 6.3.5 Proof of Claim 6.7

Finally, we give the missing proof of Claim 6.7.

**Claim 6.7** (Restated)**.** _For_ est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] _where_ (_l,r_\] _is a scale-s interval such that_ \(s\in\widetilde{S}\)_. Let <o>p</o>_<sub>_l,r_</sub> _be the shortest_ \(\widetilde{S}\)_-regular_ \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) _path. We have the following:_

**We only give up when weight distribution is imbalanced** _if_ \(max_{1\le i\le M}appr[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]=\omega\left(\frac{appr[l,y_l,r,y_r]}{M}\right)\)_, then_ \(\mathrm{TD}_M(W(\overline{p_{l,r}}))=\omega\left(\frac{w(\overline{p_{l,r}})}{M}\right)\).

**If we do not give up, we obtain a good estimate** _if_ \(max_{1\le i\le M}appr[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]\le\frac{appr[l,y_l,r,y_r]}{M}loglog(n)\)_, then with probability_ \(1-\mathrm{exp}\left(-\omega\left(log^{0.02}(n)\right)\right)\), \(\left(2\sum_{i=1}^M\eta_{l,r,i}\mathrm{est}[m_{i-1},\overline{y_i},m_i,\overline{y_i}]\right)\) _approximates_ \(\left(\sum_{i=1}^M\mathrm{est}[m_{i-1},\overline{y_i},m_i,\overline{y_i}]\right)\) _with additive error o_ \(\left(\frac{w(\overline{p_{l,r}})}{\mathrm{log}^{0.02}(n)}\right)\).

_Proof._ For (_m_<sub>_i_-1</sub>_,m<sub>i</sub>_\] we write <o>_p_</o><sub>_m<sub>i</sub>_-1_,m<sub>i</sub>_</sub> as a shorthand for the part of <o>_p_</o><sub>_l,r_</sub> from column _m_<sub>_i_-1</sub> to column _m<sub>i</sub>_ (i.e., <o>_p_</o><sub>_l,r_</sub>(_m_<sub>_i_-1</sub>_,m<sub>i</sub>_\]).

## We only give up when weight distribution is imbalanced

Since \(appr[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]=\Theta(w(\overline{p_{m_{i-1},m_i}}))\) and \(appr[l,y_l,r,y_r]=\Theta(w(\overline{p_{l,r}}))\), if we have \(max_{1\le i\le M}appr[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]=\omega\left(\frac{appr[l,y_l,r,y_r]}{M}\right)\), then we<tbc>

