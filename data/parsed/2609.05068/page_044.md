## A.5 Proof of Lemma 2.5

_Proof._ We will consider the sum of the loads of all arcs exiting _s_ and entering _t_ to show that successfully routing a throughput of \(\gamma=1\) requires \(Q_I\cup Q_J\cup Q'_J=\emptyset\).

From Lemmas 2.3 and 2.4, and the definitions of the \(\epsilon\) variables, we can bound the load on each arc of the 2-hop paths:

• For a given \(i\in I\), the upper bounds on the arc loads are \(y_{(s,u_i)}\le mw_i+(m-1)W+1-\epsilon_i\) and \(y_{(u_i,t)}\le 1+\epsilon_i\). The first bound is strict if \(i\in Q_I\). Summing over \(i\in I\) gives:<tbc>

<tbc>\(\sum_{i\in I}(y_{(s,u_i)}+y_{(u_i,t)})\le mW+n(m-1)W+2n=b_L+b_H+2n\)<tbc>

<tbc>with this inequality being strict if \(Q_I\neq\emptyset\).<tbc>

• For a given \(j\in J\), the upper bounds on the arc loads are \(y_{(s,v_j)}\le 1+\epsilon_j\) and \(y_{(v_j,t)}\le\frac{W}{m}+1-\epsilon_j\). The second bound is strict if \(j\in Q_J\). Summing over \(j\in J\) gives:<tbc>

<tbc>\(\sum_{j\in J}(y_{(s,v_j)}+y_{(v_j,t)})\le W+2m=b_L+2m\)<tbc>

<tbc>with this inequality being strict if \(Q_J\neq\emptyset\).<tbc>

• For a given \(j\in J\), the upper bounds on the arc loads are \(y_{(s,v_j^N)}\le 1+\epsilon'_j\) and \(y_{(v_j^N,t)}\le W\frac{(n+1)(n-3)}{n}+1-\epsilon'_j\). The second bound is strict if \(j\in Q'_J\). Summing over \(j\in J\) gives:<tbc>

<tbc>\(\sum_{j\in J}(y_{(s,v_j^N)}+y_{(v_j^N,t)})\le mW\frac{(n+1)(n-3)}{n}+2m=b_H+2m\)<tbc>

<tbc>with this inequality being strict if \(Q'_J\neq\emptyset\).

Because there are no arcs exiting _s_ or entering _t_ other than those analyzed above, we can sum them to obtain the global bound on the network’s entry<tbc>

