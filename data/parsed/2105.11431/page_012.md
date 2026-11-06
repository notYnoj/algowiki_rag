Theorem 4.11 applies to functions of Bernoulli random variables. In order to apply it to our situation, we introduce a coupling of \(\{Q(t)\}_{t=0}^T\) to a binomial random subset of \[_n_\]<sup>2</sup>. For every \(x\in[n]^2\), let \(x_\alpha\in[0,1]\) be i.i.d. uniformly random. Observe that for every \(q\in[0,1]\), \(R(q):=\{x\in[n]^2:x_\alpha<q\}\) is a binomial random subset of \[_n_\]<sup>2</sup> with density _q_.

Now consider the random process \(\tilde{Q}(0),\tilde{Q}(1),\dots\), defined as follows: \(\tilde{Q}(0)=\emptyset\). Suppose that for _t\<n_ we have defined \(\tilde{Q}(t)\). Let \(x\in[n]^2\) be the position that minimizes \(x_\alpha\) which is also available in \(\tilde{Q}(t)\) (by "available" we mean not sharing a row, column, or toroidal diagonal with a previously chosen position). Set \(\tilde{Q}(t+1)=\tilde{Q}(t)\cup\{x\}\). If there is no such position, set \(\tilde{Q}(t+1)=\tilde{Q}(t)\). Observe that \(\{\tilde{Q}(t)\}_{t=0}^T\) and \(\{Q(t)\}_{t=0}^T\) have the same distribution. Thus we may (and do) identify them. We remark, however, that the process \(\tilde{Q}(t)\) is defined also for \(T<t\le n\). This will be useful in the proof of the next claim.

Set _p_=1/(4_n_) and let _R=R(p_). Let \(\tilde{R}\subseteq R\) be the set of positions \(x\in R\) that are not threatened by any other element of _R_ (that is, they are the only positions in their row, column, and toroidal diagonals).

**Claim 4.12.** _With probability_ \(1-exp\left(-\Omega(n)\right)\) _it holds that_ \(\tilde{R}\subseteq Q(T)\).

_Proof._ We note that by Chernoff’s inequality we have \(\mathbb{P}\left[|R|>T\right]=exp\left(-\Omega(n)\right)\).

Let \(x\in\tilde{R}\). By definition of the process, it holds that \(x_\alpha<y_\alpha\) for every _y_ that threatens _x_. Thus, there exists some _t_ (possibly greater than _T_) such that \(x\in\tilde{Q}(t)\). Let _t<sub>x</sub>_ be the smallest _t_ such that \(x\in\tilde{Q}(t)\). It suffices to show that \(t_x\le T\). This clearly holds if \(|R|\le T\). The latter event holds with probability \(1-exp\left(-\Omega(n)\right)\), as desired. □

Due to Observation 4.5 and Claim 4.12, with probability \(1-exp\left(-\Omega(n)\right)\) we have \(\mathcal{S}_\tilde{R}(r,c)\subseteq\mathcal{S}_{Q(T)}(r,c)\) for every \((r,c)\in[n]^2\). Therefore, Lemma 4.3 follows from the following claim.

**Claim 4.13.** _There exists a constant_ \(\beta>0\) _such that w.h.p._ \(\tilde{R}\) _is_ \((\beta n)\)_-absorbing._

We will apply Theorem 4.11 to prove Claim 4.13. We will use the following Lipschitz condition.

**Claim 4.14.** _Let_ \(Q_1,Q_2\subseteq[n]^2\) _be partial toroidal n-queens configurations such that_ \(|Q_1\Delta Q_2|=1\)_. Then, for every_ \((r,c)\in[n]^2\)_, we have_ \(||\mathcal{S}_{Q_1}(r,c)|-|\mathcal{S}_{Q_2}(r,c)||\le 5\).

_Proof._ Let \((r,c)\in[n]^2\). It suffices to show that if _R_<sub>2</sub> is obtained from _R_<sub>1</sub> by adding a queen (_x,y_), then \(||\mathcal{S}_{Q_1}(r,c)|-|\mathcal{S}_{Q_2}(r,c)||\le 5\).

Since \(Q_1\subseteq Q_2\), Observation 4.5 implies that \(\mathcal{S}_{Q_1}(r,c)\subseteq\mathcal{S}_{Q_2}(r,c)\). Hence, it is enough to show that

\(|\mathcal{S}_{Q_2}(r,c)\backslash\mathcal{S}_{Q_1}(r,c)|\le 5.\)

We observe that overall, _R_<sub>2</sub> contains at most one more (not necessarily safe) absorber for (_r,c_) than _R_<sub>1</sub>. Indeed, the only candidate for a new absorber in _R_<sub>2</sub> is (_x,y_) itself. In this way, S_<sub>R<sub>2</sub></sub>(r,c_) may contain at most one absorber that is not in B_<sub>R<sub>1</sub></sub>(r,c_). Any other elements of S<sub>_Q_<sub>2</sub></sub>(_r,c_)\\S<sub>_Q_<sub>1</sub></sub>(_r,c_) must have the following form: There exists some \((x',y')\in\mathcal{B}_{Q_1}(r,c)\backslash\mathcal{S}_{Q_1}(r,c)\) and \((x',y')\in\mathcal{S}_{Q_2}(r,c)\). This occurs only if \((x,y)\in\)<tbc>

