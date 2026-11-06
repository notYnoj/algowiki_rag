**Theorem 3.4.** _Let_ \((I=(A,\succ),D)\) _be an instance with n agents of_ 0-Deviator-sri _and let G_=(_A,E_) _be the acceptability graph of I. If_ \(G'=(A,E\backslash E[A\backslash D])\) _is bipartite, then we can solve_ 0-Deviator-sri _in O(n_<sup>2</sup>) _time._

_Proof._ Suppose that \(G'=(A,E\backslash E[A\backslash D])\) is bipartite. Then the instance \(I'=(A,\succ')\) induced by the restricted acceptability graph \(G'\) is an smi instance. Any smi instance admits a stable matching _M_, and we can find one in _O(n_<sup>2</sup>) time \[21\]. Now suppose that _M_ admits a blocking pair \(\{a_r,a_s\}\in bp(M)\) with respect to instance _I_. Then, by construction of \(I'\), it must be the case that \(\{a_r,a_s\}\in E[A\backslash D]\), in which case \(\bigcup_{a_i\in D}bp_{a_i}(M)=\varnothing\) as required.

An example of a restricted preference graph can be seen in Figure 3. Unfortunately, this structural insight does not generalise to an efficiently verifiable necessary and sufficient condition for 0-Deviator-sri-Dec, as there may be complex interactions among agents between and outside _D_. The following intractability result leaves little hope for an efficiently verifiable condition for the existence of a solution to 0-Deviator-sri.

**Theorem 3.5.** 0-Deviator-sri-Dec _is_ NP-complete_, regardless of whether all preference lists are of length at most 5 or all preference lists are complete._

_Proof._ We will reduce from 0-Deviator-Perfect-smi-Dec, which we showed to be NP- complete in Theorem 3.1. Notice that membership in NP follows immediately, as we can simply iterate through _D_ and check that no agent in this set is contained in any blocking pairs of a given perfect matching.

Let \((I=(A,\succ),D)\) be an instance of 0-Deviator-Perfect-smi-Dec and let \((J=(A_J,\succ^J),D_J)\) be the instance of 0-Deviator-sri-Dec we construct, where \(A_J=A\cup A_B\), \(A_B=\{b_i^1,b_i^2;1\le i\le|A|\}\), and \(D_J=D\cup A_B\). Overall, _J_ has three times the number of agents as _I_. Now, for every agent \(a_i\in A\) with preference list _P<sub>a<sub>i</sub></sub>_ in _I_, we construct the following preference lists:

\(a_i:P_{a_i}b_i^1b_i^2\)<br>
\(b_i^1:b_i^2a_i\)<br>
\(b_i^2:a_ib_i^1\)

We claim the following correspondence between the two problems. For clarity, we will indicate the relevant instance in the notation of blocking pairs, e.g., _bp<sup>I</sup>(M_) denotes the set of blocking pairs that _M_ admits with respect to instance _I_ and \(bp_{a_i}^I(M)\) denotes the set of blocking pairs involving _a<sub>i</sub>_ that _M_ admits with respect to instance _I_.

**Claim 2.** _I admits a perfect matching M such that_ \(\bigcup_{a_i\in D}bp_{a_i}^I(M)=\varnothing\) _if and only if J admits a matching_ \(M'\) _such that_ \(\bigcup_{a_i\in D_J}bp_{a_i}^J(M')=\varnothing\).

D
A
D
Figure 3: Illustration of restricted acceptability graph (colours indicate a possible bipartition)

Figure 3: Illustration of restricted acceptability graph (colours indicate a possible bipartition)

