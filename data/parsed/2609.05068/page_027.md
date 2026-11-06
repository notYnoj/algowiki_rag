While the delay Constraints (6) are not convex, weighting them by the commodity size and aggregating them over all commodities and paths leads to a new convex constraint:

\(\sum_{k\in K}b^k\sum_{p\in P^k}\sum_{a\in p}\frac{x_p^k}{c_a-y_a}\le\sum_{k\in K}b^k\sum_{p\in P^k}d^kx_p^k\Leftrightarrow\sum_{a\in A}\sum_{k\in K,p\in P^k|_{a\in p}}\frac{b^kx_p^k}{c_a-y_a}\le\sum_{k\in K}b^k\gamma d^k\Leftrightarrow\sum_{a\in A}\frac{y_a}{c_a-y_a}\le\gamma\sum_{k\in K}d^kb^k.\) (34)

Observe that (34) can be expressed through SOCP.

These two constraints were tested numerically, but did not provide any significant impact on the problem’s resolution. Therefore, the numerical experiments measuring their impact are not reported in Section 6.

## 5 Lower bound heuristics and performance guarantees

Having derived upper bounds through the proposed relaxations, we now turn to the question of lower bounds. We begin with a result that may be viewed as negative, and then introduce several heuristics. In particular, we show that an heuristic based on the relaxation DCMF<sub>env</sub> constitutes an approximation algorithm with provable performance guarantees.

### 5.1 A negative results on heuristics

This section identifies a general limitation of heuristics applied to problems involving conditional constraints.

We define the term _convex restriction_ as the counterpart to a _convex relaxation_: the convex restriction of a domain is a convex subset of that domain. Similarly, the convex restriction of a constraint is a convex constraint that, if satisfied, guarantees the satisfaction of the original constraint.

We demonstrate that building a convex restriction of a conditional constraint reduces to a binary discrete choice: either fully activating the constraint or forcing the trigger variable to zero.

