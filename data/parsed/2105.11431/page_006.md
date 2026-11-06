positions. Finally, since we condition on _B_, there are \(3(s(t)\pm\varepsilon(t))\pm O(1)=3s(t)\pm 4\varepsilon(t)\) positions that, if chosen at time _t_+1, make (_r,c_) unavailable. Thus:

\(\mathbb{P}\left[(r,c)\notin\mathcal{A}(t+1)|\tau>t,B\right]=\frac{3s(t)\pm 4\varepsilon(t)}{n^2p(t)^4\pm 3np(t)\varepsilon(t)}=\frac{3}{np(t)}\left(1\pm\frac{5\varepsilon(t)}{np(t)^3}\right).\)

Therefore

\(\mathbb{E}\left[S_\ell(t+1)-S_\ell(t)|\tau>t,B\right]=-S_\ell(t)\frac{3}{np(t)}\left(1\pm\frac{5\varepsilon(t)}{np(t)^3}\right)\)<br>
\(=^{\tau\ge t}-(s(t)\pm\varepsilon(t))\frac{3}{np(t)}\left(1\pm\frac{5\varepsilon(t)}{np(t)^3}\right)\)<br>
\(=-3p(t)^2\left(1\pm\frac{7\varepsilon(t)}{np(t)^3}\right)=-3p(t)^2\pm\frac{21\varepsilon(t)}{np(t)}.\)

We also observe that

\(s(t+1)-s(t)=-\frac{3np(t)^2}{n}\pm\frac{6}{n}=-3p(t)^2\pm\frac{\varepsilon(t)}{np(t)}\)

and that

\(\frac{1}{2}\left(\varepsilon(t+1)-\varepsilon(t)\right)=\frac{50\varepsilon(t)}{2np(t)}\pm\frac{\varepsilon(t)}{np(t)}.\)

Therefore:

\(\mathbb{E}\left[S_\ell^+(t+1)-S_\ell^+(t)|\mathcal{F}_t\right]=-3p(t)^2+3p(t)^2-\frac{50\varepsilon(t)}{2np(t)}\pm\frac{23\varepsilon(t)}{np(t)}\le 0\)

and

\(\mathbb{E}\left[S_\ell^-(t+1)-S_\ell^-(t)|\mathcal{F}_t\right]=3p(t)^2-3p(t)^2-\frac{50\varepsilon(t)}{2np(t)}\pm\frac{23\varepsilon(t)}{np(t)}\le 0.\)

We conclude that \(\{S_\ell^+(t)\}_{t=0}^T\) and \(\{S_\ell^-(t)\}_{t=0}^T\) are supermartingales with maximal one- step change _O_(1).

We now apply Theorem 3.2 with \(\lambda=\varepsilon(t)/2\) to conclude that for every \(0\le t\le T\):

\(\mathbb{P}\left[S_\ell^+(t)\ge S_\ell^+(0)+\varepsilon(t)/2\right]\le exp\left(-\Omega\left(\frac{n^{1.02}}{np(t)^{100}}\right)\right)\)<br>
\(\le exp\left(-\Omega\left(\frac{n^{1.02}}{np(T)^{100}}\right)\right)=exp\left(-\Omega\left(n^{0.01}\right)\right).\)

Similarly:

\(\mathbb{P}\left[S_\ell^-(t)\ge S_\ell^-(0)+\varepsilon(t)/2\right]\le exp\left(-\Omega\left(n^{0.01}\right)\right).\)

Hence:

\(\mathbb{P}\left[\tau\le T\right]\le exp\left(-\Omega\left(n^{0.01}\right)\right),\)

completing the proof. □

