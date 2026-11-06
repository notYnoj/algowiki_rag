## 13:22 Tight Energy Lower Bounds for Distributed Graph Algorithms

\(\mathbf{I}\big[\hat{\Pi}:Z\big|S_{V_A},\mathcal{E}\big]\) on the right-hand side of (20). We get

\(\mathbf{I}\big[\hat{\Pi}:Z\big|S_{V_A},\mathcal{E}\big]\le\mathbf{H}\big[\hat{\Pi}\big|S_{V_A},\mathcal{E}\big]\)<br> \(=\sum_{i=1}^\bar{M}\mathbf{H}\big[R_i,\hat{\Pi}_i\big|R_{<i},\hat{\Pi}_{<i},S_{V_A},\mathcal{E}\big]\) (21)

Returning to (20), we get

\(\mathbf{I}\big[\hat{\Pi}:Z\big|S_{V_A}\big]\le\sum_{i=1}^\bar{M}\mathbf{H}\big[R_i,\hat{\Pi}_i\big|R_{<i},\hat{\Pi}_{<i},S_{V_A},\mathcal{E}\big]+\frac{L}{2}+1.\) (22)

Combining the upper bound in (22) with the lower bound in (13) shows that there must exist an index _i_<sup>∗</sup> such that

\(\mathbf{H}\big[R_{i^*},\hat{\Pi}_{i^*}\big|R_{<i^*},\hat{\Pi}_{<i^*},S_{V_A},\mathcal{E}\big]\ge\frac{L/2-1}{\bar{M}}\)<br> \(\text{(by (18))}=\frac{L/2}{2c\beta\cdot d_U}-o(1)\)<br> \(\text{(by (17))}=\frac{C}{4c}logn-o(1).\) (23)

Without loss of generality, assume that _i_<sup>∗</sup> is the smallest such index. Rewriting the entropy on the left-hand side via the chain rule (see Fact 2.3) yields

\(\mathbf{H}\big[R_{i^*},\hat{\Pi}_{i^*}\big|R_{<i^*},\hat{\Pi}_{<i^*},S_{V_A},\mathcal{E}\big]=\mathbf{H}\big[R_{i^*}\big|R_{<i^*},\hat{\Pi}_{<i^*},S_{V_A},\mathcal{E}\big]\)<br> \(+\mathbf{H}\big[\hat{\Pi}_{i^*}\big|R_{i^*},R_{<i^*},\hat{\Pi}_{<i^*},S_{V_A},\mathcal{E}\big]\)<br> \(\le\mathbf{H}\big[R_{i^*}\big|R_{<i^*},\hat{\Pi}_{<i^*},S_{V_A},\mathcal{E}\big]+|\hat{\Pi}_{i^*}|\)<br> \(\le\mathbf{H}\big[R_{i^*}\big|R_{<i^*},\hat{\Pi}_{<i^*},S_{V_A},\mathcal{E}\big]+c_2logn.\)

Due to the lower bound in (23), we get

\(\mathbf{H}\big[R_{i^*}\big|R_{<i^*},\hat{\Pi}_{<i^*},S_{V_A},\mathcal{E}\big]\ge\left(\frac{C}{4c}-c_2\right)logn-o(1).\) (24)

Let \(U_*\subseteq U\) be the nodes that receive a message from some \(v\in\partial U\) in round _R_<sub>_i_<sup>∗</sup></sub>. (Note that it may be the case that \(R_{i^*}=R_{i^*+1}=\cdots=R_{i^*+\ell}\), and in that case, multiple nodes may receive a message from their neighbors in \(\partial U\) in the same round.) The intuition behind (24) is that the exact value of _R_<sub>_i_<sup>∗</sup></sub> is not known to the nodes in _U_<sub>∗</sub> and thus they may need to guess a number of times before one of them wakes up in the correct round. Of course, when "guessing" _R_<sub>_i_<sup>∗</sup></sub>, the nodes in _U_<sub>∗</sub> may take into account all earlier received messages and the respective rounds in which they were sent, as well as the earlier unsuccessful wake up attempts in which they did not receive any message. This is represented by the conditioning on events \(R_{<i^*}=r,\hat{\Pi}_{<i^*}=\pi,S_{V_A}=s\), and E. Note that we provide more power to the algorithm by assuming that all nodes in _U_<sub>∗</sub> know _S<sub>V<sub>A</sub></sub>_, as well as all messages received so far by any node in _U_. In fact, random variable \(R':=(R_{i^*}|R_{<i^*}=r,\hat{\Pi}_{<i^*}=\pi,S_{V_A}=s,\mathcal{E})\) includes conditioning on the (joint) knowledge of the nodes in _U_<sub>∗</sub> (as well as the initial states of all other nodes in _V<sub>A</sub>_), and assumes that--in contrast to reality--the nodes even know that event E occurs, which can only strengthen the lower bound. In addition, every node in

