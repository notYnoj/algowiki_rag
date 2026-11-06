<tbc>noise the optimal rule ranks designs by their probability of being good enough [15]. These results do not optimize which comparisons to make.

### Quantum selection from estimated values.

For quantum best-arm identification with reward gaps \(\Delta_i\), order \(\sqrt{\sum_i\Delta_i^{-2}}\) queries suffice and are necessary, up to polylogarithmic factors [16]. Weaker oracle models change the rate [17]. Whether a speedup exists depends on access to the simulator’s randomness [18]. With a weak quantum oracle, a fixed-confidence algorithm identifies a given number of best arms as a set [19]. Quantum Grover adaptive search for discrete simulation optimization returns an \(\epsilon\)-optimal design with probability at least \(1-\delta\) using \(\tilde{O}(\sqrt{n})\) queries for constant \(\epsilon\) and \(\delta\) [9]. That is a fixed-confidence guarantee. Hu and Hu study fixed-budget simulation optimization through the minimax expected optimality gap and establish convergence rates under quantum simulation access [10]. Both formulations use performance values estimated from a simulator. Here success depends only on the selected rank, and we determine exact finite-budget values in a comparison-oracle model.

### Selection with comparisons.

Minimum finding uses order \(\sqrt{n}\) comparisons against a moving threshold [8], and finding the _r_ smallest values needs order \(\sqrt{rn}\) for \(r\le n/2\) [20]. Bounds for approximating an order statistic give order \(\sqrt{n/r}\), up to logarithmic factors, for an output among the top _r_ [21]. Grover adaptive search has been analyzed for reaching one of the best _r_ points [22]. That work bounds the expected cost and computes the success probability numerically as a function of the number of function evaluations for two given algorithms. Comparison oracles on permutations are the standard setting of quantum lower bounds for sorting and element distinctness [23]. Wang and Ying use a bounded-error version of this comparison oracle [24].

### Exact results with few queries.

Grover’s algorithm is exactly optimal for search with one marked item [11]. Zero-error few-query algorithms for ordered search were found numerically [25, 26], and translation-invariant algorithms are optimal for that problem [27]. For small Boolean functions, optimal success probabilities have been computed numerically by semidefinite programming in a study of zero-error quantum query complexity [28], and optimal values are known for oracle problems with a group structure [29] and for one-query AND and EQUALITY [30]. Several of these results use the semidefinite characterization of quantum query algorithms [31].

The comparison results provide query bounds for selection, while the few-query results provide methods for optimizing success at a specified budget. Below, we formulate rank alignment under comparison access, establish the exact classical benchmark and apply these methods to the one-comparison quantum problem. Selection from estimated values requires a different evaluation model, as discussed in Section 8.2.

## 3 Model and performance measures

Determining the best alignment probability at a fixed budget requires a QOO problem to specify what information queries provide and what counts as a successful selection. We first define the problem class with these choices left to each problem. We then specialize it to exact comparisons with one selected design, for which the following sections establish the results.

