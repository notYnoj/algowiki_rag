Namely, instead of going through all possible sequences of anchors, we force the anchors to resemble a straight line. An illustration of this candidate restriction is shown in Fig. 5.

We define the _curvature_ of a path to be the total, across all scales and intervals, deviation from a linear path between the endpoints of each interval:

\(\mathrm{Curv}(p):=\sum_{s\in[\mathrm{log}_M(2n)]}\sum_{(l,r]\in s}\sum_{i\in[M]}\left|(p(m_i)-p(m_{i-1}))-\frac{p(r)-p(l)}{M}\right|,\)

where we slightly abuse notation and use _s_ to denote both the scale and the set of scale-_s_ intervals. Note that curvature is closely related to tree total deviation -- curvature of _p_ is the tree total deviation on the forward difference of (_p_(0)_,p_(1)_,...,p_(2_n_)).

For ED, after we rotate the grid by 45\(^\circ\), all diagonal edges have weight 1. Thus for any interval (_l,r_\], |_p(l_)-_p(r_)| must be at most the length of the sub-path of _p_ inside (_l,r_\]. Suppose that the actual ED is \(\varepsilon n\). Our result on the tree total deviation (Lemma 4.1) implies that the total curvature across all scales is roughly only \(\varepsilon n\sqrt{\mathrm{log}_Mn}\). This saving of \(\sqrt{\mathrm{log}_Mn}\) from the naïve upper bound of \(O(\varepsilon n\mathrm{log}_Mn)\) is crucial to our ultimate quasi-polynomial saving in running time: it allows us to force parts of the paths to be a straight line to avoid overfitting to the sampled columns.

If the curvature of the optimal path inside an interval (_l,r_\] is small, then the optimal path is very close to a "straight line" from \(\langle l,p(l)\rangle\) to \(\langle r,p(r)\rangle\). This means that, at least on the _m<sub>i</sub>_’s, we can "round" the optimal path to agree with the straight line without incurring too much error. Thus when computing the answers inside (_l,r_\], even if we only consider the points \(\langle m_i,p(m_i)\rangle\) that agree with the straight line from \(\langle l,p(l)\rangle\) to \(\langle r,p(r)\rangle\), we do not lose too much precision. Fixing the endpoints of the path on each sampled column enables us to sub-sample without the risk of overfitting.

We show (Claim 6.4) that the error incurred by rounding the optimal path to straight line anchors inside (_l,r_\] is bounded by roughly _M_ times its curvature inside (_l,r_\]. We only do rounding and sub-sampling on<tbc>

E
D
C
B
A

Figure 5: In this example, the branching factor is _M_=4. Naïvely, all three paths are candidate paths. However, in our approach we only consider as a valid candidate the middle path, which is rounded to the straight line from A to E on "anchors" B, C, and D.

