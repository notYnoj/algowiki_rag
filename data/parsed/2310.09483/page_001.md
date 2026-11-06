# Sorting and Selection in Rounds with Adversarial Comparisons

Chris Trevisan<sup>∗</sup>

**Abstract**

We continue the study of selection and sorting of _n_ numbers under the adversarial comparator model, where comparisons can be adversarially tampered with if the arguments are sufficiently close.

We derive a randomized sorting algorithm that does _O(n_log<sup>2</sup>_n_) comparisons and gives a correct answer with high probability, addressing an open problem of Ajtai, Feldman, Hassadim, and Nelson [AFHN15]. Our algorithm also implies a selection algorithm that does _O(n_log_n_) comparisons and gives a correct answer with high probability. Both of these results are a log factor away from the naive lower bound. [AFHN15] shows an \(\Omega(n^{1+\varepsilon})\) lower bound for both sorting and selection in the deterministic case, so our results also prove a discrepancy between what is possible with deterministic and randomized algorithms in this setting.

We also consider both sorting and selection in rounds, exploring the tradeoff between accuracy, number of comparisons, and number of rounds. Using results from sorting networks, we give general algorithms for sorting in _d_ rounds where the number of comparisons increases with _d_ and the accuracy decreases with _d_. Using these algorithms, we derive selection algorithms in _d+O_(log_d_) rounds that use the same number of comparisons as the corresponding sorting algorithm, but have a constant accuracy. Notably, this gives selection algorithms in _d_ rounds that use _n_<sup>1+_o_(1)</sup> comparisons and have constant accuracy for all \(d=\omega(1)\), which still beats the deterministic lower bound of \(\Omega(n^{1+\varepsilon})\).

### 1 Introduction

Comparison-based sorting and selection are two of the most well-studied computational problems, with applications in all aspects of computing. Often, these problems are studied with the goal to minimize the number of comparisons needed. Classical results show that sorting takes \(\Theta(nlogn)\) comparisons [GVN47] and selection takes \(\Theta(n)\) comparisons [BFP<sup>+</sup>73].

Comparison-based sorting and selection have also been extensively studied in the parallel case. The round-based model of parallelism we consider was introduced by Valiant [Val75] for comparison- based problems, where groups of comparisons are done in rounds of interaction. There followed a long line of research in parallel sorting and selection [BR81, HH81, HH82, BT83, Pip87, AA88b, Bol88, WZ93]. Particularly similar to the problems studied in this paper are parallel sorting with limited closure [BT83, Alo86] and sorting networks of arity _k_ with low depth [TL85, PP89, NHAT89, BG90, CS92, Chv92, LB95, GL97, ZLG98, SYW14, DKP22], the latter of which we will use to derive our general sorting algorithms.

However, often it is not possible to guarantee comparisons are completely precise. For example, when ranking chess players, or comparing job applicants. Due to this, the problems of sorting and selection with imprecise comparators have also been widely considered.

Depending on the model, the manner in which the comparator is imprecise differs. The adversarial comparison model we will study was introduced in [AFHN15]. If the values being compared<tbc>

<sup>∗</sup>University of Waterloo. `chris.trevisan@uwaterloo.ca`.

arXiv:2310.09483v2 [cs.DS] 6 Sep 2025

