# Lossless Reductions and Hybrid Sampling for Phylogeny Using the Maximum Compatibility Criterion

**Abstract**

Maximum compatibility provides a criterion for phylogenetic reconstruction in which the objective is to retain a maximum set of mutually compatible characters. For binary characters, pairwise compatibility can be represented by a weighted graph whose vertices correspond to characters and whose edges connect compatible pairs. A leading algorithm by Cherry [BMC Bioinformatics, 18(1):127, 2017] uses this representation to identify maximum compatible character sets as maximum weight cliques.

We formulate the problem as maximum weight independent set enumeration on the complement graph and use deterministic postprocessing to map sampled bit strings to maximal feasible solutions. To explore the prospects of quantum computational advantage, we further construct bespoke correction-in-the-loop Quantum Approximate Optimisation Algorithm instances and find that traditional Lagrange multiplier choices may not be optimal for the enumeration problem on noisy devices.

We also introduce lossless graph reductions with reconstruction rules that preserve the complete set of optimal solutions. Our results indicate that graph reduction and sampling can be effectively combined to address the enumeration bottleneck in maximum compatibility phylogeny, while retaining exact reconstruction when the residual optimum set is completely resolved.

We enhance Cherry’s approach to maximum compatibility by introducing graph reduction techniques and quantum sampling. Our classical benchmarks show a clear difference between finding one optimum and recovering the optimum set in practice. We demonstrate the utility of our methods on graphs constructed from SARS-CoV-2 sequences.

### 1 Introduction

Phylogenetic trees describe the complex evolutionary relationships of populations of organisms, providing contexts and answers to a wide range of biological questions, such as cancer research [14], drug design [2], and, more recently, detecting outbreaks of new SARS-CoV-2

<sup>∗</sup>`ohy21@cam.ac.uk`

Orson Ye<sup>∗1,2</sup>, James Bonfield<sup>3</sup>, Joshua Cudby<sup>1,2</sup>, Richard Durbin<sup>4</sup>, Sergii Strelchuk<sup>2</sup>

<sup>1</sup>Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Cambridge, United Kingdom

<sup>2</sup>Department of Computer Science, University of Oxford, Oxford, United Kingdom

<sup>3</sup>Wellcome Sanger Institute, Hinxton, United Kingdom

<sup>4</sup>Department of Genetics, University of Cambridge, Cambridge, United Kingdom

