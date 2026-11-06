# The Longest Common Bitonic Subsequence: Match-Sensitive Algorithms and Conditional Hardness

**Abstract.** The longest common bitonic subsequence problem asks for a longest common subsequence of two ordered sequences whose values strictly increase and then strictly decrease; either phase may be empty. We formulate the problem through increasing and decreasing endpoint values at matching position pairs. This gives a constructive quadratic baseline and a match- sensitive algorithm based on two standard dominance-maximum passes. Its time is the sum of an input-sorting term and the number of matches times a squared logarithmic factor. We state the endpoint interface that permits reuse of increasing subsequence algorithms, and distinguish this specialization from new range searching machinery. A linear-size padding reduction transfers the conditional strongly subquadratic lower bound for longest common increasing subsequence to the bitonic problem. Reproducible implementations, exhaustive small-instance checks, and newly measured synthetic experiments document correctness and the practical tradeoff between sparse and dense processing.

**Keywords:** Longest common bitonic subsequence, longest common increasing subsequence, sparse dynamic programming, dominance queries, conditional lower bounds

<sup>c</sup>Corresponding author

**Md. Tanzeem Rahat**<sup>1</sup> **Md. Manzurul Hasan**<sup>1</sup> **C, Sadia Sharmin**<sup>2</sup> <sup>1</sup>_Department of Computer Science_ <sup>2</sup>_Department of Computer Science and Engineering_ <sup>3</sup>_Department of Computer Science and Engineering_ <sup>4</sup>_Bangladesh University of Engineering and Technology, Dhaka 1000, Bangladesh_ <sup>5</sup>_tanzeem.rahat@aiub.edu_ <sup>6</sup>_manzurul@aiub.edu, sadiasharmin@cse.buet.ac.bd_

