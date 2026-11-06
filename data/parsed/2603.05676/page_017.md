# Entropy-Sensitive Strictly In-Place Sorting

17

### A _c_-Adaptive ShiversSort is Walkable

In this section, we show that the recent instance-optimal stack-based mergesort, _c_-Adaptive ShiversSort \[17\], is walkable. See Algorithm 3 for its merge policy. The author defines _c_ as a tunable parameter which allows for a tighter runtime analysis. Such details are not relevant to our work, however.

**Algorithm 3** _c_-Adaptive ShiversSort’s Merge Policy (see Algorithm 1 of Algorithm 1)

1: \(\ell_1\leftarrow\lfloor log(r_1/c)\rfloor\) (resp. \(\ell_2,\ell_3\))

2: **while** \(|S|\ge 3\) and \(\ell_3\le max\{\ell_2,\ell_1\}\) **do**

3: \(R_2\leftarrow\text{Merge}(R_3,R_2)\triangleright\) _removes R_<sub>3</sub> _from S_

We first show that all successful merges during the main loop "pay for" the walk-back cost required to perform them. Assume that the condition on line 2 of Algorithm 3 is true. From Observation 1, we already know _r_<sub>1</sub>. The walkback cost to perform this operation is at most _r_<sub>2</sub>+_r_<sub>3</sub>. This is exactly the cost to merge the runs labeled _R_<sub>2</sub> and _R_<sub>3</sub>. As a result, the walk-back cost over all successful merges is bounded by the total merge cost throughout the main loop, which is at most _m_. It remains to bound the walk-back cost when the condition fails to hold. We first determine the stopping condition for _c_-Adaptive ShiversSort.

**Lemma 7.** _If_ \(r_3>2\times max\{r_1,r_2\}\)_, then_ \(\ell_3>max\{\ell_1,\ell_2\}\).

R2
R1
2r2
R3
R2
R1

Fig.10: In this figure, we illustrate what happens when the merge condition fails in _c_-Adaptive ShiversSort. Assume w.l.o.g. that \(\ell_2=max\{\ell_2,\ell_1\}\). We have walked back \(2\times r_2\) steps yet have not found _r_<sub>3</sub>. By Lemma 7, the merge condition must be false. Thus, we continue the main loop by pushing a new run onto the stack.

