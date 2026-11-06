Strategy-Proof Approximation Algorithms for the Stable Marriage Problem with Ties and Incomplete Lists

**Abstract**

In the stable marriage problem (SM), a mechanism that always outputs a stable matching is called a _stable mechanism_. One of the well-known stable mechanisms is the man-oriented Gale-Shapley algorithm (MGS). MGS has a good property that it is strategy-proof to the men’s side, i.e., no man can obtain a better outcome by falsifying a preference list. We call such a mechanism a _man-strategy-proof mechanism_. Unfortunately, MGS is not a woman- strategy-proof mechanism. (Of course, if we flip the roles of men and women, we can see that the woman-oriented Gale-Shapley algorithm (WGS) is a woman-strategy-proof but not a man-strategy-proof mechanism.) Roth has shown that there is no stable mechanism that is simultaneously man-strategy-proof and woman-strategy-proof, which is known as Roth’s impossibility theorem.

In this paper, we extend these results to the stable marriage problem with ties and incomplete lists (SMTI). Since SMTI is an extension of SM, Roth’s impossibility theorem takes over to SMTI. Therefore, we focus on the one-sided-strategy-proofness. In SMTI, one instance can have stable matchings of different sizes, and it is natural to consider the problem of finding a largest stable matching, known as MAX SMTI. Thus we incorporate the notion of approximation ratio used in the theory of approximation algorithms. We say that a stable- mechanism is _c-approximate-stable mechanism_ if it always returns a stable matching of size at least 1_/c_ of a largest one. We also consider a restricted variant of MAX SMTI, which we call MAX SMTI-1TM, where only men’s lists can contain ties (and women’s lists must be strictly ordered).

Our results are summarized as follows: (i) MAX SMTI admits both a man-strategy-proof 2-approximate-stable mechanism and a woman-strategy-proof 2-approximate-stable mechanism. (ii) MAX SMTI-1TM admits a woman-strategy-proof 2-approximate-stable mechanism. (iii) MAX SMTI-1TM admits a man-strategy-proof 1.5-approximate-stable mechanism. All these results are tight in terms of approximation ratios. Also, all these strategy- proofness results apply for strategy-proofness against coalitions.

## 1 Introduction

An instance of the _stable marriage problem_ (_SM_) [2] consists of _n_ men _m_<sub>1</sub>_,m_<sub>2</sub>_,...,m<sub>n</sub>_, _n_ women _w_<sub>1</sub>_,w_<sub>2</sub>_,...,w<sub>n</sub>_, and each person’s preference list, which is a total order of all the members of the opposite gender. If a person _q<sub>i</sub>_ precedes a person _q<sub>j</sub>_ in a person _p_’s preference list, then we

Koki Hamada<sup>1</sup>, Shuichi Miyazaki<sup>2</sup>, Hiroki Yanagisawa<sup>3</sup>

<sup>1</sup>NTT Corporation. `hamada.koki@lab.ntt.co.jp`

<sup>2</sup>Kyoto University. `shuichi@media.kyoto-u.ac.jp`

<sup>3</sup>IBM Research - Tokyo. `yanagis@jp.ibm.com`

arXiv:1902.05678v1 [cs.GT] 15 Feb 2019

