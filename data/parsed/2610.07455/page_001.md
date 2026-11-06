# Cores Characterize the One-Pass Streaming Complexity of CSPs

Joshua Brakensiek<sup>∗</sup> <br>
University of California, Berkeley <br>
josh.brakensiek@berkeley.edu

Amatya Sharma <br>
University of Michigan, Ann Arbor <br>
amatya@umich.edu

Aaron Putterman<sup>†</sup> <br>
Harvard University <br>
aputterman@g.harvard.edu

Santhoshini Velusamy<sup>‡</sup> <br>
University of Waterloo <br>
santhoshini.velusamy@uwaterloo.ca

**Abstract**

We study the one-pass streaming complexity of CSPs over a fixed finite relation _R_ under three natural objectives: SAT(_R_), deciding whether all constraints can be satisfied; Min-CSP(_R_), approximately minimizing the number of unsatisfied constraints; and Exact-CSP(_R_), exactly computing the maximum number of satisfied constraints.

Sharma and Velusamy (ESA 2026) characterized the streaming complexity of satisfiability for CSPs with literals using the non-redundancy parameter NRD<sub>_n_</sub>(_R_), which roughly measures the largest instance in which every constraint is independently necessary. For the most general setting without literals, they obtained the corresponding characterization for Boolean relations and showed obstacles to extending their techniques to larger domains. Kol, Paramonov, Saxena, and Yu (ITCS 2023) similarly characterized the streaming complexity of Exact-CSP(_R_) for Boolean CSPs with literals in terms of the degree deg(_R_) of the relation when written as a polynomial, while without literals, the corresponding result was known only for Max-Cut.

For all three of the objectives we study, we give tight characterizations for unweighted CSP instances over arbitrary finite domains. The streaming algorithms we provide are deterministic, while the corresponding bounds are tight up to polylogarithmic factors, even against randomized algorithms. The central idea in all three results is a reduction of _R_ to its core, a canonical subrelation of _R_ which admits gadgets that allow for the hard-pinning (or fixing) of variables.

<sup>∗</sup>Supported in part by NSF awards CCF-2211972 and DMS-2503280 and Venkatesan Guruswami’s Simons Investigator award. <sup>†</sup>Supported in part by a Jane Street Graduate Research Fellowship, Simons Investigator awards to Madhu Sudan and Salil Vadhan, and AFOSR award FA9550-25-1-0112. <sup>‡</sup>Supported in part by NSERC Discovery grant RGPIN-2026-04689 and ECR supplement DGECR-2026-00421.

