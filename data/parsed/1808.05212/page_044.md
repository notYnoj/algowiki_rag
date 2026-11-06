in which the maximum number of exchanges drops from 5 to 4. The worst-case input occurs when reordering (3,4,1,2) and in this case all save but the final link are active. A breakdown of total swap counts appears below:

Note that the reappearance of the central link (2,3) in (i) implies that a "needless" i.e. redundant comparison might take place, as when presented the input (1,3,2,4) requiring merely one central transposition. This cannot be helped; the network is statistically optimal. In the extreme case, sorted data requiring no exchanges will nonetheless compare at all link positions, including "redundant" links -- such is the topology of CE networks. Attempts to mitigate this, such as (software) early termination as when reaching the threshold of maximum exchange are not cost effective: they must both count and test in order to detect this condition at a cost often greater than a few additional link comparisons.

The above (i) also sheds light into the subtleties of conditional probability. While there are 4!= 24 possible inputs permutations, the first four links cannot each successively half the size of the solution space: 24 is not 4x divisible by 2. While links 3 and 4 both execute independently with 50/50 exchange statistics, they are nonetheless conditionally bound. If link 3 does execute there is a 2/3 change that link 4 does not, and vise versa. In effect, when "double winner" (max of all four) is found by exchanging element 2 with 3, previous losers to this element may be ascribed less demotion; they are more apt to retain a superior position and not trigger a link 4 exchange. Intuition aside, careful analysis of exchange statistics bears this all out.

\begin{tabular}{ccccccccc}
\multicolumn{9}{c}{Histogram of Exchanges} \\
exchanges & 0 & 1 & 2 & 3 & 4 & 5 & & \\
- & - & - & - & - & - & - & - & \\
(g) "rake" & 1 & 5 & 8 & 6 & 3 & 1(*) & & \\
(i) "comb" & 1 & 4 & 8 & 8 & 3 & 0 & & \\
\multicolumn{9}{c}{* - input 4 2 3 1} \\
\end{tabular}

