Depending on the values of _m_<sub>1</sub>_,...,m_<sub>_b_+1</sub>_,n_<sub>1</sub>_,...,n_<sub>_a_+1</sub>, some connected components may be much larger than others. We apply the Connectivity Lemma in a similar way as in Lemma 49 and only count the rankings \(\rho\) that are in small connected components, which are the rankings for which _m_<sub>1</sub>_,...,m_<sub>_b_+1</sub>_,n_<sub>1</sub>_,...,n_<sub>_a_+1</sub> are bounded. Let _m_<sup>∗</sup> and _n_<sup>∗</sup> be the minimum integers for which

\(\mathbb{P}[m_1,\dots,m_{b+1}\le m^*]\ge\frac{3}{4}\text{and}\mathbb{P}[n_1,\dots,n_{a+1}\le n^*]\ge\frac{3}{4}.\)

By a union bound, the probability that both of these events hold is at least 1/2. In other words, there are least (_a+b_)!/2 rankings \(\rho\) for which \(m_1,\dots,m_{b+1}\le m^*\) and \(n_1,\dots,n_{a+1}\le n^*\).

**Proposition 53.**<tbc>

\(\mathrm{D}(\Pi_T)\ge\frac{(a+b)!}{2(m^*)!^{a/m^*}(n^*)!^{b/n^*}}.\) (26)

<tbc>_Proof._ We consider the rankings for which \(m_1,\dots,m_{b+1}\le m^*\) and \(n_1,\dots,n_{a+1}\le n^*\). We first argue the following upper bound on the size (25) of the connected component in \(G(\Pi_\mathrm{XInv})\) of any such ranking \(\rho\):<tbc>

\((m_1)!\cdots(m_{b+1})!(n_1)!\cdots(n_{a+1})!\le(m^*)^{a/m^*}(n^*)^{b/n^*}.\) (27)

<tbc>For nonnegative integers _n_, _n_!<sup>1_/n_</sup> is increasing. This can be seen by noticing that log(_n_!<sup>1_/n_</sup>) is the average of log(1)_,...,_log(_n_). As a result, for \(i\in[b+1]\), \((m_i)!^{1/m_i}\le(m^*)!^{1/m^*}\), or equivalently, \((m_i)!\le(m^*)^{m_i/m^*}\). Using the fact that \(m_1+\cdots+m_{b+1}=a\),

\((m_1)!\cdots(m_{b+1})!\le(m^*)!^{(m_1+\cdots+m_{b+1})/m^*}=(m^*)!^{a/m^*}.\)

We can apply similar reasoning to get \((n_1)!\cdots(n_{a+1})!\le(n^*)!^{b/n^*}\). From this, we conclude that the size of the connected components among the rankings under consideration is at most the right-hand side of (27).

Since there are at least (_a+b_)!/2 of the rankings under consideration, we derive the stated bound on \(\mathrm{D}(\Pi_T)\) by applying the Connectivity Lemma.

Now, we find concrete bounds on _m_<sup>∗</sup> and _n_<sup>∗</sup>.

**Proposition 54.**<tbc>

\(\mathrm{max}\left(1,\frac{a}{b+1}\right)\le m^*\le\frac{a+b}{b}\mathrm{ln}(4(b+1)).\)

<tbc>_Symmetrically,_

\(\mathrm{max}\left(1,\frac{b}{a+1}\right)\le n^*\le\frac{a+b}{a}\mathrm{ln}(4(a+1)).\)

_Proof._ We first prove the upper bound on _m_<sup>∗</sup>. Let _k_ be a positive integer. We compute the probability, over an average ranking \(\rho\), that _m<sub>i</sub>\>k_ for a specific _i_. Notice that there is a one-to- one correspondence between the ranking \(\rho\) and the corresponding sequence of nonnegative integers _m_<sub>1</sub>_,...,m_<sub>_b_+1</sub> such that \(m_1+\cdots+m_{b+1}=a\), because the ranks of _B_ can be uniquely recovered as _m_<sub>1</sub>+1_,m_<sub>1</sub>+_m_<sub>2</sub>+2_,..._, and the remaining ranks form _A_. By stars and bars, there are \(\genfrac(){pt}{2}{a+b}{b}\) such sequences. Now, if _m<sub>i</sub>\>k_, then _m<sub>i</sub>_-(_k_+1) is an arbitrary nonnegative integer, and<tbc>

