an existing neighbor of _s_ closer to the candidate point. We prove that when the query point is not in D, the RNG’s strategy makes the lower bound of the possibility of achieving monotonic search only 50%. We demonstrate it in combination of Figure 2. Point _A_ is the current node which is selecting neighbors. Point _C_ is point A ’s one of the existing neighbors, point _B_ is the candidate neighbor and point _Q_ is the query point. At the same time, point _B_ is the nearest neighbor of _Q_. According to RNG’s strategy, point _A_ will not connect point _B_ because \(\delta(C,B)<\delta(A,B)\). According to the definition of monotonic search, the condition to achieving monotonic search from point _A_ is \(\left|\overrightarrow{CQ}\right|<\left|\overrightarrow{AQ}\right|\). If point \(Q\in\mathcal{D}\), then point _B_ equals point _Q_. There must be \(\left|\overrightarrow{CQ}\right|<\left|\overrightarrow{AQ}\right|\), the possibility is 100%. However, if point \(Q\notin\mathcal{D}\) , we can see that

\(\left|\overrightarrow{AQ}\right|>\left|\overrightarrow{CQ}\right|\)<br>
\(\Pi_\overrightarrow{AC}\overrightarrow{AQ}>\frac{1}{2}\left|\overrightarrow{AC}\right|\)<br>
\(\Pi_\overrightarrow{AC}\overrightarrow{AB}+\Pi_\overrightarrow{AC}\overrightarrow{BQ}>\frac{1}{2}\left|\overrightarrow{AC}\right|\)<br>
\(\Pi_\overrightarrow{AC}\overrightarrow{BQ}>\frac{1}{2}\left|\overrightarrow{AC}\right|-\Pi_\overrightarrow{AC}\overrightarrow{AB}\) (1)

The \(\Pi_\overrightarrow{AC}\overrightarrow{AQ}\) represents the projection of the vector \(\overrightarrow{AQ}\) on the vector \(\overrightarrow{AC}\). For convenience for discussion, we set that \(l=\left|\overrightarrow{AB}\right|\), \(\alpha=\angle CAB\), \(\theta=\angle ABC\). Inequation (1) can be represented as<tbc>

\(\Pi_\overrightarrow{AC}\overrightarrow{BQ}>\frac{lsin\theta}{2sin(\alpha+\theta)}-lcos\alpha\)

\(\Pi_\overrightarrow{AC}\overrightarrow{BQ}>-\frac{lsin(2\alpha+\theta)}{2sin(\alpha+\theta)}\) (2)

<tbc>Because \(0<\left|\overrightarrow{AC}\right|,\left|\overrightarrow{CB}\right|\le\left|\overrightarrow{AB}\right|\), there is \(0\le\alpha,\theta\le\pi-\alpha-\theta\), and \(0\le\alpha+\theta\le 2\alpha+\theta\le\pi\). It is easy to show that\(-\frac{lsin(2\alpha+\theta)}{2sin(\alpha+\theta)}\le 0\). That is to say, inequation (2) holds as long as the angle between \(\overrightarrow{AC}\) and \(\overrightarrow{BQ}\le 90^\circ\). According to the symmetry of the hyper sphere, the possibility is not less than 0.5 and equal to 0.5 if \(2\alpha+\theta=\pi\). Therefore, the lower bound is 50%.

