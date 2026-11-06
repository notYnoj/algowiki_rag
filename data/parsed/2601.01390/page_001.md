# Derandomizing Pseudopolynomial Algorithms for Subset Sum

**Abstract**

We reexamine the classical _subset sum_ problem: given a set _X_ of _n_ positive integers and a number _t_, decide whether there exists a subset of _X_ that sums to _t_; or more generally, compute the set <u>OUT</u> of all numbers \(y\in\{0,\dots,t\}\) for which there exists a subset of _X_ that sums to _y_. Standard dynamic programming solves the problem in _O(tn_) time. In SODA’17, two papers appeared giving the current best deterministic and randomized algorithms, ignoring polylogarithmic factors: Koiliaris and Xu’s deterministic algorithm runs in \(\widetilde{O}(t\sqrt{n})\) time, while Bringmann’s randomized algorithm runs in \(\widetilde{O}(t)\) time. We present the first deterministic algorithm running in \(\widetilde{O}(t)\) time.

Our technique has a number of other applications: for example, we can also derandomize the more recent output-sensitive algorithms by Bringmann and Nakos [S’20] and Bringmann, Fischer, and Nakos [SODA’25] running in \(\widetilde{O}(|\mathrm{OUT}|^{4/3})\) and \(\widetilde{O}(|\mathrm{OUT}|\sqrt{n})\) time, and we can derandomize a previous fine-grained reduction from 0-1 knapsack to min-plus convolution by Cygan et al. [ICALP’17].

### 1 Introduction

This paper studies one of the textbook problems in algorithm design, the _subset sum_ problem: given a (multi)set _X_ of _n_ positive integers and a target number _t_, decide whether there exists a subset of _X_ that sums to _t_. The problem is weakly NP-complete. Standard algorithms achieve roughly _O_(2<sup>_n/_2</sup>) time (by the meet-in-the-middle trick [HS74]) and _O(tn_) time (by dynamic programming [Bel57]). Although it has remained open whether the exponential bound 2<sup>_n/_2</sup> could be improved in the worst case, the pseudopolynomial bound _O(tn_) has been improved: in two concurrent SODA’17 papers, Koiliaris and Xu [KX19] described a deterministic \(\widetilde{O}(t\sqrt{n})\)-time algorithm,<sup>1</sup> and Bringmann [Bri17] described a randomized (Monte Carlo) \(\widetilde{O}(t)\)-time algorithm. Another elegant randomized (Monte Carlo) \(\widetilde{O}(t)\)-time algorithm was found by Jin and Wu [JW19].

All of these pseudopolynomial algorithms can solve a stronger "all-targets" version of the problem: compute \(\mathrm{OUT}=\{y\in\{0,\dots,t\}:\text{there exists a subset of}X\text{that sums to}y\}\). They can also compute a representation of a feasible subset for each \(y\in\mathrm{OUT}\) (so that a subset may subsequently be reported in \(\widetilde{O}(1)\) time per element). For the all-targets version of the problem, the randomized \(\widetilde{O}(t)\)-time algorithms are clearly near optimal since the output size is \(\Omega(t)\) in the worst case. For the original version of the problem, Abboud, Bringmann, Hermelin, and Shabtay [ABHS22] also ruled out algorithms with time bounds of the form \(O(t^{1-\varepsilon} 2^{o(n)})\) for any constant \(\varepsilon>0\), assuming SETH (see also [CDL<sup>+</sup>16] for an earlier conditional lower bound under a different hypothesis).

<sup>∗</sup>Siebel School of Computing and Data Science, University of Illinois at Urbana–Champaign, USA (tmc@illinois.edu) <sup>1</sup>Throughout this paper, the \(\widetilde{O}\) notation hides factors polylogarithmic in _n_ and _t_.

Timothy M. Chan<sup>∗</sup>

January 6, 2026

arXiv:2601.01390v1 [cs.DS] 4 Jan 2026

