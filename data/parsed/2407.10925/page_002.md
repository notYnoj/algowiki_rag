<tbc>an alternate method of encoding pairs of binary strings that allows us to pre-compute a portion of each iteration. Using this encoding, we also develop an efficient recursive strategy for sequentially reading and writing to external memory, considerably reducing the memory I/O bottleneck. Additionally, by combining several parts of the algorithm at the implementation level, we are able to reuse computations and significantly lessen how many memory I/O operations are required. In combination with advancements in compute power since the publication of previous algorithms, these improvements allowed us to achieve new state-of-the-art lower bounds for, to the best of our knowledge, all but \(\gamma_{14,2}\).

## 2 Background and Related Work

In 1975, Chvátal and Sankoff [8] began investigating the expected length of a longest common subsequence of two strings of length _n_ whose characters are selected independently and uniformly at random from an alphabet of size _k_. They observed that, for fixed _k_, the expected length of a longest common subsequence of the strings is superadditive with respect to _n_. Using this, they proved that the expected LCS length of the strings, normalized by _n_, converges to some constant _c<sub>k</sub>_ as _n_ grows to infinity. This constant is now referred to as the Chvátal- Sankoff constant \(\gamma_{k,2}\). The exact values for these constants are still unknown, but continuous progress upon upper and lower bounds has been made (see  1).

Chvátal and Sankoff established in their original paper that the Chvátal-Sankoff constant for the binary case (i.e., \(\gamma\)) falls between 0.697844 and 0.866595 [8].<tbc>

<tbc>Through Monte-Carlo simulations, they predicted the value to be around 0.8082. Deken [13] initiated efforts to refine these bounds in 1979, culminating in 1983 with a tighter interval of 0.7615 to 0.8575, achieved via diverse matching algorithms. Despite their differences, Deken’s algorithms adhere to a common procedural framework: they initialize a pointer on each sequence, alternate movements until encountering an increase in the count of differing elements between the pointers, match characters when possible, and resume the process from the matched points, disregarding any prior characters.

In 1986, Steele [25] conjectured that the exact value of the binary Chvátal-Sankoff constant was \(\frac{2}{1+\sqrt{2}}\) (≈ 0.82843). This conjecture stemmed from a heuristic approach inspired by coin-flip sequences, assuming an independent and identical distribution of each coin flip. Much of this conjecture’s development was spurred by the contributions of Arratia and Waterman [2, 1].

Dančík and Paterson [29] introduced a novel method in 1994. They defined a system of linear recurrence relations, where each relation counts the number of string pairs of length _m_ with an LCS of length _i_. Each linear recurrence additionally requires that the string pairs start with a specific pattern. They then showed that the maximum eigenvalue of the system of recurrence relations can be used to determine an upper bound \(\gamma\). By minimizing the overlap between different recurrence relations, the upper bound on \(\gamma\) is improved. In their best results, Dančík and Paterson used 52 linear recurrences, obtaining a best upper bound of 0.837623. Separately, they also calculated a lower bound of 0.77391 using analysis on finite state machines that generate the length of an LCS, given two strings as inputs [9].

Boutet de Monvel [12], in early 1999, conducted extensive Monte-Carlo simulations akin to Chvátal and Sankoff, albeit optimized, parallelized, and with increased sample size. His prediction for the binary constant stood at 0.812282. Later that year, Baeza- Yates, Gavaldà, Navarro, and Scheihing [3] estimated the constant at 0.8118, leveraging finite state automata and analysis of string generation complexity (via Kolmogorov complexity analysis). In 2001, Bundschuh [6] employed a lattice framework to tackle the longest common subsequence problem, resulting in an approximated value of 0.812653.

In 2009, Lueker [20] utilized dynamic programming to create a modified version of Dančík and Paterson’s algorithm which performed calculations on every pair of strings of length \(\ell\), to refine the bounds on \(\gamma\) to between 0.788071 and 0.82628. This disproved Steele’s conjectured value for the binary constant, as Lueker’s upper bound fell below Steele’s prediction. That same<tbc>

Bounds and Estimates of γ
0.9
Estimates
0.85
0.8
Value
0.75
0.7
1980
1990
2000
2010
2020
Year

Figure 1: The best upper and lower bounds on \(\gamma\) and estimates of \(\gamma\) over time.

