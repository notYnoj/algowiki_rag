<tbc>and exit flows:

\(\sum_{a\in\delta^+(s)}y_a+\sum_{a\in\delta^-(t)}y_a\le 2(b_L+b_H+b_2)\)

with a strict inequality if \(Q_I\cup Q_J\cup Q'_J\neq\emptyset\).

To successfully route the complete demands for all three commodities, the total flow leaving _s_ and entering _t_ must be exactly 2(_b<sub>L</sub>+b<sub>H</sub>+b_<sub>2</sub>). Therefore, we must have \(Q_I\cup Q_J\cup Q'_J=\emptyset\), meaning all \(\epsilon_i\), \(\epsilon_j\), and \(\epsilon'_j\) terms are exactly zero.

It also follows that all the upper bounds on the arc loads hold as strict equalities. We can finally deduce that \(y_{(s,u_i)}=mw_i+(m-1)W+1\), \(y_{(v_j,t)}=\frac{W}{m}+1\), \(y_{(v_j^N,t)}=W\frac{(n+1)(n-3)}{n}+1\), _y_<sub>(_u<sub>i</sub>,t_)</sub>=1, _y_<sub>(_s,v<sub>j</sub>_)</sub>=1, and \(y_{(s,v_j^N)}=1\). We also conclude that the delay on each of these arcs is exactly equal to 1.

## A.6 Proof of Lemma 2.6

_Proof._ We have observed that _k<sub>L</sub>_ cannot cross arcs in \(\{(u_i,t)\}_{i\in I}\), \(\{(s,v_j)\}_{j\in I}\), or \(\{(s,v_j^N)\}_{j\in I}\). Therefore, it cannot use paths in \(\{s\rightarrow u_i\rightarrow t\}_{i\in I}\cup\{s\rightarrow v_j\rightarrow t\}_{j\in I}\cup\{s\rightarrow v_j^N\rightarrow t\}_{j\in J}\cup\{s\rightarrow v_j\rightarrow v_j^1\rightarrow\cdots\rightarrow v_j^N\rightarrow t\}_{j\in J}\). Moreover, as established in the proof of Lemma 2.1, the delay on paths involving the arc chains \(v_j\rightarrow v_j^1\rightarrow\cdots\rightarrow v_j^N\) is strictly greater than \(d_L=2+\frac{1}{2W}\), which exceeds the delay limit for _k<sub>L</sub>_.

The only remaining feasible paths for _k<sub>L</sub>_ are therefore those in \(\{s\rightarrow u_i\rightarrow v_j\rightarrow t\}_{i\in I,j\in I}\).

## A.7 Proof of Lemma 2.7

_Proof._ From Lemma 2.6, commodity _k<sub>L</sub>_ enters vertex _t_ exclusively through the set of arcs \(\{(v_j,t)\}_{j\in J}\). Equation (8) establishes that the total load on each of these arcs is \(\frac{W}{m}+1\). Because commodity _k_<sub>2</sub> routes exactly 1 unit of flow on each arc (_v<sub>j</sub>,t_), the remaining flow on these arcs must belong to commodity _k<sub>L</sub>_. Therefore, the load of _k<sub>L</sub>_ on each arc (_v<sub>j</sub>,t_) is exactly \(\frac{W}{m}\).<tbc>

