<tbc>Moreover, since the distributions of the items in _F_ are fixed, _a_ and _b_ can be chosen such that, for all sufficiently large _t_,

\(\sum_{i=1}^I\mathbb{P}_t(\theta_i\ge a)>k,\sum_{i=1}^I\mathbb{P}_t(\theta_i\ge b)<k.\)

Since \(q\mapsto\sum_i\mathbb{P}_t(\theta_i\ge q)\) is nonincreasing in _q_ and equals _k_ at _q_<sup>∗</sup>(_t_) by (2), \(q^*(t)\in K:=[a,b]\) for all sufficiently large _t_.

For _q_<sup>†</sup>(_t_), since every posterior mean converges to a point in J, we can enlarge _K_ within J, if necessary, so that it also contains every \(\mu_i(t)\) for all sufficiently large _t_. By (3), \(\mu_{[k+1]}(t)\le q^\dagger(t)\le\mu_{[k]}(t)\), so \(q^\dagger(t)\in K\) as well.

Applying Lemma 6 to \(\Pi_i^\infty\) with the compact set _K_ gives \(\eta_i>0\) such that<tbc>

\(\mathbb{E}_{\Pi_i^\infty}[(q(t)-\theta_i)^+]-\mathbb{E}[(q(t)-X_{c_i^\infty})^+]\ge\eta_i,\)

<tbc>where \(X_{c_i^\infty}:=\mu_i^\infty+c_i^\infty(\theta_i-\mu_i^\infty)\) and \(c_i^\infty:=\sqrt{\bar{v}_i^\infty(1)/v_i^\infty}\). Once \(\Pi_{i,t}=\Pi_i^\infty\), the left-hand side is exactly \(\ell_{i,t}(0)-\ell_{i,t}(1)\). Hence \(\ell_{i,t}(0)-\ell_{i,t}(1)\ge\eta_i\) for all sufficiently large _t_. Let \(c_F:=min_{i\in F}\eta_i>0\). Then for all sufficiently large _t_,<tbc>

\(\ell_{i,t}(0)-\ell_{i,t}(1)\ge c_F\text{for every}i\in F.\)

<tbc>To get a contradiction, we next show that for every \(j\notin F\), the maximum possible improvement from allocating samples to item _j_ converges to 0. For \(j\notin F\), let<tbc>

\(R_{j,t}:=\ell_{j,t}(0)-inf_{d\ge 0}\ell_{j,t}(d)\)

<tbc>be the maximum possible improvement from allocating any number of samples to item _j_. Since \(x\mapsto(q-x)^+\) is 1-Lipschitz, for any random _X_,<tbc>

\(\big|\mathbb{E}[(q-X)^+]-(q-\mathbb{E}[X])^+\big|\le\mathbb{E}|X-\mathbb{E}[X]|\le\sqrt{\mathbb{V}(X)}.\)

<tbc>The current distribution for item _j_ has variance \(v_j(t)=\bar{v}_j(t,0)\), and \(\bar{v}_j(t,d)\le\bar{v}_j(t,0)\). Therefore<tbc>

\(R_{j,t}\le 2\sqrt{v_j(t)}\rightarrow 0.\)

<tbc>Since _F<sup>c</sup>_ is finite, \(\sum_{j\notin F}R_{j,t}\rightarrow 0\), and for all sufficiently large _t_, \(\sum_{j\notin F}R_{j,t}<c_F\). Thus, for sufficiently large _t_, the feasible allocation that places one sample on some \(i_0\in F\) and distributes the remaining _B<sub>t</sub>_-1 samples arbitrarily achieves total improvement

\(\big(\ell_{i_0,t}(0)-\ell_{i_0,t}(1)\big)+\sum_{j\neq i_0}\big(\ell_{j,t}(0)-\ell_{j,t}(d_j)\big)\ge c_F.\)

By contrast, any allocation that assigns no samples to items in _F_ has a total improvement of at most \(\sum_{j\notin F}R_{j,t}<c_F\). Therefore, the optimal solution allocates a sample to at least one item in _F_ for every sufficiently large _t_, contradicting the assumption. Hence \(F=\varnothing\). \(\square\)

