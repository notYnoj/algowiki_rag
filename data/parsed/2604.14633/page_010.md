Consider the energy difference from flipping an individual arc (_u,v_). If \(\mathbf{y}(v)\ge\mathbf{y}(u)\), then the original energy is ln(_M_+1)-ln(**y**(_v_)-**y**(_u_)+1) and the new energy is ln(_M_+1)+**y**(_v_)-**y**(_u_), so the net change in energy is

\(\big(ln(M+1)+\mathbf{y}(v)-\mathbf{y}(u)\big)-\big(ln(M+1)-ln(\mathbf{y}(v)-\mathbf{y}(u)+1)\big)\)<br>
\(=\mathbf{y}(v)-\mathbf{y}(u)+ln(\mathbf{y}(v)-\mathbf{y}(u)+1)\)<br>
\(\le\mathbf{y}(v)-\mathbf{y}(u)+ln(M+1),\)

where we use the assumption that \(\mathbf{y}(v)-\mathbf{y}(u)\le M\). Similarly, if \(\mathbf{y}(v)\le\mathbf{y}(u)\), then the original energy is ln(_M_+1)+**y**(_u_)-**y**(_v_) and the new energy is ln(_M_+1)-ln(**y**(_u_)-**y**(_v_)+1), so the net change in energy is

\(\big(ln(M+1)-ln(\mathbf{y}(u)-\mathbf{y}(v)+1)\big)-\big(ln(M+1)+\mathbf{y}(u)-\mathbf{y}(v)\big)\)<br>
\(=\mathbf{y}(v)-\mathbf{y}(u)-ln(\mathbf{y}(u)-\mathbf{y}(v)+1)\)<br>
\(\le\mathbf{y}(v)-\mathbf{y}(u).\)

In both cases, the net change in energy is at most **y**(_v_)-**y**(_u_)+ln(_M_+1). Summed over all arcs (_u,v_) on the path, the **y**(_v_)-**y**(_u_) terms telescope to **y**(_t_)-**y**(_s_), and the ln(_M_+1) terms sum to at most (_n_-1)ln(_M_+1).

## 3.3 Running Time

Outside of the calls to ToggleCut, the algorithm spends _n_<sup>1+_o_(1)</sup> time on each augmenting path: the algorithm computes a sparsifier, finds an augmenting path, flips the path, and updates the data structures. To bound the number of calls to ToggleCut, it suffices to bound the total energy increase over the course of the algorithm, since the total energy starts at _m_ln(_M_+1) and decreases by \(\Omega(\alpha^3)=1/n^{o(1)}\) on each call to ToggleCut (Lemma 14).

Let E be the current total energy. By Lemma 15, the energy increase is at most **y**(_t_)-**y**(_s_)+(_n_-1)ln(_M_+1) after flipping the next augmenting path. If \(\mathbf{y}(t)-\mathbf{y}(s)\ge 0\), then we bound **y**(_t_)-**y**(_s_) as follows. Each of the arcs (_t,s_) added during preprocessing has energy \(ln(M+1)+\mathbf{y}(t)-\mathbf{y}(s)\ge\mathbf{y}(t)-\mathbf{y}(s)\). There are \(\Omega(m)\) such arcs, so their total energy \(\Omega(m)\cdot(\mathbf{y}(t)-\mathbf{y}(s))\) is at most E. We conclude that \(\mathbf{y}(t)-\mathbf{y}(s)\le O(\mathcal{E}/m)\), and the total energy after flipping the augmenting path is at most \((1+O(1/m))\cdot\mathcal{E}+(n-1)ln(M+1)\). The total number of augmenting paths is \(F\le m\), so the total energy increase is at most \((1+O(1/m))^F\cdot(mln(M+1)+F(n-1)ln(M+1))\le O((m+nF)ln(M+1))\).

At this point, we can also justify the assumption \(max_{u,v}|\mathbf{y}(u)-\mathbf{y}(v)|\le M\) from Lemma 15 for _M=n_<sup>_O_(1)</sup> as long as the residual graph is strongly connected. For the sake of argument, re-define _M_ as the largest value of max<sub>_u,v_</sub>|**y**(_u_)-**y**(_v_)| over the course of the algorithm, and suppose for contradiction that _M_ is too large. Consider the moment of the algorithm at which **y**(_u_)-**y**(_v_)=_M_ for some \(u,v\in V\) . Consider a path from _u_ to _v_ of at most _n_-1 arcs in the current residual graph. There is an arc \((u',v')\) on the path with \(\mathbf{y}(u')-\mathbf{y}(v')\ge M/(n-1)\), which has energy \(ln(M+1)+\mathbf{y}(u')-\mathbf{y}(v')\ge M/(n-1)\). In particular, the total energy is at least _M/(n_-1). However, by the previous energy bound, the total energy at this point is at most _O_((_m+nF_)ln(_M_+1)). For large enough _M=n_<sup>_O_(1)</sup>, we obtain a contradiction.

We conclude that the algorithm has total running time \((m+nF)\cdot n^{o(1)}\) while the residual graph is strongly connected. When the flow is maximum, the residual graph _G<sub>f</sub>_ is no longer strongly connected, and the algorithm may have undefined behavior. However, we can impose a running<tbc>

