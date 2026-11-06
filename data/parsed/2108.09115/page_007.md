**Algorithm 2:** Algorithm Compress iteratively finds maximal blocks \[XStart...XEnd\] in X that have a matching maximal block \[YStart...YEnd\] in Y. At each iteration it first exponentially increases the variable \(\ell\) until \(\ell:=\lfloor log_2(XEnd-XStart)\rfloor\); it then binary searches for the exact length of the block.

**Algorithm 3:** Algorithm HIS maintains data structure (balanced binary search tree) Pareto, which stores the total weight and Y-index of the last character of each common substring of X and Y. The data structure is maintained sorted by Y-index, and we only keep common substrings that are _pareto-optimal_ (in the sense that we want common substrings that are heavier but end on lower Y-index).

**Algorithm 4:** HIS(XBlocks,Y)

\(k\leftarrow length(XBlocks)\)

\(\text{Pareto}\leftarrow\text{new balanced binary search tree}\)

\(\text{Pareto.insert(}0,0\text{)}\)

**for** _i_=1_...k_ **do**

\(\text{\texttt{/* Add the next block to Pareto: \*/}}\)

\(\text{newY}\leftarrow Y^{-1}(Xblock[i].start)\)

\(\text{prevY}\leftarrow\text{Pareto.prev(newY).Y}\)

\(\text{prevWeight}\leftarrow\text{Pareto.prev(newY).weight}\)

\(\text{newWeight}\leftarrow\text{prevWeight}+\text{Xblock.weight}\)

\(\text{Pareto.insert(newY,newWeight)}\)

\(\text{\texttt{/* Remove old blocks that are no longer pareto-optimal: \*/}}\)

\(\text{\texttt{while} newWeight}\ge\text{Pareto.next(newY).weight \textbf{do}}\)

\(\text{Pareto.next(newY).delete()}\)

**return** Pareto.max().weight

**Algorithm 2:** Algorithm Compress iteratively finds maximal blocks \[XStart...XEnd\] in X that have a matching maximal block \[YStart...YEnd\] in Y. At each iteration it first exponentially increases the variable \(\ell\) until \(\ell:=\lfloor log_2(XEnd-XStart)\rfloor\); it then binary searches for the exact length of the block.

**Algorithm 3:** Algorithm HIS maintains data structure (balanced binary search tree) Pareto, which stores the total weight and Y-index of the last character of each common substring of X and Y. The data structure is maintained sorted by Y-index, and we only keep common substrings that are _pareto-optimal_ (in the sense that we want common substrings that are heavier but end on lower Y-index).

