# Reciprocating Preferences Stablize Matching: College Admissions Revisited

23

**Definition 2** For student _s_, let _p_ be its preference list where college _c_ is ranked _r_-th. Consider a new preference list \(p'\) of _s_ which exchanges the _r_-th choice with the _j_-th (_j\<r_) choice college. A mechanism is called _rank monotonic_ if the probability of _s_ being matched to _c_ is weakly higher under \(p'\) than under _p_ no matter how preferences and reciprocating factors are distributed.

**Lemma 1** _The generalized mechanism is_ rank monotonic.

_Proof_ Consider the notation in the previous definition. Also consider any state of the matching system (i.e., any possible scores, submitted preferences of students and RF of colleges) where student _s_ submits _p_ and is matched to college _c_. In this state, student _s_ is rejected by every college prior to its _r_-th choice in _p_, and after _c_ enrolls _s_, no other students can drive _s_ out of _c_’s quota in later rounds. Mathematically, suppose _c_ has quota _q_ and _s_ is in the _i_-th position in _c_’s merit order list, then there will be at most _q_-1 students with higher position than _s_ in _c_’s list.

Hence, if student _s_ had instead submitted \(p'\), in the same state of the system, he also would have been rejected by every college prior to its _j_-th choice in \(p'\). Considering _c_’s merit order list, student _s_ can only get promoted since it lists _c_ as higher choice in \(p'\). After getting into _c_ in the _j_-th round, since preferences of all other students and colleges remains the same as under _p_, there will also be at most _q_-1 students with higher position than _s_ in _c_’s new list. So _s_ can guarantee its admission to _c_. This implies that the probability of student _s_ being matched to college _c_ is weakly larger when it submits \(p'\) instead of _p_. \(\sqcap\sqcup\)

**Definition 3** If the probability of student _s_ being matched to its _i_-th choice college is independent of its submitted preference list, we say that its preference revelation problem exhibits _college anonymity_.

**Lemma 2** _Suppose there are m colleges with quota q and n students. If the submitted preferences of all students other than s, as well as the reciprocating factors of colleges are uniformly distributed, then the preference revelation problem of student s exhibits_ college anonymity.

_Proof_ Let student _s_ submit preference list _p<sub>s</sub>_ where _p<sub>s</sub>(i_) is its _i_-th choice college in list _p<sub>s</sub>_. Denoted by _p_<sub>-_s_</sub> other student’s preferences and \(\alpha=(\alpha_1,\alpha_2,\dots,\alpha_m)\) the vector of each college’s reciprocating factor. Let P be the set of all possible _p_<sub>-_s_</sub>. And R_<sup>m</sup>_=\[_a,b\]<sup>m</sup>_ is the _m_-dimensional space containing all possible values of \(\alpha\).

For each particular \(p_{-s}\in\mathcal{P}\), denoted by \(\mathcal{R}_{p_s,p_{-s},i}^m(\alpha_1,\alpha_2,\dots,\alpha_m)\subseteq\mathcal{R}^m\) the region of \(\alpha\) in which _s_ is matched to its _i_-th choice under (_p<sub>s</sub>,p_<sub>-_s_</sub>). Then the probability of _s_ being matched to its _i_-th choice can be denoted as:

\(prob_i=\sum_{p_{-s}\in\mathcal{P}}Pr(p_{-s})\int_{\mathcal{R}_{p_s,p_{-s},i}^m}\frac{1}{(b-a)^m}d\alpha\) (2)

Now let student _s_ submit a different preference list \(p'_s\). This induces a permutation mapping _f_ from the set of colleges’ index {1,2_,...,m_} to itself which is defined as follows: for any college _c<sub>j</sub>_ (\(j\in\{1,2,\dots,m\}\), let _r<sub>c<sub>j</sub>,p<sub>s</sub></sub>_ be its ranking in list _p<sub>s</sub>_, then the image value _f(j_) is the index of college which is ranked _r<sub>c<sub>j</sub>,p<sub>s</sub></sub>_ in list \(p'_s\). By a slight abuse of notation, we express this permutation as \(f(p_s)=p'_s\) for conciseness.

For each \((p_{-s},\mathcal{R}_{p_s,p_{-s},i}^m(\alpha_1,\alpha_2,\dots,\alpha_m))\), by symmetry, we know that under<br>
\((f(p_{-s}),\mathcal{R}_{p_s,p_{-s},i}^m(\alpha_{f(1)},\alpha_{f(2)},\dots,\alpha_{f(m)}))\), student _s_ would still be matched to its _i_-th choice college in \(p'_s\). Since _f_ is a one-to-one mapping, by this way of transformation we would have listed all the possibility for the matching. Thus the probability of _s_ being matched to its _i_-th choice in \(p'_s\) can be denoted as:

\(prob'_i=\sum_{p_{-s}\in\mathcal{P}}Pr(f(p_{-s}))\int_{\mathcal{R}_{p_s,p_{-s},i}^m(f(\alpha))}\frac{d(f(\alpha))}{(b-a)^m}\) (3)

