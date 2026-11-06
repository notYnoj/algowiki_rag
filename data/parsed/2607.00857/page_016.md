for all \(e\in E(G_i)\), set _w(e_):=1.

We claim that _G_ contains a clique of size _q_-2 if and only if there is a certificate _C_ with |_C[u,v_]|=_q_ for the |_E(G_)| graphs with error at most \(|E(G)|-\genfrac(){pt}{2}{q-2}{2}\).

Suppose _G_ contains a clique _S_={_s_<sub>1</sub>_,...,s_<sub>_q_-2</sub>}. Consider the certificate that is defined as follows.

We set _C[s,t_]:=(_s,t,s_<sub>1</sub>_,...,s_<sub>_q_-2</sub>).

All other lists _C[u,v_] are filled with _u_, _v_ and _q_-2 other vertices with minimum index.

Let \(e_i=\{u,v\}\in E(G)\). We are left with the following situation. The only finite distances in _G<sub>i</sub>_ are _d<sub>G<sub>i</sub></sub>(s,u_), _d<sub>G<sub>i</sub></sub>(s,v_), _d<sub>G<sub>i</sub></sub>(u,t_), _d<sub>G<sub>i</sub></sub>(v,t_), and _d<sub>G<sub>i</sub></sub>(s,t_). All entries of the distance estimates _D<sub>i</sub>_ for _G<sub>i</sub>_ are automatically correct from the initialization except for _D<sub>i</sub>[s,t_]. The entry _D<sub>i</sub>[s,t_] is correctly filled if and only if at least one of _u_ and _v_ is in _C[s,t_]. Finally, (_s,t_) does not count into the error term \(\eta(G_i,C,p)\) if and only if _both of u and v_ and _s_ and _t_ are in _C[s,t_], since all other intermediate vertices yield an infinite detour.

This allows us to conclude that the error as stated in Problem 2 is exactly

\(|\{\{u,v\}\in E(G):\{u,v\}\unknown\subseteq C[s,t]\}|=|E(G)|-\genfrac(){pt}{2}{q-2}{2}.\)

Consider now the other direction and suppose we have a certificate _C_ that results in _D<sub>i</sub>_ with a total error of at most \(|E(G)|-\genfrac(){pt}{2}{q-2}{2}\). Without loss of generality, we can assume that for every \(a,b\in V(G_i)\) except for _a=s_ and _b=t_ the list _C[a,b_] are chosen optimally. That is because _D<sub>i</sub>[a,b_] is always correct and the lists have no influence on other values of _D<sub>i</sub>_. Then, (_a,b_) cannot contribute to the _i_-th error term. Hence, it is enough to focus on _s_ and _t_. As noticed before, (_s,t_) for _e<sub>i</sub>_={_u,v_} will contribute to the error term \(\eta(G_i,C,p)\) if and only if \(\{s,t,u,v\}\unknown\subseteq C[s,t]\). We can assume that \(\{s,t\}\subseteq C[s,t]\), otherwise the error is at least |_E(G_)|. Furthermore, by the supposed error term, for at least \(\genfrac(){pt}{2}{q-2}{2}\) edges {_u,v_}, both _u_ and _v_ appear in _C[s,t_]. Thus, _C[s,t_]\\{_s,t_} must be a clique of size _q_-2.

Since the reduction function is clearly polynomial, this proves the hardness. For the parameters, notice that clique becomes trivial if there are less than _q_-2 edges in _G_. \(\blacktriangleleft\)

## 7 Empirical estimation of prediction error

In order to understand whether in practice one can expect our prediction error to be substantially smaller than _n_<sup>2</sup>, we ran a simulation on some real-world data. Our code is available at `https://github.com/adampolak/warm-starting-apsp`.

We use two datasets consisting of network latencies between fixed sets of nodes over multiple time slices [47], available at `https://github.com/uofa-rzhu3/NetLatency-Data/`. We remark that, even though road networks are a textbook example application of APSP, in reality they are extremely sparse, and hence simply running Dijkstra from each node already gets one very close to a quadratic running time, which is a hard theoretical lower bound because of the output size. Network latency graphs constitute an example of real-world dense graphs on which people compute APSP [47].

For each of the two datasets, we independently sampled 10 graph snapshots. For each sampled graph, we computed a ground-truth certificate by solving APSP exactly. We then used this certificate as a prediction for the next graph snapshot in the time sequence. We calculated the prediction error for our algorithm with parameters set to \(p=\frac{1}{2}\sqrt{n}\) and \(q=2\sqrt{n}\).

The first dataset, called Seattle, consists of _t_=688 snapshots of a graph on _n_=99 nodes. The average prediction error that we calculated equals \(\eta_\mathrm{mean}=121.2\) (with the

