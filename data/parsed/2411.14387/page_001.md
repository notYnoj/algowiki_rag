# Hardness Amplification for Dynamic Binary Search Trees

**Shunhua Jiang**<br> Columbia University, NY, USA

**Victor Lecomte**<br> Stanford University, CA, USA

**Omri Weinstein**<br> The Hebrew University of Jerusalem, Israel

**Sorrachai Yingchareonthawornchai**<br> The Hebrew University of Jerusalem, Israel

**Abstract**

We prove direct-sum theorems for Wilber’s two lower bounds [Wilber, FOCS’86] on the cost of access sequences in the binary search tree (BST) model. These bounds are central to the question of dynamic optimality [Sleator and Tarjan, JACM’85]: the _Alternation_ bound is the only bound to have yielded online BST algorithms beating log_n_ competitive ratio, while the _Funnel_ bound has repeatedly been conjectured to exactly characterize the cost of executing an access sequence using the optimal tree [Wilber, FOCS’86, Kozma’16], and has been explicitly linked to splay trees [Levy and Tarjan, SODA’19]. Previously, the direct-sum theorem for the Alternation bound was known only when approximation was allowed [Chalermsook, Chuzhoy and Saranurak, APPROX’20, ToC’24].

We use these direct-sum theorems to amplify the sequences from [Lecomte and Weinstein, ESA’20] that separate between Wilber’s Alternation and Funnel bounds, increasing the Alternation and Funnel bounds while optimally maintaining the separation. As a corollary, we show that Tango trees [Demaine et al., FOCS’04] are optimal among any BST algorithms that charge their costs to the Alternation bound. This is true for _any_ value of the Alternation bound, even values for which Tango trees achieve a competitive ratio of _o_(loglog_n_) instead of the default _O_(loglog_n_). Previously, the optimality of Tango trees was shown only for a limited range of Alternation bound [Lecomte and Weinstein, ESA’20].

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Data structures design and analysis; Theory of computation \(\rightarrow\) Online algorithms

**Keywords and phrases** Data Structures, Amortized Analysis

**Acknowledgements** This research was supported by the European Research Council (ERC) Starting grant CODY 101039914. This work was done in part while the authors (SJ, OW, SY) were visiting the Simons Institute for the Theory of Computing, UC Berkeley.

### 1 Introduction

Direct Sum theorems assert a lower bound on a certain complexity measure C of a _composed_<sup>1</sup> problem \(f\circ g\) in terms of the individual complexities of _f_ and _g_, ideally of the form \(\mathcal{C}(f\circ g)\approx\mathcal{C}(f)+\mathcal{C}(g)\). Direct Sums have a long history in complexity theory, as they provide a _black-box_ technique for amplifying the hardness of computational problems \(\mathcal{C}(f^{\circ k})\unknown k\cdot\mathcal{C}(f)\), and are the most promising approach for proving several holy-grail lower bounds in complexity theory [23, 20, 35, 2, 24]. Moreover, a "tensorization" property of C under composition

<sup>1</sup> Formally speaking, direct-sum problems pertain to the complexity of solving _k_ separate copies of a problem _f_, rather than computing a composed function of _k_ copies _g(f(x_<sub>1</sub>)_,...,f(x<sub>k</sub>_)), but it is common to refer to both variations of the _k_-fold problem as direct-sums [23].

