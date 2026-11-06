<tbc>number of comparisons then have to be chosen together. The problem is to allocate that budget so as to maximize alignment probability, a quantum counterpart of the allocation question addressed by OCBA [14].

An evaluation model can also change what one oracle call answers. A membership query tests whether a single design belongs to the good-enough set instead of comparing two designs. The fixed-budget values of this model can be studied when the number of good designs is unknown [45, 46].

Beyond changes to the evaluation oracle, the output criterion can also change. This paper selects one design and uses alignment level one. Selecting a set with a prescribed alignment level introduces the selected-set size as a further parameter. A fixed-confidence quantum algorithm already identifies a given number of best arms as a set through a reward oracle [19]. The problem for QOO is to determine the best alignment probability under a fixed comparison budget and the corresponding exact classical benchmark.

### 8.3 Computational cost and constrained selection

The evaluation-oracle budget above counts queries rather than total computation. Computational cost also includes the implementation of a coherent comparison, its workspace and the error-correction overhead [47]. The practical question is whether the gain in alignment probability justifies that cost for a specified evaluation model and target probability.

For constrained selection, the cost model also includes feasibility checks. In constrained OO for unit commitment, the selection criterion combines feasibility with sufficiently low cost [4]. The corresponding QOO formulation specifies how feasibility is checked, what information a query returns and how those checks are charged. A performance comparison alone does not supply this information.

Power system screening with deterministic, expensive evaluations on a fixed set of scenarios can provide a first test of this cost model. Classical and quantum procedures would use the same candidates, feasibility rules and target alignment probability. Measuring evaluation, comparison and selection costs would assess the total cost of reaching that target, alongside the alignment probability per query.

## 9 Conclusion

We formulated quantum ordinal optimization as a class of problems that maximize worst-case alignment probability at a fixed oracle budget. We studied the instance with exact pairwise comparisons, selected-set size one and alignment level one. For exact classical comparisons and a budget smaller than the number of designs, uniform sampling without replacement followed by a knockout is optimal. The sample contains one more design than the budget. With quantum comparisons, the rank law averaged over a random order can have twice the classical degree. We determined the optimum with one comparison from the root of a cubic. These values quantify the benefit of coherent comparison access relative to the optimal classical procedure, and known search bounds show that the quantum-to-classical ratio in blind-pick units grows at most in proportion to the budget for the best design. To determine how that benefit changes beyond the present model, we identify questions about larger budgets, noisy and estimated comparisons, and the computational cost of each comparison as future work.

