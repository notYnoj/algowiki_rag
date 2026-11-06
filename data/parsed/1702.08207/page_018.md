**Lemma 4.9.** _Algorithm 4.3 returns a correct query sequence assignment S for tree T._

For the purposes of analysis, we extend the notion of backtracking procedure BuildStrategy in a natural way, so that, for every node \(v\in V\) and box \(0\le p\le L-1\), we describe precisely the contribution _c<sub>v</sub>_\[_p,u_\] of each vertex \(u\in V(T_v)\) to the load _s<sub>v</sub>_\[_p_\]. (See Fig. 4.1 for an illustration.)

Formally, for _u=v_ we have \(c_v[p,v]\leftarrow a_p=[[t_v,t_v+w'(v)]\cap[p\omega,(p+1)\omega]|\) if \(t_v\neq\perp\), and \(c_v[p,v]\leftarrow 0\), otherwise. Next, if \(u\neq v\) and _u_ belongs to the subtree of child _v<sub>i</sub>_ of _v_, we put:<tbc>

\(c_v[p,u]\leftarrow\left\{\begin{array}{ c c }
c_{v_i}[p,u], & \text{if}t_{end}^v>p\omega, \\
0, & \text{otherwise},
\end{array}\right.\)

<tbc>where the insertion time \(t_{end}^v\) for _v_ is defined as in Observation 4.3. Comparing with (4.8), we have directly for all \(0\le p<L\):

\(s_v[p]=\sum_{u\in V(T_v)}c_v[p,u].\)

Let _p<sub>s</sub>(u_) and _p<sub>f</sub>(u_) be the indices of the starting and final box, respectively, to which vertex _u_ adds load, formally _p<sub>s</sub>(u_)=min_P<sub>u</sub>_ and _p<sub>f</sub>(u_)=max_P<sub>u</sub>_, where \(P_u=\{p:|[t_u,t_u+w'(u)]\cap[p\omega,(p+1)\omega]|>0\}\). From the statement of Algorithm 4.3, we show immediately by inductive bottom-up argument that if \(u\in S(v)\), then \(\omega\sum_{p=p_s(u)}^{p_f(u)}c_v[p,u]=w'(u)\).

**Lemma 4.10.** _Let_ \((s_v,t_v)_{v\in T(V)}\) _be a schedule assignment computed by_ BuildStrategy_. For any vertices u and z such that_ (_u,t<sub>u</sub>_) _and_ (_z,t<sub>z</sub>_) _belong to the schedule at v, if either u or z is heavy, then_ \([[t_u,t_u+w'(u)]\cap[t_z,t_z+w'(z)]]=0\).

_Proof._ Note that procedure InsertVertex is called for a heavy input vertex with its last parameter (insertion time) being a multiple of \(\omega\), and the weight \(w'(u)\) is a multiple of \(\omega\) by definition. Thus, the interval \([t_u,t_u+w'(u)]\) starts and ends at the beginning and end of a box, respectively. Hence, Constraint (4.6) gives the lemma.

As a consequence of Lemma 4.10, if these two jobs (_u,t<sub>u</sub>_) and (_z,t<sub>z</sub>_) overlap, where _u_ and _z_ belong to the sequence assignment _S(v_), then both of the vertices _u_ and _z_ must be light, thus:<tbc>

\(t_u>t_z-w'(u)-\omega=t_z+w'(z)-w'(z)-w'(u)-\omega\ge t_z+w'(z)-(2c+1)\omega.\)

<tbc>We now define the measure of progress _M(x,i_) of strategy A_<sub>S</sub>_ when searching for target _x_ after _i_ queries as follows. Let _Q<sub>i</sub>_ be the set of the first _i_ queried vertices. Let _v<sub>i</sub>_ be the current root of the tree, \(v_i=r(T\langle Q_i,x\rangle)\). Let \(S_i(v)\subseteq S(v)\) be the subsequence (suffix) of _S(v_) consisting of those vertices which have not yet been queried. Now, we define:

\(M(x,i)=\left\{\begin{array}{ c c }
\mathrm{min}_{u\in S_i(v_i)}p_s(u), & \text{if}S_i(v_i)\neq\emptyset, \\
L, & \text{if}S_i(v_i)=\emptyset.
\end{array}\right.\)

We have by definition, \(M(x,i)\in\{0,1,\dots,L-1,L\}\). We obtain the next Lemma from a following straightforward analysis of the measure of progress: every time following sequence _S(v_) we successively complete queries with an ‘up’ result with a total duration of at least _a_ boxes, since the queried vertices are ordered in the first place according to minimum query time, and in the second place according to query duration, the value of the minimum _p<sub>s</sub>(u_), for \(u\in S(v)\) remaining to be queried, advances by at least _a_ boxes.

**Lemma 4.11.** _The measure of progress M(x,i_) _has the following properties:_

1. _If the_ (_i_+1)_-st query returns an ‘up’ result, then_ \(M(x,i+1)\ge M(x,i)\).<tbc>

