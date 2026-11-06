<tbc>in one particular admission year. The following property helps relieve our concerns of programmes’ strategies so that we may refocus on the manipulations from applicants’ side.

_Property 5_ Suppose after students submit their preferences, each college _c_ determines its true values of \(\alpha_c\) and _h<sub>c</sub>(r_) independently. Then revealing \(\alpha_c\) and _h<sub>c</sub>(r_) truthfully would be the dominant strategy for any programme \(c\in\mathcal{C}\) in the _ex post_ perspective.

_Proof_ We present the proof in Appendix D. \(\sqcap\sqcup\)

Here we take the ex post perspective<sup>12</sup> since when colleges make their strategies, students’ preferences are already submitted and fixed. In practice, when the admission authority evaluate the matching outcome each year, they can only conduct it based on the submitted preference lists of students. It would be expensive (or even impossible) to obtain the true preferences of all applicants via survey<sup>13</sup> or other methods. Thus for the single shot game, colleges would passively reveal their true parameters once they receive applicants’ preference lists.

In this section we have shown some fundamental properties of the generalized mechanism. To further investigate the degree of satisfaction participants perceive under different mechanisms, we implement simulations and present the social welfare results different mechanisms induce in the next section.

## 5 Performance Evaluation for Generalized Matching Mechanism

To define and compare social welfare under different matching outcomes, we need to quantify the utility of each participant/agent in the mechanism first.

Denoted by S the set of students and C the set of colleges. \(\mathcal{I}=\mathcal{S}\cup\mathcal{C}\) is the set of all participants and O is the set of all possible matching outcomes. For any agent \(i\in\mathcal{I}\), let _p<sub>i</sub>_ be the reciprocating preference list<sup>14</sup> of _i_ and _o(i_) be the set of participants matched to _i_ under certain outcome \(o\in\mathcal{O}\).

For each agent \(j\in o(i)\), denote integer _r(j,p<sub>i</sub>_) as the ranking agent _j_ appears in _i_’s preference list _p<sub>i</sub>_. For example, _r(j,p<sub>i</sub>_)=1 means that _j_ is the first choice in _i_’s preference list.<sup>15</sup> We use _r_=0 to denote the unmatched case.

We assume that agent _i_’s utility is additive and only determined by the orders of the matching set in the preference list, which can be written as,

\(u_i(o)=\sum_{j\in o(i),j\in\mathcal{I}}U_i(r(j,P_i))\forall i\in\mathcal{I},o\in\mathcal{O}\) (1)

<sup>12</sup> For the _ex ante_ case, say colleges need to submit their parameters before students’ submission, Property 5 may not hold since colleges would take students’ reaction into consideration before making any decisions. It would be an interesting future work for analyzing the complicated interactions from the ex ante perspective. <sup>13</sup> Still, students have no incentive to reveal their true preference to authority after the matching is over. <sup>14</sup> Here when considering students, _p<sub>i</sub>_ is students’ original preference. <sup>15</sup> For simplicity, we assume there are no ties in the preference list. Otherwise, we can break the tie by a random lottery first.

