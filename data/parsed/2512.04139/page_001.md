**Solving N-Queen Problem using Las Vegas Algorithm with State pruning**

## ABSTRACT

The N-Queens problem, placing all _N_ queens in a _N_ x_N_ chessboard where none attack the other, is a classic problem for constraint satisfaction algorithms. While complete methods like backtracking guarantee a solution, their exponential time complexity makes them impractical for large-scale instances thus, stochastic approaches, such as Las Vegas algorithm, are preferred. While it offers faster approximate solutions, it suffers from significant performance variance due to random placement of queens on the board. This research introduces a hybrid algorithm built on top of the standard Las Vegas framework through iterative pruning, dynamically eliminating invalid placements during the random assignment phase, thus this method effectively reduces the search space. The analysis results that traditional backtracking scales poorly with increasing N. In contrast, the proposed technique consistently generates valid solutions more rapidly, establishing it as a superior alternative to use where a single, timely solution is preferred over completeness. Although large N causes some performance variability, the algorithm demonstrates a highly effective trade-off between computational cost and solution fidelity, making it particularly suited for resource-constrained computing environments.

**Keywords:** N-Queens Problem, Las Vegas Algorithm, Stochastic Solutions, Backtracking, Pruning

Susmita Sharma <sup>∗</sup>, Aayush Shrestha, Prashant Timalsina, Sitasma Thapa, Prakash Poudyal

<sup>∗,1,2</sup> Department of Mathematics, Department of Computer Science and Engineering, Kathmandu University, Dhulikhel, Kavre

Corresponding Author: Prakash Poudyal Email: `prakash@ku.edu.np`

