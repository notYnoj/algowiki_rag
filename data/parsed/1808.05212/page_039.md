Exchanges are costly, often at a ratio of 2:1 or 3:1 to a simple comparison. We have affixed the likelihood of an exchange to each link. Summary statistics give the maximum and average number of exchanges for the entire network.’

The networks presented so far for N=3 are distinct and require in both cases three stages, comparisons and exchanges. Both also demonstrate that a full sort network will include all possible length=1 links as these alone can serve to reorder permutations of sorted data when merely one adjacent transposition exists. The symmetry of (b) is compelling: it allows for fully bidirectional sorting where input and output sides reverse. Unfortunately, it (like (a)) also exhibits a link in which swapping occurs more often then not.

When a link exchange occurs more than half the time, we may reverse the swap vs non-swap .67/.33 to .33/.67 by preexchanging its elements. We remove the direct cost of the exchange by reversing the order of input lines to the left of the offending link. But all inputs are unsorted so any non-conditional exchange has no sorting efficacy and may be removed. Applied to links .67 in (a), (b) give

and the networks, identical under mirror symmetry, substantially improve the average cost of exchange. More striking is a reduction in maximum exchange, which was lowered from three to two. This is unexpected and serves as the basis of non-interfering concurrent exchange. Clearly, the first link may exchange without restriction. The remaining cost of one exchange must be shared between the two remaining links: at most one may occur. This in turn implies that the central element cannot be rewritten by both links, allowing both the upper and lower link concurrent execution.

We now create a new fused dual-link element, which we name a ’2-op’ (borrowing from mathematical nomenclature used for such occurrences), depicted below:

\begin{tabular}{cc}
\multicolumn{2}{c}{(a) (b)}\\
\end{tabular}

\begin{tabular}{cc}
\multicolumn{2}{c}{(c) (c')}\\
\end{tabular}

\begin{tabular}{cc}
\multicolumn{2}{c}{(d)}\\
\end{tabular}

