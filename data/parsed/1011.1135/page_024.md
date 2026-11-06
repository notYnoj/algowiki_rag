<tbc>Since preference list is uniformly drawn, we have _Pr(p_<sub>-_s_</sub>)=_Pr(f(p_<sub>-_s_</sub>)). The integral parts in equation (2) and (3) are equivalent since it is just a simple substitution of the variables, i.e., they both equal to the following expression:

\(\int_{\mathcal{R}_{p_s,p_{-s},i}^m(x_1,x_2,\dots,x_m)}\frac{1}{(b-a)^m}dx_1dx_2\dots dx_m\)

Thus, we have \(prob_i=prob'_i\) and the lemma is proven. \(\sqcap\sqcup\)

We still use _prob<sub>i</sub>_ to denote the probability of _s_ being matched to its _i_-th choice college. Combining the conclusion in Lemma 1 and Lemma 2, we have that \(prob_i\ge prob_j\) for _i\<j_. The best response in this case is clearly to put the favorite school in the first place, the second most favorite one in the second place and so on. Thus truth-telling would be the best response for students.

## C Proof of Property 4

Suppose there are _m_ colleges and _n_ students. Without loss of generality, we assume that all students share the same preference list: \(c_1>c_2>\cdots>c_m\). Let the quota of their favorite college _c_<sub>1</sub> be _q_ and reciprocating factor of _c_<sub>1</sub> is \(\alpha_{c_1}\).

By listing _c_<sub>1</sub> as their first choice, the top _q_ students judged by score (denoted by _s_<sub>1</sub>_,s_<sub>2</sub>_,...,s<sub>q</sub>_ with _f_<sub>_s_<sub>1</sub></sub>_\>f_<sub>_s_<sub>2</sub></sub>_\>...\>f_<sub>_s<sub>q</sub>_</sub>) would still occupy the top _q_ vacancies in _c_<sub>1</sub>’s merit score list. This can be easily seen by the composition of merit score:

\(mrt_{c_1}(s_q)=(1-\alpha_{c_1})\cdot f_{s_q}+\alpha_{c_1}\cdot h_{c_1}(1)\)

For any other student _s<sub>j</sub>_ (\(q<j\le n\)) listing _c_<sub>1</sub> as _i_-th choice, its merit score would be smaller than _mrt_<sub>_c_<sub>1</sub></sub>(_s<sub>q</sub>_) since _f<sub>s<sub>j</sub></sub>\<f<sub>s<sub>q</sub></sub>_ and \(h_{c_1}(i)\le h_{c_1}(1)\).

Thus, the top _q_ would reveal their true preferences and get into their first choice college.

For the rest students, since all the quota of _c_<sub>1</sub> is filled up, they would have no incentive to still list _c_<sub>1</sub> as their first choice. To prove that truth-telling (denoted by T) is a dominated strategy, we only need to find one particular strategy which dominates _T_. We now focus on one of such strategies which requires students to always submit \(c_2>c_3>\cdots>c_m>c_1\) (denoted by S). Let _s_ be any of these remaining students and the utility of _s_ be _u<sub>i</sub>_ when it is matched with \(c_i(i\in\{1,2,\dots,m\})\). Denoted by _prob<sub>i</sub>_ the probability of _s_ being matched with _c<sub>i</sub>_ under T and \(prob'_i\) the same probability under S (notice that _prob_<sub>1</sub> and \(prob'_1\) would be zero since _c_<sub>1</sub>’s quota has already been occupied). Then the expected utility under T would be no more than that under S since:

\(E(U)^T=\sum_{i=1}^mprob_i\cdot u_i\)<br>
\(=\sum_{i=2}^mprob_i\cdot u_i\)<br>
\(\le\sum_{i=2}^mprob'_i\cdot u_i\)<br>
\(=E(U)^S\)

According to Lemma 1, the probability of _s_ being matched with \(c_i(i\in\{2,3,\dots,m\})\) would be higher under S since _c<sub>i</sub>_’s position gets promoted compared with T. Thus \(prob_i\le prob'_i\) and the inequality above holds. This gives the proof that truth-telling is a dominated strategy.

