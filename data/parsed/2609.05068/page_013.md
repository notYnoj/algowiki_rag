**Lemma 2.4.** _For_ \(j\in J\)_, the load of arc_ (_v<sub>j</sub>,t_) _is strictly less than_ \(\frac{W}{m}+1-\epsilon_j\) _if_ \(j\in Q_J\)_, and less than or equal to_ \(\frac{W}{m}+1\) _if_ \(j\in J\backslash Q_J\).

_Similarly, the load of arc_ \((v_j^N,t)\) _is strictly less than_ \(W\frac{(n+1)(n-3)}{n}+1-\epsilon'_j\) _if_ \(j\in Q'_J\)_, and less than or equal to_ \(W\frac{(n+1)(n-3)}{n}+1\) _if_ \(j\in J\backslash Q'_J\).

The proof of this lemma, given in Appendix A.4, follows the same reasoning as the proof of Lemma 2.3.

Based on Lemmas 2.3 and 2.4 above, we can establish the exact flow on several arcs of _A_:

**Lemma 2.5.** _The delays on arcs_ (_s,u<sub>i</sub>),_ (_v<sub>j</sub>,t),_ \((v_j^N,t)\) _and on the bypass arcs are equal to_ 1 _for every_ \(i\in I\) _and_ \(j\in J\)_, and the loads on these arcs are:_

\(y_{(s,u_i)}=mw_i+(m-1)W+1\forall i\in I\) (7)

\(y_{(v_j,t)}=\frac{W}{m}+1\forall j\in J\) (8)

\(y_{(v_j^N,t)}=W\frac{(n+1)(n-3)}{n}+1\forall j\in J\) (9)

\(y_{(u_i,t)}=y_{(s,v_j)}=y_{(s,v_j^N)}=1\forall j\in J,i\in I.\) (10)

This lemma is proven by summing the loads on all arcs exiting _s_ and entering _t_, and showing that if the set of arcs \(Q_I\cup Q_J\cup Q'_J\) is non-empty, this sum of loads is strictly lower than twice the size of the commodities _k_<sub>2</sub>, _k<sub>L</sub>_, and _k<sub>H</sub>_, contradicting the possibility of a throughput \(\gamma\ge 1\).

Equations (10) and Lemma 2.5 together imply that commodity _k_<sub>2</sub> routes a unit load through each path in the set

\(\{s\rightarrow u_i\rightarrow t\}_{i\in I}\cup\{s\rightarrow v_j\rightarrow t\}_{j\in J}\cup\{s\rightarrow v_j^N\rightarrow t\}_{j\in J}.\)

As a consequence, the arcs \(\{(u_i,t)\}_{i\in I}\), \(\{(s,v_j)\}_{j\in J}\), and \(\{(s,v_j^N)\}_{j\in J}\) are fully saturated by commodity _k_<sub>2</sub> if its delay is satisfied, meaning they cannot be used by commodity _k<sub>L</sub>_ or _k<sub>H</sub>_.

