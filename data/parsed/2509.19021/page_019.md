<tbc>_Round 3 (div=25)_ Active Range: `A\[3,4\]`. The predicate is ⌊_x/_25⌋=0. This is FALSE for both `620` and `124`.

Action: `COUNTING-SORT` runs on `A\[3,4\]`.

- Digits (\(\lfloor\text{val}/25\rfloor\) (mod 5)): `\[4, 4\]`<tbc>

**-** Result: The active range is sorted.

\begin{tabular}{cccc}
0 & 1 & 2 & 3 & 4 \\
1 & 3 & 4 & 620 & 124 \\
\end{tabular}

\begin{tabular}{cccc}
0 & 1 & 2 & 3 & 4 \\
1 & 3 & 4 & 124 & 620 \\
\multicolumn{2}{c}{Sorted} & \multicolumn{2}{c}{Active} \\
\end{tabular}

\begin{tabular}{cccc}
0 & 1 & 2 & 3 & 4 \\
1 & 3 & 4 & 124 & 620 \\
\end{tabular}

\begin{tabular}{cccc}
0 & 1 & 2 & 3 & 4 \\
24 & 125 & 620 & 124 & 5 \\
\end{tabular}

\begin{tabular}{cccc}
0 & 1 & 2 & 3 & 4 \\
125 & 620 & 5 & 24 & 124 \\
\end{tabular}

_Round 4 (div=125)_ The active range is still `A\[3,4\]`. The predicate is ⌊_x/_125⌋=0. This is TRUE for `124`.

State after Partitioning: The partition moves `124` to the ’sorted’ region.

Action: `COUNTING-SORT` runs the final round on index `A\[4,4\]`, the algorithm terminates after completion of this stage.

_Final Sorted Array_

We now demonstrate how SP-LSD sorts with the same sample input used to demonstrate BNRS, this demonstration is a poor example, reasoning is discussed further along in the note section.

**Input:** _A_=\[24,125,620,124,5\], Base (_n_): 5, Max Value (_k_): 620, Rounds Needed: \(\lfloor log_5(620)\rfloor+1=4\).

_Initial State_ The `first\_active\_idx` marks the start of the subarray to be processed. Initially, this is the entire array. `first\_active\_idx = 0`.

_Round 1 (div=1)_ Active Range: `A\[0,4\]`. The array is unchanged. The new partition starts at index 0. Action: `COUNTING-SORT` on the active range `A\[0,4\]`. Digits (val (mod 5)): `\[4, 0, 0, 4, 0\]`.

Result: `first\_active\_idx = 0` (No elements were finalized).

