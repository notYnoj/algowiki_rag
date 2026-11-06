The key to efficiency is to use a _sub-sampling_ technique for active scales. We first show a naive attempt that can guarantee a small additive error (we later improve it to also obtain a bound on the multiplicative error). Notice that if \(s\in\widetilde{S}\), since no overfitting can happen when the path is fixed, we can just sample half of these values and double our sum from the sample. Thus, for every scale-_s_ interval (_l,r_\], we first uniformly randomly sample _M_ 0-1 variables \(\eta_{l,r,1\dots M}\) containing exactly _M/_21’s. We use the following scheme:

\(\mathrm{est}^*[l,y_l,r,y_r]:=\left\{\begin{array}{ c c }
\mathrm{ew}[l,y_l,r,y_r], & \text{if}s=0 \\
\mathrm{min}_{\widehat{Y}\in\unknown}\sum_{i=1}^M\mathrm{est}^*[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i], & \text{if}s\notin\widetilde{S} \\
2\sum_{i=1}^M\eta_{l,r,i}\mathrm{est}^*[m_{i-1},\overline{y_i},m_i,\overline{y_i}], & \text{if}s\in\widetilde{S}
\end{array}\right.,\) (21)

Note that for every active scale, half of the sub-intervals (_m_<sub>_i_-1</sub>_,m<sub>i</sub>_\] for which \(\eta_{l,r,i}=0\) get discarded. Over \(\left|\widetilde{S}\right|\) active scales, only \(2^{-\left|\widetilde{S}\right|}\) fraction of the intervals remain, which is a significant speed-up.

Unfortunately, the scheme with (21) is not enough for a small multiplicative error, as \(\mathrm{est}^*[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]\) may be imbalanced over \(1\le i\le M\). In the most extreme example, if \(\mathrm{est}^*[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]\neq 0\) for only a single _outlier i_, then (21) either gets us an estimate that is 0 or an estimate that is twice the actual value, depending on the value of \(\eta_{l,r,i}\).

Due to the bound on tree total deviation, the weight distribution on the shortest path should intuitively not be imbalanced everywhere and there are not too many outliers in total. Thus even if we "give up" when we detect outliers, there should not be too much error. We first need to detect outliers. Recall that for each edge from \(\langle x,y\rangle\) to \(\langle x+\mathcal{B}_x,y'\rangle\), we are given a constant factor approximation \(\mathrm{aprew}[x,y,x+\mathcal{B}_x,y']\) of the edge weight \(\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\). We can (detailed later) use this to obtain a constant-factor approximation \(\mathrm{appr}[l',y'_{l^\prime},r',y'_{r^\prime}]\) of the length of the shortest \(\langle l',y'_{l^\prime}\rangle\)-\(\langle r',y'_{r^\prime}\rangle\widetilde{S}\)-regular path for every valid \((l',y'_{l^\prime},r',y'_{r^\prime})\) where \((l',r']\) is a recursion interval. We now describe how we can obtain our estimate:

1. We detect outliers by checking if \(\mathrm{max}_{1\le i\le M}\mathrm{appr}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]>\frac{\mathrm{appr}[l,y_l,r,y_r]}{M}\mathrm{loglog}(n)\).<tbc>

2. If \(\mathrm{max}_{1\le i\le M}\mathrm{appr}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]\le\frac{\mathrm{appr}[l,y_l,r,y_r]}{M}\mathrm{loglog}(n)\), we let<tbc>

<tbc>\(\mathrm{est}[l,y_l,r,y_r]:=\mathrm{min}\left(2\sum_{i=1}^M\eta_{l,r,i}\mathrm{est}[m_{i-1},\overline{y_i},m_i,\overline{y_i}],\mathrm{appr}[l,y_l,r,y_r]\right).\)<tbc>

<tbc>Namely we use the same formula as in (21), but clamp est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] to at most appr\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] to make sure that est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] does not over-estimate the answer worse than the constant-factor approximation does;<tbc>

3. If \(\mathrm{max}_{1\le i\le M}\mathrm{appr}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]>\frac{\mathrm{appr}[l,y_l,r,y_r]}{M}\mathrm{loglog}(n)\), we simply "give up" and let est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\]:=appr\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\], which still only gives us a multiplicative error of (1+_O_(1)).

<tbc>Given a path \(p'\) from column _l_ to column _r_, we let \(W(p')\) be the following sequence capturing the "weight distribution" of \(p'\):

\(W(p')=\left(w(p'(l,l+\mathcal{B}_x]),w(p'(l+\mathcal{B}_x,l+2\mathcal{B}_x]),\dots,w(p'(r-\mathcal{B}_x,r])\right)\)

We later show that this procedure satisfies the following claim:

