## 1 Introduction

The _(worst-case) sensitivity_ of an algorithm is the maximum change in its output, measured in Hamming distance, when a single input element is perturbed. For randomized algorithms we compare output distributions using earth mover’s distance (EMD). Sensitivity offers a foundational robustness metric for algorithms and has deep connections to sublinear-time and distributed computation \[15\]. Sensitivity also underpins consistent decision making and reproducible knowledge discovery. Prior work has developed low-sensitivity algorithms for numerous combinatorial optimization problems \[31, 32, 45, 47, 48\], clustering tasks \[34, 39, 46\], and decision tree learning \[25\].

On the lower-bound side, it is known that computing 2-coloring of a bipartite graph requires sensitivity \(\Omega(n)\) \[45\]. Recently, Fleming and Yoshida \[15\] leveraged probabilistically checkable proofs (PCPs) to show that, for canonical constraint satisfaction problems (CSPs) such as Max E3SAT, Max E3LIN2, and Max Cut, there exist constants \(\varepsilon,\delta>0\) for which any \((1-\varepsilon)\)-approximation algorithm must have sensitivity \(\Omega(n^\delta)\), where _n_ denotes the number of variables or vertices. Standard reductions then yield \(\Omega(n^\delta)\) lower bounds for approximation algorithms for the maximum clique and minimum vertex cover problems. While their framework provides the first nontrivial lower bounds for approximation algorithms, it nevertheless has several shortcomings:

• The \(\Omega(n^\delta)\) sensitivity bound is evidently far from tight.<tbc>

• The lower bounds for Max E3LIN2 and Max Cut are obtained via gadget reductions from Max E3SAT, so they say nothing about approximation algorithms for satisfiable instances.<tbc>

• The argument applies only to worst-case sensitivity, leaving the behavior under randomly chosen perturbations unresolved.

In this work we address these shortcomings by relating sensitivity to locally testable codes (LTCs) and showing how the existence of an LTC yields sensitivity lower bounds. We outline the framework below.

### 1.1 Our Contributions

#### Sensitivity Lower Bounds for CSPs via LTCs.

_Locally testable codes (LTCs)_ \[22\] are error- correcting codes whose membership can be checked by probing only a constant number of coordinates of the received word. An LTC is called a _strong LTC_ \[21\] if there exists \(\kappa>0\) such that the rejection probability is at least \(\kappa\) times the relative distance from the code. The parameter \(\kappa\) is called the _detection probability_ of the code. As we only consider strong LTCs in this work, we also call them LTCs. In this work, we mainly consider linear codes, meaning they form a subspace of \(\mathbb{F}_p^n\).

An LTC naturally induces a CSP instance: we regard each coordinate of the input word as a variable, and each test performed by the tester as a constraint on those variables. The _variable degree_ \(\theta\) of the tester is the maximum number of constraints that query any single coordinate. If the input is a codeword the instance is satisfiable, whereas inputs far from the code violate a fraction of the constraints that is proportional to their distance from the code. For an LTC _C_, let MaxCSP(_C_) denote the Max CSP whose constraints are restricted to those used in the tester for _C_. Throughout the introduction, we measure sensitivity for CSP instances with respect to deleting a single constraint. The main contribution of this work is showing a general scheme that converts a linear LTC _C_ to a sensitivity lower bound of MaxCSP(_C_).

