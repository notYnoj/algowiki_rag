## Round 2 (div=5)

Active Range: `A\[0,4\]`. Partitioning: `STABLE-PARTITION` is called, the predicate \(\lfloor x/5\rfloor=0\) is false for all elements. The array is unchanged. The new partition starts at index 0. Action: `COUNTING-SORT` on the active range `A\[0,4\]`. Digits (\(\lfloor\text{val}/5\rfloor\) (mod 5)): `\[0, 4, 1, 4, 4\]`.<br>
Result: `first\_active\_idx = 0` (No elements were finalized).

\begin{tabular}{ccccc}
0 & 1 & 2 & 3 & 4 \\
125 & 5 & 620 & 24 & 124 \\
\end{tabular}

\begin{tabular}{ccccc}
0 & 1 & 2 & 3 & 4 \\
5 & 24 & 125 & 620 & 124 \\
\multicolumn{2}{c}{Sorted} & \multicolumn{3}{c}{Active} \\
\end{tabular}

\begin{tabular}{ccccc}
0 & 1 & 2 & 3 & 4 \\
5 & 24 & 125 & 620 & 124 \\
\end{tabular}

\begin{tabular}{ccccc}
0 & 1 & 2 & 3 & 4 \\
5 & 24 & 124 & 125 & 620 \\
\multicolumn{2}{c}{Sorted} & \multicolumn{3}{c}{Active} \\
\end{tabular}

\begin{tabular}{ccccc}
0 & 1 & 2 & 3 & 4 \\
5 & 24 & 124 & 125 & 620 \\
\end{tabular}

\begin{tabular}{ccccc}
0 & 1 & 2 & 3 & 4 \\
5 & 24 & 124 & 125 & 620 \\
\end{tabular}

Note: For the break-even condition we needed the input to have atleast half of the elements to be partitioned in second round. This causes the cost of optimization to exceed the benefit provided in terms of number of operations.

## Round 3 (div=25)

Active Range: `A\[0,4\]`. Partitioning: `STABLE-PARTITION` is called. The predicate is \(\lfloor x/25\rfloor=0\). This is TRUE for `5` and `24`. The partition preserves the original relative order. The array becomes `\[5, 24, 125, 620, 124\]`. The new partition separating finalized and active elements is at index 2.<br>
State before Sorting:

Action: `COUNTING-SORT` on the new active range `A\[2,4\]`. Digits (\(\lfloor\text{val}/25\rfloor\) (mod 5)): `\[0, 4, 4\]`. The sorted active range is: `\[125, 620, 124\]`.<br>
Result: `first\_active\_idx = 2` (Updated for the next round).

## Round 4 (div=125)

Active Range: `A\[2,4\]`. Partitioning: `STABLE-PARTITION` is called on this sub-array. Predicate is \(\lfloor x/125\rfloor=0\). This is TRUE for `124`. The sub-array is partitioned to `\[124, 125, 620\]`. The full array `A` is now `\[5, 24, 124, 125, 620\]`. The new partition is at index 3.

State before Sorting:

Action: `COUNTING-SORT` on the new active range `A\[3,4\]`. Digits (\(\lfloor\text{val}/125\rfloor\) (mod 5)): `\[1, 4\]`. The sorted active range is `\[125, 620\]`.<br>
Result: `first\_active\_idx = 3`.

## Final Sorted Array

After the final round, the array is fully sorted.

