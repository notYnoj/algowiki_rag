Progress here would clarify to what extent \(\sqrt{T}\)-type behavior is a model artifact versus a fundamental barrier for traceback, and how sharply one can separate offline and streaming access patterns.<tbc>

4. **Parallelization and work-depth tradeoffs.** Our algorithm is deliberately sequential and recomputation-heavy: at each recursion level we process one subproblem at a time with a single frontier buffer. However, the decomposition structure suggests inherent parallelism: subproblems corresponding to disjoint time intervals and disjoint path segments could be explored concurrently. This leads to the question:<tbc>

<tbc>Is there a parallel version of the Universal Hirschberg algorithm that achieves polylogarithmic depth (NC-like) while keeping the total space close to \(O(\omega\cdot\text{polylog}T)\) (bits) and the total work near \(O(T\cdot\text{polylog}T)\)?<tbc>

<tbc>Answering this would connect traceback to parallel DP and circuit evaluation, and could inform the design of low-memory, high-throughput alignment pipelines and other large-scale DP systems. One challenge is to balance the duplication of recomputation across processors against the aggregate space used by concurrently active frontier buffers.<tbc>

5. **Time-space product lower bounds for traceback.** Proposition 2 gives a pure space lower bound in a single-pass model; our upper bound gives a pure space upper bound in an offline model. A more refined goal is to understand the joint tradeoff:<tbc>

<tbc>For a given graph family (e.g. \(N\times N\) grids, banded grids, or bounded-pathwidth DAGs), what are the best possible tradeoffs between time _T_<sub>alg</sub> and space _S_<sub>alg</sub> for traceback? Can one prove lower bounds of the form<tbc>

<tbc>\(T_\text{alg}\cdot S_\text{alg}\ge f(N)\)<tbc>

<tbc>for some _f_ tied to the structure?<tbc>

<tbc>Even modest such bounds (e.g. ruling out _T_<sub>alg</sub>=poly(_N_) and \(S_\text{alg}=o(\omega)\) simultaneously for certain natural DP formulations) would deepen the analogy between traceback and classical time- space tradeoffs for evaluation and simulation tasks, and might require new pebbling-style or communication-complexity arguments tailored to witness reconstruction rather than value computation.

### Acknowledgements.

We gratefully acknowledge the many contributors who have catalyzed breakthroughs in time-space tradeoffs and efficient simulation during the past two years; this manuscript builds directly on the results of others and would not exist without their insight. We further disclose that the exploration, analysis, drafting, and revisions of this manuscript were conducted with the assistance of large language model technology; the authors bear sole responsibility for any errors in technical claims, constructions, and proofs. There are no conflicts of interest to disclose and no external funding support to declare for this work.

## References

