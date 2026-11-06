# Selection under partial information

Benjamin Aram Berendsohn<sup>∗</sup>

The selection problem asks to find the _k_-th smallest element in a given set _X_. Its complexity is well-known to be \(\Theta(|X|)\) for every fixed _k_. We consider the _poset selection_ problem where a partial order _P_ on _X_ is given, and the underlying order of _X_ is guaranteed to be a linear extension of _P_. This generalizes several variants of the selection problem studied before.

Our main result is an algorithm that performs O(_k_+OPT(_P,k_)) comparisons, where OPT(_P,k_) is the minimum number of comparisons required for the input (_P,k_). If _P_ is a rooted tree, we obtain an O(OPTlog(_k/_OPT)) algorithm, which can be further improved to O(OPTloglog(_k/_OPT)) or O(OPTlogOPT) under mild assumptions about _P_. Our algorithms are based on the work of Kaplan, Kozma, Zamir, and Zwick [SOSA 2019], who used Chazelle’s soft heaps [J. ACM 2000] to simplify several older results. We introduce a new soft heap variant, the _weighted soft heap_, which allows greater control over which elements get corrupted.

### 1 Introduction

In the selection problem, we are given a set _X_ of _n_ distinct comparable elements<sup>1</sup> and a number \(k\in[n]\), and need to find the _k_-smallest element of _X_. While _sorting X_ easily solves this problem in O(_n_log_n_) time, the famous median-of-medians algorithm [BFP<sup>+</sup>73] runs in optimal \(\Theta(n)\) time.

In this paper, we consider the _poset selection_<sup>2</sup>, or _generalized selection_ [KKZZ18] problem, where additionally a poset _P_ on _X_ is given, and we know that the (unknown) order of _X_ must be a linear extension of _P_. More precisely, the input is a directed acyclic graph (DAG) _G_ and a comparison oracle \(\prec\) on _V(G_), and it is known that for each edge \((u,v)\in E(G)\), we have \(u\prec v\). Depending on _G_ and _k_, selection may be solved much faster than \(\Theta(n)\); see fig. 1 for some simple examples.

Several special cases of the poset selection problem have been solved with algorithms using an asymptotically optimal number of comparisons. Frederickson and Johnson [FJ82] considered<tbc>

<sup>∗</sup>Max Planck Institute for Informatics, Saarbrücken, Germany; `benjamin.berendsohn@fu-berlin.de` <sup>1</sup>Throughout the paper, we assume the _comparison model_, where these elements can only be accessed via comparisons. <sup>2</sup>This is different from the "selection in posets" problem studied by Daskalakis, Karp, Mossel, Riesenfeld, and Verbin [DKM<sup>+</sup>11].

