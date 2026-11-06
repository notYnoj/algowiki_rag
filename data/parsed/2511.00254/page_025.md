<tbc>is minimal. By the same argument, there exists a face _F_<sub>2</sub> of _G_ in Ext(_D_) such that _F_<sub>2</sub> contains both _s,t_. Since \(\mathrm{Ext}(D)\subseteq\mathrm{Ext}(C_0)\), \(F_2\neq F_1\).

## A.2 Local Uncrossing Lemma

In this subsection, we prove Theorem 3.3.

We always discuss a flow _f_ with a particular parallelization (not necessarily uncrossed, see Section 2.2), so we can assume support paths are edge-disjoint and thus cross only at nodes. We define the following. For \(v\in V\) and distinct paths _P,Q_, let \(\kappa(f,v,P,Q)\) be \(f(P)\cdot f(Q)\) if _P_ and _Q_ cross at _v_, and 0 otherwise. For \(v\in V\) , let \(\kappa(f,v)=\sum_{P,Q}\kappa(f,v,P,Q)^\text{13}\). We define the _crossing weight_ of _f_ to be \(\sum_v\kappa(f,v)\). The key lemma is as follows.

**Lemma A.1** (Local Uncrossing Lemma)**.** _Let_ (_G,H,u,d_) _be a feasible planar multiflow instance. Let f be a feasible flow that is minimum cost under unit edge costs. Suppose there exist support paths P,Q that cross at two distinct nodes z_<sub>1</sub> _and z_<sub>2</sub>_. Then there exists a feasible flow_ \(f'\) _for_ (_G,H,u,d_) _such that:_

• \(f'\) _is minimum cost,_<tbc>

• \(\kappa(f',v)\le\kappa(f,v)\) _for all_ \(v\notin\{z_1,z_2\}\)_, and_<tbc>

• \(\kappa(f',z_i)\le\kappa(f,z_i)-\epsilon^2\) _for i_=1,2_, where_ \(\epsilon=\mathrm{min}\{f(P),f(Q)\}\).

_Proof._ Let _f_ be a flow with a given parallelization. Let _P,Q_ be two (edge-disjoint) support paths that cross at nodes _z_<sub>1</sub> and _z_<sub>2</sub>. Let _h<sub>P</sub>_=(_s<sub>P</sub>,t<sub>P</sub>),h<sub>Q</sub>_=(_s<sub>Q</sub>,t<sub>Q</sub>_) be their respective demands (possibly equal). By re-labeling their extremities, we may assume both _P_ and _Q_ use _z_<sub>1</sub> before _z_<sub>2</sub> starting from _s<sub>P</sub>_ and _s<sub>Q</sub>_ respectively. Let \(\epsilon=\mathrm{min}\{f(P),f(Q)\}\). By embedding new edge-disjoint copies of _P,Q_ immediately beside their original copies, we can assume that \(f(P)=f(Q)=\epsilon\).

We decompose each of _P,Q_ into three subpaths: for _P_ these are \(P_1=P[s_P,z_1],P_2=P[z_1,z_2],P_3=P[z_2,t_P]\), and for _Q_ these are _Q_<sub>1</sub>=_Q[s<sub>Q</sub>,z_<sub>1</sub>]_,Q_<sub>2</sub>=_Q[z_<sub>1</sub>_,z_<sub>2</sub>]_,Q_<sub>3</sub>=_Q[z_<sub>2</sub>_,t<sub>Q</sub>_]. Now, define \(P'=P_1\bullet Q_2\bullet P_3\) and \(Q'=Q_1\bullet P_2\bullet Q_3\). We transfer the \(\epsilon\) units of flow on each of _P,Q_ to \(P',Q'\) respectively to define a new flow \(f'\) that routes the same demands _d_ and has the same cost as _f_.

One important catch is that \(P',Q'\) may not be (simple) paths, even if _P,Q_ are paths. For example, _Q_<sub>2</sub> may share nodes with _P_<sub>3</sub>. As discussed in Section 2.5, short-cutting walks can introduce new crossings. However, if \(P',Q'\) are not paths, then by short-cutting we obtain a flow whose cost is strictly less than that of _f_, a contradiction. <sup>14</sup>

Consider the change in the crossing weight contributions. First, consider any \(v\notin\{z_1,z_2\}\). The pair of edges that are consecutive for support paths transiting through _v_ are the same for both _f_ and \(f'\) (just possibly not belonging to the same support paths, because of swapping _P_<sub>2</sub> and _Q_<sub>2</sub>), and moreover the amount of flow on those edges is the same between _f_ and \(f'\). Hence, \(\kappa(f',v)=\kappa(f,v)\) for such _v_.

Now consider \(v\in\{z_1,z_2\}\) and a support path \(R\notin\{P,Q,P',Q'\}\) that transits through _v_. Of course, for any support path \(T\notin\{P,Q,P',Q'\}\), we have that \(\kappa(f',v,R,T)=\kappa(f,v,R,T)\), so we are interested in how _R_ interacts with \(P,Q,P',Q'\). Consider a sufficiently small disc centered at _v_. The edges from the crossing paths _P,Q_ divide the disc into four regions. The path _R_ starts in one region, then transits through _v_ into another region. If the second region is consecutive (clockwise or counterclockwise) with the first, then _R_ crosses exactly one of _P,Q_ and it also crosses exactly one of \(P',Q'\), and hence \(\sum_{T\in\{P^\prime,Q^\prime\}}\kappa(f',v,R,T)=\sum_{T\in\{P,Q\}}\kappa(f,v,R,T)\). If the second region is instead opposite the first, then _R_ crosses both _P_ and _Q_, and regardless how many of \(P',Q'\) it also crosses we have that \(\sum_{T\in\{P^\prime,Q^\prime\}}\kappa(f',v,R,T)\le\sum_{T\in\{P,Q\}}\kappa(f,v,R,T)\).

Finally, consider \(v\in\{z_1,z_2\}\) and the contributions from the paths \(P,Q,P',Q'\). The paths _P_ and _Q_ cross with \(\kappa(f,v,P,Q)=f(P)\cdot f(Q)=\epsilon^2\), while \(P'\) and \(Q'\) do not cross, so \(\kappa(f',v,P',Q')=0\).

<sup>13</sup>You could order the paths _P,Q_ to avoid double-counting them in the sums, but it ultimately does not matter for this proof. <sup>14</sup>Instead of using the minimum cost assumption, one could instead generalize the lemma to show how to decrease the crossing for non-simple flows. We use the minimum cost assumption only because the argument is more concise.

