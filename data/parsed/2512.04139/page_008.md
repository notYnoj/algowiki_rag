have been placed, every spot on the board is considered valid, and the valid space list includes all available positions.

**Maintenance:**<br> A random position is chosen from the valid space list and then is removed from that list. Positions that become invalid due to previously placed queens are marked as 0. From the remaining indices in the valid space list, the loop selects the random position. If the queen needs to be placed and there is no valid solution then the loop restarts. If all queens are successfully placed in valid positions, the loop will stop; otherwise, it restarts until a valid solution is found. The result matrix will then show the valid positions where the queen is placed, with invalid positions marked accordingly. The valid space list will contain only the positions where queens can still be placed.

**Termination:**<br> The loop ends when all queens are successfully placed in valid positions. If no valid position is found, the loop continues as usual until a valid solution is found. As a result, the result matrix shows where each queen is placed correctly, and the valid space list includes positions still available for placing additional queens.

## 4. RESULTS AND DISCUSSION

The performance of the proposed algorithm for the n-Queens problem was evaluated against the classical backtracking approach. Analysis was done on the basis of number of queens placed before reaching the correct configuration and each algorithm was run for each _n_ till first stable placement was found. As the Las Vegas Algorithm, 2 is probabilistic in nature, the algorithm was run for more than 1000 times for each _n_. Metrics such as mean, median, mode, skewness, and kurtosis of the number of those attempts were computed for the probabilistic method, while the number of attempts for backtracking was directly measured.

Histograms with kernel density estimates (KDE) for _n_ values, as in 5, reveal that the probabilistic algorithm exhibits positively skewed distributions with long right tails. This indicates that while most runs converge in relatively few attempts, there exists a non-negligible probability of encountering runs requiring orders of magnitude more attempts.

The skewness values consistently lie around 1.9-2.1, with kurtosis between 5.1-6.6, suggesting heavy-tailed, leptokurtic distributions. This implies a concentration of outcomes around the mean but with frequent outliers on the higher end. The best-fitting distributions for various _n_ include gamma, Weibull (minimum), and Pareto distributions, indicating that the algorithm’s runtime is probabilistically bounded but not safe from to rare, extreme delays.

Histogram with KDE n8 2000 1500 Frequency 1000 500 0
0 200 400 600 800 1000 Value

Histogram with KDE n19 2000 1750 1500 1250 Frequency 1000 750 500 250 0
0 20000 20000 50000 40000 50000 Value

Histogram with KDE n36 2000 1500 Frequency 1000 500 0
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.0 Value

(a) Las Vegas Attempt distribution for n = 8 (b) Las Vegas Attempt distribution for n = 22 (c) Las Vegas Attempt distribution for n = 36

Figure 1: Las Vegas Algorithm Attempt Distributions for n = 8, 22, 36

