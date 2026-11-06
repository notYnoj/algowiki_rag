<tbc>expectation is

\(\mathbb{E}\left[\frac{\mathrm{cut}(\sigma(\epsilon))}{|E|}\right]=\frac{1}{|E|}\sum_{(u,v)\in E}\mathrm{Prob}\big[\sigma_u\neq\sigma_v\big]=c_\mathrm{VIRAL}(p).\) (8)

Now, a random variable is at least as large as its mean with positive probability and, since there are finitely many seed configurations, some \(\epsilon^*\) satisfies \(\mathrm{cut}(\sigma(\epsilon^*))/|E|\ge c_\mathrm{VIRAL}(p)\), and the maximum cut is at least as large, i.e.<tbc>

\(\frac{\mathrm{MaxCut}(G)}{|E(G)|}\ge c_\mathrm{VIRAL}(p).\) (9)

<tbc>Note that nothing about _G_ was used except its degree and its girth, so Eq. (9) holds for every graph in the class defining _M<sub>g</sub>_, and thus for their infimum. Together with the fact that _M<sub>g</sub>_ is non-decreasing in _g_ we conclude that

\(\mathrm{lim}_{g\rightarrow\infty} M_g\ge M_{2p+2}\ge c_\mathrm{VIRAL}(p).\) (10)

This is precisely the argument by which Farhi _et al._ turn a QAOA expectation value into a bound on _M<sub>g</sub>_ \[4\]. The only difference is that the expectation in Eq. (8) is over classical random seeds rather than over a quantum state.

Two consequences follow. First, the bound is constructive, in that on any 3-regular graph of girth at least 2_p_+2, one run of the algorithm costs _O(p|E_|) operations and produces a cut whose expected fraction is _c_<sub>VIRAL</sub>(_p_), with the parameters precomputed once for each _p_. Second, _c_<sub>VIRAL</sub>(_p_) is a classical expectation that we estimate by sampling the seeds, whereas the QAOA expectation of Ref. \[4\] is evaluated exactly by tensor-network methods. Each sample returns one bit, i.e., whether the root edge is cut, so from _S_ samples with _K_ cut events the estimate \(\hat{c}=K/S\) has standard error \(\sigma=\sqrt{\hat{c}(1-\hat{c})/S}\). For _S_=10<sup>7</sup> the estimate is Gaussian to high accuracy, and the probability that it exceeds the true value by more than \(5.2\sigma\) is 10<sup>-7</sup>. Hence

\(L=\hat{c}-5.2\sigma\) (11)

is a lower bound on _c_<sub>VIRAL</sub>(_p_) at 99.9999% confidence level.  I reports the exact binomial bound at the same level, which agrees with Eq. (11) to within 10<sup>-6</sup>. Since Eq. (10) holds for every value of _c_<sub>VIRAL</sub>(_p_), the statement \(M_g\ge L\) for all \(g\ge 2p+2\) holds at the same confidence level.

_Computing c_<sub>VIRAL</sub>(_p_) - The depth-_p_ tree is not a truncation of the infinite tree but the exact object to consider, in that nothing beyond it reaches the root edge. We draw the _N<sub>p</sub>_ i.i.d. seeds, run Eq. (3) on the tree, and record the single bit \(\unknown[\sigma_u\neq\sigma_v]\). Then _c_<sub>VIRAL</sub>(_p_) is the mean of this bit over _S_=10<sup>7</sup> independent draws. In particular, at _p_=2 no sampling is needed: the tree has 14 vertices, as in Fig. 1, so all 2<sup>14</sup>=16384 seed configurations can be run through Eq. (3) one by one, and we find that 12380 of them cut the root edge. The exact<tbc>

<tbc>value _c_<sub>VIRAL</sub>(2)=12380/16384=0.755615 agrees with the sampled one in  I within 1.2 standard errors.

_Parameters_ - The 2_p_+1 parameters are those obtained in Ref. \[15\] by training VIRAL on random 3- regular graphs, and are used here unchanged \[18\]. We computed them for even _p_ only, which is why  I lists even depths. Each training instance consists of a random 3-regular graph with _N_=10<sup>6</sup> vertices and one fixed realization of the seeds. The cost function is the continuous energy \(\sum_{(i,j)\in E}s_i^z(p)s_j^z(p)\) averaged over 10 instances, whose gradient with respect to \((\alpha,\beta_n,\gamma_n)\) is computed exactly by backpropagation through the _p_ layers of Eq. (3). Two remarks are in order: first, the same parameters are used on every graph, as the argument leading to Eq. (10) requires; second, they are not optimal for the tree, since they were optimized on graphs with cycles. Therefore, every value in  I is a conservative estimate of what VIRAL can guarantee at that depth, in that parameters optimized on the tree itself can only do better.

_Discussion_ - Evaluated on the depth-_p_ tree, VIRAL yields rigorous lower bounds on _M<sub>g</sub>_ for every girth up to 66. At equal depth they exceed the QAOA bounds by 0.005 to 0.011 and those of Ref. \[8\] at every \(p\ge 4\), and at _g_=66 they pass 0.912, a value previously reached only in the limit of infinite girth. Therefore, the asymptotic lower bound in Eq. (2) becomes

\(0.9127\le\mathrm{lim}_{g\rightarrow\infty} M_g\le 0.92386.\) (12)

The bounds are constructive, and the algorithm attaining them runs in time linear in the number of edges.

These results bear on the question of quantum advantage for local algorithms. Ref. \[4\] found that on 3-regular graphs the QAOA beats the best classical local algorithm with a provable guarantee for \(g\ge 16\), and Ref. \[19\] has recently extended this comparison to Max-_k_-Cut on _d_- regular graphs, where the QAOA overtakes an improved vector algorithm for \(g\ge 20\) at every _k_ and _d_ considered, an apparent quantum advantage at moderate girth. The tree value _c_<sub>VIRAL</sub>(_p_) is a guarantee of the same kind, and at _k_=2 and _d_=3 it exceeds the QAOA value at every even depth \(p\ge 4\) up to 32, in particular at every girth where Ref. \[4\] found the QAOA ahead of the classical algorithms. In this case, therefore, the advantage does not exist. Whether the same holds at higher degree and for \(k\ge 3\) is a natural next test. The same conclusion was reached on the Sherrington-Kirkpatrick (SK) model, which governs the large-degree limit of Max-Cut on regular graphs \[11\]. There VIRAL outperforms the QAOA at every depth \[15\], and so does the semiclassical limit of the QAOA itself \[16\]. In both cases, the dense SK model and sparse 3-regular graphs, the quantum fluctuations of the QAOA are not a resource. Their classical remnant, i.e. the random seeds, is all the dynamics needs, and it does better without the rest.

Finally, we note that the increments _c_<sub>VIRAL</sub>(_p_)-_c_<sub>VIRAL</sub>(_p_-2) are still decreasing at _p_=32 and the<tbc>

