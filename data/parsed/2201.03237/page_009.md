We call the graph achieving monotonic search as Monotonic Search Network (MSNET). This definition of MSNET differs from MSNET in NSG\[14\] and NSSG\[20\], which we will elaborate later. This MSNET is quite fit for nearest neighbor search, because it ensure that the search results are exact, and the search process does not need backtracking to ensure high efficiency. However, such an ideal MSNET is almost impossible to construct, mainly because the location of the query point _q_ cannot be predicted when we build the graph. To solve this problem, we propose the definition of (_r,p_)-MSNET.

**Definition 3.** _((r,p)-MSNET). For a given query point q, if_ \(\delta(q,o^*)\le r\) _where o_<sup>∗</sup> _is the nearest neighbor of q, a graph is a_ (_r,p)-MSNET when the probability of achieving monotonic search is greater than p._

For a given point set D, we can construct a (_r,p_)-MSNET following three steps:

1. First, we list all node \(s\in\mathcal{D}\) as the starting node of search.<tbc>

2. For each node _s_, we list all node \(e\in E=\mathcal{D}-\{s\}\) as the nearest neighbor of query point _q_ assuming \(\delta(q,e)<r\). Sort _E_ in ascending order of \(\delta(s,e)\). Here, _E_ is the candidate neighbor set of _s_ and \(V=\phi\) originally.<tbc>

3. For each node \(e\in E\) we list all existing neighbor \(v\in V\) and calculate the probability of \(\delta(q,v)<\delta(q,s)\). If all the probabilities are lower than _p_, _e_ is added to _V_ , otherwise not. Finally we set the neighbor set of _s_ in _G_ as _V_ .

It is easy to prove that the graph constructed by the above steps is a (_r,p_)- MSNET. When given a query point _q_ and the distance between _q_ and its nearest neighbor _o_<sup>∗</sup> less than _r_, we start the search from any point _s_. If the point _s_ is not _o_<sup>∗</sup>, the point _o_<sup>∗</sup> must be included in _E_=D-{_s_}. We use _V_ to denote the neighbor set of _s_, if there is a point \(v\in V\) closer to query _q_ than _s_, the monotonic search can be achieved. Therefore, only if all the probabilities are lower than _p_, the edge \(\overrightarrow{se}\) is necessary.

