for any path _p_ from _s_ to _t_ not included in the set above, the minimum delay \(\sum_{a\in p}\frac{1}{c_a}\) is greater than _d_<sub>2</sub>.

The next lemma states that the paths described in Lemma 2.1 are actually used by _k_<sub>2</sub>.

**Lemma 2.2.** _k_<sub>2</sub> _uses all paths in_ \(\{s\rightarrow u_i\rightarrow t\}_{i\in I}\cup\{s\rightarrow v_j\rightarrow t\}_{j\in J}\cup\{s\rightarrow v_j^N\rightarrow t\}_{j\in J}\).

This lemma is proved by assuming that one of the paths is not used and showing that the additional load carried on the remaining paths would increase the path’s delay above the commodity’s limits. The full proof can be found in Appendix A.2.

In order to compute the exact load of commodity _k_<sub>2</sub> over each used path, we define for each \(i\in I\) and \(j\in J\) the scalars \(\epsilon_i\), \(\epsilon_j\), and \(\epsilon'_j\) in ]-1,1[ such that:<tbc>

\(y_{(u_i,t)}=1+\epsilon_i\forall i\in I,y_{(s,v_j)}=1+\epsilon_j\forall j\in J,y_{(s,v_j^N)}=1+\epsilon'_j\forall j\in J.\)

<tbc>We also consider the sets \(Q_I\subset I\), \(Q_J\subset J\), and \(Q'_J\subset J\) defined as follows:

\(Q_I=\{i\in I|\epsilon_i\neq 0\},Q_J=\{j\in J|\epsilon_j\neq 0\},Q'_J=\{j\in J|\epsilon'_j\neq 0\}.\)

We will show in Lemma 2.5 that \(Q_I\cup Q_J\cup Q'_J\) is necessarily empty. In order to prove this result, we will first give upper bounds on the load of arcs (_s,u<sub>i</sub>_) for every \(i\in I\) in Lemma 2.3, and upper bounds on the load of arcs (_v<sub>j</sub>,t_) and \((v_j^N,t)\) for every \(j\in J\) in Lemma 2.4.

**Lemma 2.3.** _For_ \(i\in I\)_, the load of arc_ (_s,u<sub>i</sub>_) _is strictly less than mw<sub>i</sub>_+(_m_-1)\(W+1-\epsilon_i\) _if_ \(i\in Q_I\)_, and less than or equal to mw<sub>i</sub>_+(_m_-1)_W_+1 _if_ \(i\in I\backslash Q_I\).

The proof of this lemma can be found in Appendix A.3. It relies on the fact that commodity _k_<sub>2</sub> uses the arcs (_u<sub>i</sub>,t_) - enforcing a maximum delay of _b_<sub>2</sub>=2 on the path \(s\rightarrow u_i\rightarrow t\), and on a linear under-estimator of the delays of arcs (_s,u<sub>i</sub>_) and (_u<sub>i</sub>,t_).

