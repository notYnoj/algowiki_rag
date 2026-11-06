## D Proof of Property 5

For analyzing colleges’ strategies, we borrow the idea of _dropping strategies_ and _rejection chains algorithm_ from Kojima and Pathak (2008) and show that it is impossible for colleges to find an effective dropping strategy and manipulate the matching successfully. Thus the best matching colleges may achieve is via revealing their true preferences (i.e., their merit order lists).

To complete our proof, we first briefly restate some basic definitions and lemmas in Kojima and Pathak (2008). Let _p<sub>c</sub>_ be the reciprocating preference of college _c_ obtained through its true \(\alpha_c\) and _h<sub>c</sub>(r_). _s_<sub>1</sub> and _s_<sub>2</sub> are two students applying to college _c_.

**Definition 4** A report \(p'_c\) is said to be a _dropping strategy_ if (i) _p<sub>c</sub>:s_<sub>1</sub>_\>s_<sub>2</sub> and \(p'_c:s_1>\varnothing\) imply \(p'_c:s_1>s_2\), and (ii) \(p_c:\varnothing>s_1\) implies \(p'_c:\varnothing>s_1\).

In other words, a dropping strategy of a college is obtained by removing some students from its true lists of acceptable students, which never changes its relative preference of any two students.

**Lemma 3** (Dropping strategies are exhaustive)**:** _If under certain strategy_ \(p'_c\) _the mechanism produces matching outcome_ \(\mu\)_, then there must exist a dropping strategy of college c that produces a matching that c weakly prefers to_ \(\mu\) _according to its true preference p<sub>c</sub>._

The detailed proof can be found in Appendix B of Kojima and Pathak (2008). Lemma 3 implies that if there exists any successful strategy \(p'_c\) for college _c_ (by manipulating its \(\alpha_c\) and _h<sub>c</sub>(r_)), we can always find a dropping strategy which achieves at least the same improvement. That is to say, if we can prove that for every dropping strategy, we cannot make college _c_ better off, then _c_ would be forced to act truthfully.

For any dropping strategies, the "dropped" students in _c_ would re-apply to other colleges in the student-proposing DA algorithm, which would cause a chain of rejection and acceptance in the subsequent stages. This can be analyzed in details through the so-called _rejection chains_ algorithm as follows.

**Algorithm 1.** Rejection Chains

Let \(\mu\) be the outcome of student-proposing DA algorithm and \(B_c^1\) a subset of \(\mu(c)\). Let _c_ reject all the applicants in \(B_c^1\). Initially, we set _i_=0 and _flag=false_.

**BEGIN**

Let _i_:=_i_+1;

1. If \(B_c^i=\varnothing\), **return**;

2. Otherwise, let _s_ be the least preferred student by _c_ among \(B_c^i\), and let \(B_c^{i+1}:=B_c^i\backslash s\).

3. Iterate the following steps.

(a) _s_ continues to apply:

i. If _s_ has already applied to every college in _p<sub>s</sub>_, **GO TO** BEGIN;

ii. Otherwise, let \(c'\) be the most preferred college of _s_ among those which _s_ has not yet applied. If \(c'=c\), set _flag=ture_ then **return**;

(b) Acceptance and/or rejection:

i. If \(c'\) has no vacant position and prefers each of its current mates to _s_, then \(c'\) rejects _s_, **GO TO** Step 3.

ii. Otherwise, \(c'\) accepts _s_. If \(c'\) has a vacant position, **GO TO** BEGIN; Otherwise, \(c'\) rejects the least preferred student among those who were matched to \(c'\). Let this rejected student be _s_ then **GO TO** Step 3;

**END**

When Algorithm 1 returns, _flag_ could be either _false_ or _true_. We say that Algorithm 1 **returns to** _c_ if it returns with _flag=true_.

We then re-state Lemma 3 in Kojima and Pathak (2008) as follows:

**Lemma 4** _For any_ \(c\in\mathcal{C}\)_, if Algorithm 1 does not return to c for any non-empty_ \(B_c^1\subseteq\mu(c)\)_, then c cannot profitably manipulate by a dropping strategy._

