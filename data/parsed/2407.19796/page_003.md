there exists an _f_-segmentation (_u_<sub>1</sub>_,...,u<sub>f</sub>_) of _P_ that can be embedded to _T_. The set of _f_-segmental subsequences of _T_ is denoted by \(SubSeq^{\le f}(T)\). Any element of \(SubSeq(T)=\bigcup_SubSeq^{\le f}(T)\) is called a _subsequence_.

We consider the following decision problem:

**Problem 1** (SegE)**.** Given strings _T_ and _P_ and a positive integer _f_, decide whether \(P\in SubSeq^{\le f}(T)\).

Note that since each gap _g<sub>i</sub>_ in an embedding can be the empty string, SegE asks if _P_ has a segmentation with at most _f_ segments that can be embedded into _T_.

The following problem asks the minimum number of segments with which _P_ can be embedded into _T_:

**Problem 2** (MinSegE)**.** Given strings _T_ and _P_, find the smallest positive integer _f_ such that \(P\in SubSeq^{\le f}(T)\) if it exists, and return _nil_ otherwise.

We also consider the segmental version of the _longest common subsequence_ (_LCS_) problem, which we call SegLCS<sup>2</sup>. A pattern _P_ is said to be an _f-segmental common subsequence_ (_f-SegCS_) of two strings _T_<sub>1</sub> and _T_<sub>2</sub> if _P_ has a segmentation (_u_<sub>1</sub>_,...,u<sub>f</sub>_) of size _f_ that can be embedded to both _T_<sub>1</sub> and _T_<sub>2</sub>. We denote by slcs(_S,T,f_) the length of a longest _f_-SegCS of _S_ and _T_.

**Problem 3** (SegLCS)**.** Given strings _T_<sub>1</sub>_,T_<sub>2</sub>, and a positive integer _f_, compute slcs(_T_<sub>1</sub>_,T_<sub>2</sub>_,f_).

## 3 \(O\big(\big(mn\big)^{1-\epsilon}\big)\)-time Conditional Lower Bound for SegE

In this section, we present a lower bound for SegE such that there is no strongly sub-quadratic solution exists unless the famous _strong exponential-time hypothesis_ (_SETH_) fails.

**Problem 4** (_k_-SAT problem)**.** Given a propositional logic formula of conjunctive normal form which has at most _k_ literals in each clause, decide whether there exists an interpretation that satisfies the input formula.

**Conjecture 1** (The Strong Exponential-Time Hypothesis; SETH)**.**<br>
_For any_ \(\epsilon>0\)_, there exists_ \(k\ge 3\) _such that the k-SAT problem cannot be solved in_ \(O(2^{(1-\epsilon)n})\) _time, where n is the number of variables._

Bille et al. \[2\] have shown a conditional lower bound on the complexity of _Episode Matching_.

**Problem 5** (Episode Matching)**.** Given two strings _T_ and _P_, compute a shortest factor _S_ of _T_ such that \(P\in SubSeq(S)\).

**Theorem 1** (\[2\])**.** _For any_ \(\epsilon>0\) _and any_ \(\alpha\le 1\)_, Episode Matching on binary strings T and P with_ \(|P|\in\Theta(|T|^\alpha)\) _cannot be solved in_ \(O((|T||P|)^{1-\epsilon})\) _time, unless SETH is false._

This section proves a conditional lower bound on the complexity of SegE by a reduction from Episode Matching. We use Theorem 1 with \(\alpha=1\). The proof by Bille et al. implies that only deciding whether a desired factor has a certain length is already as hard.

**Corollary 1** (\[2\])**.** _For any_ \(\epsilon>0\)_, given binary strings T and P with_ \(|P|\in\Theta(|T|)\) _and an integer h, one cannot decide whether there is a factor S of T such that_ \(|S|\le h\) _and_ \(P\in SubSeq(S)\) _in_ \(O(|T|^{2-\epsilon})\) _time, unless SETH is false._

<sup>2</sup>SegLCS for _f_ is equivalent to the longest _f_-common sub-string problem (longest _f_-CSS) in \[13\] and the _f_-longest common factor with gaps problem (_f_-LCFg) in \[1\].

