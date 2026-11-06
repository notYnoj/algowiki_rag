(2009) showed that both popular and unpopular colleges have motives of giving preferential treatment to applicants who rank them as top choices. Does this imply that different colleges tend to have similar reciprocating factors in practice? This question may not be addressed immediately since these "inside" information of colleges is typically inaccessible to the public.

3. We have showed some positive results of the hybrid system through simulation, however, simulation alone is insufficient to cover all complicated strategies of students. As the future work, we plan to design some lab experiments which would involve real participants to play and learn during the game. We believe that these empirical results would provide more evidence and insight for supporting and spreading the adoption of hybrid system like JUPAS in Hong Kong.

## Appendices

### A Proof of Property 2

It is easy to see that when all RF are zero, the generalized mechanism reduces to DA which is strategy-proof. To prove a mechanism is non-truthful in general, we just need to find one counter-example for any given RF which are not all zero.

Suppose all colleges have zero RF except college _c_ with positive \(\alpha_c\). Besides, _c_ has quota for only one student. Let \(\alpha_c\) equal to any small \(\epsilon>0\). Suppose that there are two students _s_<sub>1</sub> and _s_<sub>2</sub>. _s_<sub>1</sub> achieves a higher score _f_<sub>_s_<sub>1</sub></sub> and _c_ is his/her second choice school; _s_<sub>2</sub> gets a lower score _f_<sub>_s_<sub>2</sub></sub> but lists _c_ as his/her first choice. The merit score of _s_<sub>2</sub> in _c_ is then:

\(mrt_c(s_2)=(1-\epsilon)\cdot f_{s_2}+\epsilon\cdot h_c(1)\)

If telling truth, _s_<sub>1</sub>’s merit score in _c_ would be:

\(mrt_c(s_1)=(1-\epsilon)\cdot f_{s_1}+\epsilon\cdot h_c(2)\)

By letting _mrt<sub>c</sub>(s_<sub>1</sub>)_\<mrt<sub>c</sub>(s_<sub>2</sub>), we have the condition when _c_ prefers _s_<sub>2</sub> to _s_<sub>1</sub>:

\(f_{s_1}-f_{s_2}<\frac{\epsilon}{1-\epsilon}(h_c(1)-h_c(2))\unknown\delta\)

Since \(0<\epsilon<1\) and _h<sub>c</sub>_ is a (strictly) decreasing function of choice order, we have \(\delta>0\).

We further assume that _s_<sub>1</sub> knows he/she would not succeed in his/her first choice college, thus the best he/she can achieve is getting into college _c_. By listing _c_ as the first choice, _s_<sub>1</sub> would obtain a higher merit score in _c_:

\(mrt_c(s_1)^S=(1-\epsilon)\cdot f_{s_1}+\epsilon\cdot h_c(1)\)

which is always larger than _mrt<sub>c</sub>(s_<sub>2</sub>).

Therefore, as long as \(f_{s_1}-f_{s_2}<\delta\), _s_<sub>1</sub> would have incentive to deviate from truth-telling for better matching outcome, which proves that the hybrid mechanism is not strategy-proof in general.

### B Proof of Property 3

Here we follow the terms in Featherstone and Niederle (2008) and adapt their proof for BM to our context of generalized mechanism. We first give some basic definitions and lemmas.

