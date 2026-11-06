<tbc>algorithm to be _robust_ in the sense that a man’s proposal order is not affected by other men’s preference lists.

**Ties _or_ Incomplete Lists.** When only ties are present (SMT) or only incomplete lists are present (SMI), all the stable matchings of one instance have the same cardinality. The former is due to the fact that any stable matching is a perfect matching, and the latter is due to the Rural Hospitals theorem [3]. Hence approximability is not an important issue in these cases. As for strategy-proofness, since SMT and SMI are generalizations of SM, Roth’s impossibility theorem holds and no strategy-proof stable mechanism exists. Existence of one-sided strategy-proofness for SMI is already known as we have mentioned in "Coalition" part above, and that for SMT follows directly from Theorem 1.2.

## 2 Results for MAX SMTI

In this section, we give a proof of Theorem 1.2. We start with the positive part:

**Lemma 2.1** _MAX SMTI admits both a man-strategy-proof_ 2_-approximate-stable mechanism and a woman-strategy-proof_ 2_-approximate-stable mechanism._

_Proof._ Consider a mechanism _S_<sup>∗</sup> that is described by the following algorithm. Given a MAX SMTI instance _I_, _S_<sup>∗</sup> first breaks each tie so that persons in a tie are ordered increasingly in their indices, that is, if _q<sub>i</sub>_ and _q<sub>j</sub>_ are in the same tie of _p_’s list, then after the tie break \(q_i\succ_pq_j\) holds if and only if _i\<j_. (This ordering is only for the purpose of making the algorithm deterministic, so any _fixed_ tie-breaking rule is valid.) Let \(I'\) be the resulting instance. Its preference lists are incomplete but do not include ties; such an instance is called an _SMI instance_. It then applies MGS modified for SMI [4] to \(I'\) and obtains a stable matching _M_ for \(I'\). It is easy to see that _M_ is stable for _I_. Also it is well-known that in MAX SMTI, any stable matching is a 2-approximate solution [10]. Hence _S_<sup>∗</sup> is a 2-approximate-stable mechanism.

We then show that _S_<sup>∗</sup> is a man-strategy-proof mechanism for MAX SMTI. Suppose not. Then there is a MAX SMTI instance _I_ and a man _m_ who has a successful strategy in _I_. Let _J_ be a MAX SMTI instance in which only _m_’s preference list differs from _I_, and by using it _m_ obtains a better outcome. Let _M<sub>I</sub>_ and _M<sub>J</sub>_ be the outputs of _S_<sup>∗</sup> on _I_ and _J_, respectively. Then _m_ prefers _M<sub>J</sub>_ to _M<sub>I</sub>_, that is, either (i) \(M_J(m)\succ_mM_I(m)\) with respect to _m_’s true preference list in _I_, or (ii) _m_ is single in _M<sub>I</sub>_ and matched in _M<sub>J</sub>_, and _M<sub>J</sub>(m_) is acceptable to _m_ in _I_. Let \(I'\) and \(J'\), respectively, be the SMI-instances constructed from _I_ and _J_ by breaking ties in the above mentioned manner. Then _M<sub>I</sub>_ and _M<sub>J</sub>_ are, respectively, the results of MGS applied to \(I'\) and \(J'\). Since \(I'\) is the result of tie-breaking of _I_ and _m_ prefers _M<sub>J</sub>_ to _M<sub>I</sub>_ in _I_, _m_ prefers _M<sub>J</sub>_ to _M<sub>I</sub>_ in \(I'\). Note that, due to the tie-breaking rule, the preference lists of people except for _m_ are same in \(I'\) and \(J'\). This means that when MGS is used in SMI, _m_ can have a successful strategy in \(I'\) (i.e., to change his list to that of \(J'\)),contradicting to the man-strategy-proofness of MGS for SMI (page 57 of [4]).

If we exchange the roles of men and women in _S_<sup>∗</sup>, we obtain a woman-strategy-proof 2- approximate-stable mechanism.

We then show the negative part. We remark that \(\epsilon\) is not necessarily a constant.

**Lemma 2.2** _For any positive_ \(\epsilon\)_, MAX SMTI admits neither a man-strategy-proof_ \((2-\epsilon)\)_- approximate-stable mechanism nor a woman-strategy-proof_ \((2-\epsilon)\)_-approximate-stable mechanism._

