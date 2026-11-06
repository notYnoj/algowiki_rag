Intuition and Extension

To some the lowered statistics seem surprising. Typical reasoning follows: "to sort three, order any two, the third draws a bye. Bye enters and plays to establish an overall winner (WLOG, loser); third step ranks the runner’s up." While accurate when elements are chosen freely, as a memory-based method each element carries a rank implicit in its index. CE sorting ranks all elements, chosen pairs are not isomorphic. In the case of N=3 we may disambiguate thus: "Choosing any two at most omits the median, our set is are guaranteed to hold at least the min or max. Choosing and sorting the outermost elements therefore guarantees at least on of max or min landing in its final position. A single swap will place the remaining extrema; both extreme must be treated (a 2-op). With both extrema placed, median is properly placed by process of elimination".

Students of computer science will recognize (a) as bubble-sort, whose initial link leaves the maximum element in central position 2/3 of the time (for the remaining 1/3 it started in proper position and will not move), thereby encumbering subsequent links the task of floating it into its outer position. By comparison, the non-interfering method is seen as a selection or insertion sort whose improved swapping statistics are well-known. It is ironic such study of CE networks is rare and that the total number of links (or stages) has remained the sole performance metric for so long.

Conceptually, the longer prefacing element link in (c) serves as a guard in assuring that no double-exchange occurs, allowing fusion into one 2-op. The final links might not be unit length, as seen in the improved sort/median on nine elements. The guard need only protect (operate on) the outer two unshared elements. As a second and more interesting means of extension, we envision a 3-op of higher order, formed by allowing two adjacent 2-ops to execute concurrently. We explore the latter now.

Sorting N=4

A trial network (e) overlaps two optimal 3-sorts, sharing a central element,

\begin{tabular}{ccccc}
 & \multicolumn{2}{c}{Swaps} & \multicolumn{2}{c}{Stages} \\
 & avg & max & \multicolumn{2}{c}{Swaps} \\
old & 9.11 & 19 & 9 & 11.56 25 11 \\
new & 6.99 & 13 & 6 & 9.44 18 8 \\
%ch & 77% & 68% & 67% & 72% 82% 73% \\
\end{tabular}

