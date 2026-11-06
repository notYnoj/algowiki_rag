The difficulty is that A can otherwise be arbitrary. Yet _L_ is convex, so we may symmetrize \(\tilde{\mathcal{A}}\) by averaging over permutations of message coordinates and alphabet symbols without increasing _L_. Composing the symmetrized encoder \(\tilde{\mathcal{A}}\) with the nearest-message decoder \(\sigma\) produces, for each message _m_, a distribution \(\nu_m^*\) over \(\Sigma^k\) whose probabilities depend only on the Hamming distance to _m_, making the analysis tractable. We then show that some neighboring pair \(m\sim m'\) forces \(\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m))\) and \(\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\) to differ with constant probability, yielding the desired sensitivity lower bound.

### Sensitivity lower bounds from explicit LTCs

Given the connection between sensitivity lower bounds and LTCs, we instantiate our framework with two explicit families. First, we adapt the left-right Cayley complex (LRCC) codes of Dinur, Evra, Livne, Lubotzky, and Mozes \[12\] into systematic LTCs whose induced CSP is Max E3LIN2. This transformation preserves their rate, distance, and detection probability, letting us transfer the _c_<sup>3</sup>-LTC guarantees and derive \(\Omega(n)\) average-sensitivity lower bounds for every \((1-\varepsilon)\)-approximation algorithm, thereby proving Theorem 1.2.

Second, we analyze signed repetition codes that duplicate each message coordinate alongside its complement. We partition the coordinates into _A_ (original copies) and _B_ (flipped copies), embed a bipartite expander on \(A\cup B\), and use a two-query tester that checks random edges for disagreement, thereby realizing a Max Cut instance. The replication factor controls both the rate and distance, and feeding this construction into our framework establishes Theorem 1.3.

## 1.3 Related Work and Discussion

### Max Cut.

It is natural to ask whether one can beat the sensitivity lower bound of Theorem 1.3 by applying Theorem 1.1 to a different two-query LTC. However, in such a tester, every constraint enforces that a pair of queried coordinates differs, so codewords correspond exactly to 2-colorings of the tester’s constraint graph. The number of codewords, and hence the rate, is dictated by the number of connected components, while the minimum distance is governed by the sizes of those components. Consequently, an LTC obtained this way cannot simultaneously achieve high rate and large distance, preventing stronger lower bounds via this route.

### Lower Bounds for Other CSPs.

For a linear code _C_, MaxCSP(_C_) necessarily collapses to a system of linear equations. Attempts to extend our lower bounds via gadget reductions such as pp-definitions or pp-interpretations \[4, 8\] stall here: starting from linear equations one cannot reach target languages whose expressive power is incomparable with (or weaker than) linear systems, so reductions to templates like 2SAT or Horn-SAT are ruled out. Another idea is to replace LTCs with dictatorship tests from the PCP literature \[27, 30\], but it remains unclear whether such tests can be adapted to yield sensitivity lower bounds.

### Machine Unlearning

_(Exact) machine unlearning_ is often formalized by requiring that, after deleting a data item, the algorithm’s output matches the model one would obtain by retraining on the pruned dataset \[6, 24, 37\]. Viewed through this lens, our sensitivity lower bounds translate directly into recourse lower bounds for unlearning. In particular, Theorem 1.5 shows that for the maximum _k_-coverage problem--a canonical abstraction for summarization and selection tasks--the deletion of a single universe element forces any exact-unlearning mechanism that maintains a \((1-\varepsilon)\)- approximation to modify \(\Omega(k)\) members of the selected set family to match the retrained solution. Hence exact unlearning cannot rely on small, local "patches": even a single deletion necessitates wholesale restructuring of the learned summary.

