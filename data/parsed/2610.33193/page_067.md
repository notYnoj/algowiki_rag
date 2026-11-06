\(=\mathbb{E}_{y\sim f(\mathcal{D})}\left[\mathbb{E}_{x\sim\mathcal{D}_{|f^{-1}(y)}}[log(\mathrm{Pr}_\mathcal{D}[x]/\mathrm{Pr}_{f(\mathcal{D})}[y])+Q(x)]\right]\)<br>
\(=\mathbb{E}_{y\sim f(\mathcal{D})}\left[\mathbb{E}_{x\sim\mathcal{D}_{|f^{-1}(y)}}[log(\mathrm{Pr}_{\mathcal{D}_{|f^{-1}(y)}}[x])+Q(x)]\right]\)<br>
\(=\mathbb{E}_{y\sim f(\mathcal{D})}\left[\mathbb{E}_{x\sim\mathcal{D}_{|f^{-1}(y)}}[log(2^{Q(x)}\mathrm{Pr}_{\mathcal{D}_{|f^{-1}(y)}}[x])]\right].\)

Since \(\mathsf{EP}_g((\mathcal{G}_Q)_{|f^{-1}(y)})=\mathbb{E}_{x\sim(\mathcal{G}_Q)_{|f^{-1}(y)}}[log(2^{Q(x)}\mathrm{Pr}_{(\mathcal{G}_Q)_{|f^{-1}(y)}}[x])]\) we can rewrite Eq. (16) as:

\(\mathbb{E}_{y\sim f(\mathcal{D})}\left[\mathsf{EP}_g((\mathcal{G}_Q)_{|f^{-1}(y)})+\mathbb{E}_{x\sim\mathcal{D}_{|f^{-1}(y)}}[log(2^{Q(x)}\mathrm{Pr}_{\mathcal{D}_{|f^{-1}(y)}}[x])]-\mathbb{E}_{x\sim(\mathcal{G}_Q)_{|f^{-1}(y)}}[log(2^{Q(x)}\mathrm{Pr}_{(\mathcal{G}_Q)_{|f^{-1}(y)}}[x])]\right]\) (17)

\(=\mathbb{E}_{y\sim f(\mathcal{D})}\left[\mathsf{EP}_g((\mathcal{G}_Q)_{|f^{-1}(y)})\right]\)<br>
\(+\mathbb{E}_{y\sim f(\mathcal{D})}\left[\mathbb{E}_{x\sim\mathcal{D}_{|f^{-1}(y)}}[log(2^{Q(x)}\mathrm{Pr}_{\mathcal{D}_{|f^{-1}(y)}}[x])]-\mathbb{E}_{x\sim(\mathcal{G}_Q)_{|f^{-1}(y)}}[log(2^{Q(x)}\mathrm{Pr}_{(\mathcal{G}_Q)_{|f^{-1}(y)}}[x])]\right].\)

Now by the definition of (G_<sub>Q</sub>_)<sub>|_f_<sup>-1</sup>(_y_)</sub>, for every \(x\in\mathrm{supp}((\mathcal{G}_Q)_{|f^{-1}(y)})\), \(2^{Q(x)}\mathrm{Pr}_{(\mathcal{G}_Q)_{|f^{-1}(y)}}[x]=1/\sum_{x^\prime\in f^{-1}(y)}2^{-Q(x^\prime)}\). This implies that this quantity has the same value for every element of the set _f_<sup>-1</sup>(_y_). Therefore, any convex combination over the terms with the same values of _y_ will give the same value. This lets us rewrite Eq. (17) as:

\(=\mathbb{E}_{y\sim f(\mathcal{D})}[\mathsf{EP}_g((\mathcal{G}_Q)_{|f^{-1}(y)})]+\mathbb{E}_{x\sim\mathcal{D}}[log(2^{Q(x)}\mathrm{Pr}_{\mathcal{D}_{|f^{-1}(f(x))}}[x])-log(2^{Q(x)}\mathrm{Pr}_{(\mathcal{G}_Q)_{|f^{-1}(f(x))}}[x])]\)<br>
\(=\mathbb{E}_{y\sim f(\mathcal{D})}[\mathsf{EP}_g((\mathcal{G}_Q)_{|f^{-1}(y)})]+\mathbb{E}_{x\sim\mathcal{D}}[log(\mathrm{Pr}_{\mathcal{D}_{|f^{-1}(f(x))}}[x]/\mathrm{Pr}_{(\mathcal{G}_Q)_{|f^{-1}(f(x))}}[x])]\)<br>
\(=\mathbb{E}_{y\sim f(\mathcal{D})}[\mathsf{EP}_g((\mathcal{G}_Q)_{|f^{-1}(y)})]+\mathbb{E}_{x\sim\mathcal{D}}\left[log\left(\frac{\mathrm{Pr}_\mathcal{D}[x]\mathrm{Pr}_{f(\mathcal{D}^*)}[f(x)]}{\mathrm{Pr}_{f(\mathcal{D})}[f(x)]\mathrm{Pr}_{\mathcal{D}^*}[x]}\right)\right]\)<br>
\(=\mathbb{E}_{y\sim f(\mathcal{D})}[\mathsf{EP}_g((\mathcal{G}_Q)_{|f^{-1}(y)})]+D_\mathrm{KL}(\mathcal{D}||\mathcal{D}^*)-D_\mathrm{KL}(f(\mathcal{D})||f(\mathcal{D}^*))\)

as desired.

There are actually some subtlety in our statement of Proposition C.3 that becomes obvious with the language of heat functions. In particular, we cannot always take D<sup>∗</sup> to be the distribution over inputs that minimizes the entropy production. Due to Corollary C.2, we know that such a D<sup>∗</sup> would only have support on _y_ that minimize EP_<sub>g</sub>_((G_<sub>Q</sub>_)<sub>|_f_<sup>-1</sup>(_y_)</sub>), and thus for many choices of D we will not have that \(\mathrm{supp}(f(\mathcal{D}))\subseteq\mathrm{supp}(f(\mathcal{D}^*))\). Proposition C.3 actually has a nice intuitive interpretation in terms of heat functions. The term _D_<sub>KL</sub>(D||D<sup>∗</sup>)-_D_<sub>KL</sub>(_f_(D)||_f_(D<sup>∗</sup>)) corresponds to how well suited _Q_ is for the input distribution D while E<sub>_y∼f_(D))</sub>\[EP_<sub>g</sub>_((G_<sub>Q</sub>_)<sub>|_f_<sup>-1</sup>(_y_)</sub>)\] corresponds to how close _Q_ is to being optimal on the best possible distributions over the preimage of each _y_.

## D Entropy production from modularity

Heat functions only consider the inputs to a specific gate to determine the corresponding heat release. Thus, they do not account for correlations between the inputs to this gate and the rest<tbc>

