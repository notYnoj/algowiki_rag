<tbc>every clause, in which case \(\{c_j^s,u_\alpha^1(c_j^s)\}\in bp^J(M)\). Hence, \(|bp_{c_j^s}(M)|\ge k-1\), where each of the _k_-1 blocking pairs come from the \(u_\alpha^1(c_j^s)\) agents.

From Claims 7-8 we know that _B_ is satisfiable \(\Leftrightarrow I\) admits a perfect matching with at most _n+m_ blocking pairs \(\Leftrightarrow I\) admits a perfect matching in which no communication edge between clause and variable gadgets is blocking \(\Leftrightarrow I\) admits a perfect matching _M_ with \(max_{a_r\in A}|bp_{a_r}^I(M)|\le 1\).

It remains to show that _I_ admits a perfect matching _M_ with \(max_{a_r\in A}|bp_{a_r}^I(M)|\le 1\) if and only if _J_ admits a perfect matching _M_ with \(max_{a_r\in A^J}|bp_{a_r}^J(M)|\le k\).

First, suppose that _I_ admits a perfect matching _M_ with \(max_{a_r\in A}|bp_{a_r}^I(M)|\le 1\). Consider the matching \(M'=M\cup\{\{u_\alpha^1(c_j^s),u_\alpha^2(c_j^s)\}|\forall c_j^s\forall\alpha\}\). Clearly, \(M'\) is a perfect matching of _J_. Furthermore, because we add no more than _k_-1 entries to any agent’s preference list and maintain the relative preference order of \(\succ\) in \(\succ^J\), we have that, for all \(a_r\in A\), \(|bp_{a_r}^J(M')|\le|bp_{a_r}^I(M)|+k-1\). Thus, \(|bp_{a_r}^J(M')|\le k\) as required.

For the converse direction, suppose that _J_ admits a perfect matching _M_ that satisfies \(max_{a_r\in A^J}|bp_{a_r}^J(M)|\le k\). Notice that no communication edge can be blocking in _M_: suppose, for the sake of contradiction, that there exists some \(c_j^s\) agent that blocks with \(x(c_j^s)\). Then because _M_ is perfect, \(c_j^s\) must be matched to _q<sub>j</sub>_ and, by construction of the preference lists and our observation above, we must have that \(bp_{c_j^s}^J(M)=\{\{c_j^s,p_j^s\},\{c_j^s,x(c_j^s)\},\{c_j^s,u_1^1(c_j^s)\},\{c_j^s,u_2^1(c_j^s)\},\dots,\{c_j^s,u_{k-1}^1(c_j^s)\}\}\), in which case, \(|bp_{c_j^s}^J(M)|=k+1>k\), a contradiction. Thus, it is easy to see that \(M'=M|_I\) (i.e., _M_ restricted to pairs that involve agents in _A_) is a perfect matching of _I_ in which no communication edge is blocking, in which case \(max_{a_r\in A}|bp_{a_r}^I(M')|\le 1\).

In fact, we can also extend this new reduction above even further to establish a remarkably tight intractability bound as follows.

**Theorem 4.8.** _For any_ \(\varepsilon\in(0,1)\)_, the problem k_-Max-AlmostStable-Max-smi _is_ NP- complete _for_ \(k=\left\lfloor N^{1-\varepsilon}\right\rfloor\)_, where N is the number of agents._

_Proof._ The same reduction from a (2,2)-e3-sat instance _B_ as in the proof of Theorem 4.7 applies - all that remains to show is that an instance with the correct number of agents exists and can be constructed in polynomial time (in the size of _B_).

We argued previously that our construction produces an smi instance with _N_=8_n_+2_m_(1+3_k_) agents. Now substitute _k_ to see that \(N=8n+2m\left(1+3\left\lfloor N^{1-\varepsilon}\right\rfloor\right)\) and notice that _N_ is an integer value (we will later show that _N_ is strictly positive under our assumptions on _n_ and _m_).

2 (c1)
2 (c1)
2 (c1)
1
1
1
2
2
1 (c1)
1 (c1)
2 (c1)
1 (c1)
1
1
1
1
4
k+ 1
3
2
1
1
Cj
k + 2
qj

Figure 11: The modified clause gadget construction illustrated on a \(c_j^1\) agent

