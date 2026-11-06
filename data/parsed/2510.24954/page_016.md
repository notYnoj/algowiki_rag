Since by assumption, there are \(\eta s\) paths and each path passes through _U_<sub>1</sub> while \(|U_1|\le s/(4rk)\), the average number of paths passing through a vertex in _U_<sub>1</sub> is at least \(4\eta rk\). Now, consider layer _L_<sub>_t-k_</sub> or _L_<sub>_t+k_</sub> , i.e., a layer prior to or subsequent to layer _L<sub>t</sub>_ by _k_ steps. Denote the set of supported vertices in this layer by _U_<sub>2</sub>. We consider the logical bipartite graph \(H=(U_1\sqcup U_2,E_H)\) obtained by connecting every vertex \(u\in U_1\) to all vertices in _U_<sub>2</sub> that lie on a path in P passing through _u_. We denote the set of neighbors of _u_ in _H_ by _N<sub>H</sub>(u_) and its degree by deg_<sub>H</sub>(u_):=|_N<sub>H</sub>(u_)|. For two vertices _u_<sub>1</sub>_,u_<sub>2</sub>, we write _u_<sub>1</sub>∼_<sub>H</sub>u_<sub>2</sub> to denote that _u_<sub>1</sub>_,u_<sub>2</sub> are adjacent in _H_.

For each vertex \(u_1\in U_1\), we define \(p(u_1):=\sum_{u_2\in N_H(u_1)}\mathrm{deg}_H(u_2)\) such that _p(u_<sub>1</sub>) is equal to the total number of critical paths passing through the neighbors of _u_<sub>1</sub> in _H_. We show that there is a vertex \(u_1\in U_1\) with \(p(u_1)\ge 4rk\eta^2\). To this end, note that

\(\sum_{u_1\in U_1}p(u_1)=\sum_{u_1\in U_1}\sum_{u_2\in N_H(u_1)}\mathrm{deg}_H(u_2)\)<br>
\(=\sum_{u_1\in U_1}\sum_{u_2\in U_2}\mathbb{1}(u_1\sim_Hu_2)\mathrm{deg}_H(u_2)\)<br>
\(=\sum_{u_1\in U_1}\sum_{u_2\in U_2}\sum_{u_1^\prime\in U_1}\mathbb{1}(u_1\sim_Hu_2)\mathbb{1}(u_2\sim_Hu'_1)\)<br>
\(=\sum_{u_2\in U_2}\mathrm{deg}_H(u_2)^2.\)

Now, applying Cauchy-Schwarz,

\(\left(\sum_{u_2\in U_2}\mathrm{deg}_H(u_2)^2\right)\cdot|U_2|\ge\left(\sum_{u_2\in U_2}\mathrm{deg}_H(u_2)\right)^2,\)

and since \(\sum_{u_2\in U_2}\mathrm{deg}_H(u_2)=\eta s\) and \(|U_2|\le s\) because we assumed that the total support of P is at most _s_, we get

\(\sum_{u_1\in U_1}p(u_1)=\sum_{u_2\in U_2}\mathrm{deg}_H(u)^2\ge\frac{1}{s}\left(\sum_{u\in U^\prime}\mathrm{deg}_H(u)\right)^2=\eta^2s.\)

This in turn implies that the average of _p(u_<sub>1</sub>) over \(u_1\in U_1\) is

\(\frac{1}{|U_1|}\sum_{u_1\in U_1}p(u_1)\ge 4rk\eta^2,\)

because \(|U_1|\le s/(4rk)\). We conclude that there exists some \(u\in U_1\) such that \(p(u)\ge 4rk\eta^2\).

Note that the vertices corresponding to _N<sub>H</sub>(u_) have a pairwise Euclidean distance within the _dk_-dimensional grid associated to layer _U_ of at most 2_rk_ since all of them are reachable from _u_ by following a critical direction, each of which has total Euclidean norm \(\le rk\). We claim that following all critical paths incident to the vertices in _N<sub>H</sub>(u_) for _\>_2_rk_ steps, we reach _p(u_) distinct vertices. Indeed, if there were a vertex _v_ reachable from two distinct critical paths starting at two vertices \(u_1,u_2\in N_H(u)\) after _\>_2_rk_ steps, then \(\|\vec{u_1}-\vec{u_2}\|_2>2rk\) contradicting the fact that the Euclidean distance between _u_<sub>1</sub>_,u_<sub>2</sub> is at most 2_rk_ as required by the assumption that _u_<sub>1</sub>_,u_<sub>2</sub> are both neighbors of _u_ in _H_.<sup>6</sup> This uses that the critical directions are distinct vectors with integer coordinates. Accordingly, if \(|i-j|\ge 4rk\), then

\(4rk\eta^2\le s\)

<sup>6</sup>For any \(u\in L_i\), let \(\vec{u}\) denote the position of _u_ in the _dk_-dimensional integer grid associated with layer _L<sub>i</sub>_.

